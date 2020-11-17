#!/bin/sh
#generate a back-ground image with appropriate label/title

DIR="${HOME}/tmp/rpy_projects/TonysPlace/game/images"
# Canvas Size 
H=1280
V=720

convert -background grey -size ${H}x${V} -fill blue -pointsize 72 label:${1} ${DIR}/${1}.png

echo "Written: ${DIR}/${1}.png"
