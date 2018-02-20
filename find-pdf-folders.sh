#!/bin/bash
sudo  find . -name *.pdf -exec dirname {} \; | sort | uniq -c | sort
