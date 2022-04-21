
# TensorFlow is an open source machine learning library
import tensorflow as tf
# Keras is TensorFlow's high-level API for deep learning
from tensorflow import keras

def getFLOPS(model):
    """
        get FLOPS of the model

        2 FLOPS is about one MACC
    """
    # from https://github.com/tensorflow/tensorflow/issues/32809#issuecomment-768977280
    from tensorflow.python.framework.convert_to_constants import  convert_variables_to_constants_v2_as_graph

    concrete = tf.function(lambda inputs: model(inputs))
    concrete_func = concrete.get_concrete_function(
        [tf.TensorSpec([1, *inputs.shape[1:]]) for inputs in model.inputs])
    frozen_func, graph_def = convert_variables_to_constants_v2_as_graph(concrete_func)
    with tf.Graph().as_default() as graph:
        tf.graph_util.import_graph_def(graph_def, name='')
        run_meta = tf.compat.v1.RunMetadata()
        opts = tf.compat.v1.profiler.ProfileOptionBuilder.float_operation()
        flops = tf.compat.v1.profiler.profile(graph=graph, run_meta=run_meta, cmd="op", options=opts)
        return flops.total_float_ops

def save_model(model, name=None, folder="storedANN"):
    """
        Save as model.h5, model_weights.h5, and model.json

        from https://jiafulow.github.io/blog/2021/02/17/simple-fully-connected-nn-firmware-using-hls4ml/
    """

    if name is None:
        name = model.name

    model.save(folder + "/" + name + '.h5')
    model.save_weights(folder + "/" + name + '_weights.h5')
    with open(folder + "/" + name + '.json', 'w') as outfile:
        outfile.write(model.to_json())
    return

def save_model_image(model):
    # save an image of the ANN
    tf.keras.utils.plot_model(model, 
            to_file=model.name+".png",    # output file name
            #show_layer_activations=True,  # show activation functions
            show_layer_names=True,        # show layer names
            show_dtype=True,              # show datatype
            show_shapes=True,             # show input / output shapes
            rankdir='LR'                  # left to right image
        )
