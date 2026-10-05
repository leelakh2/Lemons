import pandas as pd

input_file = "ibtracs.ALL.list.v04r01.csv"
output_file = "ibtracs_global_1945_present_daily.csv"

df = pd.read_csv(
    input_file,
    low_memory=False,
    skiprows=[1]
)

# Make year numeric
df["SEASON"] = pd.to_numeric(df["SEASON"], errors="coerce")

# Keep only 1945-present
df = df[df["SEASON"] >= 1945]

# Convert time to a real date
df["ISO_TIME"] = pd.to_datetime(df["ISO_TIME"], errors="coerce")
df["DATE"] = df["ISO_TIME"].dt.strftime("%Y-%m-%d")

# Keep only the variables we actually need
df = df[
    [
        "SID",
        "SEASON",
        "NAME",
        "DATE",
        "BASIN",
        "LAT",
        "LON",
        "USA_WIND",
        "USA_SSHS"
    ]
]

# Keep one location record per storm per day
df = df.drop_duplicates(
    subset=["SID", "DATE"],
    keep="first"
)

# Save final smaller dataset
df.to_csv(output_file, index=False)

print("Done!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("File created:", output_file)