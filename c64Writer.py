#!/usr/bin/env python

import webview

window = webview.create_window(
    "Welcome to c64Writer.",
    url="mainview.html",
    min_size=(1024, 700),
    confirm_close=True,
)
webview.start()
