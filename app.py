from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Quantium Dash Workbench"),
        html.P("Starter app ready for data exploration."),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3, 4], "y": [4, 1, 3, 5], "type": "line", "name": "Series A"},
                    {"x": [1, 2, 3, 4], "y": [2, 2, 4, 3], "type": "bar", "name": "Series B"},
                ],
                "layout": {"title": "Example Chart"},
            },
        ),
    ],
    style={"maxWidth": "900px", "margin": "40px auto", "fontFamily": "Helvetica, Arial, sans-serif"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
