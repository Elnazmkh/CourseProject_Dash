import dash_html_components as html
from utils import Header


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6
            html.Div(
                [
                    # Row 1
                            html.Div(
                                [
                                    html.H6("Correlation Observations", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "According to the graphs daily detections of Sensor 2 & 3 are \
                                                 more correlated and in a more granualr\
                                                 level like hourly analysis, it seems that there is no\
                                                  significant difference between the correlation. However\
                                                  when we get more granular like in a minutely manner, sensors\
                                                   1 & 2 are more correlated. Hence, for a more accurate \
                                                 result we need more information of theses detectors, like\
                                                  what are the nature of these detectors and what exactly \
                                                  they are doing."
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row"),
                    html.Div(
                        [
                            html.H6("Lagging Observations", className="subtitle padded"),
                            html.Br([]),
                            html.Div(
                                [
                                    html.P(
                                        "According to the graphs, it seems that by shifting sensor 1 \
                                         for data two days (= 48 hours) , we will get more correlated data."
                                    ),
                                    html.P(
                                        "According to the graphs Sensor 2 and 3 do not\
                                         have any lags in terms of days, however \
                                        in terms of hours there might be a lag of 4 \
                                        hours and in terms of minutes a lag of 5 minutes is\
                                        observed. "
                                    ),
                                ],
                                style={"color": "#7a7a7a"},
                            ),
                        ],
                        className="row"),

                ],
                className="sub_page"),
        ],
        className="page",
    )
