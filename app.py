from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_players():
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, rank FROM players ORDER BY score DESC")
    players = cursor.fetchall()
    conn.close()
    return players

@app.route('/')
def index():
    players = get_players()
    return render_template('index.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)
