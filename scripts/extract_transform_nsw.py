import pandas as pd
from pathlib import Path

# -----------------------------
# Configuration
# -----------------------------
RAW_DATA_PATH = Path("raw_data/population_by_region.xlsx")
OUTPUT_PATH = Path("cleaned_data/nsw_sa2_population_2023_24.csv")
STATE_FILTER = "New South Wales"


# -----------------------------
# Extract
# -----------------------------
def extract_population_data(file_path: Path) -> pd.DataFrame:
    print("Extracting raw population data...")
    df = pd.read_excel(file_path)
    print(f"Raw rows extracted: {len(df)}")
    return df


# -----------------------------
# Transform
# -----------------------------
def transform_nsw_sa2_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Transforming data...")

    # Filter for NSW
    df_nsw = df[df["State"] == STATE_FILTER].copy()
    print(f"Rows after NSW filter: {len(df_nsw)}")

    # Drop rows with missing SA2 or population
    df_nsw = df_nsw.dropna(subset=["SA2", "Population"])

    # Standardise column names
    df_nsw.columns = (
        df_nsw.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert year to integer
    df_nsw["year"] = df_nsw["year"].astype(int)

    # Sort for consistency
    df_nsw = df_nsw.sort_values(by=["sa2", "year"])

    print("Transformation complete.")
    return df_nsw


# -----------------------------
# Load (to CSV)
# -----------------------------
def load_to_csv(df: pd.DataFrame, output_path: Path) -> None:
    print("Loading cleaned data to CSV...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data written to {output_path}")


# -----------------------------
# Main pipeline
# -----------------------------
def main():
    df_raw = extract_population_data(RAW_DATA_PATH)
    df_clean = transform_nsw_sa2_data(df_raw)
    load_to_csv(df_clean, OUTPUT_PATH)
    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    main()
