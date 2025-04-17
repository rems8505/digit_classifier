from sklearn.datasets import load_digits
import json

digits = load_digits()

samples = {}
for digit in range(10):
    # Find first sample of this digit
    index = next(i for i, y in enumerate(digits.target) if y == digit)
    samples[digit] = {
        "features": digits.data[index].tolist(),
        "label": int(digits.target[index])
    }

# Print JSON-style examples
for k, v in samples.items():
    print(f"\nDigit: {k}")
    print(json.dumps(v, indent=2))
