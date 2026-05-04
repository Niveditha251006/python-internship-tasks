import pandas as pd

try:
    df = pd.read_csv("data.csv")

    print("Dataset:\n", df)

    print("\nAverage Marks:", df["Marks"].mean())
    print("Highest Marks:", df["Marks"].max())
    print("Lowest Marks:", df["Marks"].min())

    # Filter students >80
    top_students = df[df["Marks"] > 80]
    print("\nTop Students:\n", top_students)

except Exception as e:
    print("Error:", e)