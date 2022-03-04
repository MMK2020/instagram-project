from urllib import request
from app import app    #import the app object from the app itself 
from flask import render_template, request
import requests
from bs4 import BeautifulSoup

@app.route("/")	       #Define the route using the @app.route decorator and passing the URL 
def index():            #index is a view function
    return render_template("index.html")

@app.route('/get_post', methods=['POST'])
def get_post():
    url = request.form['url']
    try:
        v_url = getdata(url)
        return render_template('index.html', found=True, video=v_url)
    except:
        print('not found')
        return render_template('index.html', found=True, video="Not found")
    
def getdata(url):
    result = requests.get(url).text
    soup = BeautifulSoup(result, "html.parser")
    video_url = soup.find('meta', attrs={'property':'og:video'})['content']
    return video_url