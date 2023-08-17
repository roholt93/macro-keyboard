#!/bin/bash
set -exou pipefail

[[ $EUID -ne 0 ]] || {
    echo "[ERROR]     Do not run as root!"
    exit 1
}

SERVICE_FILE_LOCATION="/etc/systemd/system/"
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TEMP_DIR=$THISDIR/temp

[ ! -d ${TEMP_DIR} ] && mkdir -p ${TEMP_DIR}

USER=`id -nu`

sed "s,{{WORKING_DIR}},${THISDIR},g" ${THISDIR}/macro-keyboard.service > ${TEMP_DIR}/macro-keyboard.service
sed -i "s,{{LOCAL_USER}},${USER},g" ${TEMP_DIR}/macro-keyboard.service

sudo cp ${TEMP_DIR}/macro-keyboard.service ${SERVICE_FILE_LOCATION}/macro-keyboard.service
sudo systemctl daemon-reload
sudo systemctl enable macro-keyboard
