import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/countries_quality_of_life_index.18-10-2021.csv')

# Creating gets values of quality of life index for each name
new_df = df

# Sorting values
new_df = new_df.sort_values(by=['QualityOfLifeIndex'], ascending=[False])

# Preparing data
data = [go.Bar(x=new_df['Name'], y=new_df['QualityOfLifeIndex'])]

# Preparing layout
layout = go.Layout(title='Countries quality of life index', xaxis_title="Countries",
                   yaxis_title="Quality Of Life Score")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
