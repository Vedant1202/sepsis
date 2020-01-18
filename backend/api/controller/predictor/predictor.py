import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR
import math
import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.iolib.smpickle import load_pickle





def getPredictions(patientId=None):
    # read csv
    finaldf = pd.read_csv('finaldf.csv')
    finaldf.drop(['vitalperiodicid'], axis=1, inplace=True)

    # setup variables
    patIds = finaldf['patientunitstayid'].unique()
    wbcVals = finaldf['wbc'].unique()

    if not patientId:
        rno = np.random.randint(0, 10, size=1)[0]
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
                 'actual': finaldf})


getPredictions()

























#
