import random

from flask import Flask, render_template, request, redirect, send_file

from so import get_so_jobs
from wework import get_wework_jobs
from remote import get_remote_jobs

from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", img_file=f"img/{random.randrange(1,4)}.jpg")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_remote_jobs(word) + get_wework_jobs(word) + get_so_jobs(
                word)
            db[word] = jobs
    else:
        redirect("/")
    return render_template("report.html",
                           resultNumber=len(jobs),
                           searchingBy=word,
                           jobs=jobs)

@app.route("/details")
def details():
  site = request.args.get('site')
  word = request.args.get('word')
  jobs = db.get(word)
  return render_template("details.html", jobs = jobs, searchingFrom = site, searchingBy=word)

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
        return send_file(f"{word}_jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")
