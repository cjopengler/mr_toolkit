#!/usr/bin/env bash
cat ./data1/1.txt > ./data1/tmp.txt
cat ./data1/2.txt >> ./data1/tmp.txt
cat ./data1/tmp.txt | python2.7 test_mapper.py | sort > ./data1/mapper_result.txt

rm ./data1/tmp.txt
cat ./data1/mapper_result.txt