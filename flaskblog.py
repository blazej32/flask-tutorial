from flask import Flask, render_template
app = Flask(__name__)

matches = [
    {
        'date': '25.05.2023',
        'home': 'FC Barcelona',
        'away': 'Real Madrid',
        'home_goals': 5,
        'away_goals': 0
    },
    {
        'date': '02.12.2005',
        'home': 'Bayern Munich',
        'away': 'Borussia Dortmund',
        'home_goals': 2,
        'away_goals': 2
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=True)
