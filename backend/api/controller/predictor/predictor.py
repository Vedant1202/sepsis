import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR
import math
import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.iolib.smpickle import load_pickle
import plotly
import plotly.graph_objs as go
from flask import jsonify
import json


def create_plot(dfact, dfpred, dfmarker, rate):


    trace0=go.Scatter(
    x=dfact.index, # assign x as the dataframe column 'x'
    y=dfact['heartrate'],
    #mode = 'lines+markers'
    )
    trace1=go.Scatter(
    x=dfpred.index, # assign x as the dataframe column 'x'
    y=dfpred['heartrate'],
    #mode = 'lines+markers'
    )
    data1 = [trace0,trace1]
    fig1=go.Figure(data1)
    fig1.update_layout(
        shapes=[
        # 1st highlight during Feb 4 - Feb 6
        go.layout.Shape(
            type="rect",
            # x-reference is assigned to the x-values
            xref="x",
            # y-reference is assigned to the plot paper [0,1]
            yref="y",
            x0=0,
            y0=90,
            x1=250,
            y1=120,
            fillcolor="#ff0000",
            opacity=0.07,
            layer="below",
            line_width=0,
        )])
    fig1.update_xaxes(range=[-30,240])
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)



    trace2=go.Scatter(
    x=dfact.index, # assign x as the dataframe column 'x'
    y=dfact['temperature'],
    # mode = 'lines+markers'
    )
    trace3=go.Scatter(
    x=dfpred.index, # assign x as the dataframe column 'x'
    y=dfpred['temperature'],
    # mode = 'lines+markers'
    )
    data2 = [trace2,trace3]
    fig2=go.Figure(data2)
    fig2.update_layout(
        shapes=[
        # 1st highlight during Feb 4 - Feb 6
        go.layout.Shape(
            type="rect",
            # x-reference is assigned to the x-values
            xref="x",
            # y-reference is assigned to the plot paper [0,1]
            yref="y",
            x0=0,
            y0=35,
            x1=250,
            y1=36,
            fillcolor="#ff0000",
            opacity=0.07,
            layer="below",
            line_width=0,
        ),
        go.layout.Shape(
            type="rect",
            # x-reference is assigned to the x-values
            xref="x",
            # y-reference is assigned to the plot paper [0,1]
            yref="y",
            x0=0,
            y0=38,
            x1=250,
            y1=39,
            fillcolor="#ff0000",
            opacity=0.07,
            layer="below",
            line_width=0,
        )])
    fig2.update_xaxes(range=[-30,240])
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)



    trace4=go.Scatter(
    x=dfact.index, # assign x as the dataframe column 'x'
    y=dfact['respiration'],
    # mode = 'lines+markers'
    )
    trace5=go.Scatter(
    x=dfpred.index, # assign x as the dataframe column 'x'
    y=dfpred['respiration'],
    # mode = 'lines+markers'
    )
    data3 = [trace4,trace5]
    fig3=go.Figure(data3)
    fig3.update_layout(
        shapes=[
        # 1st highlight during Feb 4 - Feb 6
        go.layout.Shape(
            type="rect",
            # x-reference is assigned to the x-values
            xref="x",
            # y-reference is assigned to the plot paper [0,1]
            yref="y",
            x0=0,
            y0=20,
            x1=250,
            y1=23,
            fillcolor="#ff0000",
            opacity=0.07,
            layer="below",
            line_width=0,
        )])
    fig3.update_xaxes(range=[-30,240])
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)


    #rate1=3
    valuelist1=[rate[0],4-rate[0]]
    trace21=go.Pie(values=valuelist1,hole=.6)
    fig21=go.Figure(data21)
    fig21.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig21.update_layout(annotations=[dict(text=str(rate[0])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    #rate2=3
    valuelist2=[rate[1],4-rate[1]]
    trace22=go.Pie(values=valuelist2,hole=.6)
    fig22=go.Figure(data22)
    fig22.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig22.update_layout(annotations=[dict(text=str(rate[1])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    #rate3=3
    valuelist3=[rate[2],4-rate[2]]
    trace23=go.Pie(values=valuelist3,hole=.6)
    fig23=go.Figure(data23)
    fig23.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig23.update_layout(annotations=[dict(text=str(rate[2])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    #rate4=3
    valuelist4=[rate[3],4-rate[3]]
    trace24=go.Pie(values=valuelist4,hole=.6)
    fig24=go.Figure(data24)
    fig24.update_traces(hoverinfo='none',textinfo='none',marker=dict(colors=["#00bfff","#ffffff"]))
    fig24.update_layout(annotations=[dict(text=str(rate[3])+'/4',x=0.51,y=0.4,font_size=45)],showlegend=False)

    data21 = [trace21]
    data22 = [trace22]
    data23 = [trace23]
    data24 = [trace24]

    graph21JSON = json.dumps(fig21, cls=plotly.utils.PlotlyJSONEncoder)
    graph22JSON = json.dumps(fig22, cls=plotly.utils.PlotlyJSONEncoder)
    graph23JSON = json.dumps(fig23, cls=plotly.utils.PlotlyJSONEncoder)
    graph24JSON = json.dumps(fig24, cls=plotly.utils.PlotlyJSONEncoder)

    pie={'heartRatePie':graph21JSON,'temperaturePie':graph22JSON,'respirationPie':graph23JSON, 'wbcPie':graph24JSON}




    multi_graph={'heartrate':graph1JSON,'temperature':graph2JSON,'respiration':graph3JSON,'pieCharts':pie}

    return multi_graph




def getPredictions(patientId=None):
    # read csv
    finaldf = pd.read_csv('finaldf.csv')
    finaldf.drop(['vitalperiodicid'], axis=1, inplace=True)

    # setup variables
    patIds = finaldf['patientunitstayid'].unique()
    wbcVals = finaldf['wbc'].unique()

    if not patientId:
        # rno = np.random.randint(0, 10, size=1)[0]
        rno = 0
        patientId = patIds[rno]

    # get patient dataframe
    finaldf = finaldf[finaldf['patientunitstayid'] == patientId].copy().sort_values(by='observationoffset').reset_index(drop=True)

    newvitalsid = []
    for i in finaldf['observationoffset']:
        newvitalsid.append(i - finaldf['observationoffset'].tolist()[0])

    finaldf['observationoffset'] = pd.Series(newvitalsid)
    finaldf.drop(['patientunitstayid'], axis=1, inplace=True)

    finaldf.set_index('observationoffset', drop=True, inplace=True)
    train = finaldf.drop(['wbc'], axis=1)[:int(0.8*(len(finaldf)))]

    model = VAR(endog=train)
    model_fit = model.fit()

    prediction = model_fit.forecast(model_fit.y, steps=48)
    preds = prediction
    prediction = pd.concat([pd.DataFrame(prediction, columns=['heartrate', 'respiration', 'temperature']),
                           pd.DataFrame([wbcVals[rno]]*48, columns=['wbc'])], axis=1)

    new_ind = list(range(train.index[-1], train.index[-1] + 240, 5))
    prediction = pd.concat([prediction, pd.DataFrame(new_ind, columns=['new_ind'])], axis=1)
    prediction = prediction.set_index(['new_ind']).copy()

    crits = []
    for i in preds:
        count = 0
        if i[2] > 38 or i[2] < 36:
            count += 1
        if i[0] > 90:
            count += 1
        if i[1] > 20:
            count += 1

        if count > 1:
            crits.append(i)

        crits = pd.DataFrame(crits, columns=['heartrate', 'respiration', 'temperature'])

    print(prediction)
    return dict({'predictions': prediction,
                 'critical': crits,
                 'actual': train})


def get_graph():
        try:
            preds = getPredictions()
            plot = create_plot(preds['actual'], preds['predictions'], preds['critical'])
            resp = jsonify(data=plot)
            resp.status_code = 200
            return resp
        except Exception as e:
            print('====================== EXCEPTION ========================')
            print(e)
        # finally:
            # cursor.close()
            # conn.close()
create_plot()























#
