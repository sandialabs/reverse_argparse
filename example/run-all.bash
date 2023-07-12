#!/usr/bin/env bash
quote_arg() {
    if [[ "$1" =~ ( ) ]]; then
        echo -n "'$1' "
    else
        echo -n "$1 "
    fi
}

run_script() {
    echo
    echo -n "~~~~~  Running "
    for arg in "$@"; do
        quote_arg "${arg}"
    done
    echo " ~~~~~"
    echo
    python3 "$@"
    echo
}

ORIG_DIR=$(pwd)
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
cd "${SCRIPT_DIR}" || exit 1
python3 -m pip uninstall -y reverse_argparse
cd ..
python3 -m pip install .
cd "${SCRIPT_DIR}" || exit 1
run_script basic.py --foo bar
run_script default_values.py --foo bar
run_script relative_references.py --src bar.txt
run_script post_processing.py --before '30 minutes ago'
run_script pretty_printing.py --foo eggs --src file.txt --before 'today'
run_script subparsers.py foo --one eggs
cd "${ORIG_DIR}" || exit 1
