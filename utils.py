from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor

import plotly.express as px
import plotly.graph_objs as go
import numpy as np

def grapht(df1, model_value):

    df1.dropna(inplace =True)
    Z = df1[['Dosage, g/t']].astype(float)
    y =  df1['Output, t/h']


    fig = px.scatter(df1, x = 'Dosage, g/t', y = "Output, t/h", )
    fig.add_trace(go.Scatter(mode='lines', x  = df1['Dosage, g/t'] , y =model_list(df1[['Dosage, g/t']],df1['Output, t/h'])[model_value].predict(df1[['Dosage, g/t']]), name = "predicted output" ))
    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="left",
     ))
    return fig



def model_list( X, y):

    pipe=Pipeline([ ('polynomial', PolynomialFeatures(include_bias=False, degree=2)), ('model',LinearRegression())])
    DT =  DecisionTreeRegressor()
    ereg = VotingRegressor(estimators=[ ('rf', pipe), ('lr', DT)])

    pipe.fit(X, y)
    DT.fit(X, y)
    ereg.fit(X,y)

    modeldata = [pipe, DT, ereg]
    return modeldata


def gh(df1):
    df1['Output, t/h'].loc[1:].replace(0, np.nan, inplace =True)
    df1.dropna(inplace=True)
    return df1
