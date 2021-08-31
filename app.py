from flask import Flask, render_template, request, redirect
from accountant import manager

app = Flask(__name__)

@app.route("/")
def home():
    stock = manager.stock.items()
    saldo = manager.account
    return render_template("index.html", stock = stock, saldo = saldo)

@app.route("/zakup/", methods=["GET", "POST"])
def zakup_app():
    stock = manager.stock.items()
    saldo = manager.account
    if request.method == "POST":
        manager.history.append(["zakup", request.form["nazwa_produktu"], request.form["cena_jednostkowa"], request.form["ilosc_sztuk"]])
        manager.save(manager.history)
        return redirect("/zakup/")
    return render_template("zakup.html", stock = stock, saldo = saldo)

@app.route("/sprzedaz/")
def sprzedaz_app():
    stock = manager.stock.items()
    saldo = manager.account
    return render_template("sprzedaz.html", stock = stock, saldo = saldo)

@app.route("/saldo/")
def saldo_app():
    stock = manager.stock.items()
    saldo = manager.account
    return render_template("saldo.html", stock = stock, saldo = saldo)

@app.route("/historia/")
def historia_app():
    stock = manager.stock.items()
    saldo = manager.account
    return render_template("historia.html", stock = stock, saldo = saldo)