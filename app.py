from dash import Dash, html, dcc, Input, Output
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import dash_bootstrap_components as dbc
from kafka import KafkaConsumer
from json import loads
import psycopg2
import json

conn = psycopg2.connect(database = "root", user = "root", password = "secret", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

global top3, top3_2

top3 = {}
top3_2 = {}

app = Dash(__name__, external_stylesheets=external_stylesheets)

consumer = KafkaConsumer(
    'topic3',
    bootstrap_servers=['localhost:29092'],
    value_deserializer=lambda x: loads(x),
    auto_offset_reset='earliest'
)

consumer2 = KafkaConsumer(
    'topic3_2',
    bootstrap_servers=['localhost:29092'],
    value_deserializer=lambda x: loads(x),
    auto_offset_reset='earliest'
)

def update_graph():
    try:
        horizontal = make_subplots(rows=1, cols=1, specs=[[{}]], shared_xaxes=True, shared_yaxes=False, vertical_spacing=0.001)
       
        df = pd.DataFrame(list(zip(list(top3.keys()), list(top3.values()))), columns =['name', 'val'])
        df = df.sort_values(by='val', ascending=False)
            
        horizontal.append_trace(go.Bar(
            x=df["val"],
            y=df["name"],
            marker=dict(
                color='rgba(50, 171, 96, 0.6)',
                line=dict(
                    color='rgba(50, 171, 96, 1.0)',
                    width=1
                ),
            ),
            orientation='h',
        ), 1, 1)

        horizontal.update_layout(
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=True,
                domain=[0, 0],
            ),
            xaxis=dict(
                zeroline=False,
                showline=False,
                showticklabels=False,
                showgrid=False,
                domain=[0, 0.2],
            ),
            legend=dict(x=0.029, y=1.038, font_size=10),
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgb(255,255,255)',
            plot_bgcolor='rgb(255,255,255)',
        )

        horizontalAnnotations = []

        y_s = np.round(df["val"], decimals=2)

        for yd, xd in zip(y_s, df["name"]):
            horizontalAnnotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd + 10,
                            text=str(yd) + ' Person',
                            font=dict(family='Arial', size=12,
                                    color='rgb(50, 171, 96)'),
                            showarrow=False))
        horizontal.update_layout(annotations=horizontalAnnotations)
    except Exception as e: print(f"[ERROR]: {e}")
    return horizontal

def update_graph2():
    try:

        horizontal = make_subplots(rows=1, cols=1, specs=[[{}]], shared_xaxes=True, shared_yaxes=False, vertical_spacing=0.001)
        df_sentiment = pd.DataFrame(list(zip(list(top3_2.keys()), list(top3_2.values()))), columns =['name', 'val'])
        df_sentiment = df_sentiment.sort_values(by='val', ascending=False).head(10)

        horizontal.append_trace(go.Bar(
                y=df_sentiment["val"],
                x=df_sentiment["name"],
                marker=dict(
                    color='rgba(50, 171, 96, 0.6)',
                    line=dict(
                        color='rgba(50, 171, 96, 1.0)',
                        width=1
                    ),
                ),
        ), 1, 1)

        horizontal.update_layout(
                yaxis=dict(
                    showgrid=True,
                    showline=True,
                    showticklabels=True,
                    title='Number of Persons',
                ),
                xaxis=dict(
                    zeroline=False,
                    showline=False,
                    showticklabels=True,
                    showgrid=False,
                ),
                legend=dict(x=0.029, y=1.038, font_size=10),
                margin=dict(l=0, r=0, t=0, b=0),
                paper_bgcolor='rgb(255,255,255)',
                plot_bgcolor='rgb(255,255,255)',
            )

    except Exception as e: print(f"[ERROR]: {e}")
    return horizontal

def getConsumer():
    try:
        for message in consumer:
            if message:
                print(message)
                top3[str(json.loads(message.key.decode('utf-8')))] = dict(message.value)["TOTAL"]
        
    except Exception as e: print(f"[ERROR]: {e}")   

def getConsumer2():
    try:
        for message in consumer2:
            if message:
                print(message)
                top3_2[str(json.loads(message.key.decode('utf-8')))] = dict(message.value)["TOTAL"]
        
    except Exception as e: print(f"[ERROR]: {e}")   

app.layout = html.Div(children=[
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0),
    html.Div(
        className = "centent-wrapper",
        children = [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            className = "box-centent-wrapper",
                            children=[
                                html.H1("What are some of the reasons that make you eat comfort food.", style = { "flex": "1" }),
                              
                            ],
                            style = { "height": "auto" }
                        ),
                        html.Div(
                            className = "box-centent-wrapper",
                            children=[
                                dcc.Graph(
                                    id='top-data',
                                    style = { "flex": "1" },
                                ),
                            ]
                        ),
                    ]
                )
            )
        ]
    ),
    html.Div(
        className = "centent-wrapper",
        children = [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            className = "box-centent-wrapper",
                            children=[
                                html.H1("Comfort foods that come to mind.", style = { "flex": "1" }),
                            ],
                            style = { "height": "auto" }
                        ),
                        html.Div(
                            className = "box-centent-wrapper",
                            children=[
                                dcc.Graph(
                                    id='message-data',
                                    style = { "flex": "1" }
                                ),
                            ]
                        ),
                    ],
                )
            )
        ], style={"margin-top": "1rem"}
    ),
], style = { "padding": "1rem", "backgroundColor": "whitesmoke",  "height": "100vh"})
    
@app.callback(
    Output('top-data', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph_live(n):
    if n == 0:
        getConsumer()
    return update_graph()

@app.callback(
    Output('message-data', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph_live2(n):
    if n == 0:
        getConsumer2()
    return update_graph2()

if __name__ == '__main__':
    app.run_server(debug=True)
  
