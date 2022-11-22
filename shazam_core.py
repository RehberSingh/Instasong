import requests
import json
from pprint import pprint
import re

def shazamAPI(wav_file):
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/recognize'

    files = {'file': (wav_file, open(wav_file,'rb'), 'audio/wav')}
    headers = {
    'X-RapidAPI-Key': '54e1e1c2f9msh50a9264fc352c84p143f4bjsned8e3f1f3bfe',
    'X-RapidAPI-Host': 'shazam-core.p.rapidapi.com'
    }

    response = requests.request('POST', url, files=files, headers=headers)
    x=json.loads(response.text)
    print(x)
    main_song = []
    dict={}
    track_name  = x['track']['urlparams']['{tracktitle}']
    dict['track_name']  = re.sub(r"[%123456789]", " ", track_name).replace('+',' ')
    artist_name =  (x['track']['urlparams']['{trackartist}'].replace('+',' ')).replace('%27',' ')
    dict['artist_name'] = re.sub(r"[%123456789]", " ", artist_name).replace('+',' ')
    dict['album_art'] = x['track']['share']['image']
    dict['artist_pic'] = (x['track']['sections'][0]['metapages'][0]['image'])
    try:
        dict['lyrics'] = (x['track']['sections'][1]['text'])
    except:
        dict['lyrics'] = []
    main_song.append(dict)
    print(main_song)
    return main_song



