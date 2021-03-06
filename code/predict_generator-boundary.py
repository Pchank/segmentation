import helper.visualize
import helper.data_provider
import helper.model_builder

import skimage.io

import sys

data_dir_x = "/home/jr0th/github/segmentation/data/BBBC022_hand_200/test/x/"
data_dir_y = "/home/jr0th/github/segmentation/data/BBBC022_hand_200/test/y_boundary_4/"


out_label = 'pred_generator'
out_dir = '/home/jr0th/github/segmentation/out_boundary_4_random_augment/'

weights_path = '/home/jr0th/github/segmentation/checkpoints/boundary_4_random_augment/checkpoint_0065.hdf5'
batch_size = 10
bit_depth = 8

dim1 = 256
dim2 = 256

# get generator for test data
test_generator = helper.data_provider.single_data_from_images_1d_y(
    data_dir_x,
    data_dir_y,
    batch_size,
    bit_depth,
    dim1, 
    dim2
)

# build model and laod weights
model = helper.model_builder.get_model_1_class(dim1, dim2)
model.load_weights(weights_path)

# get one batch of data from the generator
(test_x, test_y) = next(test_generator)

# get model predictions
y_pred = model.predict_on_batch(test_x)

# visualize them
helper.visualize.visualize_boundary_hard(y_pred, test_x, test_y, out_dir=out_dir, label=out_label)