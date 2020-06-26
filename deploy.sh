#! /bin/sh

set euo pipefail
pip3 install -t lib/ -r requirements.txt
gcloud app deploy
