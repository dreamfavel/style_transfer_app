import os
from flask import Flask, render_template, request
 # request, redirect, url_for, send_from_directory,


app = Flask(__name__)

@app.route('/') # @app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('template.html')

@app.route('/', methods=['POST'])
def content_img():
    print('USE FIRST FUNC')
    content_img = request.files.get('content_img')
    if content_img:
        filename =  os.getcwd() + '/static/content_img.jpg'
        filename2 = 'content_img.jpg'
        content_img.save(filename)
        return render_template('template.html', filename_content = filename2)
    else:
        return render_template('template.html')

@app.route('/', methods=['POST'])
def style_img():
    print(request.files)
    print('SOME')
    style_img = request.files.get('style_img')
    if style_img:
        filename =  os.getcwd() + '/static/style_img.jpg'
        filename2 = 'style_img.jpg'
        style_img.save(filename)
        return render_template('template.html', filename_style = filename2)
    else:
        return render_template('template.html')



if __name__ == '__main__':
    app.run()
