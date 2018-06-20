import sys

from keras.preprocessing.image import img_to_array, load_img
from scipy import misc
import config
import os
import model
import preprocessor


def predict(img_file):
    img = load_img(img_file)
    return predict_img(img)


def predict_img(img):
    x = img_to_array(img)
    x = misc.imresize(x, (150, 150, 3))
    x = x.reshape((1,) + x.shape)

    convnet = model.small_convnet()

    weights_path = os.path.join(config.weights_dir, config.weights_name)

    convnet.load_weights(weights_path)
    p = convnet.predict_classes(x, verbose=1)
    print(p)
    # get label indices
    train_generator = preprocessor.train_data_generator()
    class_dictionary = train_generator.class_indices
    return list(class_dictionary.keys())[list(class_dictionary.values())[int(p[0])]]


if __name__ == '__main__':
    print("Predicted class is: %s" % (predict(sys.argv[1])))
