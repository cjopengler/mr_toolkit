#!/usr/bin/env bash

cat data.txt | python2.7 mapper.py | sort | python2.7 reducer.py