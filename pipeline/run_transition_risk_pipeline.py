from scripts.ingestion.ingest_transition_sources import ingest_all_sources
from scripts.harmonisation.harmonise_transition_data import harmonise_all
from scripts.scoring.score_transition_risk import compute_score
from scripts.output.generate_transition_risk_report import export_report

def run():
    ingest_all_sources()
    harmonised = harmonise_all()
    scores = compute_score(harmonised)
    export_report(scores)
    print(scores.head())

if __name__ == "__main__":
    run()

