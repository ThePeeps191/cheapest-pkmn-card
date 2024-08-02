from flask import Flask, render_template, url_for, redirect
from scraper import scrape

app = Flask('app')

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/get/<card>/')
def getcard(card):
	card = card.replace("%20", "+").replace(" ", "+").lower()
	s = scrape(card);
	if (s == -1):
		return render_template("index.html", warning="Invalid Search Results Found")
	else:
		return redirect(s);

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', warning="<b>Error 404: </b>Requested Page Was Not Found<br><b>If You Searched Something:</b> Maybe you put a <code>/</code> character in the search bar?"), 404

app.run(host='0.0.0.0', port = 8080, debug = True)