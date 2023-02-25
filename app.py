from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Chicago',
    'salary': 100000
  },
  {
    'id': 2,
    'title': 'Clown',
    'location': 'Austin',
    'salary': 1000000
  },
  {
    'id': 3,
    'title': 'Professor',
    'location': 'Atlanta',
    'salary': 150000
  },
  {
    'id': 4,
    'title': 'Influencer',
    'location': 'Washington D.C.',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs=JOBS)

# returns JSON
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)