import numpy as np
#import h5py
from sklearn import datasets    
    
def load_dataset():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def load_dataset_iris():
    iris = datasets.load_iris()
#    print("data shape:", iris['data'].shape )
#    print("target shape:", iris['target'].shape, " label:", set(iris['target']))
#    print("target_names:", set(iris['target_names']))
#    print("feature_names:", iris['feature_names'])

    shuffled_data = np.random.permutation(np.concatenate((iris['data'], iris['target'].reshape(150,1)), axis=1))
    
    train_set_x_orig = shuffled_data[:100,:4]
    test_set_x_orig = shuffled_data[100:,:4]
    train_set_y_orig = (shuffled_data[:100,4:]==2).astype(np.int)
    test_set_y_orig = (shuffled_data[100:,4:]==2).astype(np.int)

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig
