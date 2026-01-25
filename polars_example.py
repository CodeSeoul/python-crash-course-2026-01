import polars


dataframe_csv = polars.read_csv("sample.csv",
                                try_parse_dates=True)
print(dataframe_csv)

result = dataframe_csv.group_by(
    polars.col("employee"),
).agg(
    polars.col("hours").sum()
)
print(result)
