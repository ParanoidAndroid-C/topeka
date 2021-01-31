import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import time
import pandas as pd
import sys
import json
import requests
from bs4 import BeautifulSoup
import config

client_credentials_manager = SpotifyClientCredentials(client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Takes in command line arguments
#arg = str(sys.argv[1])
#
#if "spotify:artist:" in arg:
#    artist_uri = arg
#else:
#    artist_uri = sp.search(q="artist:" + arg, type="artist")
#
#print(artist_uri)
q = []
answ = {}
albums = []
cnt = 3

def get_artist_info(name):
    artist_uri = search_artists_by_name(name)['uri']
    return get_artist_top_tracks(artist_uri)

def search_artists_by_name(name):
    artist = sp.search(q="artist:" + name, type="artist")['artists']['items'][0]
    return artist

def get_artist_top_tracks(uri):
    global cnt
    top_tracks = sp.artist_top_tracks(uri)
    tracks = []
    for track in top_tracks['tracks']:
        add_track = {}
        track_uri = track['uri']
        meta = sp.track(track_uri) 
        features = sp.audio_features(track_uri)

        add_track['name'] = meta['name']
        add_track['album'] = {}
        add_track['album']['name'] = meta['album']['name']
        add_track['album']['artist'] = meta['album']['artists'][0]['name']
        add_track['album']['release_date'] = meta['album']['release_date']
        date = meta['album']['release_date'][0:4];
        
        if (cnt > 0 and  not (meta['album']['name'] in albums)):
            dateq = {}
            dateq["type"] = "picker"
            dateq["question"] = "In which year was " +  meta['album']['name'] + " released?"
            albums.append(meta['album']['name'])
            dateq["min"] = int(date) - 10
            dateq["max"] = int(date) + 10
            dateq["answer"] = int(date)
            q.append(dateq)
            cnt = cnt - 1
        
        
        
        add_track['duration_ms'] = meta['duration_ms']
        add_track['popularity'] = meta['popularity']
        add_track['lyrics'] = get_lyrics(sp.track(track_uri))
        tracks.append(add_track)
    return tracks

def get_lyrics(song):
    artist = str(song['artists'][0]['name']).strip().replace(' ', '-')
    # print(artist)
    song_name = str(song['name']).strip().replace(' ', '-')

    song_path = artist + "-" + song_name 

    song_notations = []
    song_path.replace('&' , 'and')

    song_path.replace("'" , "")
    # print(song_path)

    song_notations.append(song_path)

    dash_indices = song_path.find('---')
    # print(dash_indices)
    song_notations.append(song_path[:dash_indices])

    # print(song_notations)

    server = "genius.com"

    for song_notation in song_notations:
        lyrics_url = "https://" + server + "/" + song_notation + "-lyrics"
        # print(lyrics_url)
        resp = requests.get(lyrics_url)

        if resp.status_code == 200:
            soup = BeautifulSoup(requests.get(lyrics_url).content, 'lxml')
            #html_code = BeautifulSoup(resp.text, features="html.parser")
            #print(html_code.prettify)

            #if html_code.find("div", {"class": "lyrics"}) is None:
            #    print('--------------------------------------making a new request because was redirected----------------------------------------------------')
            #    time.sleep(2)
            #    lyricsrequest([raw_name])
            #    return False

            #lyrics = html_code.find("div", {"class": "lyrics"}).get_text()
            cs = soup.select('div[class^="Lyrics__Container"]')
            if cs:
                text = get_text(cs)
            else:
                text = get_text(soup.select('.lyrics'))

            # print(text)

            #print(lyrics)
            
            x = text.split('\n');
            question = x[10];
            answer = x[11];
            answ[question] = answer;
            answ[x[2]] = x[3];
            answ[x[8]] = x[9];
            answ[x[5]] = x[6];
            
            print(answ)
            
            
            return text
        else:
            print("Sorry, I can't find the actual lyrics on this request")

    return False


def get_text(elements):
    text = ''
    for c in elements:
        for t in c.select('a, span'):
            t.unwrap()
        if c:
            c.smooth()
            text += c.get_text(strip=True, separator='\n')
    return text

outfile = open("artist_results.json", "w")
json.dump(get_artist_info("Queen"), outfile, indent=4)

final ={}
final["Name"] = "Queen Live"
final["id"] = "queen"

l = list(answ)
t = 0;

while t < 3 :
    questions = {}
    questions["type"] = "four-quarter"
    questions["question"] = answ[l[t]];
    questions["options"] = [answ[l[t+1]], answ[l[t+2]], answ[l[t+3]], answ[l[t+4]]]
    an = []
    an.append(1);
    questions["answer"] = an
    t = t + 1
    print(questions["question"])
    q.append(questions)
        
final["quizzes"] = q
final["scores"] = [0,0,0,0, 0,0]
final["solved"] = "false"

outfile2 = open("trivia.json", "w")
json.dump(final, outfile2, indent=4)


#search_artists_by_name("Queen")
#print(get_artist_top_tracks("spotify:artist:1dfeR4HaWDbWqFHLkxsg1d"))
song_uri = "spotify:track:3xXBsjrbG1xQIm1xv1cKOt"
#song_uri = "spotify:track:0YCQJdVLN6n9wvfj7ihlTb"
# get_lyrics(sp.track(song_uri))
print(sp.track(song_uri))
