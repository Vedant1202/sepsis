from flask import Flask, render_template #this has changed
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
app = Flask(__name__)

def create_plot(rate):

    #rate1=3
    valuelist1=[rate[0],4-rate[0]]
    trace1=go.Pie(values=valuelist1,hole=.6)
    fig1=go.Figure(data1)
    fig1.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig1.update_layout(annotations=[dict(text=str(rate[0])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    #rate2=3
    valuelist2=[rate[1],4-rate[1]]
    trace2=go.Pie(values=valuelist2,hole=.6)
    fig2=go.Figure(data2)
    fig2.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig2.update_layout(annotations=[dict(text=str(rate[1])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    #rate3=3
    valuelist3=[rate[2],4-rate[2]]
    trace3=go.Pie(values=valuelist3,hole=.6)
    fig3=go.Figure(data3)
    fig3.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig3.update_layout(annotations=[dict(text=str(rate[2])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    #rate4=3
    valuelist4=[rate[3],4-rate[3]]
    trace4=go.Pie(values=valuelist4,hole=.6)
    fig4=go.Figure(data4)
    fig4.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig4.update_layout(annotations=[dict(text=str(rate[3])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    data1 = [trace1]
    data2 = [trace2]
    data3 = [trace3]
    data4 = [trace4]

    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    multi_graph={'pie1':graph1JSON,'pie2':graph2JSON,'pie3':graph3JSON, 'pie4':graph4JSON}

    return multi_graph

@app.route('/')
def index():

    bar = create_plot()
    return render_template('index.html', plot=bar)


if __name__ == '__main__':
    app.run()
