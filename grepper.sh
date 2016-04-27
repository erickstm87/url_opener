#!/bin/sh

cat output.txt | tr -d '\000' | grep -oh beacon_type=start > beacon_types.txt
cat output.txt | tr -d '\000' | grep -oh beacon_type=complete >> beacon_types.txt
cat output.txt | tr -d '\000' | grep -oh view_percent=[0-9]* >> beacon_types.txt
