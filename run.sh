#!/bin/bash
set -eou pipefail

ENV_DIR=".env"

[ ! -d ${ENV_DIR} ] && python3 -m venv ${ENV_DIR}
source ${ENV_DIR}/bin/activate

python3 -m pip install -r requirements.txt
python3 macro-watcher.py