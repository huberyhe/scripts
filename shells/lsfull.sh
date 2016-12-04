#!/bin/bash
set +e
ls $* | sed "s:^:`pwd`/:"
