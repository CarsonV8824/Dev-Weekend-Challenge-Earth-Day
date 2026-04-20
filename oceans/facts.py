import json
import random
import os

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fact_for_atlantic() -> str:
    path = os.path.join(PROJECT_ROOT, "oceans", "json", "atlantic_facts.json")
    with open(path, "r") as f:
        facts = json.load(f)
    return random.choice(facts)

def fact_for_pacific() -> str:
    path = os.path.join(PROJECT_ROOT, "oceans", "json", "pacific_facts.json")
    with open(path, "r") as f:
        facts = json.load(f)
    return random.choice(facts)
