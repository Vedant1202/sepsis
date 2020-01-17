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


def create_plot(dfact, dfpred):


    trace0=go.Scatter(
    x=df1['x'], # assign x as the dataframe column 'x'
    y=df1['y']
    )
    trace1=go.Scatter(
    x=df2['x'], # assign x as the dataframe column 'x'
    y=df2['y'],
    )
    data = [trace0,trace1]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    # return graphJSON
    print(graphJSON)

    # @app.route('/')
    # def index():
    #
    #
    #     bar = create_plot()
    #     return bar


    if __name__ == '__main__':
        # app.run()
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df1 = pd.DataFrame({'x': x[0:21], 'y': y[0:21]})
        df2 = pd.DataFrame({'x': x[20:], 'y': y[20:]})
        create_plot(df1, df2)
