import hashlib
from bottle.ext import sqlite
import os,bottle
from bottle import route, request, static_file, run, template, BaseTemplate, static_file

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url

app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='db.db')
app.install(plugin)

@route('/user-count-log/precache-manifest.3afdd022b20aa72b3976a6bd3acaabaf.js')
def root():
    return static_file('precache-manifest.3afdd022b20aa72b3976a6bd3acaabaf.js',root='.')

@route('/user-count-log/css/app.01f598db.css')
def root():
    return static_file('css/app.01f598db.css',root='.')

@route('/user-count-log/js/app.933eb632.js')
def root():
    return static_file('js/app.933eb632.js',root='.')

@route('/user-count-log/js/chunk-vendors.d47151e8.js')
def root():
    return static_file('js/chunk-vendors.d47151e8.js',root='.')

@route('/user-count-log/js/app.933eb632.js')
def root():
    return static_file('js/app.933eb632.js',root='.')

@route('/manifest.json')
def root():
    return static_file('manifest.json',root='.')

@route('/')
def root():
    return static_file('index.html', root='.')

@route('/user-count-log/service-worker.js')
def root():
    return static_file('service-worker.js',root='.')

@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    save_path = "/tmp/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    os.system("python3 /home/kali/Desktop/face_len.py "+file_path+"> rez.txt")
    f = open("rez.txt","r")
    a = f.read(1)
    return "Faces in the photo: " + a

@route('/api',method='POST',apply=[plugin])
def data(db):
    data = request.body.read()
    data2 = str(data)
    data_hash = hashlib.sha256(data2.encode())
    row = db.execute("SELECT Hash FROM Hashes WHERE Hash='"+data_hash.hexdigest()+"'")
    row = row.fetchall()
    if(row):
        return bottle.HTTPResponse(status=403)

    db.execute("INSERT INTO Hashes (Hash) VALUES (\""+data_hash.hexdigest()+"\")")
    data = str(data.decode('utf-8'))
    data = data.split(',')
    arr = []
    for i in data:
        arr.append(i[1:-1])

if __name__ == '__main__':
    run(host='localhost', port=8000)
