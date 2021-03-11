#!/bin/bash

fail_count=0
fail_tolerance=2

echo "I'm working..."
while :
do 
	./path_to_virtualenv_directory/bin/python check_notification.py
	((fail_count++))
	echo $"Failure ${fail_count}"
	if ((fail_count > tolerance)); then
		aplay -d 10 song.wav
		break
	fi
	sleep 30s
done
