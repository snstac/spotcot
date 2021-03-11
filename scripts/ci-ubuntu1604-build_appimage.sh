#!/bin/bash


set -eux 

sudo apt -y install git wget curl jq software-properties-common

# install the deadsnakes ppa to get a newer version of python on ubuntu xenial
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# install python 
sudo apt install python$PYTHON_VERSION python$PYTHON_VERSION-dev python$PYTHON_VERSION-venv -y



# install pip 
wget https://bootstrap.pypa.io/get-pip.py
python$PYTHON_VERSION get-pip.py

# replace python3 with python$PYTHON_VERSION
mv `which python$PYTHON_VERSION` `which python3`

# install some runtime dependencies 
sudo apt install -y libtool libcairo-dev libxcb-xinerama0 build-essential

# clone pyappimage and install it
git clone https://github.com/srevinsaju/pyappimage.git --depth=1 pyapim && cd pyapim
python3 -m pip install -r requirements.txt
python3 -m pip install .
cd ..

echo "$(git describe --tags --always --match '*[0-9]*')"

# build the appimage
python3 -m pyappimage.cli build

 
