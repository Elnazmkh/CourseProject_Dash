import dash_html_components as html
import dash_core_components as dcc
import pandas as pd


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])



def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("header.jpg"),
                        className="logo",
                        style={'height': '30%', 'width': '95%'}
                    ),

                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H4("Object Detection")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/Object-Detection/overview",
                className="tab first",
            ),
            dcc.Link(
                "Time Series Analysis",
                href="/Object-Detection/timeSeriesAnalysis",
                className="tab",
            ),
            dcc.Link(
                "Daily Correlation Analysis",
                href="/Object-Detection/dailyCorrelation",
                className="tab",
            ),
            dcc.Link(
                "Hourly Correlation Analysis",
                href="/Object-Detection/hourlyCorrelation",
                className="tab"
            ),
            dcc.Link(
                "Minutely Correlation Analysis",
                href="/Object-Detection/minutelyCorrelation",
                className="tab",
            ),
            dcc.Link(
                "Cross-Correlation Analysis",
                href="/Object-Detection/crossCorrelation",
                className="tab",
            ),
            dcc.Link(
                "Conclusion",
                href="/Object-Detection/conclusion",
                className="tab",
            )
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """

    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def make_dash_table_with_header(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """

    table = []
    cols = df.columns.to_list()
    cols[0] = 'Date'
    html_row = []
    for i in range(len(cols)):
        html_row.append(html.Td([cols[i]]))
    table.append(html.Tr(html_row))

    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

def sensor_trend(df, trend):
    return (df.groupby([trend])['Detection'].count()/(len(df))).to_list()

def df_preview(df, h, t):
    x = df[:h]
    y = pd.DataFrame([['...'] * df.shape[1]], columns=df.columns, index=['...'])
    z = df[-t:]
    frame = [x, y, z]
    result = pd.concat(frame)
    return result