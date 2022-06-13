
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from app import app
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
from utils import model_list
import json


def create_layout(app):
    return    html.Div(children =[

                                     dbc.Row(
                                              dbc.Col(html.Div(html.H4('Optimum dosage (dosage g/t for max saving $/t)'),
                                              style={"height": "100%", "textAlign" :"center"}), className="mb-4")),

                                     dcc.Graph(id='figurka')




                                  ])

@app.callback(
              Output('figurka', 'figure'),

              Input('cost_model', 'data'),
              Input('intermediate-value','data'),
              Input('model_value_list', 'data')

                               )

def output_table(value_in, value_table, model_value_list):

     dff = pd.read_json(value_table, orient='split')
     dff.dropna(inplace =True)
     Z = dff[['Dosage, g/t']].astype(float)
     y = dff['Output, t/h'].astype(float)
     d=json.loads(model_value_list)["model_value"]


     if len(dff['Output, t/h'].loc[dff['Dosage, g/t']==0]) == 0:
         mill_output_blank = round (model_list(Z,y)[d].predict([[0]]).item(0))
     else:
         mill_output_blank = dff['Output, t/h'].loc[dff['Dosage, g/t']==0].iloc[0]

     aDict = json.loads(value_in)
     dosage = aDict['dosage']
     mill_power = aDict['mill_power']
     ancillares = aDict['ancillares']
     electricity = aDict['electricity']
     rm = aDict['rm']
     additive_cost = aDict['additive_cost']
     tot_power = mill_power+ancillares



     dfv = pd.DataFrame({"dosage,g/t":[],"output":[]})
     for dosage in range (0,1000,10):
        saving = round(model_list(Z,y)[d].predict([[dosage]]).item(0))
        #roi = saving/(round ( dosage*additive_cost/1000000,2))
        g =   {"dosage,g/t":dosage,"output":saving}
        dfv=dfv.append(g, ignore_index =True)

     dfv['net saving,$/t'] = (tot_power /mill_output_blank*electricity+rm-tot_power /dfv['output'] *electricity+mill_output_blank/dfv['output']*rm)-dfv['dosage,g/t']*additive_cost/1000000


     optimupd=dfv['dosage,g/t'].loc[dfv['net saving,$/t']== dfv['net saving,$/t'].max()].iloc[0]

     fig = px.scatter(dfv, x = 'dosage,g/t',  y ='net saving,$/t', color = 'dosage,g/t')

     fig.add_annotation( xref="x domain",
         yref="y domain", x =0.05, y = 0.95, text = (f"optimum dosage:{optimupd}"),
           showarrow=False, font=dict(family="Courier New, monospace",size=16,
                 color="#0275d8"))


     return fig
