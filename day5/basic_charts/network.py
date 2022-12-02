# code from https://infovis.fh-potsdam.de/tutorials/infovis7networks.html
# if doing network, need to run (if you don't already have)
# python3 -m pip install networkx nx_altair

import altair as alt
import networkx as nx
import nx_altair as nxa

import requests
import json

# create a random graph
G_ran = nx.fast_gnp_random_graph(n=50, p=0.1)

# draw graph with nx_altair
nxa.draw_networkx(G_ran)  # .show()

###########################################################
# show connections in Les Mis
url = "http://bost.ocks.org/mike/miserables/miserables.json"

lesmis = json.loads(requests.get(url).text)

# we specify that the dataset is not a multigraph, there are no self-loops
# or multiedges, multiple edges between nodes
G = nx.readwrite.json_graph.node_link_graph(lesmis, multigraph=False)
print(nx.info(G))  # print how many nodes and how many edges are in graph

# find connectedness of nodes
degrees = dict(G.degree(G.nodes()))

# save the degrees as a node attribute
nx.set_node_attributes(G, degrees, "degree")
pos = nx.spring_layout(
    G,
    seed=1
)  # spring layout is default, but nx has other options (https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)

nxa.draw_networkx(
    G,
    pos,
    # width='value:Q',
    node_size="degree:Q",
    node_color="group:N",
    cmap="category10",  # pass colormap that is used
    node_tooltip="name:N",
    linewidths=0,  # remove borders from circles
).properties(width=600, height=500,).configure_view(strokeWidth=0)

# rectangular selection in the network view
selection = alt.selection_interval(encodings=['x', 'y'])

# group selection in the bar chart
selection2 = alt.selection(type="multi", fields=['group'])


# first we create the force-directed layout
chart = nxa.draw_networkx( G, pos=pos,
    node_size=100,
    node_color='group:N',
    width='value:Q',
    node_tooltip='name',
    linewidths=0
)

# get node and edge layers from chart
edges = chart.layer[0]
nodes = chart.layer[1]

# group numbers (needed to keep bar chart stable during selections)
groups = list(range(1,10))

# separate color definition used across both charts
color = alt.Color('group:N', scale=alt.Scale(domain=groups), legend=None)

# adjust node opacity and fill color according to selections
nodes = nodes.encode(
    opacity=alt.condition(selection, alt.value(1), alt.value(0.25)),
    fill=alt.condition(selection2, color, alt.value('lightgray')),
).add_selection(selection,selection2).properties(width=500, height=400)

# interactive bar chart 
bars = alt.Chart(nodes.data).mark_bar().encode(
    x=alt.X('count()', scale=alt.Scale(domain=(0,20))),
    y = alt.Y('group:O', scale=alt.Scale(domain=(groups))),
    color=color,
    opacity=alt.condition(selection2, alt.value(1), alt.value(0.25)),
).transform_filter(selection).add_selection(selection2).properties(width=500, height=200)

# concatenate all layers into one multi-view layout
alt.vconcat(edges+nodes, bars).show()