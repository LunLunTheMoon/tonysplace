#!/usr/bin/env bash

#find all the missing images and create placeholders
H="${HOME}/tmp/rpy_projects/TonysPlace"
SCRIPT="${H}/scripts"
GAME="${H}/game"
LAB="${GAME}/labels"
IMG="${GAME}/images"

L=$(cat ${LAB}/*.rpy | grep ' scene' | sort | uniq | awk '{print $2}' | grep -v 'black')

for png in ${L}
do
  if ! [ -f "${IMG}/${png}.png" ]
  then
    ${SCRIPT}/make_bg.sh ${png}
  fi
done
