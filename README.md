# Recipe Assistant

Scrapes BBC Good Food for recipes and helps you decide what to cook based on the ingredients you have. Optionally generates step-by-step instructions using a local LLM.

## Files

| File | Purpose |
|------|---------|
| `Data gathering & cleanup.ipynb` | Scrapes BBC Good Food and outputs `recipes.csv` |
| `Recipe assistent.py` | Interactive assistant — matches your ingredients to recipes |
| `recipes.csv` | Pre-scraped dataset (410 recipes, ready to use) |

## Requirements

Python 3.8+ and the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

For the LLM feature you also need [Ollama](https://ollama.com) installed and running locally with the `llama3` model:

```bash
# Install ollama from https://ollama.com, then:
ollama pull llama3
ollama serve
```

## Usage

Run the recipe assistant:

```bash
python "Recipe assistent.py"
```

You will be prompted for:
1. **Ingredients** — comma-separated, e.g. `chicken, garlic, lemon`
2. **Meal type** — `breakfast`, `lunch`, `dinner`, or press Enter to skip
3. **LLM generation** — type `y` to get full instructions (requires Ollama running)

## Re-scraping data

Open and run `Data gathering & cleanup.ipynb` to re-scrape BBC Good Food. This overwrites `recipes.csv`.
