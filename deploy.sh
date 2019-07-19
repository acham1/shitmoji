#! /bin/sh

set euo pipefail
pip install -t lib/ -r requirements.txt
gcloud app deploy
