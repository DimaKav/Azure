from flask import Flask
import pyodbc
import json
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

def read_data():
    # Database connection logic
    server = os.getenv('SERVER')
    database = os.getenv('DATABASE')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    driver= os.getenv('DRIVER')
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    # Read data from sql connection into a pandas dataframe, output to json
    neg = "SELECT created_at, author, tweet_text, sentiment FROM negative_sentiment"
    pos = "SELECT created_at, author, tweet_text, sentiment FROM positive_sentiment"
    pos = pd.read_sql(pos, cnxn)
    neg = pd.read_sql(neg, cnxn)
    df = pd.concat([pos,neg],0)
#     return df.sort_values(['sentiment','created_at'])[:10].to_html(index=False)
    return df.sort_values(['sentiment','created_at'])[:10].to_json(orient='records')

@app.route("/")
def hello():
    return str(read_data())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
