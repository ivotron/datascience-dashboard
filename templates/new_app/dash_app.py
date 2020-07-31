from dash.dependencies import Input, Output, State # noqa
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def dash_app(app):
    # layout #################################################################

    layout = dbc.Container(
        fluid=True,
        children=[
            html.H1("This is an example of a dash app!"),
            html.Br(),
            html.H3("Write something:"),
            dcc.Input(id="input_text"),
            html.Br(),
            html.Div(id="target"),
        ]
    )

    # app callbacks ##########################################################

    @app.callback(
        Output("target", "children"),
        [Input("input_text", "value")]
    )
    def callback_example(value):
        return "Your input is {}".format(value)

    return app, layout
