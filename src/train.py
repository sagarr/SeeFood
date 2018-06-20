from model import small_convnet
from preprocessor import train_data_generator, val_data_generator
import config
import os


def train():
    batch_size = 16
    train_generator = train_data_generator()
    val_generator = val_data_generator()

    model = small_convnet()

    model.summary()

    weights_path = os.path.join(config.weights_dir, config.weights_name)

    if config.fine_tune:
        model.load_weights(weights_path)

    model.fit_generator(
        train_generator,
        steps_per_epoch=2000 // batch_size,
        epochs=config.epochs,
        validation_data=val_generator,
        validation_steps=800 // batch_size)

    model.save_weights(weights_path)


if __name__ == '__main__':
    train()