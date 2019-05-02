from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():

    mars_info = mongo.db.mars_info.find_one()

    return render_template("index.html", mars_info=mars_info)

@app.route('/scrape_new')
def scrape_new ():
    mars_info = mongo.db.mars_info
    mars_info.update({}, scrape(), upsert=True)
    return redirect("/")

if __name__ == "__main__": 
    app.run(debug= True)