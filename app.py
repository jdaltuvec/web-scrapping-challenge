# Import dependencies
from flask import Flask, render_template, jsonify, request
import scrape_mars
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.mars.drop()


# Set route to scrape
@app.route('/scrape')
def scrape():
    s = scrape_mars.scrape()
    db.mars.insert(s)
    return jsonify(list(db.mars.find()))


# Set route
# @app.route('/')
# def index():
#     # Store the entire team collection in a list

#     mars = list(db.mars.find())
#     print(mars)

#     # Return the template with the list passed in
#     return render_template('index.html', mars=mars)


if __name__ == "__main__":
    app.run(debug=True)
