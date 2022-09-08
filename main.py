#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:14:08 2022

@author: chef
"""

#from flask import Flask, render_template, resquest, send_file, redirect, url_for, Response, redirect
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

app = Flask(__name__)

import sys
import os

@app.route('/', methods=['GET', 'POST'])

def menu():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)
