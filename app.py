import os, random, json

from flask import (
    Flask,
    render_template,
    request,
    Response,
    jsonify,
    flash,
)
from werkzeug.middleware.shared_data import SharedDataMiddleware
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import numpy as np

# def video_feed():
# return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# camera = cv2.VideoCapture(0)
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''

# configuration steps for Flask
# load the model 
# set some defaults 
app = Flask(__name__, template_folder='templates', static_folder='static')

curdir = os.getcwd()
app.config['BASE_FOLDER'] = curdir
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER'] = curdir + '/upload'
app.config['PROCESSED_FOLDER'] = curdir + '/published'
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024 * 2
curdir = os.getcwd()

app.add_url_rule('/published/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/published': app.config['PROCESSED_FOLDER'],
})

app.add_url_rule('/upload/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/upload': app.config['UPLOAD_FOLDER'],
})

os.makedirs('upload', exist_ok=True)
os.makedirs('published', exist_ok=True)

# helper functions

import matplotlib.pyplot as plt

# https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
def plot_coords(x,y, task):
    plt.plot(x,y)
    plt.title(task.upper()+' - X and Y coords') 
    plt.xlabel('X coords')
    plt.ylabel('Y coords')
    plt.savefig(task+'.png')
    plt.close()

def get_coords(data):
    xlist=list()
    ylist=list()
    for i in range(len(data)):
        xlist.append(data[i][0])
        ylist.append(data[i][1])
    return xlist, ylist

# API routes
@app.route('/', methods=['GET'])
def serve_front():
    base_url = request.base_url
    return render_template('index.html', url=base_url)

@app.route('/templates/<sessionid>', methods=['GET'])
def templates(sessionid):
    base_url = request.base_url.split('/templates')[0]
    return render_template('templates.html', url=base_url, sessionid=sessionid)

@app.route('/record/<age>/<gender>', methods=['GET'])
def record_session(age, gender, base_url):
    return render_template('record.html', base_url=base_url, age=age, gender=gender)

@app.route('/picture/<sessionid>', methods=['GET'])
def picture(sessionid):
    base_url = request.base_url
    # edit the session with .JSON data (post)
    return render_template('picture.html', base_url=base_url)

@app.route('/video/<sessionid>', methods=['GET'])
def video(sessionid):
    base_url = request.base_url
    # edit the session with .JSON data (post)
    return render_template('video.html', base_url=base_url)

@app.route('/sentence/<sessionid>', methods=['GET'])
def sentence(sessionid):
    base_url = request.base_url
    # edit the session with .JSON data (post)
    return render_template('sentence.html', base_url=base_url)

@app.route('/calibration', methods=['GET'])
def calibration():
    # base_url = request.base_url
    return render_template('calibration.html')

@app.route('/loading/<sessionid>', methods=['GET'])
def loading(sessionid):
    base_url = request.base_url
    return render_template('loading.html', url=base_url, session=sessionid)

@app.route('/video_feed', methods=['GET'])
def video_feed():
    base_url = request.base_url
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/report/<sessionid>', methods=['GET'])
def get_reports(sessionid):
    base_url = request.base_url.split('/report')[0]
    folder = app.config['UPLOAD_FOLDER']+'/'+sessionid
    # assumes all are in listdir 
    # ['baseline.json', 'image.json', 'text.json','video.json']
    # and 
    # ['baseline.png', 'image.png', 'text.png', 'video.png']
    
    # get all the below from loadiing in the .JSON documents 

    # baseline 
    os.chdir(folder)
    g=json.load(open('baseline.json'))
    data=g['data']
    xlist, ylist = get_coords(data)
    baseline_x_avg=np.mean(xlist)
    baseline_y_avg=np.mean(ylist)
    baseline_x_std=np.std(xlist)
    baseline_y_std=np.std(xlist)

    # image 
    g=json.load(open('image.json'))
    data=g['data']
    xlist, ylist = get_coords(data)
    image_x_avg=np.mean(xlist)
    image_y_avg=np.mean(ylist)
    image_x_std=np.std(xlist)
    image_y_std=np.std(ylist)

    # video
    g=json.load(open('video.json'))
    data=g['data']
    xlist, ylist = get_coords(data)
    video_x_avg=np.mean(xlist)
    video_y_avg=np.mean(ylist)
    video_x_std=np.std(xlist)
    video_y_std=np.std(ylist)

    # text 
    g=json.load(open('text.json'))
    data=g['data']
    xlist, ylist = get_coords(data)
    text_x_avg=np.mean(xlist)
    text_y_avg=np.mean(ylist)
    text_x_std=np.std(xlist)
    text_y_std=np.std(ylist)

    return render_template('report.html', session=sessionid, folder=folder, url=base_url, baseline_x_avg=baseline_x_avg, baseline_y_avg=baseline_y_avg, baseline_x_std=baseline_x_std, baseline_y_std=baseline_y_std, image_x_avg=image_x_avg, image_y_avg=image_y_avg, image_x_std=image_x_std, image_y_std=image_y_std, video_x_avg=video_x_avg, video_y_avg=video_y_avg, video_x_std=video_x_std, video_y_std=video_y_std, text_x_avg=text_x_avg, text_y_avg=text_y_avg, text_x_std=text_x_std, text_y_std=text_y_std)

@app.route('/api/<task>', methods=["POST"])
def api_features(task):
    data = request.get_json()
    print(data)

    # write database to .json
    curdir=os.getcwd()
    session=data['sessionId']
    os.chdir(app.config['UPLOAD_FOLDER'])
    try:
        os.mkdir(session)
        os.chdir(session)
    except:
        os.chdir(session)

    jsonfilename='%s.json'%(task)
    if jsonfilename not in os.listdir():
        jsonfile=open(jsonfilename,'w')
        json.dump(data,jsonfile)
        jsonfile.close()
    else:
        print('FILE EXISTS - ' + jsonfilename)
    
    xy=data['data']
    x=list()
    y=list()
    for j in range(len(xy)):
        x.append(xy[j][0])
        y.append(xy[j][1])
    # now make a .PNG as the files come in
    plot_coords(x,y, task)
    
    os.chdir(curdir)

    return jsonify(data)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

class NameForm(Form):
    age = StringField('What is your age?', validators=[Required()])
    gender = SelectField(choices=[('male', 'Male'), ('female', 'Female')])
    submit = SubmitField('Next')

@app.route('/register', methods=['GET', 'POST'])
# taken from https://www.oreilly.com/library/view/flask-web-development/9781491947586/ch04.html
# docs: https://wtforms.readthedocs.io/en/2.3.x/fields/
def index():
    base_url = request.base_url.replace('/register','')

    if request.method == 'GET':
        age = None
        gender = None
        form = NameForm()
        if form.validate_on_submit():
            age = form.age.data
            gender = form.gender.data

        return render_template('register.html', form=form, age=age, url=base_url)

    elif request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        return render_template('record.html', age=age, gender=gender, url=base_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000, ssl_context=('adhoc'))
