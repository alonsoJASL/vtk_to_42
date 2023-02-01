#!/usr/bin/env bash
set -euo pipefail

if [ $# -eq 0 ] ; then
    >&2 echo 'No arguments supplied'
    exit 1
fi

DIR=$1

docker run --rm --volume=$DIR:/data cemrg/vtk_to_42:latest "${@:2}" 

