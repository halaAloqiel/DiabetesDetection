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
            html.P(["Introduction:",
                html.Br(),
                "Diabetes is a chronic health condition which affects how your body turns food into energy. The food that we consume is broken down into glucose(sugar) and is released into the bloodstream. Normally, when the sugar in the bloodstream increases, the pancreas releases insulin which acts as a key to let the blood in our body’s be uses as energy. However, a diabetic person either doesn’t make enough insulin or can’t use the insulin it makes as well as it should. Diabetes can cause health problems such as heart disease, vision loss, and kidney disease. ",
                html.Br(),
                html.Br(),
                "Scope:",
                html.Br(),
                "This project demonstrates the detection of Diabetes using machine learning classification algorithms. Using the data found at Kaggle, which contains 22 columns and over 25 thousand rows. The features that I’m using, includes the Diabetes indicator, which tells us weather the patient has diabetes or not, BMI, HighBP, HighChol, age, sex, smoker, stroke.  This project applies logistic regression, decision Tree classification, gradient boost classification, and random forest classification model to predict whether a person is at a risk of getting diabetes.  "

                ])
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
