from flask import Flask, request, render_template
import sys

from pyosu.web_api import get_replay_from_file, get_replay_beatmap, get_taps_on_hit_objects

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/replay", methods=["POST"])
def replay():
    # print(request.files['file'])
    uploaded_file = request.files["file"]

    if uploaded_file.filename != '':
        # Can now work with the uploaded file, such as saving it or processing it
        replay = get_replay_from_file(uploaded_file)
        beatmap = get_replay_beatmap(replay)
        
        # Get taps on each hit object (excluding spinners)
        hit_object_taps = get_taps_on_hit_objects(beatmap, replay)
        return render_template('replay.html', HitObjectTaps=hit_object_taps, User=replay.username, BMName=beatmap.MetadataSection.Title)
    else:
        # TODO: change to an error.html
        return 'No file selected or invalid file name.'