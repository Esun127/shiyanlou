#!/bin/bash

if [[ $# -gt 0 ]]; then
    for name in $*; do
		if [ ! -f $name ]; then
        	echo "#!/usr/bin/env python3" > $name
        	chmod a+x $name
		fi
        vim $name
    done
else
    exit 1
fi
