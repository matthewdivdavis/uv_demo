import pandas as pd

scores = pd.DataFrame(
    {
        "section": ["A", "A", "B", "B"],
        "score": [82, 94, 88, 92],
    }
)

print(scores.groupby("section")["score"].mean())