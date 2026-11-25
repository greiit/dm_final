"""Download the Diabetes 130-US Hospitals dataset (UCI id=296) to data/raw/."""
from pathlib import Path
from ucimlrepo import fetch_ucirepo

out = Path(__file__).resolve().parents[1] / "data" / "raw"
out.mkdir(parents=True, exist_ok=True)

ds = fetch_ucirepo(id=296)
df = ds.data.original  # features + targets together
df.to_csv(out / "diabetic_data.csv", index=False)
print(f"Saved {df.shape[0]} rows, {df.shape[1]} columns to {out / 'diabetic_data.csv'}")
