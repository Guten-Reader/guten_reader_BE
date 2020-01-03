## Base Url
`https://guten-server.herokuapp.com/`

## Endpoints

### GET recommendation for Spotify track using sentiment analysis 

`GET api/v1/recommendation`

**Description:** A user turns a new page in their Gutenberg book. A GET request is sent to `api/v1/recommendation`. The request includes the user's access_token, user_id, and the new page's full text in the request body. 
The endpoint conducts a sentiment analysis on the text and returns a value of either 1(Positive), 0.5(Neutral), or 0(Negative) internally. The sentiment value and access_token is used to call Spotify's track recommendation endpoint. The track recommendation endpoint returns a classical track with either a positive, neural, or negative mood. The recommendation endpoint also returns the artist and name of the recommendation track. 

Note: 
- access_token expires hourly. In future iterations, sad path will be built in to automatically request and use an new access token. 
- user_id to be passed into request body to handle potential sad path in future iterations.

**Request**
```
GET api/v1/recommendation
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
  "artist": "George Frideric Handel",
  "track_id": "1kr73pbla9W6iI4HMkT9aP",
  "track_name": "Messiah, HWV 56: Part II, Sc. 6, Hallelujah!"
}

```

**Unsuccessful Response**
```
status: 400

{
    "error": "invalid request"
}
```
