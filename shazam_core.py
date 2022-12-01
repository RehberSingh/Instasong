import requests
import json
import re

def shazamAPI(wav_file):
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/recognize'

    files = {'file': (wav_file, open(wav_file,'rb'), 'audio/wav')}
    headers = {
    'X-RapidAPI-Key': 'Insert Your Own key here',
    'X-RapidAPI-Host': 'shazam-core.p.rapidapi.com'
    }

    response = requests.request('POST', url, files=files, headers=headers)
    x=json.loads(response.text)
    print(x)
    try:
        main_song = []
        dict={}
        track_name  = x['track']['urlparams']['{tracktitle}']
        dict['track_name']  = re.sub(r"[%123456789]", " ", track_name).replace('+',' ')
        artist_name =  (x['track']['urlparams']['{trackartist}'].replace('+',' ')).replace('%27',' ')
        dict['artist_name'] = re.sub(r"[%123456789]", " ", artist_name).replace('+',' ')
        dict['album_art'] = x['track']['share']['image']
        dict['artist_pic'] = (x['track']['sections'][0]['metapages'][0]['image'])
    except:
        print('Not Found')
        return(False)
    try:
        dict['lyrics'] = (x['track']['sections'][1]['text'])
    except:
        dict['lyrics'] = []
    main_song.append(dict)
    return main_song






