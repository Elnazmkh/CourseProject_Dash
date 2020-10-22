import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

sensor1_shared = pd.read_csv(DATA_PATH.joinpath("sensor1_shared.csv"), index_col=0)
sensor2_shared = pd.read_csv(DATA_PATH.joinpath("sensor2_shared.csv"), index_col=0)
sensor3_shared = pd.read_csv(DATA_PATH.joinpath("sensor3_shared.csv"), index_col=0)

sensor1_shared.index = pd.to_datetime(sensor1_shared.index)
sensor2_shared.index = pd.to_datetime(sensor2_shared.index)
sensor3_shared.index = pd.to_datetime(sensor3_shared.index)


#joining data
s1 = sensor1_shared.Detection.resample('D').count().to_frame()
s1 = s1/s1.max()
s2 = sensor2_shared.Detection.resample('D').count().to_frame()
s2 = s2/s2.max()
s3 = sensor3_shared.Detection.resample('D').count().to_frame()
s3 = s3/s3.max()
g12 = s1.join(s2, lsuffix='_Sensor1', rsuffix='_Sensor2', how='outer').fillna(0)
g13 = s1.join(s3, lsuffix='_Sensor1', rsuffix='_Sensor3', how='outer').fillna(0)
g23 = s2.join(s3, lsuffix='_Sensor2', rsuffix='_Sensor3', how='outer').fillna(0)


#sensor 1 and sensor 2
fig12 = go.Figure()
fig12.add_trace(
    go.Scatter(x=list(g12.index),
               y=list(g12.Detection_Sensor1),
               name="Sensor1",
               line=dict(color="#97151c")))
fig12.add_trace(
    go.Scatter(x=list(g12.index),
               y= list(g12.Detection_Sensor2),
               name="Sensor2",
               visible=False,
               line=dict(color="#827e7e")))
fig12.update_layout(
yaxis_title="No. of Detections",
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Sensor1",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Sensor1"}]),
                dict(label="Sensor2",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Sensor2"}]),
                dict(label="Both - Pearson",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Pearson Correlation = " + str(g12.corr(method = 'pearson').iloc[1][0])}]),
                dict(label="Both - Kendall",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Kendall Correlation = " + str(g12.corr(method = 'kendall').iloc[1][0]) }]),
                dict(label="Both - Spearman",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Spearman Correlation = " + str(g12.corr(method = 'spearman').iloc[1][0]) }]),
            ]),
        )
    ])
fig12.update_layout()

#Sensor 1 and Sensor 3
fig13 = go.Figure()
fig13.add_trace(
    go.Scatter(x=list(g13.index),
               y=list(g13.Detection_Sensor1),
               name="Sensor1",
               line=dict(color="#97151c")))
fig13.add_trace(
    go.Scatter(x=list(g13.index),
               y= list(g13.Detection_Sensor3),
               name="Sensor3",
               visible=False,
               line=dict(color="#3db87b")))
fig13.update_layout(
yaxis_title="No. of Detections",
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Sensor1",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Sensor1"}]),
                dict(label="Sensor3",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Sensor3"}]),
                dict(label="Both - Pearson",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Pearson Correlation = " + str(g13.corr(method='pearson').iloc[1][0])}]),
                dict(label="Both - Kendall",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Kendall Correlation = " + str(g13.corr(method='kendall').iloc[1][0])}]),
                dict(label="Both - Spearman",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Spearman Correlation = " + str(g13.corr(method='spearman').iloc[1][0])}]),
            ]),
        )
    ])
fig13.update_layout()

#Sensor 2 , 3
fig23 = go.Figure()
fig23.add_trace(
    go.Scatter(x=list(g23.index),
               y=list(g23.Detection_Sensor2),
               name="Sensor2",
               line=dict(color="#827e7e")))
fig23.add_trace(
    go.Scatter(x=list(g23.index),
               y= list(g23.Detection_Sensor3),
               name="Sensor3",
               visible=False,
               line=dict(color="#3db87b")))
fig23.update_layout(
yaxis_title="No. of Detections",
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Sensor2",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Sensor2"}]),
                dict(label="Sensor3",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Sensor3"}]),
                dict(label="Both - Pearson",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Pearson Correlation = " + str(g23.corr(method='pearson').iloc[1][0])}]),
                dict(label="Both - Kendall",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Kendall Correlation = " + str(g23.corr(method='kendall').iloc[1][0])}]),
                dict(label="Both - Spearman",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "Spearman Correlation = " + str(g23.corr(method='spearman').iloc[1][0])}]),
            ]),
        )
    ])
fig23.update_layout()



def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    #Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Sensor 1 & Sensor 2", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-56",
                                        figure=fig12,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns")]

                        , className='row'),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Sensor 1 & Sensor 3", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-57",
                                        figure=fig13,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns")]

                        , className='row'),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Sensor 2 & Sensor 3", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-58",
                                        figure=fig23,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns")]
                        , className='row'),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
