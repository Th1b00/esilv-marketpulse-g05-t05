from pathlib import Path
import csv
import json

# Remonte depuis ce fichier jusqu'à trouver le dossier data/
HERE = Path(__file__).resolve().parent
PROJECT_ROOT = next(p for p in [HERE, *HERE.parents] if (p / "data").exists())
DATA_DIR = PROJECT_ROOT / "data" / "sample"


def load_instruments(filepath=DATA_DIR / "instruments.json"):
    """Load and parse JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)


def load_prices(filepath=DATA_DIR / "prices.csv"):
    """Load market observations from CSV into a list of dictionaries."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    """Filter observation dictionaries matching a specific ticker."""
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    """Return the initial close price of a price series as a float."""
    if not prices:
        return 0.0
    return float(prices[0]["close"])


def get_last_close(prices):
    """Return the final close price of a price series as a float."""
    if not prices:
        return 0.0
    return float(prices[-1]["close"])