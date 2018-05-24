from flask import Flask, redirect, url_for, request
from selenium import webdriver
from subprocess import Popen
from time import sleep
from os import system
import sys

running = False
browser = None
process = None

app = Flask(__name__)

def render(title,source):
    global running
    if not running:
       return redirect(url_for("home")) 
    global process
    temp_index_html = open("index.html", "w")
    temp_index_html.write(source.encode("utf-8"))
    temp_index_html.close()
    process = Popen(["lynx","index.html"])
    return title

@app.route("/")
def home():
    print "Hello World!"
    return "Heyo"
    #return render("Home", "<html><body><h1>Heyo, run /start to start</h1></body></html>")

@app.route("/start")
def start():
    global running
    if running:
        return redirect(url_for("home"))
    global browser
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    browser = webdriver.Firefox(firefox_options=options)
    running = True
    return render("Start", "<html><body><h1>Now running!</h1></body></html>")

@app.route("/close")
def close():
    global running
    if not running:
       return redirect(url_for("home")) 
    global browser
    global process
    process.terminate()
    browser.quit()
    system("killall lynx")
    sys.exit(0)

@app.route("/link", methods=["POST"])
def link():
    global running
    if not running:
        return redirect(url_for("/link/gnu.org"))
    url = request.json["url"].encode("ascii","ignore")
    print request.get_json()
    global browser
    browser.get(url)
    return render(browser.title,browser.page_source)

app.run()
