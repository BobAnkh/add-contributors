#!/bin/bash
###
 # @Author: BobAnkh
 # @Github: https://github.com/BobAnkh
 # @Date: 2020-07-29 11:47:58
 # @LastEditors: BobAnkh
 # @LastEditTime: 2020-08-02 22:32:22
 # @FilePath: /add-contributors/entrypoint.sh
 # @Description: Entrypoint of Github Action
 # @Copyright 2020 BobAnkh
### 

set -e

python -m pip install --upgrade pip setuptools wheel
pip install -r /requirements.txt

python /main.py
