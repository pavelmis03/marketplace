#!/bin/bash

pycodestyle $(ls -d */ | grep -v -e static -e venv -e ci -e docs -e media -e public -e apps) --statistics > public/pycodestyle.txt
exit 0
