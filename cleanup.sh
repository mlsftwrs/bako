#!/usr/bin/bash

swd=$(dirname $0)
cwd=$(pwd)

cd $swd
for i in $(find . -name *~);
do
    echo "Removing ${i}"
    rm $i
done

for i in $(find . -name __pycache__);
do  
    echo "Removing ${i}"
    rm -rf ${i}
done

if [ -d "./dist" ];
then
    rm -rf "./dist"
fi

if [ -d "./build" ];
then
    rm -rf "./build"
fi

for i in $(find . -name "*egg-info");
do
    rm -rf $i
done

cd $cwd
