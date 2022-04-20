#!/bin/bash

# set project root folder
export AI_PROJECT_ROOT=`pwd`

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

# we are done with this folder, deactivate environment
deactivate

################################################################################

echo " ... done"
# and return to project folder
cd $AI_PROJECT_ROOT

################################################################################
# prepare ai8x-synthesis venv
echo "INIT ai8x-synthesis ..."
cd ai8x-synthesis
python3 -m venv .

# activate environment and install some needed python modules
source bin/activate
pip3 install --upgrade pip
pip3 install -U pip wheel setuptools
pip3 install -r requirements.txt

pip3 install matplotlib

# deactivate environment
deactivate

################################################################################
cd $AI_PROJECT_ROOT
echo "finished setup of environment"

