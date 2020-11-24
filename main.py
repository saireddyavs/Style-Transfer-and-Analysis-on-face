import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import requests

import os
import sys
from PIL import Image
from deepface import DeepFace

import numpy as np
import tweepy

#variables for accessing twitter API
consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

tweet_text="My Auto Tweet for #CodeChella"


def compressMe(folder, file):
    picture = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], file))
    picture.save(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + file),
                 "JPEG",
                 optimize=True,
                 quality=15)
    return True


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed')
        return render_template('upload.html', filename=os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route("/post_to_twitter/<path:filename>")
def post_to_twitter(filename):
    status = api.update_with_media(filename, tweet_text)
    print(status)
    return render_template('upload.html', filename= filename)





@app.route('/style', methods=['POST'])
def style_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if request.form.get("mosaic"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=mosaic"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" + filename)):
                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" +filename) )

            # filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" +filename)


            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" +filename))
        if request.form.get("udnie"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=udnie"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" + filename)):
                return render_template('show_image.html', filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" +filename))

            # print("Hello")
            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" +filename))
        if request.form.get("candy"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=candy"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" + filename)):
                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" +filename))

            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" +filename))
        if request.form.get("rain_princess"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=rain_princess"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" + filename)):
                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" +filename))

            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" +filename) )
        else:
            try:
                # print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                obj = DeepFace.analyze(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(obj)
                obj['age']=int(obj['age'])

                # print(filename)

                return render_template('show_image.html', age=obj['age'],dominant_emotion=obj['dominant_emotion'],dominant_race=obj['dominant_race'],gender=obj['gender'],filename=os.path.join(app.config['UPLOAD_FOLDER'],  filename))



            except Exception as e:
                print("In except ")
                print(e)
                return render_template('show_image.html', message="Can not find the face correctly in the image or else there is no face in the image" ,filename=os.path.join(app.config['UPLOAD_FOLDER'],  filename))



        return render_template('show_image.html', filename=os.path.join(app.config['UPLOAD_FOLDER'], filename))

    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

    # do something



@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)

    # app.run(debug=True)