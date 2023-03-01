from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    column_names = result.keys() 
    jobs = []
    for row in result_all:
      jobs.append(dict(zip(column_names, row)))
    return jobs

@app.route("/")
def hello_world():
  jobs = load_jobs()
  return render_template('home.html',
                        jobs=JOBS)

# returns JSON
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)