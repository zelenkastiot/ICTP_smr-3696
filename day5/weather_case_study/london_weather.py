import altair as alt
import pandas as pd

# read in data
data = pd.read_csv("./data/london_weather_2021.csv")

# only look at weather data from this year (2022)
data["DATE"] = pd.to_datetime(data["DATE"], format="%Y-%m-%d")
london_2022 = data.loc[(data["DATE"] >= "2022-01-01")]
print(london_2022.head())


highlight = alt.selection_single(on="mouseover")


# how is the rain distributed throughout the year? When did these huge rain days happen? When are the so-called 200 "dry" days we saw in the binned plot happening?
precip_time = (
    alt.Chart(london_2022)
    .mark_line()
    .encode(alt.X("DATE:T"), alt.Y("PRCP:Q"), tooltip=["DATE:T", "PRCP:Q"])
    .properties(title="Daily temperature in London (2022)", width=1000, height=500)
)

# what is the distribution of high-low rain days in a different way
precip = (
    alt.Chart(london_2022)
    .mark_bar()
    .encode(alt.X("TMAX:Q"), alt.Y("count(TMAX)"))
    .properties(title="Count of temperature in London 2022")
)

# maybe I want to bin this data (quantitative data harder)
precip_binned = (
    alt.Chart(london_2022)
    .mark_bar()
    .encode(alt.X("TMAX:Q", bin=True), alt.Y("count(TMAX)"))
    .properties(title="Count of TMAX in London 2022")
).transform_bin("binned_precip", "TMAX", bin=alt.Bin(maxbins=10))

# how does the rain amount break down per month?
# Are there really dry/really rainy months?
precip_time_month = (
    alt.Chart(london_2022)
    .mark_line(color="black")
    .encode(
        alt.X("yearmonth(DATE):T"),
        alt.Y("average(TMAX):Q"),
        tooltip=[
            alt.Tooltip("average(TMAX):Q", format=",.2f", title="Avg month precip")
        ],
    )
    .properties(title="Average Monthly TMAX in London 2022", width=800, height=500)
)

# so this gives the average, but what if I want to show the full range here?
line = precip_time_month.mark_trail(opacity=0.8).encode(
    alt.X("DATE:T"),
    alt.Y("TMAX:Q"),
    alt.Size("average(TMAX)"),
    alt.Color("month(DATE):N", scale=alt.Scale(scheme="tableau20")),
    tooltip=["DATE:T", "TMAX"],
)

(precip_time_month + line).add_selection(highlight).show()
