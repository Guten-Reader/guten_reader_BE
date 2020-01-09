# GutenReader Microservice
[![Build Status](https://travis-ci.com/Guten-Reader/guten_reader_BE.svg?branch=master)](https://travis-ci.com/Guten-Reader/guten_reader_BE)

![image](https://user-images.githubusercontent.com/18686466/72020934-1a54c600-322a-11ea-9e19-52c827510294.png)

[GutenReader](https://github.com/Guten-Reader/guten_reader_FE) is an app built in React Native for reading books hosted by [Project Gutenberg](https://www.gutenberg.org/). This microservice allows the app to play music that matches the current mood of the page the user is reading. GutenReader also uses a [Rails API](https://github.com/Guten-Reader/guten_reader_api) to handle database interaction.

## Installation
NOTE: You will need to create an account at [monkeylearn.com](https://monkeylearn.com/) and include the API key and model id as environment variables MONKEYLEARN_KEY, MONKEYLEARN_MODEL_ID.

1. Clone the repository
```
$ git clone git@github.com:Guten-Reader/guten_reader_BE.git
```

2. Create/activate virtual environment
```
$ virtualenv venv --python=python3.7
$ source venv/bin/activate
```

3. Install dependencies
```
$ pip install -r requirements.txt
```

4. Start the server in development environment
```
$ export APP_SETTINGS="config.TestingConfig"
$ python app.py
```

5. Run the tests
```
$ nose2
```

## Base Url
`https://micro-guten.herokuapp.com/`

## Endpoints

### POST recommendation for Spotify track using sentiment analysis 

`POST api/v1/recommendation`


**Description:** A user turns a new page in their Gutenberg book. A GET request is sent to `/api/v1/recommendation`. The request includes the user's `access_token`, the `current_mood`, and the new page's full `text` in the request body. 
The endpoint conducts a sentiment analysis on the text and returns a value of either 1(Positive), 0.5(Neutral), or 0(Negative) internally. The sentiment value and access_token is used to call Spotify's track recommendation endpoint. The track recommendation endpoint returns an array of 10 classical tracks (as track_uri) with either a positive, neutral, or negative mood.

#### Note: Use the track_uri to play the song in Spotify.


**Request**
```
POST /api/v1/recommendation
Content-Type: application/json
Accept: application/json

{
  "current_mood": "Neutral",
	"text": "This is a very happy and positive statement.",
	"access_token": "BQCUhf-kwMIv9TrDe9boSzrRr-Z6xmuPLoqTAgEyJDJD6G4HIMlQHgRX6BWllCfIxOpK2kQQCiHDsqa3svALu0jPyuAnw6-dn1tjkpB1SSAGL6ma3Q1ZIegcIfKS1v4ag-Gb8uUKc9ch5tt20vazj_PXmK0"
}
```

**Successful Response - If new page has DIFFERENT MOOD than current_mood**

```
status: 200

{
  "mood": "Positive",
  "recommended_tracks": [
    "spotify:track:0qkMYjXnxz91fEnnuMZNi0",
    "spotify:track:2LhRrWfxTV6ZW1XAOb2OGa",
    "spotify:track:6ZFbXIJkuI1dVNWvzJzown",
    "spotify:track:4m5rO8vfR0H6V4J8sKTU2J",
    "spotify:track:4HBMnZFquWVTATSjTABueZ",
    "spotify:track:7AE8dFDObE3tbl8JloJVJD",
    "spotify:track:4tomnQKFLdhCYOtTSmlv4Q",
    "spotify:track:0abApP5Xl9PVwuE0Vo4Oyz",
    "spotify:track:1ZNlk8aE9BhgCxTlm53KAX",
    "spotify:track:5rSR9a0inBSyYlNTLa8BLi"
  ],
  "status_code": 200
}
```
**Successful Response - If new page has SAME MOOD than current_mood**

```
status: 204

NO CONTENT

```


**Unsuccessful Response - If access_token expired**

```
status: 401

{
  "message": "The access token expired",
  "status_code": 401
}

```
**Unsuccessful Response - If invalid body request. Missing access_token, current_mood, and/or text**

```
status: 400

{
    "error": {
        "missing_params": [
            "current_mood"
        ]
    }
}
```

**Unsuccessful Response - If invalid request by Spotify external API call**
```
status: 400

{
    "error": "invalid request"
}
```

## Contributors
- **Mack Halliday**
    - [GitHub](https://github.com/MackHalliday)
    - [LinkedIn](https://www.linkedin.com/in/mackhalliday/)
- **Fenton Taylor**
    - [GitHub](https://github.com/fentontaylor)
    - [LinkedIn](https://www.linkedin.com/in/fenton-taylor-006057122/)
