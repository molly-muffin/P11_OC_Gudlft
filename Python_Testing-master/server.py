import json
from datetime import datetime
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


@app.route('/')
def index(error=None):
    return render_template('index.html', error=error)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    multiple_club = [club for club in clubs if club['email'] == request.form['email']]
    try:
        one_club = multiple_club[0]
    except IndexError:
        return index("Sorry, that email was not found.\nContact the administrator.")
    return render_template('welcome.html',club=one_club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    maxPlaces = min(12, int(foundCompetition['numberOfPlaces']))
    current_datetime = datetime.now()
    competition_date = datetime.strptime(foundCompetition['date'], '%Y-%m-%d %H:%M:%S')
    if competition_date < current_datetime:
        flash("Sorry, this competition is expired.")
        return render_template('welcome.html', club=foundClub, competitions=competitions)
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition, maxPlaces=maxPlaces)
    else:
        flash("Something went wrong - please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    clubPoints = int(club["points"])
    if clubPoints >= placesRequired:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        club['points'] = int(club['points'])-placesRequired
        flash('Great-booking complete !')
    else:
        flash('Sorry, you do not have the number of available places required to book this number of places.')
  
    return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/boardpoints')
def boardpoints():
    return render_template('boardpoints.html', clubs=clubs)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))