from model import small_convnet
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from scipy import ndimage, misc
from preprocessor import train_data_generator
import sys

def predict(img_file):
    model = small_convnet()

    model.load_weights('weights/weights.h5')

    img = load_img(img_file)
    x = img_to_array(img)
    x = misc.imresize(x, (150, 150, 3))
    x = x.reshape((1,) + x.shape)
    p =  model.predict_classes(x, verbose=1)
    print(p)
    # get label indices
    train_generator = train_data_generator()
    class_dictionary = train_generator.class_indices
    
    return class_dictionary.keys()[class_dictionary.values().index(int(p[0]))]


if __name__ == '__main__':
    print("Predicted class is: %s" %(predict(sys.argv[1])))