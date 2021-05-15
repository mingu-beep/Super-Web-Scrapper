from flask import Flask, render_template, request, redirect, send_file
<<<<<<< HEAD
from so import get_so_jobs
=======
from scrapper import get_jobs
>>>>>>> 3850ab26391d09fe0ecd8b6d4306ba07aa525f2b
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_so_jobs(word)
            db[word] = jobs
    else:
        redirect("/")
    return render_template("report.html",
                           resultNumber=len(jobs),
                           searchingBy=word,
                           jobs=jobs)

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")

app.run(host="0.0.0.0")
