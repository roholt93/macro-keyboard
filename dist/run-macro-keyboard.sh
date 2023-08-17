#!/bin/bash
set -eou pipefail

# directory of the script, can be useful for locating files which are next to the script.
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ENV_DIR="${THISDIR}/../.env"

[ ! -d ${ENV_DIR} ] && python3 -m venv ${ENV_DIR}
source ${ENV_DIR}/bin/activate

python3 -m pip install -r $THISDIR/../requirements.txt
python3 ${THISDIR}/../macro-watcher.py