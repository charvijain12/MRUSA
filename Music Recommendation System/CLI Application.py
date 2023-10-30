# dependencies for App
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

# dependencies for sentiment prediction 
# import os (repeat so commenting out)
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import Model_Application       # importing sentiment predictor

# other dependencies
import genre_mapping

# load client environment info
path = "./requirements/.env"
load_dotenv(path)

# get client info
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# generating token to access api
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers= headers, data= data)

    json_result = json.loads(result.content)
    token = json_result['access_token']

    return token

# get headers
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# search query
def get_genre_based_tracks(token, g):
    url = "https://api.spotify.com/v1/recommendations/"
    headers = get_auth_header(token)
    query = f"?seed_genres={g[0]}&limit=10"

    query_url = url + query

    result = get(query_url, headers=headers)

    json_result = json.loads(result.content)['tracks']

    return json_result


# MAIN CODE

#get token to run spotify api
token = get_token()

# run sentiment predictor
emotion = Model_Application.Get_Sentiment()

# handle errors
if emotion == 11:
    print("ERROR: Bag Of Words Vocabulary error. Please get the right vocabulary file and save it as \"BoW_Vocab.txt\"....")
elif emotion == 22:
    print("ERROR: No Sentiment analysis model exists. Please have a file \"Sentiment_Prediction_Model.txt\" with the exported model....")
else:
    # get mapping of emotion-to-genre
    mapping = genre_mapping.get_mappings()

    required_genre = mapping[f"{emotion}"]

    result = get_genre_based_tracks(token, required_genre)
    if len(result) == 0:
        print("No song recommendations could be found.")
    else:
        # show output in readable format
        for idx, song in enumerate(result):
            print(f"{idx + 1}. {song['name']}")