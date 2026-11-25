from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "diabetic_data.csv"
PROCESSED_DIR = ROOT / "data" / "processed"
CLEAN = PROCESSED_DIR / "clean.csv"
FEATURES = PROCESSED_DIR / "features.csv"

RANDOM_STATE = 42
TARGET = "target"            # 1 if readmitted < 30 days, else 0
GROUP_COL = "patient_nbr"    # same patient can have many encounters -> split by group
