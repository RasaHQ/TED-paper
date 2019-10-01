#!/usr/bin/env bash

# Set directory to the one this script is in
cd $(dirname $0)

rasa test core \
	--stories data/test \
	--out results/test \
	-v &> test-test.out

