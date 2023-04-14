from flask import Flask, render_template, request
from PIL import Image
from url_utils import get_base_url
import requests
import io
import base64

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
headers = {"Authorization": "Bearer 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"}


def query(filename):

    response = requests.post(API_URL, headers=headers, data=filename)
    return response.json()


# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
    return render_template('index.html')


@app.route('/index.html', methods=["GET"])
def home2():
    return render_template('index.html')


@app.route('/about.html', methods=["GET"])
def about():
    return render_template('about.html')


@app.route('/products.html', methods=["GET"])
def products():
    return render_template('products.html')


@app.route('/New', methods=["POST"])
def imageClassiffication():
    if request.method == "POST":
        image = request.files["image"]
        img_stream = io.BytesIO(image.read())
        img = Image.open(img_stream)
        img = img.resize((224, 224))

        img_bytes = io.BytesIO()
        # save the resized image to the BytesIO object
        img.save(img_bytes, format='PNG')
        # seek to the start of the BytesIO object
        img_bytes.seek(0)
        img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')
        output = query(img_bytes)
        final = max(output, key=lambda x: x['score'])
        confidence = str(round(final["score"] * 100, 2))
        label = str(final["label"])
        if label == "No helmet":
            final = 0
        elif label == "Helmet":
            final = 1
        else:
            final = 2
        return render_template('Final_ans.html',
                               image_file=img_base64,
                               confidence=confidence,
                               isHelmet=final)


# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'localhost'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
