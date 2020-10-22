# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from pages import timeSeriesAnalysis, dailyCorrelation, hourlyCorrelation, overview, minutelyCorrelation ,crossCorrelation, conclusion

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(dash.dependencies.Output("page-content", "children"), [dash.dependencies.Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/Object-Detection/timeSeriesAnalysis":
        return timeSeriesAnalysis.create_layout(app)
    elif pathname == "/Object-Detection/dailyCorrelation":
        return dailyCorrelation.create_layout(app)
    elif pathname == "/Object-Detection/hourlyCorrelation":
        return hourlyCorrelation.create_layout(app)
    elif pathname == "/Object-Detection/minutelyCorrelation":
        return minutelyCorrelation.create_layout(app)
    elif pathname == "/Object-Detection/crossCorrelation":
        return crossCorrelation.create_layout(app)
    elif pathname == "/Object-Detection/conclusion":
        return conclusion.create_layout(app)
    elif pathname == "/Object-Detection/full-view":
        return (
            overview.create_layout(app),
            timeSeriesAnalysis.create_layout(app),
            dailyCorrelation.create_layout(app),
            hourlyCorrelation.create_layout(app),
            minutelyCorrelation.create_layout(app),
            crossCorrelation.create_layout(app),
            conclusion.create_layout(app),

        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
