from model import small_convnet
from preprocessor import train_data_generator, val_data_generator

def train():
	train_generator = train_data_generator()
	val_generator = val_data_generator()

	model = small_convnet()
	
	model.summary()

	model.load_weights('weights/weights.h5')

	model.fit_generator(
        train_generator,
        steps_per_epoch=2000 // batch_size,
        epochs=10,
        validation_data=val_generator,
        validation_steps=800 // batch_size)

	model.save_weights('weights/weights.h5')


if __name__ == '__main__':
	train()