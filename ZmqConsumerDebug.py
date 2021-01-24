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
data_buffer = []
##buffer_no = 0

while True:
    if socket.poll(10) != 0: # check if there is a message on the socket
        msg = socket.recv() # grab the message
        print(len(msg)) # size of msg
        print(msg)
        data = np.frombuffer(msg, dtype=np.ubyte, count=-1) # make sure to use correct data type (complex64 or float32); '-1' means read all data in the buffer
        for i in range (len(data)):
            data_buffer.append(data[i])


        # print(data_buffer)
        # print(buffer_no)
        if (len(data_buffer) < 102):
            pass
        else:
            print(data_buffer)
            ##buffer_no = 0
            print(len(data_buffer))
            
            
            for n in range(len(data_buffer) - 8):
                print(len(data_buffer))
                print(data_buffer)
                print(n)
                print(data_buffer[n : n + 8])
                if data_buffer[n : n + 8] == [1, 0, 1, 0, 1, 0, 1, 0]:
                    if(data_buffer[n + 8 : n + 16] == [1,1,1,1,1,1,1,1]):
                        print("Hi!!")
                        
            data_buffer = []
            

        #     data_buffer = []

        

            
        #print(data[0:8])
        #print(data[2:10])
        #print(data)
        #print([x>>7 for x in data])
        # plt.plot(np.real(data))
        # plt.plot(np.imag(data))
        # plt.show()
        ##print(data_buffer)
    else:
        time.sleep(0.1) # wait 100ms and try again
