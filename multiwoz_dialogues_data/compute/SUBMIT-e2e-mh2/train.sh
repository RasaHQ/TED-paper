#!/usr/bin/env bash

# Set directory to the one this script is in
cd $(dirname $0)

rasa train core \
	--stories data/train \
	--domain domain.yml \
	--config config.yml \
	--augmentation 0 \
	-v &> train.out
