The main purpose of this project is simple; to scrape BBC Good Food's website for recipes,
which can then be used to figure out what to make for your next meal, based on ingredients you currently have.

The main files' purpose are as follows:
Data gathering & cleanup.ipynb: as the title suggests, this file is used to scrape the BBC's recipes, and clean the data for further use.
Recipe assistent.py: the chatbot that uses the recipes data. Asks you for the ingredients you have, what kind of meal you want to make, and whether to generate it. Runs on ollama
recipes.csv: the cleaned recipes data

(improve the current readme with the things below, there are a few things missing):

## Installation
It is recommended to use a virtual environment.

Dependencies are currently not specified in a requirements.txt file. 
Adding one would improve reproducibility.

## Usage

### Data collection
Run the notebook:
Data gathering & cleanup.ipynb

### Recipe assistant
Run:
python "Recipe assistent.py"

Note: The assistant uses Ollama. Make sure Ollama is installed and running.

## Notes
- A requirements.txt file is currently missing
- Adding explicit dependencies would improve reproducibility and usability