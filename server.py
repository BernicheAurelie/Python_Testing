import json
import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

def today():
    today = datetime.datetime.now()
    return today.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions, today=today())
    except IndexError:
        flash("Sorry this email doesn't exist in the club list")
        return render_template('index.html')

@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    except IndexError:
        flash("Something went wrong-please try again")
        return render_template('index.html')

@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    club_points_available = int(club['points'])
    try:
        placesRequired = int(request.form['places'])
        if placesRequired > int(competition['numberOfPlaces']):
            flash(f"Sorry, there isn't enough places for the {competition['name']}")
            return render_template('welcome.html', club=club, competitions=competitions, today=today())
        elif placesRequired <= (club_points_available/3) and placesRequired<=12:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club['points'] = club_points_available - placesRequired*3
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions, today=today())
        elif placesRequired>12:
            flash("Sorry, you can't book more than twelve places per competition")
            return render_template('welcome.html', club=club, competitions=competitions, today=today())
        else:
            flash("Sorry, Club doesn't have enough available points")
            return render_template('welcome.html', club=club, competitions=competitions, today=today())
    except ValueError:
        flash("You have to specify how many places you want to book, please try again")
        return render_template('welcome.html', club=club, competitions=competitions, today=today())

@app.route('/points',methods=['GET'])
def showPoints():
    return render_template('points.html', clubs=clubs)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))