import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.io as pio
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

sensor1_shared = pd.read_csv(DATA_PATH.joinpath("sensor1_shared.csv"), index_col=0)
sensor2_shared = pd.read_csv(DATA_PATH.joinpath("sensor2_shared.csv"), index_col=0)
sensor3_shared = pd.read_csv(DATA_PATH.joinpath("sensor3_shared.csv"), index_col=0)


#Sensor 1
fig1 = go.Figure()
data1 = [dict(
  x = sensor1_shared.index,
  autobinx = False,
  autobiny = True,
  marker = dict(color = '#8a0000'),
  name = 'Date',
 type = 'histogram',
  xbins = dict(
    start = '2020-04-19 00:00:00',
    end = '2020-05-01 23:59:59',
    size = 'D1'
  )
)]

layout1 = dict(
margin={
        "r": 50,
        "t": 10,
        "l": 50,
        },
    height = 270,
  xaxis = dict(
    type = 'datetime'
  ),
  yaxis = dict(
    title = 'No. of Detections',
    type = 'linear'
  ),
  updatemenus = [dict(
        x = 0.1,
        y = 1.3,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,
        buttons = [
            dict(
                args=['xbins.size', '3600000'],
                label='Hour',
                method='restyle',

            ), dict(
                args=['xbins.size', 'D1'],
                label='Day',
                method='restyle',
            ), dict(
                args=['xbins.size', '1800000'],
                label='Half-Hour',
                method='restyle',
            ), dict(
                args=['xbins.size', '600000'],
                label='10 Minute',
                method='restyle'
            ), dict(
                args=['xbins.size', '60000'],
                label='Minute',
                method='restyle'
            )]
  )]
)

fig_dict1 = dict(data=data1, layout=layout1)


# Sensor 2
fig2 = go.Figure()
data2 = [dict(
  x = sensor2_shared.index,
  autobinx = False,
  autobiny = True,
  marker = dict(color = '#827e7e'),
  name = 'Date',
  type = 'histogram',
  xbins = dict(
    start = '2020-04-19 00:00:00',
    end = '2020-05-01 23:59:59',
    size = 'D1'
  )
)]

layout2 = dict(
margin={
        "r": 50,
        "t": 10,
        "l": 50,
        },
    height = 270,
  xaxis = dict(
    type = 'datetime'
  ),
  yaxis = dict(
    title = 'No. of Detections',
    type = 'linear'
  ),
  updatemenus = [dict(
        x = 0.1,
        y = 1.2,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,
        buttons = [
            dict(
                args=['xbins.size', '3600000'],
                label='Hour',
                method='restyle',

            ), dict(
                args=['xbins.size', 'D1'],
                label='Day',
                method='restyle',
            ), dict(
                args=['xbins.size', '1800000'],
                label='Half-Hour',
                method='restyle',
            ), dict(
                args=['xbins.size', '600000'],
                label='10 Minute',
                method='restyle'
            ), dict(
                args=['xbins.size', '60000'],
                label='Minute',
                method='restyle'
            )]
  )]
)

fig_dict2 = dict(data=data2, layout=layout2)



# Sensor 3
fig3 = go.Figure()
data3 = [dict(
  x = sensor3_shared.index,
  autobinx = False,
  autobiny = True,
  marker = dict(color = '#3db87b'),
  name = 'Date',
  type = 'histogram',
  xbins = dict(
    start = '2020-04-19 00:00:00',
    end = '2020-05-01 23:59:59',
    size = 'D1'
  )
)]

layout3 = dict(
margin={
        "r": 50,
        "t": 10,
        "l": 50,
        },
    height = 270,
  xaxis = dict(
    type = 'datetime'
  ),
  yaxis = dict(
    title = 'No. of Detections',
    type = 'linear'
  ),
  updatemenus = [dict(
        x = 0.1,
        y = 1.2,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,
        buttons = [
            dict(
                args=['xbins.size', '3600000'],
                label='Hour',
                method='restyle',

            ), dict(
                args=['xbins.size', 'D1'],
                label='Day',
                method='restyle',
            ), dict(
                args=['xbins.size', '1800000'],
                label='Half-Hour',
                method='restyle',
            ), dict(
                args=['xbins.size', '600000'],
                label='10 Minute',
                method='restyle'
            ), dict(
                args=['xbins.size', '60000'],
                label='Minute',
                method='restyle'
            )]
  )]
)

fig_dict3 = dict(data=data3, layout=layout3)





def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row 1
                     html.Div(
                                [
                                    html.H5("Detection Distribution in Different Time Slots ", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "The shared time during which all 3 sensors \
                                                 have been actively detecting is from April 19 to May 1. You can \
                                                go through the menu and see the distributions in different time slots.",
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                    html.H6("Sensor 1", className="subtitle padded"),
                                    dcc.Graph(figure=fig_dict1)
                                ],
                         className="10 columns",
                            ),


                    # Row 2
                    html.Div(
                        [
                            html.H6("Sensor 2", className="subtitle padded"),
                            dcc.Graph(figure=fig_dict2)
                        ],
                        className="10 columns",
                    ),

                    html.Div(
                        [
                            html.H6("Sensor 3", className="subtitle padded"),
                            dcc.Graph(figure=fig_dict3)
                        ],
                        className="10 columns",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
