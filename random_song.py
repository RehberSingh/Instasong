import sqlite3
import random

def add_song(song):
  conn = sqlite3.connect(r'song_data.db')
  cursor = conn.cursor()
  track = song[0]['track_name']
  i = (track , )
  cursor.execute('''SELECT * from song_data where track_name = ?''', i)
  result = cursor.fetchall()

  if result != []:
    conn.close()
  else:
    a = song[0]['track_name']
    b = song[0]['artist_name']
    c = song[0]['album_art']
    d = song[0]['artist_pic']
    str = ","
    e =str.join(song[0]['lyrics'])
    data = (a,b,c,d, e)
    cursor.execute('''INSERT INTO song_data(track_name,artist_name,album_art, artist_pic , lyrics) VALUES (?, ?, ?, ?,? )''' , data)
    conn.commit()
    conn.close()

def extra():
  conn = sqlite3.connect(r'song_data.db')
  cursor = conn.cursor()
  cursor.execute('''SELECT * FROM song_data''')
  i = (random.randint(1,len(cursor.fetchall())-1),)
  print(i)
  cursor.execute('''SELECT * from song_data where id = ?''', i)
  result = cursor.fetchone()
  conn.close()
  random_song = []
  dict={}
  dict['track_name'] = result[1]
  dict['artist_name'] =result[2] 
  dict['album_art'] = result[3]
  dict['artist_pic'] = result[4]
  dict['lyrics'] = result[5].replace('['or']' , '').replace('"','').replace(chr(39) , '').split(',')
  random_song.append(dict)
  return random_song
