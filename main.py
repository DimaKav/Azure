from flask import Flask
import pyodbc
import json
import pandas as pd
import os

app = Flask(__name__)

def read_data():
    # Database connection logic
    server = os.environ('SERVER')
    database = os.environ('DATABASE')
    username = os.environ('USER')
    password = os.environ('PASSWORD')
    driver= os.environ('DRIVER')
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    # Read data from sql connection into a pandas dataframe, output to json
    neg = "SELECT created_at, author, tweet_text, sentiment FROM negative_sentiment"
    pos = "SELECT created_at, author, tweet_text, sentiment FROM positive_sentiment"
    pos = pd.read_sql(pos, cnxn)
    neg = pd.read_sql(neg, cnxn)
    df = pd.concat([pos,neg],0)
    return df.sort_values(['sentiment','created_at'])[:10].to_html(index=False)

@app.route("/")
def hello():
    return read_data()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
