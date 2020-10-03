from flask import Flask, render_template, session
from random import choice
app = Flask(__name__)
app.debug = True
app.secret_key = 'kascf ascfhasiocfhasiocfawefawfhasiocfh'
#
def vrat_pocet_vyher():
    if not 'hrac_vyhry' in session:
        hrac_vyhry = 0
        session['hrac_vyhry'] = 0
    else:
        hrac_vyhry = session['hrac_vyhry']
    if not 'bot_vyhry' in session:
        bot_vyhry = 0
        session['bot_vyhry'] = 0
    else:
        bot_vyhry = session['bot_vyhry']
    if not 'remizy' in session:
        remizy = 0
        session['remizy'] = 0
    else:
        remizy = session['remizy']
    hry_celkove = hrac_vyhry + bot_vyhry + remizy
    return hrac_vyhry, bot_vyhry, remizy, hry_celkove;
#
def pridej_vyhru(vyhry):
    if vyhry == 0:
        session['hrac_vyhry'] = session['hrac_vyhry'] + 1
    elif vyhry == 1:
        session['bot_vyhry'] = session['bot_vyhry'] + 1
    elif vyhry == 2:
        session['remizy'] = session['remizy'] + 1
    return;
#
def porovnej(vysledek1, vysledek2):
    volba = ["vyhrál hráč", "vyhrál bot", "remíza"]
    vysledek = "nic"
    if vysledek1 == "kámen":
        if vysledek2 == "nůžky":
            vysledek = volba[0];
        if vysledek2 == "papír":
            vysledek = volba[1];
        if vysledek2 == "kámen":
            vysledek = volba[2];
    elif vysledek1 == "nůžky":
        if vysledek2 == "nůžky":
            vysledek = volba[2];
        if vysledek2 == "papír":
            vysledek = volba[0];
        if vysledek2 == "kámen":
            vysledek = volba[1];
    elif vysledek1 == "papír":
        if vysledek2 == "nůžky":
            vysledek = volba[1];
        if vysledek2 == "papír":
            vysledek =  volba[2];
        if vysledek2 == "kámen":
            vysledek =  volba[0];
    if vysledek == volba[0]:
        pridej_vyhru(0)
    elif vysledek == volba[1]:
        pridej_vyhru(1)
    elif vysledek == volba[2]:
        pridej_vyhru(2)
    return vysledek;
#
@app.route('/volba/<volba>')
def vyber(volba):
    vysledek1 = volba
    vysledek2 = choice(["kámen", "nůžky", "papír"])
    return render_template('index.html',hrac1=vysledek1, hrac2=vysledek2, vyhra=porovnej(vysledek1,vysledek2), vyhry=vrat_pocet_vyher())
#
@app.route('/')
def zacatek():
    return render_template('vyber.html', vyhry=vrat_pocet_vyher())
#
if __name__ == '__main__':
    app.run()
#