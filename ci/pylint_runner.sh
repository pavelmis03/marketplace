#!/bin/bash

# run pylint
folders=$(ls -d */ | grep -v -e static -e venv -e ci -e docs -e media -e public -e apps)
pylint $folders | tee pylint.txt

# get badge
score=$(sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' pylint.txt)
anybadge --value=$score --file=public/pylint.svg pylint
echo "Pylint score was $score"

# get html
pylint --load-plugins=pylint_json2html $folders --output-format=jsonextended > pylint.json
pylint-json2html -f jsonextended -o public/pylint.html pylint.json

#cleanup
rm pylint.txt pylint.json

exit 0
