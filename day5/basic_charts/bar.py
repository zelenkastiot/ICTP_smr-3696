import altair as alt
import pandas as pd

penguins_data = pd.read_json("./data/penguins.json")
print(penguins_data.head())

# how many of each species of penguin are there?
penguin_species_bar = (
    alt.Chart(penguins_data)
    .mark_bar()
    .encode(alt.Y("Species:N", sort="x"), x="count()", color="Species")
    .properties(title="Number of Penguins by Species")
)

penguin_species_bar.configure_title(fontSize=20, anchor="start").save(
    "./basic_charts_html_output/bar.html"
)

# how does beak depth distribution vary between penguin species?
penguin_species_beak_depth_histo = (
    alt.Chart(penguins_data)
    .mark_bar(opacity=0.3, binSpacing=0)
    .encode(
        alt.X("Beak Depth (mm)", bin=True),
        alt.Y("count()", stack=None),
        alt.Color("Species:N"),
    )
    .properties(title="Penguin Beak Depth by Species")
)

penguin_species_beak_depth_histo.configure_title(fontSize=20, anchor="start").save(
    "./basic_charts_html_output/histo.html"
)

penguin_species_bar.show()
penguin_species_beak_depth_histo.show()