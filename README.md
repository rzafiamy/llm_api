# llm_api 📊

Welcome to the `llm_api` repository! This repository is dedicated to tracking and displaying pricing information for various Language Learning Models (LLMs) offered by different providers. Our aim is to provide an easy-to-use reference for comparing costs associated with using different LLMs based on token usage (input/output).

## Features 🚀

- **LLM Providers List:** Detailed listing of LLM providers and the models they offer.
- **Model Details:** Explore the capabilities and specific features of each model.
- **Pricing Comparison:** Compare the pricing per token for both input and output operations across different providers.

## How to Use 🔍

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rzafiamy/llm_api.git
   ```
2. **Navigate into the repository directory:**
   ```bash
   cd llm_api
   ```
3. **Install Dependencies:**
   ```bash
   python3 -m venv .pyenv
   source .pyenv/bin/activate
   pip install -r requirements.txt
   ```
4. **Run the Application:**
   ```bash
   python llm-api-cli.py
   ```

## Contributing 🤝

Interested in contributing? Great! We welcome contributions from everyone. Here are some ways you can contribute:
- Reporting bugs.
- Suggesting enhancements.
- Adding documentation.
- Updating pricing data.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

# Source

- [Openai](https://openai.com/api/pricing/)
- [Anthropic](https://www.anthropic.com/pricing#anthropic-api)
- [Mistral](https://mistral.ai/technology/#pricing)
- [Cohere](https://cohere.com/pricing)


# Example

```bash
python llm-api-cli.py  list
```

|------------|--------------------------------------|---------------|----------------|
| provider   | model                                |   input_price |   output_price |
|------------|--------------------------------------|---------------|----------------|
| OpenAI     | gpt-4o                               |          5    |          15    |
| OpenAI     | gpt-4o-2024-08-06                    |          2.5  |          10    |
| OpenAI     | gpt-4o-2024-05-13                    |          5    |          15    |
| OpenAI     | gpt-4o-mini                          |          0.15 |           0.6  |
| OpenAI     | gpt-4o-mini-2024-07-18               |          0.15 |           0.6  |
| OpenAI     | text-embedding-3-small               |          0.02 |           0.02 |
| OpenAI     | text-embedding-3-large               |          0.13 |           0.13 |
| OpenAI     | ada v2                               |          0.1  |           0.1  |
| OpenAI     | gpt-4o-mini-2024-07-18 (fine-tuning) |          0.3  |           1.2  |
| Mistral    | open-mistral-nemo-2407               |          0.27 |           0.27 |
| Mistral    | large-2407                           |          2.7  |           8.2  |
| Mistral    | codestral-mamba                      |          0.2  |           0.2  |
| Mistral    | codestral-2405                       |          0.9  |           2.8  |
| Mistral    | mistral-embed                        |          0.1  |           0.1  |
| Mistral    | open-mistral-7b                      |          0.2  |           0.2  |
| Mistral    | open-mixtral-8x7b                    |          0.65 |           0.65 |
| Mistral    | open-mixtral-8x22b                   |          1.9  |           5.6  |
| Mistral    | mistral-small-latest                 |          0.9  |           2.8  |
| Mistral    | mistral-medium-latest                |          2.5  |           7.5  |
| Anthropic  | Claude 3.5 Sonnet                    |          3    |          15    |
| Anthropic  | Claude 3 Opus                        |         15    |          75    |
| Anthropic  | Claude 3 Haiku                       |          0.25 |           1.25 |
| Anthropic  | Claude 3 Sonnet                      |          3    |          15    |
| Anthropic  | Claude 2.1                           |          8    |          24    |
| Anthropic  | Claude 2.0                           |          8    |          24    |
| Anthropic  | Claude Instant                       |          0.8  |           2.4  |
|------------|--------------------------------------|---------------|----------------|

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support 💬

If you need help or have queries, please open an issue. We will get back to you as soon as possible!

## Acknowledgements 🙏

- Thanks to all the LLM providers for their transparent pricing information.
- Contributors who spend time improving this repo.
