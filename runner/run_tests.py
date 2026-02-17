import json
from pathlib import Path

def load_cases():
    path = Path(__file__).parent.parent / "tests" / "regression_cases.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run():
    cases = load_cases()
    total = len(cases)
    print(f"Running {total} cases...\n")

    for i, case in enumerate(cases, 1):
        print(f"[{i}] {case['id']} - {case['category']}")
        print(f"Prompt: {case['prompt']}")
        print(f"Expected pattern: {case['expected_pattern']}")
        print("-" * 40)

    print("\nNote: This runner displays expected structural patterns.")
    print("It does not auto-judge models (by design).")

if __name__ == "__main__":
    run()
