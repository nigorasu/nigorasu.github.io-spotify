from flask import Flask, render_template, request, jsonify
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

app = Flask(__name__)

client_credentials_manager = SpotifyClientCredentials(client_id='ef958ecb19c045ed803cc160fdd16624',
                                                      client_secret='3a406f21601947f4a45fb9b8019ed20b')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.json['artist']
    results = sp.search(q=query, type='artist')
    artists = results['artists']['items']
    return jsonify(artists=artists)


if __name__ == '__main__':
    app.run(debug=True)
