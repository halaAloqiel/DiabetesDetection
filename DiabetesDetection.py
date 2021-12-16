import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

data = pd.read_csv("data/diabetes.csv")

app = dash.Dash(__name__)

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])


app.layout = html.Div([

    html.Div(className="app-header",
             children=html.H1('Diabetes Detection')),
    dbc.Row([
        dbc.Col(
            html.P("Introduction:")
        ),


        dbc.Col([
            dcc.Graph(figure = px.histogram(data , x="Diabetes_012")),
            dcc.Graph(figure = px.histogram(data , x="HighBP")),
            dcc.Graph(figure = px.histogram(data , x="HighChol")),
            dcc.Graph(figure = px.histogram(data , x="Age", color="Diabetes_012")),
            dcc.Graph(figure = px.histogram(data , x="BMI"))
         ])
    ])
])

if __name__=='__main__':
    app.run_server(debug=True)