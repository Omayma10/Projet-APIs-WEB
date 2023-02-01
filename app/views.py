#!/usr/bin/env python3
# -- coding: utf-8 --

from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

conn = sqlite3.connect('database.db')
print("Base de données ouverte avec succès")
conn.execute('CREATE TABLE IF NOT EXISTS identifiant (user TEXT)')
print("Table créée avec succès")
conn.execute('CREATE TABLE IF NOT EXISTS emotions (date TEXT, humeur TEXT, emotion TEXT, raison_emotion TEXT)')
print("Table créée avec succès")
conn.execute('CREATE TABLE IF NOT EXISTS intentions (date TEXT, intention TEXT)')
print("Table créée avec succès")
conn.close()

d =''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accueil', methods = ['GET'])
def accueil():
    result=request.args
    u = result['user']
    # with sqlite3.connect("database.db") as con:
    #     cur = con.cursor()
    #     cur.execute("INSERT INTO identifiant(user) VALUES (?)", (u,))
    #     con.commit()
    #     # con.close()
    return render_template("accueil.html", user=u)
    
@app.route('/accueil/suivi_emotions', methods = ['GET'])
def suivi_emotions():
    return render_template("suivi_emotions.html")

@app.route('/accueil/journal', methods = ['GET'])
def journal():
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * from emotions where date=?", [d])
        result=cur.fetchall()
        con.commit()  
    con.close()
    return render_template ('journal.html', resultat = result)
    
@app.route('/accueil/suivi_emotions/recap_emotions', methods = ['GET'])
def recap_emotions():
    result=request.args
    d = result['date']
    h = result['humeur']
    e = result['emotion']
    r = result['raison_emotion']
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO emotions(date, humeur, emotion, raison_emotion) VALUES (?,?,?,?)", (d,h,e,r))
        con.commit()
        # con.close()
    return render_template("recap_emotions.html")

@app.route('/accueil/intentions', methods = ['GET'])
def intentions():
    return render_template("intentions.html")
    
app.run(debug=True)











