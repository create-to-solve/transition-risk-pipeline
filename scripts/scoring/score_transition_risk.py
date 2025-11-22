import pandas as pd

def compute_score(harmonised):
    bres = harmonised["bres"]
    df = pd.DataFrame()
    df["area_code"] = bres["area_code"]
    df["transition_risk_score"] = 1.0
    return df

