import dash
import dash_bootstrap_components as dbc

import json
from app import app
import pandas as pd
import numpy as np


from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from utils import grapht,model_list


valued =  dbc.InputGroupText("$/t", style ={"width":"50px"})

def create_layout(app):
    return  html.Div( children = [

                         dbc.Row(
                                  dbc.Col(html.Div(html.H4('Value model'),
                                  style={"height": "100%", "textAlign" :"center"}), className="mb-4")),
                                  html.Div('separator is "."'),

                       dbc.Row([dbc.Col(
                          dbc.InputGroup(
                           [
                             dbc.InputGroupText("Mill power",   style ={"width":"150px"}),
                             dbc.Input(placeholder="Amount", id = "mill_power",type="number", persistence=True),
                             dbc.InputGroupText("kW"),
                           ],
                                         )
                               ),
                       dbc.Col(dbc.InputGroup(
                           [
                             dbc.InputGroupText("Electricity", style ={'width':"150px"}),
                             dbc.Input(placeholder="Amount", id = "electricity", type="number", persistence=True),
                             dbc.InputGroupText("$/kWh"),
                           ],
                           ))
                       ],    className="g-6"),

              dbc.Row([dbc.Col(dbc.InputGroup(
                        [
                          dbc.InputGroupText("Ancillares",  style ={'width':"150px"}),
                          dbc.Input(placeholder="Amount", id ="ancillares" ,type="number", persistence=True),
                          dbc.InputGroupText("kW"),
                        ],
                        )),
                        dbc.Col((dbc.InputGroup(
                                  [
                                    dbc.InputGroupText("R&M", style ={'width':"150px"} ),
                                    dbc.Input(placeholder="Amount", id = "r&m", type="number", persistence=True),
                                    valued

                                  ],

                                  )))
                        ], ),

                 dbc.Row([dbc.Col(dbc.InputGroup(
                                   [
                                     dbc.InputGroupText("Currency",  style ={'width':"150px"}),
                                     dbc.Input(placeholder="currency", persistence=True),
                                     dbc.InputGroupText("", style={"width":"50px"}),
                                   ],
                                   )),
                                   dbc.Col((dbc.InputGroup(
                                             [
                                               dbc.InputGroupText("Annual production", style ={'width':"150px"} ),
                                               dbc.Input(placeholder="Amount", id = "annual_production", type="number", persistence=True),
                                               dbc.InputGroupText("t", style={"width":"50px"}),

                                             ],

                                             )))
                                   ], ),






                 dbc.Row([dbc.Col(
                                   dbc.InputGroup(
                                                    [
                                                   dbc.InputGroupText("Additive name", style={"width":"150px"}),
                                                   dbc.Input(placeholder="Blank"),
                                                   dbc.Input(placeholder="additive name", persistence=True),
                                                    dbc.InputGroupText("", style={"width":"50px"}),

                                                     ]
                                                  )
                                  ),

                          ], className ="mt-2"),

                 dbc.Row([dbc.Col(
                                   dbc.InputGroup(
                                                    [
                                                   dbc.InputGroupText("Additive cost", style={"width":"150px"}),
                                                   dbc.Input(placeholder="0"),
                                                   dbc.Input(placeholder="Amount", type="number" , id ='additive_cost', persistence=True),
                                                   dbc.InputGroupText("$,t", style={"width":"50px"}),
                                                     ]
                                                  )
                                  ),

                          ]),








                     dbc.Row(dbc.Col(
                                      dbc.InputGroup(

                              [
                               dbc.InputGroupText("Additive dosage", style={"width":"150px"}),
                               dbc.InputGroupText(html.Output(id = 'dosage'),   style ={"width":556, "color":"blue", "backgroundColor": "white"}),
                               dbc.InputGroupText("g/t", style ={"width":"50px"})

                              ])), className = "g - 0"),


                 dbc.Row(dbc.Col( html.Div(dcc.Slider (id ='slider_dosage', max= 800, min =1, persistence=True,
                  tooltip={"placement": "bottom", "always_visible": True}),style ={"width":"100%", "backgroundColor": "PaleTurquoise",   "componentColor": "red" }))),



                    dbc.Row(dbc.Col(
                                     dbc.InputGroup(

                             [
                              dbc.InputGroupText("Mill output", style={"width":"150px"}),
                              dbc.InputGroupText(html.Output(id = 'mill_output_blank'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                              #dbc.Input(placeholder="Amount", type="number" , id ='mill_output_blank' ),
                              dbc.InputGroupText(html.Output(id = 'mill_output_additive'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                              dbc.InputGroupText("t/h", style ={"width":"50px"})

                             ])), className = "g - 0"),

                            dbc.Row(dbc.Col(
                                             dbc.InputGroup(

                                     [
                                      dbc.InputGroupText("Efficiency", style={"width":"150px"}),
                                      dbc.InputGroupText(html.Output(id = 'efficiency_blank'),    style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                      dbc.InputGroupText(html.Output(id = 'efficiency_additive'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                      dbc.InputGroupText("kW/t", style ={"width":"50px"})

                                     ])), className = "g - 0"),

                         dbc.Row(dbc.Col(
                                                     dbc.InputGroup(

                                             [
                                              dbc.InputGroupText("Energy cost", style={"width":"150px"}),
                                              dbc.InputGroupText(html.Output(id = 'energy_cost_blank'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                              dbc.InputGroupText(html.Output(id = 'energy_cost_additive'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                              dbc.InputGroupText("$/t", style ={"width":"50px"})

                                             ])), className = "g - 0"),

                         dbc.Row(dbc.Col(
                                                         dbc.InputGroup(

                                                 [
                                                  dbc.InputGroupText("R&M cost", style={"width":"150px"}),
                                                  dbc.InputGroupText(html.Output(id = 'rm_cost_blank'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                                  dbc.InputGroupText(html.Output(id = 'rm_cost_additive'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                                  dbc.InputGroupText("$/t", style ={"width":"50px"})

                                                 ])), className = "g - 0"),





                                 dbc.Row(dbc.Col(
                                                                         dbc.InputGroup(

                                                                 [
                                                                  dbc.InputGroupText("SUM", style={"width":"150px"}),
                                                                  dbc.InputGroupText(html.Output(id = 'sum_blank'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                                                  dbc.InputGroupText(html.Output(id = 'sum_additive'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                                                  dbc.InputGroupText("$/t", style ={"width":"50px"})

                                                                 ])), className = "g - 0"),


                                 dbc.Row(dbc.Col(
                                                                             dbc.InputGroup(

                                                                         [
                                                                          dbc.InputGroupText("Saving", style={"width":"150px"}),
                                                                          dbc.InputGroupText(html.Output(id = 'dosage1'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                                                          dbc.InputGroupText(html.Output(id = 'saving'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                                                          dbc.InputGroupText("$/t", style ={"width":"50px"})

                                                                         ])), className = "g - 0"),


                                     dbc.Row(dbc.Col(
                                                                                 dbc.InputGroup(

                                                                             [
                                                                              dbc.InputGroupText("Treatment cost", style={"width":"150px"}),
                                                                              dbc.InputGroupText(html.Output(id = 'dosage1'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                                                              dbc.InputGroupText(html.Output(id = 'tcost'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                                                              dbc.InputGroupText("$/t", style ={"width":"50px"})

                                                                             ])), className = "g - 0"),
                                     dbc.Row(dbc.Col(
                                                                                 dbc.InputGroup(

                                                                             [
                                                                              dbc.InputGroupText("Net saving", style={"width":"150px"}),
                                                                              dbc.InputGroupText(html.Output(id = 'dosage1'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                                                              dbc.InputGroupText(html.Output(id = 'net_saving'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                                                              dbc.InputGroupText("$/t", style ={"width":"50px"})

                                                                             ])), className = "g - 0"),

                                     dbc.Row(dbc.Col(
                                                                                 dbc.InputGroup(

                                                                             [
                                                                              dbc.InputGroupText("Annual saving", style={"width":"150px"}),
                                                                              dbc.InputGroupText(html.Output(),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                                                              dbc.InputGroupText(html.Output(id = 'sum_ann'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                                                              dbc.InputGroupText("$", style ={"width":"50px"})

                                                                             ])), className = "g - 0"),

                                         dbc.Row(dbc.Col(
                                                                                     dbc.InputGroup(

                                                                                 [
                                                                                  dbc.InputGroupText("Return", style={"width":"150px"}),
                                                                                  dbc.InputGroupText(html.Output(),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),
                                                                                  dbc.InputGroupText(html.Output(id = 'return_add'),   style ={"width":278, "color":"blue", "backgroundColor": "white"}),

                                                                                  dbc.InputGroupText("%", style ={"width":"50px"})

                                                                                 ])), className = "g - 0")




      ])





@app.callback(
    Output('dosage', 'children'),
    Output('mill_output_blank', 'children'),
    Output('mill_output_additive', 'children'),
    Output('efficiency_blank', 'children'),
    Output('efficiency_additive', 'children'),
    Output('energy_cost_blank', 'children'),
    Output('energy_cost_additive', 'children'),
    Output('rm_cost_blank', 'children'),
    Output('rm_cost_additive', 'children'),
    Output('sum_blank', 'children'),
    Output('sum_additive', 'children'),
    Output('saving', 'children'),
    Output('tcost', 'children'),
    Output('net_saving', 'children'),
    Output('sum_ann', 'children'),
    Output('return_add', 'children'),
    Output('cost_model', 'data'),





    Input('slider_dosage', 'value'),
    Input('mill_power', 'value'),
    Input('ancillares', 'value'),
    Input('electricity', 'value'),
    Input('r&m', 'value'),
    Input ('additive_cost', 'value'),
    Input ('annual_production', 'value'),
    Input('intermediate-value', 'data'),
    Input('model_value_list','data')




    )
def update_output(dosage, mill_power, ancillares,electricity,rm, additive_cost,annual_production, model_value, model_value_list):


         dff = pd.read_json(model_value, orient='split')
         dff.dropna(inplace =True)
         Z = dff[['Dosage, g/t']].astype(float)
         y = dff['Output, t/h'].astype(float)
         d=json.loads(model_value_list)["model_value"]
         #pipe.fit(Z,y)

         if len(dff['Output, t/h'].loc[dff['Dosage, g/t']==0]) == 0:
             mill_output_blank = round (model_list(Z,y)[d].predict([[0]]).item(0))
         else:
             mill_output_blank = dff['Output, t/h'].loc[dff['Dosage, g/t']==0].iloc[0]



         mill_output_additive= round (model_list(Z,y)[d].predict([[dosage]]).item(0))

         tot_power =  mill_power+ ancillares
         efficiency_blank= round(tot_power /mill_output_blank,2)
         efficiency_additive = round(tot_power /mill_output_additive,2)
         energy_cost_blank = round(efficiency_blank*electricity,2)
         energy_cost_additive = round(efficiency_additive *electricity,2)

         rm_additive = round (mill_output_blank/mill_output_additive*rm,2)
         sum_blank = round (energy_cost_blank+rm,2)
         sum_additive = round (energy_cost_additive+rm_additive,2)
         saving = round (sum_blank-sum_additive,2)
         tcost = round ( dosage*additive_cost/1000000,2)
         net_saving = round(saving-tcost,2)
         total_saving= round (net_saving *annual_production)
         return_add= round (net_saving/tcost*100,2)

         dictionary= {'dosage': dosage, 'mill_power': mill_power, 'ancillares': ancillares,'electricity': electricity,'rm':rm, 'additive_cost' :additive_cost}
         hui  =  json.dumps(dictionary)




         return dosage,  mill_output_blank , mill_output_additive, efficiency_blank, efficiency_additive, energy_cost_blank , energy_cost_additive, rm, rm_additive, sum_blank, sum_additive, saving, tcost, net_saving, total_saving, return_add, hui
