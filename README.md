# azure-tweet-sentiment-webapp

This app uses logic apps and app services on Azure. 

The logic apps component grabs tweets (#chipotle), analyzes their sentiment, and stores them in a SQL database which I've created on Azure.

The app services component was deployed as a Flask application which loads the SQL data into a pandas dataframe and renders the top 10 most recent and most negative tweets. App services uses continuous deployement with github, so whenever changes are pushed to this repo, the application is updated in the cloud.
