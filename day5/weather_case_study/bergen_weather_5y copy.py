import altair as alt
import pandas as pd

# but now I want to compare this over 5 years
bergen_florida_5y = pd.read_csv("weather_case_study/data/bergen_weather_2018_22.csv")

highlight = alt.selection(
    type="single", on="mouseover", fields=["year(DATE)"], nearest=True
)

base = (
    alt.Chart(bergen_florida_5y)
    # .mark_line()
    .encode(
        alt.X("month(DATE):T"),
        alt.Y("average(PRCP)"),
        color=alt.condition(highlight, "year(DATE):N", alt.value("lightgray")),
        # color="year(DATE):N",
        tooltip=[
            alt.Tooltip("average(PRCP):Q", format=",.2f", title="Avg month precip")
        ],
    ).properties(title="Average Monthly Rain in Bergen 2018-22", width=500, height=500)
)

points = base.mark_circle().encode(opacity=alt.value(0)).add_selection(highlight)

lines = base.mark_line().encode(
    # size=alt.condition(~highlight, alt.value(1), alt.value(3))
    color=alt.condition(highlight, "year(DATE):N", alt.value("lightgray")),
)

base.save("./weather_case_study/output/6_precip_month_2018_22.html")

# # this looks cool, but is very cluttered. What if we just plotted CI instead?
# # add a bootstrapped 95% confidence interval band
# band = precip_time_month.mark_errorband(extent="ci", opacity=0.2).encode(
#     alt.Y("PRCP:Q", title="Precip"),
#     alt.Color("year(DATE):N"),
# )
# (band + precip_time_month).save(
#     "./weather_case_study/output/7_precip_month_2018_22_band.html"
# )
