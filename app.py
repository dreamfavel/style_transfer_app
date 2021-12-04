import os
import gc
import shutil
from flask import Flask, render_template, request, send_from_directory
from utils import tensor_to_image, load_img
from utils import create_stylized_image, hub_module

STATIC_DIR =  os.getcwd() + '/static/'
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

app = Flask(__name__)

@app.route('/') # @app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('template.html')

@app.route('/', methods=['GET', 'POST'])
def upload_images():

    if request.method == 'POST':
        # clean previos predictions
        for filename in os.listdir(STATIC_DIR):
            file_path = os.path.join(STATIC_DIR, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        # get content image from request
        content_img = request.files.get('content_img')
        filename1 =  STATIC_DIR + 'content_img.jpg'
        content_img.save(filename1)
        # get style image from request
        style_img = request.files.get('style_img')
        filename2 =  STATIC_DIR + 'style_img.jpg'
        style_img.save(filename2)

        # transform images to the required format
        content_img = load_img(filename1)
        style_img = load_img(filename2)
        # create path to predicted image
        img_path = STATIC_DIR + 'predict_img.jpg'
        # predict and save image with transfered style
        create_stylized_image(hub_module, content_img, style_img, img_path)
        # clean ram
        gc.collect()

        return render_template('template.html', filename = 'true')

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=STATIC_DIR, path=filename)

if __name__ == '__main__':
    app.run()
