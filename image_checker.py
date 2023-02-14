import pickle

import numpy as np


class ImageChecker:
    def __init__(self):
        self.model = pickle.load(open('model.pkl', 'rb'))

    def check_image(self, image: np.ndarray):
        image = image.reshape(1, 784)
        return self.model.predict(image)
