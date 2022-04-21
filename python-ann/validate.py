"""
    test the performance of the ANN
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import tensorflow as tf
from tensorflow import keras

# import parameters
from parameters import *

# import generation of waveforms
from training import generate_training_data

def validate(model):

    # number of test waveforms
    SAMPLES = 1000

    waveforms = []        # generated waveforms
    orig_parameters = []  # parameters, which are used for the generation
    NN_parameters = []    # parameters, reconstructed by the NN

    # vary the parameters to have a look a the performance outside the trained 
    # parameter boundaries.
    parameter_variation = 0.0

    # increase the range of parameters in order to see, what is happening
    T_width    = ( P_width[0]    * (1 - parameter_variation) , P_width[1]    * (1 + parameter_variation) )
    T_position = ( P_position[0] * (1 - parameter_variation) , P_position[1] * (1 + parameter_variation) )
    T_height   = ( P_height[0]   * (1 - parameter_variation) , P_height[1]   * (1 + parameter_variation) )
    T_offset   = ( P_offset[0]   * (1 - parameter_variation) , P_offset[1]   * (1 + parameter_variation) )

    parameters, waveforms = generate_training_data(SAMPLES, T_width, T_position, T_height, T_offset)

    for i in range( len(waveforms) ):
      print(i, "of", len(waveforms) )
      # waveform needs to be reshaped to be fed into ANN
      waveform = waveforms[i].reshape(1,128)
      width, position, height = model.predict(waveform)[0]

      #width *= SCALE_WIDTH
      #position *= SCALE_POS
      #height *= SCALE_HEIGHT

      NN_parameters.append( (width, position, height))

    plot_x = [k[0] for k in parameters]
    plot_y = [k[0] for k in NN_parameters]

    plt.hist2d(plot_x, plot_y, bins=32, cmin=1, cmap='summer')
    plt.vlines(np.array(P_width),ymin=0, ymax=100)
    plt.plot( [np.min(plot_x), np.max(plot_x)], [np.min(plot_x), np.max(plot_x)])
    plt.colorbar()
    plt.title("Colab Width")
    plt.ylabel("NN parameter")
    plt.xlabel("truth parameter")
    plt.savefig("val_width.png")
    plt.show()

    plot_x = [k[1] for k in parameters]
    plot_y = [k[1] for k in NN_parameters]
    plt.hist2d(plot_x, plot_y, bins=32, cmin=1, cmap='summer')
    plt.vlines(np.array(P_position),ymin=0, ymax=100)
    plt.plot( [np.min(plot_x), np.max(plot_x)], [np.min(plot_x), np.max(plot_x)])
    plt.colorbar()
    plt.title("Colab Postition")
    plt.ylabel("NN parameter")
    plt.xlabel("truth parameter")
    plt.savefig("val_position.png")
    plt.show()

    plot_x = [k[2] for k in parameters]
    plot_y = [k[2] for k in NN_parameters]
    plt.hist2d(plot_x, plot_y, bins=32, cmin=1, cmap='summer')
    plt.vlines(np.array(P_height),ymin=0, ymax=1000)
    plt.plot( [np.min(plot_x), np.max(plot_x)], [np.min(plot_x), np.max(plot_x)])
    plt.colorbar()
    plt.title("Colab Height")
    plt.ylabel("NN parameter")
    plt.xlabel("truth parameter")
    plt.savefig("val_height.png")
    plt.show()


if __name__ == "__main__":
    # Recreate the exact same model, including its weights and the optimizer
    model = tf.keras.models.load_model('storedANN/network_MAX78000_v0.1.h5')

    # Show the model architecture
    model.summary()

    validate(model)
