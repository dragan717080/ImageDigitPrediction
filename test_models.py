import numpy as np
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from typing import Tuple

model = load_model('mnist_model.h5')

def get_model_accuracy() -> Tuple[float]:
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

    test_labels = to_categorical(test_labels)

    loss, accuracy = model.evaluate(test_images, test_labels)

    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}") # 99.10%

    return loss, accuracy

def predict_digit_from_image(img: Image.Image) -> int:
    img = ImageOps.grayscale(img)
    img = img.resize((28, 28))
    img.save('static/images/test_image.jpg')
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = np.expand_dims(img_array, axis=-1)

    predictions = model.predict(img_array)

    # Get the predicted digit (index of the highest probability)
    predicted_digit = np.argmax(predictions[0])
    print('Predicted digit:', predicted_digit)

    return predicted_digit
