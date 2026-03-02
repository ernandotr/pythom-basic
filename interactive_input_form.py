import ipywidgets as w
from IPython.display import display

slider = w.IntSlider(description ="Value", min=0, max=100)

checkbox = w.Checkbox(description="Enable")
text = w.Text(description="Name")

display(w.VBox([slider, checkbox, text]))
