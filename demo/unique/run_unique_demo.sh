#!/usr/bin/env bash
DATA=$1

cat ${DATA} | python2.7 mapper.py | sort | python2.7 reducer.py