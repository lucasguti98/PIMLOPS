from fastapi import FastAPI
import pandas as pd
app = FastAPI()


#Enpoint 1
@app.get("/userdata/{User_id}")
def userdata(User_id : str):
    df_endpoint1 = pd.read_csv("datos\df_endpoint1.csv")
    df_endpoint1['user_id'] = df_endpoint1['user_id'].astype(str)
    user_data = df_endpoint1[df_endpoint1["user_id"] == User_id]
    user_data_dict = user_data.to_dict(orient="records")

    return user_data_dict

#Enpoint 2
#@app.get("/countreviews/{year}")
#def countreviews(year : str):

#Enpoint 3
@app.get("/genre_rank/{genre}")
def genre(genre : str): 
    df_endpoint3 = pd.read_csv("datos\df_endpoint3.csv")
    rank = df_endpoint3[df_endpoint3['genre'] == genre]
    genre_rank = rank.to_dict(orient="records")
    
    return genre_rank

#Endpoint 4
#def userforgenre( género : str ):

#Endpoint 5
@app.get("/developer_data/{developer}")
def developer(developer : str):
    df_endpoint5 = pd.read_csv("datos\df_endpoint5.csv")
    developer_data = df_endpoint5[df_endpoint5["developer"] == developer]
    developer_data_dict = developer_data.to_dict(orient="records")

    return developer_data_dict


#Enpoint 6
@app.get("/sentiment_per_year/{year}")
def sentiment_analysis(year : int):
    df_endpoint6 = pd.read_csv("datos\df_endpoint6.csv")
    sentiment_data = df_endpoint6[df_endpoint6["Year"] == year]
    sentiment_data_dict = sentiment_data.to_dict(orient="records")

    return sentiment_data_dict


#Endpoint Recommendation system
@app.get("/Recommendation_system/{Game}")
def recomendacion_juego(Game : str):   
    df_RS = pd.read_csv("datos\Recommendation_system.csv")
    RS_data = df_RS[df_RS["Game"] == Game]
    RS_data_dict = RS_data.to_dict(orient="records")

    return RS_data_dict

