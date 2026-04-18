import json
import random
import os

def fact_for_atlantic() -> str:
    path = os.path.join("oceans", "json", "atlantic_facts.json")
    with open(path, "r") as f:
        facts = json.load(f)
    return random.choice(facts)

def fact_for_pacific() -> str:
    path = os.path.join("oceans", "json", "pacific_facts.json")
    with open(path, "r") as f:
        facts = json.load(f)
    return random.choice(facts)
