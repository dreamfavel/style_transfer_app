import os
from flask import Flask, render_template
 # request, redirect, url_for, send_from_directory,


app = Flask(__name__)


@app.route('/') # @app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('template.html')




if __name__ == '__main__':
    app.run()
