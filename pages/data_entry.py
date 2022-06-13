import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback_context
import dash
import dash_table
import pandas as pd
from utils import grapht, model_list,gh
from app import app
import json
from dash.exceptions import PreventUpdate




def create_layout(app):

    return    dbc.Container([

                       dbc.Row(
                                dbc.Col(html.H4('Dosage and relative mill output'),
                                style={"height": "100%", "textAlign" :"center"})),


                       dbc.Row(
                           dbc.Col(
                              dash_table.DataTable(id = 'table_mill',   export_format='xlsx',
                                 export_headers='display',
                                 editable=True,
                                 style_header={ "backgroundColor": "#1E90FF", "fontSize": "18px","color": "white", 'textAlign': 'center', 'height': 'auto', 'width':'auto'},
                                 style_data={'whiteSpace': 'normal', 'height': 'auto' },
                                 fixed_rows={"headers": False},style_cell={"width": "auto", "fontSize": "auto",'textAlign': 'center'},
                                style_data_conditional=[
                                  {
                                   'if': {'row_index': 'odd'},'backgroundColor': 'gainsboro'},

                                   {'if': {'column_id': 'время'},
                                      'whiteSpace': 'normal','height': 'auto', 'lineHeight': '15px' }
                                                        ],
                                  sort_action="native",
                                  sort_mode="multi",
                                  page_action="native",
                                  page_size= 14,
                                  page_current= 2,
                                  row_deletable=True,
                                                ),
                                      ),
                             ),

                          dbc.Row(
                             dbc.Col([
                                 dbc.Button('add row', id='row_button',
                              n_clicks=0, outline=True, size ='lg', color = 'primary'),
                                 dbc.Button('save', id='save_button',
                                 n_clicks=0, outline=True,  size ='lg', color ="primary")],

                              )
                             ),

                     dbc.Row(
                                   dbc.Col(html.H4('Dosage response curve'),
                                   style={"height": "100%", "textAlign" :"center"})),

                    dbc.Row(dbc.Col(dcc.Dropdown( id = 'drop_model',
                                                   options=[
                          {'label': 'Polinomial regression', 'value': 0},
                          {'label': 'Decisison tree', 'value': 1},
                          {'label': 'Ensemble', 'value': 2},
                                                          ],
                            value=2, persistence=True

                        ))),

                        dbc.Row(

                            dbc.Col([
                                     dcc.Graph(id='mill_ouput_graph')
                                    ], className ="mt-2")
                               )
])


@app.callback(
    Output('table_mill', 'data'),
    Output('table_mill', 'columns'),
    Output('storing', 'data'),

    Output('intermediate-value', 'data'),
    Output('mill_ouput_graph', 'figure'),
    Output('model_value_list', 'data'),
    


    Input('row_button', 'n_clicks'),
    Input('save_button', 'n_clicks'),
    Input('drop_model', 'value'),

    State('storing','data'),
    State('table_mill', 'data'),
    State('table_mill', 'columns'))

def add_row(row_clicks,save_click, model_value, storing, data_table, columns_table):
    if row_clicks  is None:
        raise PreventUpdate
    else:
        ctx = dash.callback_context
        ctrl_id = ctx.triggered[0]['prop_id'].split('.')[0]
        df=pd.read_json(storing, orient='split')


        if data_table is None:
            rows = df.to_dict("records")


        else:
            rows = data_table
        columns  = [{"id": c, "name": c} for c in  df.columns]




        if row_clicks  is None:
            raise PreventUpdate

        else:
             if  ctrl_id == 'row_button':
                 rows.append({c['id']: 0 for c in columns[:1]})
                 df1=pd.DataFrame(rows, columns=[c['name'] for c in columns])
                 df1= df1.astype("float")
                 df1.dropna(inplace =True)
                 df1.sort_values(by = df1.columns[0], ascending=True, inplace =True)


                 df=df1.to_json(date_format='iso', orient='split')
                 model_value_list = json.dumps({'model_value':model_value})


                 return rows, columns, df, df, grapht(df1, model_value),model_value_list


             elif ctrl_id == 'save_button':
                 df1=pd.DataFrame(rows, columns=[c['name'] for c in columns])
                 df1=df1.astype("float")
                 df1.dropna(inplace =True)
                 df1.sort_values(by = df1.columns[0], ascending=True, inplace =True)
                 df=df1.to_json(date_format='iso', orient='split')
                 last_page = json.dumps({'last':len(df1)})
                 model_value_list = json.dumps({'model_value':model_value})


                 return rows, columns, df, df, grapht(df1, model_value),model_value_list


             else:
                 df1=pd.DataFrame(rows, columns=[c['name'] for c in columns])
                 df=df1.to_json(date_format='iso', orient='split')
                 df1=df1.astype("float")

                 model_value_list = json.dumps({'model_value':model_value})


                 return rows, columns, df , df, grapht(df1, model_value),model_value_list
