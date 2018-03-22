#!/bin/bash
# change to the user Download directory
cd ~/Downloads || exit;
ls | grep -E '.*\s\(\d\).pdf' | tr '\\n' '\\0' | xargs -0 rm -v
