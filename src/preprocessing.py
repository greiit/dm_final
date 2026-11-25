"""Member A: load_data() and preprocess()."""
import pandas as pd
from . import config


def load_data() -> pd.DataFrame:
    return pd.read_csv(config.RAW, na_values=["?"])


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # TODO (A): duplicates, missing values, outliers, encoding, scaling, transformations.
    # Notes: build binary target from `readmitted`; remove encounters where the patient
    # died or went to hospice (discharge_disposition_id); decide what to do with `weight`
    # (~97% missing) and justify each decision in the report.
    raise NotImplementedError
