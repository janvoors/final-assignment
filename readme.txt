The main purpose of this project is simple; to scrape BBC Good Food's website for recipes,
which can then be used to figure out what to make for your next meal, based on ingredients you currently have.

The main files' purpose are as follows:
Data gathering & cleanup.ipynb: as the title suggests, this file is used to scrape the BBC's recipes, and clean the data for further use.
Recipe assistent.py: the chatbot that uses the recipes data. Asks you for the ingredients you have, what kind of meal you want to make, and whether to generate it. Runs on ollama
recipes.csv: the cleaned recipes data