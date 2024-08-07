import json
import pandas as pd
from tabulate import tabulate
import argparse

def load_data():
    with open('llm_pricing.json', 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data['models'])

def save_data(df):
    with open('llm_pricing.json', 'w') as file:
        json.dump({"models": df.to_dict('records')}, file, indent=4)

def list_models(df, sort_by=None, ascending=True):
    if sort_by:
        df = df.sort_values(by=sort_by, ascending=ascending)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

def add_update_model(df, provider, model, input_price, output_price, update=False):
    match = (df['provider'] == provider) & (df['model'] == model)
    if update and match.any():
        df.loc[match, 'input_price'] = input_price
        df.loc[match, 'output_price'] = output_price
    elif not match.any():
        df = df.append({
            'provider': provider, 'model': model,
            'input_price': input_price, 'output_price': output_price
        }, ignore_index=True)
    return df

def filter_models(df, provider=None, model=None):
    if provider:
        df = df[df['provider'].str.contains(provider, case=False)]
    if model:
        df = df[df['model'].str.contains(model, case=False)]
    return df

def parse_args():
    parser = argparse.ArgumentParser(description="Manage LLM pricing data")
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all models')
    list_parser.add_argument('--sort', choices=['provider', 'model', 'input_price', 'output_price'], help='Sort by this column')
    list_parser.add_argument('--ascending', action='store_true', help='Sort in ascending order')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new model')
    add_parser.add_argument('provider')
    add_parser.add_argument('model')
    add_parser.add_argument('input_price', type=float)
    add_parser.add_argument('output_price', type=float)

    # Update command
    update_parser = subparsers.add_parser('update', help='Update an existing model')
    update_parser.add_argument('provider')
    update_parser.add_argument('model')
    update_parser.add_argument('input_price', type=float)
    update_parser.add_argument('output_price', type=float)

    # Filter command
    filter_parser = subparsers.add_parser('filter', help='Filter models')
    filter_parser.add_argument('--provider')
    filter_parser.add_argument('--model')

    return parser.parse_args()

def main():
    args = parse_args()
    df = load_data()
    
    if args.command == 'list':
        list_models(df, sort_by=args.sort, ascending=args.ascending)
    elif args.command in ['add', 'update']:
        df = add_update_model(df, args.provider, args.model, args.input_price, args.output_price, update=(args.command == 'update'))
        save_data(df)
        print("Model data has been updated.")
    elif args.command == 'filter':
        filtered_df = filter_models(df, provider=args.provider, model=args.model)
        list_models(filtered_df)

if __name__ == "__main__":
    main()
