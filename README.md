## Base Url
`https://micro-guten.herokuapp.com/`

## Endpoints

### GET recommendation for Spotify track using sentiment analysis 

`GET api/v1/recommendation`

**Description:** A user turns a new page in their Gutenberg book. A GET request is sent to `/api/v1/recommendation`. The request includes the user's `access_token`, the `current_mood`, and the new page's full `text` in the request body. 
The endpoint conducts a sentiment analysis on the text and returns a value of either 1(Positive), 0.5(Neutral), or 0(Negative) internally. The sentiment value and access_token is used to call Spotify's track recommendation endpoint. The track recommendation endpoint returns an array of 10 classical tracks (as track_uri) with either a positive, neutral, or negative mood.

#### Note: Use the track_uri to play the song in Spotify.

**Request**
```
GET /api/v1/recommendation
Content-Type: application/json
Accept: application/json

{
  "current_mood": "Neutral",
	"text": "This is a very happy and positive statement.",
	"access_token": "BQCUhf-kwMIv9TrDe9boSzrRr-Z6xmuPLoqTAgEyJDJD6G4HIMlQHgRX6BWllCfIxOpK2kQQCiHDsqa3svALu0jPyuAnw6-dn1tjkpB1SSAGL6ma3Q1ZIegcIfKS1v4ag-Gb8uUKc9ch5tt20vazj_PXmK0"
}
```

**Successful Response**

```
# if the new page has a DIFFERENT MOOD than `current_mood`

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

# if the new page has the SAME MOOD than `current_mood`

status: 204

NO CONTENT
```

**Unsuccessful Response**
```
status: 401

{
  "message": "The access token expired",
  "status_code": 401
}

status: 400

{
    "error": "invalid request"
}
```
