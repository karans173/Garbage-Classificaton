from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from keras.saving import register_keras_serializable
@register_keras_serializable()
def xception_preprocessing(x):
    return preprocess_input(x)

custom_objects = {'xception_preprocessing': xception_preprocessing}
model = load_model("model/model.h5", custom_objects=custom_objects)

categories = {0: 'Battery', 1: 'Biological', 2: 'Brown-glass', 3: 'Cardboard', 4: 'Clothes', 5: 'Green-glass',
              6: 'Metal', 7: 'Paper', 8: 'Plastic', 9: 'Shoes', 10: 'Trash',
              11: 'White-glass'}

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(320, 320))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Preprocess and predict
            img_array = preprocess_image(file_path)
            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions)

            return render_template("index.html", uploaded_image=file.filename, predicted_class=categories[predicted_class])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
