# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.examples.tutorials.mnist import input_data

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)
fashion_mnist        = input_data.read_data_sets('data/fashion')


(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

