## Base Url
`https://micro-guten.herokuapp.com/`

## Endpoints

### POST recommendation for Spotify track using sentiment analysis 

`POST api/v1/recommendation`

**Description:** A user turns a new page in their Gutenberg book. A POST request is sent to `/api/v1/recommendation`. The request includes the user's access_token, user_id, and the new page's full text in the request body. 
The endpoint conducts a sentiment analysis on the text and returns a value of either 1(Positive), 0.5(Neutral), or 0(Negative) internally. The sentiment value and access_token is used to call Spotify's track recommendation endpoint. The track recommendation endpoint returns a classical track with either a positive, neural, or negative mood with the attributes artist, track_name, track_id, and track_uri.

### ATTENTION: Use the track_uri to play the song in Spotify.


**Request**
```
POST /api/v1/recommendation
Content-Type: application/json
Accept: application/json

{
	"text": "This is a very happy and positive statement.", 
	"access_token": "BQCUhf-kwMIv9TrDe9boSzrRr-Z6xmuPLoqTAgEyJDJD6G4HIMlQHgRX6BWllCfIxOpK2kQQCiHDsqa3svALu0jPyuAnw6-dn1tjkpB1SSAGL6ma3Q1ZIegcIfKS1v4ag-Gb8uUKc9ch5tt20vazj_PXmK0", 
	"user_id": "5"
}
```

**Successful Response**

```
status: 200

{
  "artist": "Modest Mussorgsky",
  "track_id": "67F2FBLJL9Wn09qvPe6XVa",
  "track_name": "Night on Bare Mountain",
  "track_uri": "spotify:track:67F2FBLJL9Wn09qvPe6XVa"
}

```

**Unsuccessful Response**
```
status: 401
{
  "error": "invalid token"
}

status: 400

{
    "error": "invalid request"
}
```
