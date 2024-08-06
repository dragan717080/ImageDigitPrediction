from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

class Mnist:
    def __init__(self) -> None:
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

        self.train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
        self.test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

        self.train_labels = to_categorical(train_labels)
        self.test_labels = to_categorical(test_labels)

        self.build_model()
        self.compile_model()
        self.train_model()
        self.evaluate_model()
        self.save_model()

    def build_model(self):
        self.model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])

    def compile_model(self):
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

    def train_model(self):
        self.history = self.model.fit(self.train_images, self.train_labels, epochs=5, batch_size=64, validation_split=0.1)

    def evaluate_model(self):
        self.test_loss, self.test_acc = self.model.evaluate(self.test_images, self.test_labels)

        print(f"Test accuracy: {self.test_acc:.4f}")

    def save_model(self):
        # Save the trained model to HDF5 file format
        self.model.save('mnist_model.h5')

mnist_model = Mnist()
