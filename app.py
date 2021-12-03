import os
from flask import Flask, # request, redirect, url_for, send_from_directory,
                  render_template

app = Flask(__name__)


@app.route('/') # @app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('template.html')




if __name__ == '__main__':
    app.run()
