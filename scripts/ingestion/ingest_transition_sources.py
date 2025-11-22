from datetime import datetime
from pathlib import Path

import yaml

from metadata.metadata_store import MetadataEntry, MetadataStore
from scripts.ingestion.download_utils import download_file, load_csv, load_xlsx

REGISTRY = Path("registry/transition_risk_sources.yaml")


def load_registry():
    with REGISTRY.open("r") as f:
        return yaml.safe_load(f)["datasets"]


def ingest_all_sources():
    datasets = load_registry()
    store = MetadataStore()
    loaded_data = {}

    for dataset in datasets:
        dataset_id = dataset["id"]
        dataset_format = dataset.get("format", "").lower()
        url = dataset["url"]

        if dataset_format == "csv":
            loader = load_csv
        elif dataset_format == "xlsx":
            loader = load_xlsx
        else:
            raise ValueError(f"Unsupported dataset format: {dataset_format}")

        timestamp = datetime.utcnow()
        timestamp_str = timestamp.strftime("%Y%m%dT%H%M%SZ")

        raw_dir = Path("data/raw") / dataset_id
        raw_dir.mkdir(parents=True, exist_ok=True)

        timestamp_path = raw_dir / f"{timestamp_str}.{dataset_format}"
        latest_path = raw_dir / f"latest.{dataset_format}"

        download_file(url, timestamp_path)
        latest_path.write_bytes(timestamp_path.read_bytes())

        df = loader(timestamp_path)
        loaded_data[dataset_id] = df

        store.append(
            MetadataEntry(
                dataset_id=dataset_id,
                event="ingested",
                timestamp=timestamp.isoformat(),
                details={
                    "file_path": str(timestamp_path),
                    "status": "success"
                },
            )
        )

    return loaded_data
