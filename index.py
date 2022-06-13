import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from pages import data_entry, value_model, graph, introduction
from app import app


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "0rem",
    "bottom": 0,
    "padding": "2rem 1rem",
    "background-color": "azure",
    "padding": "2rem 1rem",

}

CONTENT_STYLE = {

    "padding": "6rem 2rem",
    "background-color":"PaleTurquoise"

}

sidebar = dbc.Col(html.Div(
    [
        html.H4("Dosage optimization", className="display-6"),
        html.Hr(),
        html.P(
            "page navigation", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("INTRODUCTION", href="/introduction", active ="exact"),
                dbc.NavLink("DATA ENTRY", href="/data_entry", active="exact"),
                dbc.NavLink("VALUE MODEL", href="/value_model", active="exact"),
                dbc.NavLink("GRAPH", href="/graph", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
), width=2)



content = dbc.Col(dbc.Card(id="page-content", style=CONTENT_STYLE), width={"size": True, "offset": 1},className = 'shadow-lg p-3 mb-2  rounded' )


store = dcc.Store(id='intermediate-value', data=None, storage_type='session')
cost_model = dcc.Store(id='cost_model', data=None, storage_type='session')

datat = pd.DataFrame({'Dosage, g/t':[0], 'Output, t/h':[0]})
data1 = datat.to_json(date_format='iso', orient='split')
zalupa =  dcc.Store(id='storing', data=data1, storage_type='session')
hub = dcc.Store(id ='model_value_list', data=None, storage_type='session')




def serve_layout():

    return dbc.Container(dbc.Row([dcc.Location(id="url"), sidebar, content, store, cost_model, zalupa, hub]))

app.layout=serve_layout


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/data_entry":
        return data_entry.create_layout(app)
    elif pathname == "/value_model":
        return value_model.create_layout(app)
    elif pathname == "/graph":
        return graph.create_layout(app)
    elif pathname =="/introduction":
        return introduction.create_layout(app)

    else:
        return data_entry.create_layout(app)




if __name__ == "__main__":
    app.run_server(port=8000,debug=True, dev_tools_ui= True,dev_tools_props_check= True )
