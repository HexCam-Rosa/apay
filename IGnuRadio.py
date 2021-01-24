import zmq
import random
import sys
import time
import numpy as np
import pmt
import base64

port = 4020

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:%s" % port)

a = [170,170,170,255,0,255,0,]
while True:
    # socket.send(pmt.serialize_str(pmt.to_pmt(a[i])))
    # socket.send(pmt.serialize_str(pmt.to_pmt(170)))
    socket.send(pmt.serialize_str(pmt.to_pmt(a)))
    # socket.send(bytes(pmt.to_pmt(170)))
    #print(pmt.to_pmt(a))
    time.sleep(0.5)
