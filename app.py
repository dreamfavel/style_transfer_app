import os
from flask import Flask, render_template, request
from utils import tensor_to_image, load_img
from utils import create_stylized_image, hub_module


app = Flask(__name__)

@app.route('/') # @app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('template.html')

@app.route('/', methods=['GET', 'POST'])
def upload_images():

    if request.method == 'POST':
        # get content image from request
        content_img = request.files.get('content_img')
        filename1 =  os.getcwd() + '/static/content_img.jpg'
        content_img.save(filename1)
        # get style image from request
        style_img = request.files.get('style_img')
        filename2 =  os.getcwd() + '/static/style_img.jpg'
        style_img.save(filename2)

        # transform images to the required format
        content_img = load_img(filename1)
        style_img = load_img(filename2)
        # create path to predicted image
        img_path = os.getcwd() + '/static/predict_img.jpg'
        # predict and save image with transfered style
        create_stylized_image(hub_module, content_img, style_img, img_path)

        return render_template('template.html', filename = 'true')




if __name__ == '__main__':
    app.run()
