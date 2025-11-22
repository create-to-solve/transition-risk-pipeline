import pandas as pd
from pathlib import Path

def load_latest(dataset_id: str) -> pd.DataFrame:
    path = Path(f"data/raw/{dataset_id}/latest.csv")
    return pd.read_csv(path)

def harmonise_all():
    bres = load_latest("bres")
    lcree = load_latest("lcree")
    skills_apprenticeships = load_latest("skills_apprenticeships")
    aps = load_latest("aps")
    lfs = load_latest("lfs")
    idbr_business_counts = load_latest("idbr_business_counts")
    energy_consumption = load_latest("energy_consumption")
    la_co2_emissions = load_latest("la_co2_emissions")
    grid_mix = load_latest("grid_mix")
    imd = load_latest("imd")
    population_estimates = load_latest("population_estimates")
    ons_geo_lookups = load_latest("ons_geo_lookups")

    return {
        "bres": bres,
        "lcree": lcree,
        "skills_apprenticeships": skills_apprenticeships,
        "aps": aps,
        "lfs": lfs,
        "idbr_business_counts": idbr_business_counts,
        "energy_consumption": energy_consumption,
        "la_co2_emissions": la_co2_emissions,
        "grid_mix": grid_mix,
        "imd": imd,
        "population_estimates": population_estimates,
        "ons_geo_lookups": ons_geo_lookups,
    }

