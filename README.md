# Transition Risk Pipeline

This repository implements a minimal, question-driven data pipeline to answer:

**"Where are transition risks concentrated across local areas?"**

The architecture is organised directly around the data and analytical steps needed
to compute a transition risk score from publicly-available UK datasets.

Pipeline stages:
1. Load dataset registry
2. Ingest required datasets
3. Harmonise geographies and formats
4. Compute transition indicators
5. Generate a composite risk score
6. Export charts and tables

To run:
    python pipeline/run_transition_risk_pipeline.py

