#!/bin/bash
# SPDX-FileCopyrightText: 2026 Aruto Katsuno
# SPDX-License-Identifier: BSD-3-Clause
ng () {
        echo ${1}行目のテスト失敗
        res=1
}
res=0
### NORMAL INPUT (stdin) ###
out=$(echo "1 1 1" | timeout 2 ./coffee_break.py)
[ "$?" = 124 ]      || ng "$LINENO"
[ "${out}" != "" ]  || ng "$LINENO"
### NORMAL INPUT (args) ###
out=$(timeout 2 ./coffee_break.py -w 1 -b 1 -c 1)
[ "$?" = 124 ]      || ng "$LINENO"
[ "${out}" != "" ]  || ng "$LINENO"
### HELP ###
./coffee_break.py --help > /dev/null
[ "$?" = 0 ]        || ng "$LINENO"
### STRANGE INPUT ###
out=$(echo あ | ./coffee_break.py 2>/dev/null)
[ "$?" = 1 ]        || ng "$LINENO"
[ "${out}" = "" ]   || ng "$LINENO"
out=$(echo "0 1 1" | ./coffee_break.py 2>/dev/null)
[ "$?" = 1 ]        || ng "$LINENO"
[ "${out}" = "" ]   || ng "$LINENO"
out=$(echo "-1 1 1" | ./coffee_break.py 2>/dev/null)
[ "$?" = 1 ]        || ng "$LINENO"
[ "${out}" = "" ]   || ng "$LINENO"
out=$(echo | ./coffee_break.py 2>/dev/null)
[ "$?" = 1 ]        || ng "$LINENO"
[ "${out}" = "" ]   || ng "$LINENO"
out=$(./coffee_break.py -w 0 2>/dev/null)
[ "$?" = 1 ]        || ng "$LINENO"
[ "${out}" = "" ]   || ng "$LINENO"
[ "${res}" = 0 ] && echo OK
exit $res

