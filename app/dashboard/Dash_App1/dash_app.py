# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:39:33 2018

@author: jimmybow
"""
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html


def dash_app(app):
    layout = html.Div(
        [html.Div("This is dash app1"), html.Br(), dcc.Input(id="input_text"), html.Br(), html.Br(), html.Div(id="target")]
    )

    @app.callback(Output("target", "children"), [Input("input_text", "value")])
    def callback_fun(value):
        return "your input is {}".format(value)

    return app, layout
