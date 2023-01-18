import sys
sys.path.append('/Users/rohitsharma/opt/anaconda3/lib/python3.9/site-packages')

from flask import Flask, request
from flask import make_response

import subprocess

app = Flask(__name__)

@app.route('/runscript', methods=['POST'])
def run_script():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    event = data['event']
    subprocess.call(["python", "signcalfinal2.py", latitude, longitude, event])
    return "Script Running"

resp = make_response("Input received and script ran successfully",200)
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=8000)
