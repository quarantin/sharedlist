#!/bin/bash

. $(dirname $0)/env.sh

cd ${ROOTDIR}

${PYTHON} manage.py runserver
