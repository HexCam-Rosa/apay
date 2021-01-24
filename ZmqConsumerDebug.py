#!/usr/bin/python3
# -*- coding: utf-8 -*-

# zmq_SUB_proc.py
# Author: Marc Lichtman

import zmq
import numpy as np
import time
import matplotlib.pyplot as plt

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:4030") # connect, not bind, the PUB will bind, only 1 can bind
socket.setsockopt(zmq.SUBSCRIBE, b'') # subscribe to topic of all (needed or else it won't work)

buffer = []
preamb = [1,0,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
found = False
message_len = 128
message = []

while True:
    if socket.poll(10) != 0: # check if there is a message on the socket
        msg = socket.recv() # grab the message
        # print(len(msg)) # size of msg
        # print(msg)
        data = np.frombuffer(msg, dtype=np.ubyte, count=-1) # make sure to use correct data type (complex64 or float32); '-1' means read all data in the buffer
        #print(data[0:8])
        #print(data[2:10])
        #print(data)
        #print([x>>7 for x in data])
        # plt.plot(np.real(data))
        # plt.plot(np.imag(data))
        # plt.show()
        # print(data)
        buffer.extend(data)
        if found:
            message.extend(buffer)
            if len(message) >= message_len:
                message = message[:message_len]
                found = False
                print(message)
                message = [] 

        if len(buffer) > 100 and (found is not None):
            for i in range(len(buffer)-len(preamb)):
                for j in range(len(preamb)):
                    if buffer[i+j] != preamb[j]:
                        break
                else:
                    print("Found_prefix")
                    found = True
                    message.extend(buffer[i+j:])
                    buffer = []
                    break

            if len(buffer) > 150:
                buffer = buffer[:100]



    else:
        time.sleep(0.1) # wait 100ms and try again


