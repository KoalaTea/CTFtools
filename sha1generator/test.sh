#!/bin/bash
for i in `seq 1 100`; do
	echo $i >> test.txt
	echo $i | sha1sum >> test.txt
done
