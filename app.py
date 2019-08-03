import json
# ❶ osモジュールをインポートする
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

ex_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=ex_stylesheets)

# ❷ serverをProcfileのgunicornに設定。
app.server = server

app.layout = html.Div(
    children=[
        html.H1("Nihao-Dash",
                style={"textAlign": "center", "color": "#75D701"}),
        html.H4("データを棒グラフで可視化します", style={
                "textAlign": "center", "color": "red"}),
        dcc.Graph(
            id="nihao-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [2, 3, 4],
                        "type": "bar", "name": "Kyoto"},
                    {"x": [1, 2, 3], "y": [4, 2, 4],
                        "type": "bar", "name": "Tokyo"},
                    {"x": [1, 2, 3], "y": [3, 1, 4],
                        "type": "bar", "name": "Osaka"},
                ],
                "layout": {"title": "Dash Data Visualization"},
            },
            # ❶ Graphクラスのstyleプロパティの定義
            style={"width": "80%", "margin": "auto"},
        ),
        html.H3(
            id="callback_to_H3",
            style={"textAlign": "center", "color": "rgb(115,122,232)"},
        ),
    ],
    # ❷ 最初にあるDivに対するstyleプロパティの定義
    style={"backgroundColor": "#cff0da"},
)


@app.callback(Output("callback_to_H3", "children"), [Input("nihao-graph", "hoverData")])
def update_h3(hoverData):
    return json.dumps(hoverData)


if __name__ == "__main__":
    app.run_server(debug=True)
