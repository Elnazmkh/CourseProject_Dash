
import dash_html_components as html
from utils import Header
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import base64

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

sensor1_shared = pd.read_csv(DATA_PATH.joinpath("sensor1_shared.csv"), index_col=0)
sensor2_shared = pd.read_csv(DATA_PATH.joinpath("sensor2_shared.csv"), index_col=0)
sensor3_shared = pd.read_csv(DATA_PATH.joinpath("sensor3_shared.csv"), index_col=0)
sensor1_shared.index = pd.to_datetime(sensor1_shared.index)
sensor2_shared.index = pd.to_datetime(sensor2_shared.index)
sensor3_shared.index = pd.to_datetime(sensor3_shared.index)


#Sensor 1 & 2

#Daily
s1 = sensor1_shared.Detection.resample('D').count().to_frame()
s1 = s1/s1.max()
s2 = sensor2_shared.Detection.resample('D').count().to_frame()
s2 = s2/s2.max()
s3 = sensor3_shared.Detection.resample('D').count().to_frame()
s3 = s3/s3.max()

g12 = s1.join(s2, lsuffix='_Sensor1', rsuffix='_Sensor2', how='outer').fillna(0)
g13 = s1.join(s3, lsuffix='_Sensor1', rsuffix='_Sensor3', how='outer').fillna(0)
g23 = s2.join(s3, lsuffix='_Sensor2', rsuffix='_Sensor3', how='outer').fillna(0)

fig = plt.figure()
plt.xcorr(g12['Detection_Sensor1'], g12['Detection_Sensor2'], usevlines=True, maxlags=12, normed=True, lw=2)
plt.grid()
fig.savefig('assets/day12.png', dpi=fig.dpi)

fig = plt.figure()
plt.xcorr(g13['Detection_Sensor1'], g13['Detection_Sensor3'], usevlines=True, maxlags=12, normed=True, lw=2)
plt.grid()
fig.savefig('assets/day13.png', dpi=fig.dpi)

fig = plt.figure()
plt.xcorr(g23['Detection_Sensor2'], g23['Detection_Sensor3'], usevlines=True, maxlags=12, normed=True, lw=2)
plt.grid()
fig.savefig('assets/day23.png', dpi=fig.dpi)


#Hourly
s1 = sensor1_shared.Detection.resample('H').count().to_frame()
s1 = s1/s1.max()
s2 = sensor2_shared.Detection.resample('H').count().to_frame()
s2 = s2/s2.max()
s3 = sensor3_shared.Detection.resample('H').count().to_frame()

s3 = s3/s3.max()
g12 = s1.join(s2, lsuffix='_Sensor1', rsuffix='_Sensor2', how='outer').fillna(0)
g13 = s1.join(s3, lsuffix='_Sensor1', rsuffix='_Sensor3', how='outer').fillna(0)
g23 = s2.join(s3, lsuffix='_Sensor2', rsuffix='_Sensor3', how='outer').fillna(0)

fig = plt.figure()
plt.xcorr(g12['Detection_Sensor1'], g12['Detection_Sensor2'], usevlines=True, maxlags=50, normed=True, lw=2)
plt.grid()
fig.savefig('assets/hour12.png', dpi=fig.dpi)

fig = plt.figure()
plt.xcorr(g13['Detection_Sensor1'], g13['Detection_Sensor3'], usevlines=True, maxlags=50, normed=True, lw=2)
plt.grid()
fig.savefig('assets/hour13.png', dpi=fig.dpi)

fig = plt.figure()
plt.xcorr(g23['Detection_Sensor2'], g23['Detection_Sensor3'], usevlines=True, maxlags=50, normed=True, lw=2)
plt.grid()
fig.savefig('assets/hour23.png', dpi=fig.dpi)


#10 Minutely
s1 = sensor1_shared.Detection.resample('T').count().to_frame()
s1 = s1/s1.max()
s2 = sensor2_shared.Detection.resample('T').count().to_frame()
s2 = s2/s2.max()
s3 = sensor3_shared.Detection.resample('T').count().to_frame()
s3 = s3/s3.max()

g12 = s1.join(s2, lsuffix='_Sensor1', rsuffix='_Sensor2', how='outer').fillna(0)
g13 = s1.join(s3, lsuffix='_Sensor1', rsuffix='_Sensor3', how='outer').fillna(0)
g23 = s2.join(s3, lsuffix='_Sensor2', rsuffix='_Sensor3', how='outer').fillna(0)

fig = plt.figure()
plt.xcorr(g12['Detection_Sensor1'], g12['Detection_Sensor2'], usevlines=True, maxlags=50, normed=True, lw=2)
plt.grid()
fig.savefig('assets/minute12.png', dpi=fig.dpi)

fig = plt.figure()
plt.xcorr(g13['Detection_Sensor1'], g13['Detection_Sensor3'], usevlines=True, maxlags=50, normed=True, lw=2)
plt.grid()
fig.savefig('assets/minute13.png', dpi=fig.dpi)

fig = plt.figure()
plt.xcorr(g23['Detection_Sensor2'], g23['Detection_Sensor3'], usevlines=True, maxlags=50, normed=True, lw=2)
plt.grid()
fig.savefig('assets/minute23.png', dpi=fig.dpi)

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [

                    #row1
                    html.Div(
                        [
                            html.H5("Sensor 1 & Sensor 2", className="subtitle padded"),
                            html.Div(
                                [
                                    html.H6(
                                        ["Daily"], className="subtitle padded"
                                    ),

                                    html.Img(
                                        src = app.get_asset_url("day12.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Hourly"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("hour12.png"),
                                        className="logo",
                                        style={'height': '150%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),


                            html.Div(
                                [
                                    html.H6(
                                        ["Minutely"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("minute12.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),
                        ],
                        className= "row ",
                    ),


                    #row 2
                    html.Div(
                        [
                            html.H5("Sensor 1 & Sensor 3", className="subtitle padded"),
                            html.Div(
                                [
                                    html.H6(
                                        ["Daily"], className="subtitle padded"
                                    ),

                                    html.Img(
                                        src=app.get_asset_url("day13.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Hourly"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("hour13.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),

                            html.Div(
                                [
                                    html.H6(
                                        ["Minutely"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("minute13.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),
                        ],
                        className= "row"
                    ),
                    # row 2
                    html.Div(
                        [
                            html.H5("Sensor 2 & Sensor 3", className="subtitle padded"),
                            html.Div(
                                [
                                    html.H6(
                                        ["Daily"], className="subtitle padded"
                                    ),

                                    html.Img(
                                        src=app.get_asset_url("day23.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Hourly"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("hour23.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),

                            html.Div(
                                [
                                    html.H6(
                                        ["Minutely"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("minute23.png"),
                                        className="logo",
                                        style={'height': '100%', 'width': '100%'}
                                    ),
                                ],
                                className="four columns",
                            ),
                        ],
                        className="row"
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
