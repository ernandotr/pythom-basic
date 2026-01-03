import plotly.express as px
import pandas as pd

data = {
    "labels": ["A", "B", "C", "D", "E", "F", "G"],
    "parents": ["", "A", "A", "B", "B", "C", "D"],
    "values": [10, 14, 12, 7, 7, 6, 4]
}

fig = px.sunburst(data, names='labels', parents='parents', values='values')
fig.update_layout(title_text="Sunburst Chart Example", title_x=0.5)
fig.show()