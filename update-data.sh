#!/bin/bash -ex

./import_data.py

GIT_COMMIT=`git rev-parse HEAD`

DATA_FILE=marine-sweep-width-data-table.js
TMP_FILE=${DATA_FILE}.tmp

cp ${DATA_FILE} ${TMP_FILE}

git checkout main

mv ${TMP_FILE} ${DATA_FILE}

git commit -a -m "Update data table from ${GIT_COMMIT}"
