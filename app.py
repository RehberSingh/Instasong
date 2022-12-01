from flask import * 
from shazam_core import shazamAPI
from random_song import extra , add_song
import os
from output import audio_processing
import  validators


app = Flask(__name__)


@app.route('/')
def upload_file():
   return render_template('index.html')

	
@app.route('/', methods = ['GET', 'POST'])
def show_results():
   if request.method == 'POST':
      f = request.form['text']
      if validators.url(f) == True:
         output_file = audio_processing(f)
         if output_file != "Not Found":
            mainsong = shazamAPI(output_file)
            os.remove(output_file)
            if mainsong != False:
               add_song(mainsong)
               return render_template('results.html' , main_song = mainsong)
            else:
               return render_template('not_found.html')
         else:
            return render_template('load.html')
      else:
         return render_template('index.html')

@app.route('/random')
def random_song():
    random_song = extra()
    return render_template('random.html' , random_song = random_song)   

if __name__ == '__main__':
    app.run(debug=True)
