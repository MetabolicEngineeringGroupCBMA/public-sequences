#!/usr/bin/env bash

while read line; do
    cp "$line" .
done < paths.txt


echo "press any key to close"
read -n1 slask
