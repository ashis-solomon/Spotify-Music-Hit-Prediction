from flask import Flask, render_template, request
import json
import pandas as pd
import pickle
import joblib
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/audio',methods=['POST','GET'])
def audio():
    displayName = request.args.get("displayName")

    trkID = request.args.get("trkID")

    trkPop = request.args.get("trkPop")

    return render_template('audio.html',displayName=displayName,trkID=trkID,trkPop=trkPop)


@app.route('/stat',methods=['POST','GET'])
def stat():
    pass_str = request.form.get('hoo')
    items=pass_str.split('!@#$%')
 
 
    x_x=[]
    x=json.loads(items[0])

    for i in x:

       
     if type(i) is type(None):
      print("Can't find song")
     else:
      x_x.append(i)

    y=pd.DataFrame(x_x)
    df=y.sort_values(by=['popularity'], ascending=False)
    df.drop(['type','uri','track_href','id','analysis_url'], axis=1,inplace=True)
    dfx=df.drop_duplicates(subset=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'duration_ms', 'time_signature', 'name', 'explicit'] ,keep='first',ignore_index=False)
    dfxx=dfx.drop(['key','mode','explicit','time_signature','name'], axis=1)
    dfxx = dfxx.add_suffix('_ar')
    df_ar = dfxx[['danceability_ar','energy_ar','loudness_ar','speechiness_ar','duration_ms_ar','acousticness_ar','instrumentalness_ar','liveness_ar','valence_ar','tempo_ar','popularity_ar']].mean()
    dfdict=df_ar.to_dict()

    yy=json.loads(items[2])
    yy["year"]=float(yy["release_date"][:4])
    yy.pop("release_date")
    yy.pop('s_id')
    yy.pop('time_signature')
    if yy["explicit"] == False:
        yy["explicit"]=0.0
    else:
        yy["explicit"]=1.0
    for i in range(12):
        yy[f'key_{i}']=0.0
    yy[f'key_{yy["key"]}']=1.0 
    yy.pop("key")
    yy.pop("key_0")


    acousticness = float(yy["acousticness"])
    danceability = float(yy["danceability"])
    duration_ms = float(yy["duration"])
    energy = float(yy["energy"])
    explicit = float(yy["explicit"])
    instrumentalness = float(yy["instrumentalness"])
    liveness = float(yy["liveness"])
    loudness = float(yy["loudness"])
    speechiness = float(yy["speechiness"])
    tempo = float(yy["tempo"])
    valence = float(yy["valence"])
    year = float(yy["year"])
    #key_0 = yy["key_0"]
    key_1 = yy["key_1"]
    key_2 = yy["key_2"]
    key_3 = yy["key_3"]
    key_4 = yy["key_4"]
    key_5 = yy["key_5"]
    key_6 = yy["key_6"]
    key_7 = yy["key_7"]
    key_8 = yy["key_8"]
    key_9 = yy["key_9"]
    key_10 = yy["key_10"]
    key_11 = yy["key_11"]
    mode = float(yy["mode"])
    acousticness_ar = float(dfdict["acousticness_ar"])
    danceability_ar = float(dfdict["danceability_ar"])
    duration_ms_ar = float(dfdict["duration_ms_ar"])
    energy_ar = float(dfdict["energy_ar"])
    instrumentalness_ar = float(dfdict["instrumentalness_ar"])
    liveness_ar = float(dfdict["liveness_ar"])
    loudness_ar = float(dfdict["loudness_ar"])
    speechiness_ar = float(dfdict["speechiness_ar"])
    tempo_ar = float(dfdict["tempo_ar"])
    valence_ar = float(dfdict["valence_ar"])
    popularity_ar = float(dfdict["popularity_ar"])
    model = joblib.load('model.pkl')
    prediction=model.predict([[acousticness,danceability,duration_ms,energy,explicit,instrumentalness,liveness,loudness,speechiness,tempo,valence,year,
    key_1,key_2,key_3,key_4,key_5,key_6,key_7,key_8,key_9,key_10,key_11,mode,acousticness_ar,
    danceability_ar,duration_ms_ar,energy_ar,instrumentalness_ar,liveness_ar,loudness_ar,speechiness_ar,tempo_ar,valence_ar,popularity_ar]])
    
    output=prediction[0]

    return render_template('stat.html',pass_str=pass_str,output=output)

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/tryout')
def tryout():
    return render_template('tryout.html')

@app.route('/statTRY',methods=['GET'])
def statTRY():
    details = request.args.get("details")

    yy=json.loads(details)

    if yy["explicit"] == "false" or yy["explicit"] == "False":
        yy["explicit"]=0.0
    else:
        yy["explicit"]=1.0
    for i in range(12):
        yy[f'key_{i}']=0.0
    yy[f'key_{yy["key"]}']=1.0 
    if yy["mode"] == 1:
        yy["mode"] = 1.0
    else:
        yy["mode"] = 0.0
    yy.pop("key")
    yy.pop("key_0")
 

    acousticness = float(yy["acousticness"])
    danceability = float(yy["danceability"])
    duration_ms = float(yy["duration"])
    energy = float(yy["energy"])
    explicit = float(yy["explicit"])
    instrumentalness = float(yy["instrumentalness"])
    liveness = float(yy["liveness"])
    loudness = float(yy["loudness"])
    speechiness = float(yy["speechiness"])
    tempo = float(yy["tempo"])
    valence = float(yy["valence"])
    key_1 = yy["key_1"]
    key_2 = yy["key_2"]
    key_3 = yy["key_3"]
    key_4 = yy["key_4"]
    key_5 = yy["key_5"]
    key_6 = yy["key_6"]
    key_7 = yy["key_7"]
    key_8 = yy["key_8"]
    key_9 = yy["key_9"]
    key_10 = yy["key_10"]
    key_11 = yy["key_11"]
    mode = float(yy["mode"])

    model = joblib.load('statfinmodel.pkl')
    prediction=model.predict([[acousticness,danceability,duration_ms,energy,explicit,instrumentalness,liveness,loudness,speechiness,tempo,valence,
    key_1,key_2,key_3,key_4,key_5,key_6,key_7,key_8,key_9,key_10,key_11,mode]])
    
    output=prediction[0]
  





  
    return render_template('statTRY.html',output=output)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "main":
    app.run(debug=True)
