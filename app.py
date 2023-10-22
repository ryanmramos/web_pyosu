from flask import Flask, request, render_template
import sys

from pyosu.web_api import get_replay_from_file, get_replay_beatmap

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/replay", methods=["POST"])
def replay():
    print(request.files['file'])
    uploaded_file = request.files["file"]

    if uploaded_file.filename != '':
        # You can now work with the uploaded file, such as saving it or processing it.
        # Here's an example of saving it to the server's filesystem:
        replay = get_replay_from_file(uploaded_file)
        beatmap = get_replay_beatmap(replay)
        print(beatmap.hit_objects)
        return 'File uploaded successfully!'
    else:
        return 'No file selected or invalid file name.'