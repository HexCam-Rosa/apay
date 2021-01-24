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
for i in range(5):
    #topic = np.random.random_integers(0,1, 100).astype(np.int8)
    topic = np.random.random_integers(-128,127, 100).astype(np.int8)
    #topic = np.random.random_integers(8,8, 100).astype(np.int8)
    print(topic)
    string_rep = base64.binascii.b2a_base64(topic).decode("ascii")
    #string_rep = "Testsentence"
    print(string_rep)
    socket.send(pmt.serialize_str(pmt.to_pmt( string_rep )))
    time.sleep(0.05)
