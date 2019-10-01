#!/usr/bin/env bash

# Set directory to the one this script is in
cd $(dirname $0)

rasa test core \
	--stories data/train \
	--out results/train \
	-v &> test-train.out

