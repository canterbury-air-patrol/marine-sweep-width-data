#!/bin/bash -ex

./import_data.py

DATA_FILE=marine-sweep-width-data-table.js
TMP_FILE=${DATA_FILE}.tmp

cp ${DATA_FILE} ${TMP_FILE}

git fetch origin
git checkout -b main origin/main

mv ${TMP_FILE} ${DATA_FILE}
