# azure-tweet-sentiment-webapp

This app uses logic apps and app services on Azure. The logic apps component grabs tweets (#chipotle), analyzes their sentiment, and stores them in a SQL database which I've created on Azure.
The app services component was deployed as a Flask application which loads the SQL data into a pandas dataframe and renders the most recent and most negative tweets in a website.
