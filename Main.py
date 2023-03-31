# import requirements needed
from flask import Flask, render_template, request
from url_utils import get_base_url
import requests

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
  app = Flask(__name__)
else:
  app = Flask(__name__, static_url_path=base_url + 'static')

API_URL = "https://api-inference.huggingface.co/models/pzalavad/AiCampHelmet"
headers = {"Authorization": ""}


def query(filename):
  
  response = requests.post(API_URL, headers=headers, data=filename)
  return response.json()


# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
  return render_template('index.html')


@app.route('/New', methods=["POST"])
def imageClassiffication():
  if request.method == "POST":
    image = request.files["image"]
    output = query(image)
    max_label = max(output, key=lambda x: int(x['score']))['label']
    return f"There is {max_label} in picture"

# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page

if __name__ == '__main__':
  # IMPORTANT: change url to the site where you are editing this file.
  website_url = 'url'

  print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
  app.run(host='0.0.0.0', port=port, debug=True)
