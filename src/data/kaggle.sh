#!/bin/bash
pip install kaggle
export KAGGLE_API_TOKEN=KGAT_80aa0efe971ac3dfa1cc4a81bc9c52ed

kaggle datasets download -d leondesilva1/travel-destinations -p /Users/arthopoda/Tourism-project/src/data --unzip -o

rm -f travel-destinations.zip || echo "Zip not found"
