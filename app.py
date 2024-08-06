from flask import Flask, render_template, request
import base64
from io import BytesIO
from PIL import Image
import re
from test_models import predict_digit_from_image
from ImageUtils import ImageUtils

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/post_drawing')
def post_drawing():
    base64_image = request.form['canvas_image']
    base64_image = re.sub('^data:image/.+;base64,', '', base64_image)
    image_data = base64.b64decode(base64_image)

    img = Image.open(BytesIO(image_data))

    img = ImageUtils.convert_transparent_to_color(img, new_color=(0, 0, 0), color_non_transparents=(255, 255, 255))
    img = img.convert('RGB')

    # Save the modified image
    img.save('static/images/original_image.jpg')

    predicted_number = predict_digit_from_image(img)

    return str(predicted_number)

if __name__ == '__main__':
    app.run(debug=True)
