import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import pathlib
from utils import Header, make_dash_table_with_header , sensor_trend , df_preview

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

sensor1_df = pd.read_csv(DATA_PATH.joinpath("sensor1.csv"))
sensor2_df = pd.read_csv(DATA_PATH.joinpath("sensor2.csv"))
sensor3_df = pd.read_csv(DATA_PATH.joinpath("sensor3.csv"))
sensor1_shared = pd.read_csv(DATA_PATH.joinpath("sensor1_shared.csv"), index_col=0)
sensor2_shared = pd.read_csv(DATA_PATH.joinpath("sensor2_shared.csv"), index_col=0)
sensor3_shared = pd.read_csv(DATA_PATH.joinpath("sensor3_shared.csv"), index_col=0)


#Graph 1 - Monthly
a = sensor_trend(sensor1_df,'Month')
a.insert(0,0)
b = sensor_trend(sensor2_df,'Month')
b.insert(0,0)
c = sensor_trend(sensor3_df,'Month')

#Graph 2 - Daily shared Time
sensor1_shared.index = pd.to_datetime(sensor1_shared.index)
sensor2_shared.index = pd.to_datetime(sensor2_shared.index)
sensor3_shared.index = pd.to_datetime(sensor3_shared.index)
shared_dates = sensor1_shared.resample('D').count().index


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Project Summary"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    In this project we will be analyzing a series of real-life data sets. \
                                    We now have 3 motion detection datasets, each \
                                    with their own format as follows.We convert these datasets into data frames\
                                    with a uniform format (data wrangling, data cleaning etc.) and datetime as \
                                    the index.Then for each dataset, we plot the distribution of detection\
                                    and investigate if the detection from the detectors are correlated? If we could\
                                    identify that there are correlations, it means that the detectors are detecting\
                                     in the same area.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    html.Div(
                        [
                            html.H5("Data", className="subtitle padded"),
                            html.Br([]),
                            html.Div(
                                [
                                    html.P(
                                        "let's take a look at the data to get a better understanding of the time range for the detections."
                                    ),
                                ],
                                style={"color": "#7a7a7a"},
                            ),
                        ],
                        className="row",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Sensor1"], className="subtitle padded"
                                            ),
                                    html.Table(make_dash_table_with_header(df_preview(sensor1_df,2,2))),
                                ],
                                className="four columns",
                                    ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Sensor2"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table_with_header(df_preview(sensor2_df,2,2))),
                                ],
                                className="four columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Sensor3"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table_with_header(df_preview(sensor3_df,2,2))),
                                ],
                                className="four columns",
                                     ),
                        ]
                    ),


                    # Row 3
                    html.Div(
                        [
                            # graph monthly
                            html.Div(
                                [
                                    html.H5(
                                        "Monthly Distribution of Detections",
                                        className="subtitle padded",
                                    ),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                " As we can see all the sensors did \
                                                 detections mainly in April and the early May\
                                                 . However sensor 3 has been detecting since some date in March."
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "March",
                                                        "April",
                                                        "May"
                                                    ],
                                                    y=a,
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Sensor 1",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "March",
                                                        "April",
                                                        "May"
                                                    ],
                                                    y=b,
                                                    marker={
                                                        "color": "#827e7e",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Sensor 2",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "March",
                                                        "April",
                                                        "May"
                                                    ],
                                                    y=c,
                                                    marker={
                                                        "color": "#3db87b",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Sensor 3",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.4,
                                                font={"family": "Raleway", "size": 12},
                                                height=500,
                                                hovermode="closest",
                                                legend={
                                                    "x": 0,
                                                    "y": -0.15,
                                                    "orientation": "h",
                                                    "yanchor": "bottom",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=450,
                                                xaxis={
                                                    "autorange": True,
                                                    #"range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    #"range": [0, 100000000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "Detections Percentage",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),

                                ],
                                className="six columns"
                                ), # row 3 column 1

                            #daily graph
                            html.Div(
                                [
                                    html.H5(
                                        "Daily Distribution of Detections in Shared Time",
                                        className="subtitle padded",
                                    ),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "The number of daily detections for both sensor 1 and 3 has been \
                                                 somehow decreasing till around 18th and 19th and has suddenly\
                                                  started to grow till around 29 and then we seem to have had a \
                                                   decrease again while in sensor 2 the data is more fluctiated \
                                                   and seems not to follow a certain pattern or even if there is any\
                                                   , it is not simillar to those two."
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x= shared_dates,
                                                    y=[2, 0, 29, 38, 56, 65, 69, 20, 70, 72, 64, 68, 71],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Sensor 1",
                                                ),
                                                go.Bar(
                                                    x=shared_dates,
                                                    y=[977, 777, 805, 681, 415, 460, 594, 629, 880, 836, 666, 348, 592],
                                                    marker={
                                                        "color": "#827e7e",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Sensor 2",
                                                ),
                                                go.Bar(
                                                    x=shared_dates,
                                                    y = [3420, 2224, 2815, 3297, 3118, 2756, 2200, 4228, 4105, 3234, 3325, 1615, 2432],
                                                    marker={
                                                        "color": "#3db87b",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Sensor 3",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.2,
                                                font={"family": "Raleway", "size": 12},
                                                height=500,
                                                hovermode="closest",
                                                legend=
                                                {
                                                    "x": 0.2,
                                                    "y": -0.4,
                                                    "orientation": "h",
                                                    #"yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 40,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=400,
                                                xaxis={
                                                    "autorange": True,
                                                    # "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 100000000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "Detections",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            )
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 4
                    html.Div(
                        [
                            # graph monthly
                            html.Div(
                                [
                                    html.H5(
                                        "Average Daily Detection in Shared Time",
                                        className="subtitle padded",
                                    ),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                " According to the graph, Sensor 3 has the most daily number of detections."
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                    dcc.Graph(
                                        id="graph-3",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        'Sensor 1',
                                                        'Sensor 2',
                                                        'Sensor 3'
                                                    ],
                                                    y=[sensor1_shared.Detection.resample('D').count().mean(),
                                                       sensor2_shared.Detection.resample('D').count().mean(),
                                                       sensor3_shared.Detection.resample('D').count().mean()],
                                                    marker={
                                                        "color": "#acf4d1",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Means",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.4,
                                                font={"family": "Raleway", "size": 12},
                                                height=300,
                                                width = 450,
                                                hovermode="closest",
                                                legend={
                                                    "x": 0,
                                                    "y": -0.15,
                                                    "orientation": "h",
                                                    #"yanchor": "bottom",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 30,
                                                    "l": 50,
                                                },
                                                showlegend=False,
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },

                                                yaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "Detections Percentage",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),

                                ],
                                className="six columns"
                            ),  # row 4 column 1

                            # daily graph
                            html.Div(
                                [
                                    html.H5(
                                        "Average Hourly Detection in Shared Time",
                                        className="subtitle padded",
                                    ),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                " According to the graph, Sensor 3 has the most hourly number of detections."
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        'Sensor 1',
                                                        'Sensor 2',
                                                        'Sensor 3'
                                                    ],
                                                    y=[sensor1_shared.Detection.resample('H').count().mean(),
                                                       sensor2_shared.Detection.resample('H').count().mean(),
                                                       sensor3_shared.Detection.resample('H').count().mean()],
                                                    marker={
                                                        "color": "#eb6868",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 1,
                                                        },
                                                    },
                                                    name="Means",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.4,
                                                font={"family": "Raleway", "size": 12},
                                                height=300,
                                                width=450,
                                                hovermode="closest",
                                                legend={
                                                    "x": 0,
                                                    "y": -0.15,
                                                    "orientation": "h",
                                                    # "yanchor": "bottom",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 30,
                                                    "l": 50,
                                                },
                                                showlegend=False,
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },

                                                yaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "Detections Percentage",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),

                                ],
                                className="six columns",
                            )
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
