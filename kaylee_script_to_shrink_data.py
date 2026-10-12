import glob
import os
import pandas as pd

input_data = glob.glob("*.dat")[0]       # monthly temperature file
input_stations = glob.glob("*.inv")[0]   # station locations file
output_file = "ghcnm_global_1945_present_monthly.csv.gz"

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

# Read station locations (fixed-width text file)
stations = pd.read_fwf(
    input_stations,
    colspecs=[(0, 11), (12, 20), (21, 30)],
    names=["STATION_ID", "LAT", "LON"]
)

# Keep stations between 60S and 60N (where shark attacks and hurricanes occur)
stations = stations[(stations["LAT"] >= -60) & (stations["LAT"] <= 60)]
stations["LAT"] = stations["LAT"].round(2)
stations["LON"] = stations["LON"].round(2)

# Read monthly temperatures: one row per station per year, 12 months across
df = pd.read_fwf(
    input_data,
    colspecs=[(0, 11), (11, 15)] + [(19 + 8*i, 24 + 8*i) for i in range(12)],
    names=["STATION_ID", "YEAR"] + months
)

# Keep only 1945-present
df = df[df["YEAR"] >= 1945]

# -9999 means missing; convert hundredths of a degree to °C (1 decimal)
for m in months:
    df[m] = (df[m].where(df[m] != -9999) / 100).round(1)

# Drop station-years with no temperature data at all
df = df.dropna(subset=months, how="all")

# Add latitude and longitude so it can be joined with the other datasets
df = stations.merge(df, on="STATION_ID")

# Save final smaller dataset (compressed to fit GitHub's upload limit)
df.to_csv(output_file, index=False, compression="gzip")

print("Done!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("File created:", output_file)
print("Size:", round(os.path.getsize(output_file) / 1e6, 1), "MB")