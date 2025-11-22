from pathlib import Path

import pandas as pd
import requests


def download_file(url: str, output_path: Path) -> None:
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise ValueError(f"Failed to download {url}: status {response.status_code}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def load_xlsx(path: Path) -> pd.DataFrame:
    return pd.read_excel(path)
