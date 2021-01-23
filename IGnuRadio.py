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

while True:
    topic = np.random.random_integers(-128,127, 10).astype(np.int8)
    print(topic)
    string_rep = base64.binascii.b2a_base64(topic).decode("ascii")
    socket.send(pmt.serialize_str(pmt.to_pmt( string_rep )))
    time.sleep(.5)
