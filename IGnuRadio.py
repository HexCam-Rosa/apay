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

#while True:
for i in range(100):
    #topic = np.random.random_integers(0,1, 100).astype(np.int8)
    #topic = np.random.random_integers(-128,127, 100).astype(np.int8)
    #topic = np.random.random_integers(5,5, 100).astype(np.int8)
    #topic = np.random.random_integers(127,127, 100).astype(np.ubyte)
    #print(topic)
    #string_rep = base64.binascii.b2a_base64(topic).decode("ascii")
    #string_rep = "Testsentence"
    #print(string_rep)
    #byte_data = np.array([127,5,0,8]).astype(np.ubyte)
    # a = [170,170,170,255,0,255,0,]
    # a = np.random.choice([0, 1], 100)
    # a = np.ones(100)
    a = np.array([1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    #a = [3,1,0,2,3,2,1]
    socket.send(pmt.serialize_str(pmt.to_pmt(a)))
    #print(pmt.to_pmt(a))
    #time.sleep(0.5)
    print(a)
    time.sleep(0.05)
