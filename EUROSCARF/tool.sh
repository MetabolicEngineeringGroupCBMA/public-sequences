#!/bin/bash

base="http://euroscarf.de/plasmid_details.php?accno="
site="http://euroscarf.de"

accnos=(
P30104 P30113 P30105 P30108 P30106 P30109 P30107 P30110
P30111 P30112 P30119 P30120 P30121 P30122 P30115 P30114
P30116 P30117 P30118
)

for acc in "${accnos[@]}"; do
    url="${base}${acc}"
    echo "Processing $acc"

    html=$(curl -s "$url")

    echo "$html" | grep -oE 'href="[^"]+\.(pdf|dna)"' | sed 's/href="//;s/"//' | while read link; do
        
        # handle relative vs absolute links
        if [[ "$link" =~ ^http ]]; then
            full_link="$link"
        else
            full_link="$site/$link"
        fi

        echo "  Downloading $full_link"
        wget -q "$full_link"
    done
done
