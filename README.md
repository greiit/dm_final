<<<<<<< HEAD
# Prediction of 30-day Hospital Readmission for Diabetic Patients

**Course:** Data Mining, Final Project
**Team:** Kumar Aray, Zhumabek Askerbekuly, Izimbetova Aigerim
**Project type:** Classification

## Problem
Predict whether a diabetic patient will be readmitted to the hospital within 30 days of discharge
(`readmitted == "<30"` vs. everything else). Early readmissions are costly and often preventable,
so identifying high-risk patients helps hospitals target follow-up care.

## Dataset
Diabetes 130-US Hospitals for Years 1999-2008 (UCI Machine Learning Repository, id 296).
Link: https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008
(Verify record/feature counts and license on the page and record them in the report.)

## Setup
```bash
git clone https://github.com/greiit/dm_final
cd diabetes-readmission
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/download_data.py  # saves the raw data to data/raw/
```

## File structure
```
README.md
requirements.txt
TASKS.md                  # who does what
data/                     # raw data is NOT committed (see data/README.md)
scripts/download_data.py
src/                      # shared code: config, preprocessing, features, models
notebooks/                # 01_preprocessing, 02_eda_features, 03_modeling
reports/                  # report, slides, TEAM_CONTRIBUTIONS.md
```

## Run order
1. `python scripts/download_data.py`
2. `notebooks/01_preprocessing.ipynb` -> writes `data/processed/clean.csv`
3. `notebooks/02_eda_features.ipynb` -> writes `data/processed/features.csv`
4. `notebooks/03_modeling.ipynb` -> trains, tunes and evaluates models

## Reproducibility
All random seeds come from `src/config.py` (`RANDOM_STATE = 42`).
=======
# dm_final
>>>>>>> efa78931b1000d6f2a6b8d2e2756cfeecc82fccf
