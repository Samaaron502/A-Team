import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/cost of living 2020.csv')

# Creating gets values of quality of life index for each name
new_df = df

# Sorting values
new_df = new_df.sort_values(by=['Cost of Living Index'], ascending=[False])

# Preparing data
data = [go.Bar(x=new_df['Country'], y=new_df['Cost of Living Index'])]

# Preparing layout
layout = go.Layout(title='Countries Cost of living indexes', xaxis_title="Countries",
                   yaxis_title="Cost of Living Score")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart2.html')
