#!/usr/bin/env python3
# Soubor: views.py
# Úloha:  Flask --- pohledy
############################################################################
from flask import (render_template, Markup, request, flash,
                   redirect, session, url_for)
from webksicht import app
from werkzeug.security import check_password_hash
############################################################################


def prihlasit():
    "Dekorátot pro přihlašování"
    
    
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')

pw_hash = {}
pw_hash['sick'] = 'pbkdf2:sha1:1000$KSj1oS1Z$1d565bcf170044d7f576eb280c31419497b25f61'#mick
pw_hash['pick'] = 'pbkdf2:sha1:1000$jpdQ9EWx$56be74e2d0fa4cf996ba126252bc89a14e0cb859'#rick
pw_hash['lick'] = 'pbkdf2:sha1:1000$5xr8x4qW$6af60a18d1c27fb5ed72066ed9dbf216a5495a62'#kick

@app.route('/login/', methods=['POST'])
def login_post():
    jmeno=request.form.get('jmeno')
    heslo=request.form.get('heslo')
    print(jmeno,heslo)
    next = request.args.get('next')
    if check_password_hash(pw_hash[jmeno],heslo):
        session['jmeno'] = jmeno
        flash ('úspěšně jste se přihlásil','zelena')
        return redirect(next or url_for('index'))
    else:
        flash('chybné jméno nebo heslo','cervena')
        if next:
            return redirect(url_for('login', next=next))
        else:
            return redirect(url_for('login'))
    
@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('jmeno',None)
    return redirect(url_for('login'))

@app.route('/tajne/')
def tajne():
    if 'jmeno' in session:
        return render_template('tajne.html')
    else:
        flash('Tato stránka je jen pro přihlášené','oranzova')
        return redirect(url_for('login', next=request.full_path))

@app.route('/super/')
def super():
    return render_template('super.html')


@app.errorhandler(404)
def page_not_found(error):
    print(error.code)
    print(error.name)
    print(error.description)
    return render_template('404.html', e=error), 404



