#!/bin/bash
set +e
if [[ $1 != '' ]]; then
    cd $1
fi

ls | sed "s:^:`pwd`/:"
