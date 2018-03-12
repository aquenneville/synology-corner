#!/bin/bash
# cd in your Download directory
cd ~/Downloads
ls | egrep '.*\s\(\d\).pdf' | tr "\n" "\0" | xargs -0 rm -v
