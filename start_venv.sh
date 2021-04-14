#!/bin/bash
python_version=`python3 -c 'import sys; version=sys.version_info[:3]; print("{0}.{1}.{2}".format(*version))'`
if [ -z "${python_version}" ]
then
  echo "python3 not found!"
  exit 2
fi
if [ "$python_version" \> "3.7" ]
then
    echo "found python ${python_version}, continue... "
else
    echo "python verison has to be greater than 3.7, exit!"
    exit 2
fi

pip3 install wheel
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
