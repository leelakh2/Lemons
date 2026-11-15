import pandas as pd

input_file = "ibtracs.ALL.list.v04r01.csv"
output_file = "ibtracs_global_1945_present_daily.csv"

df = pd.read_csv(
    input_file,
    low_memory=False,
    skiprows=[1],
    keep_default_na=False, # pandas was making "NA" label into n/a
    na_values=["", " "],
)

# Make year numeric
df["SEASON"] = pd.to_numeric(df["SEASON"], errors="coerce")

# Keep only 1945-present
df = df[df["SEASON"] >= 1945]

# Convert time to a real date
df["ISO_TIME"] = pd.to_datetime(df["ISO_TIME"], errors="coerce")
df["DATE"] = df["ISO_TIME"].dt.strftime("%Y-%m-%d")

# sort to keep earlier observation of the day
df = df.sort_values(["SID", "ISO_TIME"])

KEEP_COLS = [
    "SID", "SEASON", "NAME", "ISO_TIME", "DATE", "BASIN",
    "LAT", "LON", "USA_WIND", "USA_SSHS", "TRACK_TYPE", "DIST2LAND",
]
df = df[KEEP_COLS]

# Save final smaller dataset
df.to_csv(output_file, index=False)

print("Done!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("File created:", output_file)
