import dash
import dash_bootstrap_components as dbc
from app import app
import dash_html_components as html

def create_layout(app):
    return html.Div(style = dict(textAlign='center'), children=[

        dbc.Card(style = dict(backgroundColor ='#e8f4ff'), children = [
        dbc.Card(dbc.CardBody([
        html.Div([html.H4("Introduction")], className = 'py-2'),

        html.Div(style =dict(textAlign='left', fontSize = 17), children = [

        html.Div([html.P("    The application is designed to estimate the optimum dosage of grinding aids.\
                              Optimum means  lowest dosage at highest output or maximum return.")]),

        html.P("The app is based on very basic machine learning algorithms. The machine learning models use your  data as input to predict new output values."),

        html.Div([html.H5("Manual")], className = 'py-2'),

        html.P(" 1.	Data entry page. Start your field trial,  enter dosage of  grinding aid and relative mill output.\
                    More data is better. The quality of prediction and calculation depends on the size of dataset.\
                    The model requires at least 30 rows( idealy should be 60+), but woks with  few rows as well."),
        html.P(    "Enter mill output  with no GA, at dosage 0 or Blank , if not entered the mill output with no GA\
                     is estimated by the model( is better to avoid for a small dataset)."),

        html.P ("2.	Select a machine learning model(optional)."),
        html.P (" Polynomial regression  – very general model, likely underfitted but requires small dataset."),
        html.P("  Decision tree – usually overfitted , just fitted the  entered data."),
        html.P(" Ensemble – ensemble of polynomial and decision tree, a trade-off between Polynomial  and Decision tree."),
        html.P("Internet browser remembers your selection until its closed."),

        html.P("3. Value model page. Enter the energy cost and other parameters. The mill output will be estimated by the model,\
                   adjust the dosage by the slider. "),
        html.P("4. Graph page. Builds visualization where you can see how the dosage is related to   saving. Generates the optimum dosage depends on your target.")

                     ])  ], ))  ], )
        ])
