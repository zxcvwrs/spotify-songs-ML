from fastapi import FastAPI
from pydantic import BaseModel

from joblib import load
from datetime import date

import db


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


def create_db_record(data : request_body, genre : str, group : str ):
    prediction_date = date.today()
    prediction_date.strftime('%m/%d/%Y')
    record = [
            prediction_date,group,data.id,data.name,data.popularity,data.duration_ms,
            data.explicit,data.id_artist,data.release_date,
            data.danceability,data.key,data.energy,data.loudness,
            data.speechiness,data.acousticness,data.instrumentalness,
            data.liveness,data.valence,data.tempo,genre
            ]
    return record

def write_to_db(record):
    db_connection = db.create_connection(r"database\saved_data.db")
    db.add_prediction(db_connection,record)

def get_track_features(data : request_body):
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
    return track_features

    
@app.post("/predict_A")
def predict_A(data : request_body):
    model = load("models\m1_classifier")
    track_features = get_track_features(data)
    prediction = model.predict(track_features)
    record = create_db_record(data, prediction[0],"A")
    write_to_db(record)
    return {'genre' : prediction[0]}

@app.post("/predict_B")
def predict_B(data : request_body):
    #model = load("models\m1_classifier")
    track_features = get_track_features(data)
    #prediction = model.predict(track)
    return {'genre' : 'unknown'}

     