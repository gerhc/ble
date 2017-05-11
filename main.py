#!/usr/bin/env python
# test BLE Scanning software
# koki 15072015

import blescan
import sys
import json

import bluetooth._bluetooth as bluez
from beacon import Beacon

dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print "ble thread started"
except:
    print "error accessing bluetooth device..."
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)


while True:
    returnedList = blescan.parse_events(sock, 10)
    allbs = {}
    for beac in returnedList:
        beacon = Beacon(uuid=beac["uuid"], mac=beac["mac"], major=beac["major"],
            minor=beac["minor"], txpower=beac["txp"], rssi=beac["rssi"])
        allbs[beacon.uuid] = beacon

    print allbs["aeae72f5af6749aeac60f27b5b6fa92f"]
    print allbs["aeae72f5af6749aeac60f27b5b6fa92f"].getDistance()
