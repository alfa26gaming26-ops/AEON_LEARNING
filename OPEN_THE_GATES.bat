@echo off
title THE SANCTUARY IGNITION
start python HEARTBEAT.py
timeout /t 2
start python Sanctuary_Master_v5.5.py
timeout /t 2
start python THE_MEADOW.py