import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime
from metadata.metadata_store import MetadataStore, MetadataEntry

REGISTRY = Path("registry/transition_risk_sources.yaml")

def load_registry():
    with REGISTRY.open("r") as f:
        return yaml.safe_load(f)["datasets"]

def ingest_all_sources():
    datasets = load_registry()
    store = MetadataStore()

    for ds in datasets:
        dataset_id = ds["id"]
        raw_dir = Path(f"data/raw/{dataset_id}")
        raw_dir.mkdir(parents=True, exist_ok=True)

        # Placeholder ingestion logic
        df = pd.DataFrame({"area_code": ["A"], "value": [1]})
        out_path = raw_dir / "latest.csv"
        df.to_csv(out_path, index=False)

        store.append(MetadataEntry(
            dataset_id=dataset_id,
            event="ingested",
            timestamp=datetime.utcnow().isoformat(),
            details={"path": str(out_path)}
        ))

    return True

