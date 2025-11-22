import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT_DIR = Path("outputs")

def export_report(df):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_DIR / "transition_risk_scores.csv", index=False)

    plt.figure()
    plt.bar(df["area_code"], df["transition_risk_score"])
    plt.savefig(OUTPUT_DIR / "transition_risk_chart.png")
    plt.close()

