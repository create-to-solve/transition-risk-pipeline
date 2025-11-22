import json
from dataclasses import dataclass, asdict
from pathlib import Path

STORE_PATH = Path("metadata/metadata_log.jsonl")

@dataclass
class MetadataEntry:
    dataset_id: str
    event: str
    timestamp: str
    details: dict

class MetadataStore:
    def append(self, entry: MetadataEntry) -> None:
        STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with STORE_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(entry)) + "\n")

