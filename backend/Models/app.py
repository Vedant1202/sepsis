#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template #this has changed
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
# app = Flask(__name__)

N = 40
x = np.linspace(0, 1, N)
y = np.random.randn(N)
print('hello')
df1 = pd.DataFrame({'x': x[0:21], 'y': y[0:21]})
df2 = pd.DataFrame({'x': x[20:], 'y': y[20:]})
df3 = pd.DataFrame({'x': x[20:], 'y': y[20:]})
print(df1)
print(df2)

def create_plot(dfact, dfpred, dfmarker, rate):


    trace0=go.Scatter(
    x=dfact.index, # assign x as the dataframe column 'x'
    y=dfact['heartrate'],
    mode = 'lines+markers'
    )
    trace1=go.Scatter(
    x=dfpred.index, # assign x as the dataframe column 'x'
    y=dfpred['heartrate'],
    mode = 'lines+markers'
    )
    trace6=go.Scatter(
    x=dfmarker.index,
    y=dfmarker['heartrate'],
    mode="markers",
    marker=dict(size=16,color='red')
    )
    trace2=go.Scatter(
    x=dfact.index, # assign x as the dataframe column 'x'
    y=dfact['temperature'],
    mode = 'lines+markers'
    )
    trace3=go.Scatter(
    x=dfpred.index, # assign x as the dataframe column 'x'
    y=dfpred['temperature'],
    mode = 'lines+markers'
    )
    trace7=go.Scatter(
    x=dfmarker.index,
    y=dfmarker['temperature'],
    mode="markers",
    marker=dict(size=16,color='red')
    )
    trace4=go.Scatter(
    x=dfact.index, # assign x as the dataframe column 'x'
    y=dfact['respiration'],
    mode = 'lines+markers'
    )
    trace5=go.Scatter(
    x=dfpred.index, # assign x as the dataframe column 'x'
    y=dfpred['respiration'],
    mode = 'lines+markers'
    )
    trace8=go.Scatter(
    x=dfmarker.index,
    y=dfmarker['respiration'],
    mode="markers",
    marker=dict(size=16,color='red')
    )

    data1 = [trace0,trace1,trace6]
    data2 = [trace2,trace3,trace7]
    data3 = [trace4,trace5,trace8]

    graph1JSON = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3JSON = json.dumps(data3, cls=plotly.utils.PlotlyJSONEncoder)

    multi_graph={'heartrate':graph1JSON,'temperature':graph2JSON,'respiration':graph3JSON}

    return multi_graph
    # print(multi_graph)

    # @app.route('/')
    # def index():
    #
    #
    #     bar = create_plot()
    #     return bar


# if __name__ == '__main__':
#         # app.run()
#     N = 40
#     x = np.linspace(0, 1, N)
#     y = np.random.randn(N)
#     df1 = pd.DataFrame({'x': x[0:21], 'y': y[0:21]})
#     df2 = pd.DataFrame({'x': x[20:], 'y': y[20:]})
#     create_plot(df1, df2)
