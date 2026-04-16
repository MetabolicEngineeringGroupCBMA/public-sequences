#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

declare -A map=(
  [P30104]=pAG25
  [P30113]=pAG26
  [P30105]=pAG29
  [P30108]=pAG31
  [P30106]=pAG32
  [P30109]=pAG34
  [P30107]=pAG35
  [P30110]=pAG36
  [P30111]=pAG60
  [P30112]=pAG61
  [P30119]=pSH47
  [P30120]=pSH62
  [P30121]=pSH63
  [P30122]=pSH65
  [P30115]=pUG27
  [P30114]=pUG6
  [P30116]=pUG66
  [P30117]=pUG72
  [P30118]=pUG73
)

for file in *.*; do
  stem="${file%.*}"   # P30104
  ext="${file##*.}"   # gb or pdf

  if [[ -n "${map[$stem]:-}" ]]; then
    new="${map[$stem]}.${ext}"

    if [[ -e "$new" ]]; then
      echo "Skipping $file -> $new (target exists)"
    else
      echo "Renaming $file -> $new"
      mv -- "$file" "$new"
    fi
  fi
done
