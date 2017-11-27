#!/usr/bin/env python3
# Soubor: views.py
# Úloha:  Flask --- pohledy
############################################################################
from flask import (render_template, Markup, request,
                   redirect, session)
from webksicht import app
############################################################################


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/super/')
def super():
    text = "Dnes je máme programování, což mi udělalo velikou radost :-)"
    return render_template('super.html', text=text)


@app.route('/number/<i>')
def number(i):
    return render_template('number.html', number=i)


@app.errorhandler(404)
def page_not_found(error):
    print(error.code)
    print(error.name)
    print(error.description)
    return render_template('404.html', e=error), 404
