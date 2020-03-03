# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
import scrape_mars
import pymongo
from pprint import pprint

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db


# Set route to scrape
@app.route('/scrape')
def scrape():
    # Drops collection if available to remove duplicates
    db.mars.drop()
    
    s = scrape_mars.scrape()
    db.mars.insert(s)
    return redirect("/", code=302)


# Set route
@app.route('/')
def index():
    mars_data = list(db.mars.find())
    print(mars_data)
    # Return the template with the list passed in
    return render_template('index.html', mars_data=mars_data)


if __name__ == "__main__":
    app.run(debug=True)
