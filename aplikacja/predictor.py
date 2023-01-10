from fastapi import FastAPI
from pydantic import BaseModel
 
from joblib import load
import json


app = FastAPI()
class request_body(BaseModel):
    id : str
    name : str
    popularity : float
    duration_ms : int
    explicit : int
    id_artist : str
    release_date : str
    danceability : float
    key : float
    energy : float
    loudness : float
    speechiness : float
    acousticness : float
    instrumentalness : float
    liveness : float
    valence : float
    tempo : float

def append_to_json(new_data, filename='history.json'):
    with open(filename) as fp:
        listObj = json.load(fp)
    listObj.append(new_data)
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4)

def save_to_history(data : request_body, genre : str, group : str ):
    line = {
        "id" : data.id,
        "name" : data.name,
        "popularity" : data.popularity,
        "duration_ms" : data.duration_ms,
        "explicit" : data.explicit,
        "id_artist" : data.id_artist,
        "release_date" : data.release_date,
        "danceability" : data.danceability,
        "key" : data.key,
        "energy" : data.energy,
        "loudness" : data.loudness,
        "speechiness" : data.speechiness,
        "acousticness" : data.acousticness,
        "instrumentalness" : data.instrumentalness,
        "liveness" : data.liveness,
        "valence" : data.valence,
        "tempo" : data.tempo,
        "genre" : genre,
        "group" : group
    }
    append_to_json(line)
    


@app.post("/predict_A")
def predict_A(data : request_body):
    model = load("models\m1_classifier")
    track_features = [[

        data.danceability,
        data.key,
        data.energy,
        data.loudness,
        data.speechiness,
        data.acousticness,
        data.instrumentalness,
        data.liveness,
        data.valence,
        data.tempo
    ]]
    prediction = model.predict(track_features)
    save_to_history(data, "prediction","A")
    return {'genre' : prediction[0]}

@app.post("/predict_B")
def predict_B(data : request_body):
    #model = load("models\m1_classifier")
    track_features = [[
        data.danceability,
        data.key,
        data.energy,
        data.loudness,
        data.speechiness,
        data.acousticness,
        data.instrumentalness,
        data.liveness,
        data.valence,
        data.tempo
    ]]
    #prediction = model.predict(track)
    return {'genre' : 'unknown'}



     