#!/bin/bash
if [[ $1 != "" && $2 != "" && $3 != "" ]]; then
  git add . --all
  git commit -a -S --author="${1} <${2}>" -m "${3}"
else
  echo "USAGE: ${0} '<full name>' <email address> '<git commit comments>'"
fi
