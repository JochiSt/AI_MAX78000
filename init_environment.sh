#!/bin/bash

# set project root folder
export AI_PROJECT_ROOT=`pwd`

# check python version
PYTHONVERS=`python -c "import sys; print(''.join(map(str, sys.version_info[:2])))"`
if [ "$PYTHONVERS" -lt "37" ] 
then
    echo "Python Version $PYTHONVERS not supported python >= 3.7 needed!"
    exit -1
fi

# update all submodules
# --force to really ensure a fresh environment
git submodule update --init --recursive --force

################################################################################
# prepare ai8x-training venv
echo "INIT ai8x-training ..."
cd ai8x-training 
python3 -m venv .

# activate environment and install some needed python modules
source bin/activate
pip3 install --upgrade pip
pip3 install -U pip wheel setuptools

cd TensorFlow
pip3 install -r requirements_tf.txt

# matplotlib is needed as well
pip3 install matplotlib

# was needed
pip3 install tensorflow
pip3 install tensorflow_datasets

# install converter to ONNX format
pip3 install tf2onnx

# since we want to get a nice image of the ANN
pip3 install pydot


# we are done with this folder, deactivate environment
deactivate

################################################################################

echo " ... done"
# and return to project folder
cd $AI_PROJECT_ROOT

################################################################################
# prepare ai8x-synthesis venv
echo "INIT ai8x-synthesis ..."

# we have to make sure python version > 3.6, because otherwise numpy is limited 
# to <1.20, which is a problem here.

cd ai8x-synthesis
python3 -m venv .

# activate environment and install some needed python modules
source bin/activate
pip3 install --upgrade pip
pip3 install -U pip wheel setuptools
pip3 install -r requirements.txt

#pip3 install matplotlib

# install pytorch for generating the examples
# somehow gen-tf-demos-max78000.sh needs pyTorch and some other packages
#pip3 install torch colorama onnx onnxruntime pyyaml yamllint

# deactivate environment
deactivate

################################################################################
cd $AI_PROJECT_ROOT
echo "finished setup of environment"

