from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Pizza, Rezervacia
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        nazov = request.form.get('pizza')

        nova_pizza = Pizza(nazov=nazov, user_id=current_user.id)
        db.session.add(nova_pizza)
        db.session.commit()
        flash('Pizza bola pridaná do košíka!', category='success')
        
    return render_template("home.html", user=current_user)

@views.route('/rezervacia', methods=['GET', 'POST'])
@login_required
def rezervacia():
    if  request.method == 'POST':
        meno = request.form.get('meno')
        priezvisko = request.form.get('priezvisko')
        tel = request.form.get('tel')
        pocet = request.form.get('pocet')
        mesto = request.form.get('mesto')
        den = request.form.get('den')
        mesiac = request.form.get('mesiac')
        rok = request.form.get('rok')
        hod = request.form.get('hod')
        min = request.form.get('min')

        rezervacia = Rezervacia.query.filter_by(mesto=mesto, den=den, mesiac=mesiac, rok = rok).first()
        if len(meno) < 2:
            flash('Zadajte meno.', category='error')
        elif len(priezvisko) < 2:
            flash('Zadajte priezvisko.', category='error')
        elif len(tel) < 2:
            flash('Zle tel. cislo.', category='error')
        elif rezervacia:
            flash('Rezervacia už existuje.', category='error')
        else:
            nova_rezervacia = Rezervacia(meno=meno, priezvisko=priezvisko, tel=tel, pocet=pocet, mesto=mesto, den=den, mesiac=mesiac, rok=rok,hod = hod,min = min,user_id=current_user.id)
            db.session.add(nova_rezervacia)
            db.session.commit()
            flash('Rezervacia pridaná!', category='success')
    return render_template("rezervacia.html", user=current_user)

@views.route('/kosik', methods=['GET', 'POST'])
@login_required
def kosik():
    pizze = Pizza.query.all()
    celkovaCena = 0
    for pizza in pizze:
        if pizza.user_id == current_user.id:
            if pizza.nazov == "1":
                celkovaCena += 3
            elif pizza.nazov == "2":
                celkovaCena += 5
            elif pizza.nazov == "3":
                celkovaCena += 4
            elif pizza.nazov == "4":
                celkovaCena += 6
            elif pizza.nazov == "5":
                celkovaCena += 5
            elif pizza.nazov == "6":
                celkovaCena += 7
            elif pizza.nazov == "7":
                celkovaCena += 4
            elif pizza.nazov == "8":
                celkovaCena += 6
            elif pizza.nazov == "9":
                celkovaCena += 6
            elif pizza.nazov == "10":
                celkovaCena += 8
            elif pizza.nazov == "11":
                celkovaCena += 5
            elif pizza.nazov == "12":
                celkovaCena += 7
    rezervacie = Rezervacia.query.all()
    for rezervacia in rezervacie:
        if rezervacia.user_id == current_user.id:
            celkovaCena += 5
    if celkovaCena == 0:
        flash("Košík je prázdny, objednaním pizze alebo rezerváciou ho naplníš.", category="error")
    else:
        sprava = "Celková cena " + str(celkovaCena) +"€."
        flash(sprava, category="success")
    return render_template("kosik.html", user=current_user)

@views.route('/vymaz-pizzu', methods=['POST'])
def vymaz_pizzu():
    pizza = json.loads(request.data)
    pizzaId = pizza['pizzaId']
    pizza = Pizza.query.get(pizzaId)
    if pizza:
        if pizza.user_id == current_user.id:
            db.session.delete(pizza)
            db.session.commit()
            flash('Pizza odobraná z košíka', category='success')
            
    return jsonify({})   

@views.route('/vymaz-rezervaciu', methods=['POST'])
def vymaz_rezervaciu():
    rezervacia = json.loads(request.data)
    rezervaciaId = rezervacia['rezervaciaId']
    rezervacia = Rezervacia.query.get(rezervaciaId)
    if rezervacia:
        if rezervacia.user_id == current_user.id:
            db.session.delete(rezervacia)
            db.session.commit()
            flash('Rezervácia odobraná z košíka', category='success')
            
    return jsonify({})   

@views.route('/zaplatit', methods=['POST'])
def zaplatit():
    pizze = Pizza.query.all()
    for pizza in pizze:
        if pizza.user_id == current_user.id:
            db.session.delete(pizza)
            db.session.commit()
    rezervacie = Rezervacia.query.all()
    for rezervacia in rezervacie:
        if rezervacia.user_id == current_user.id:
            db.session.delete(rezervacia)
            db.session.commit()
    return jsonify({}) 