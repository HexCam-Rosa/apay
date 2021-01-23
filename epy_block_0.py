import numpy as np
from gnuradio import gr

import pmt
import base64

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=None,
            out_sig=[np.byte]
        )
        self.message_port_register_in(pmt.intern('msg_in'))
        self.set_msg_handler(pmt.intern('msg_in'), self.handle_msg)
        
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.toSend = np.array([], dtype=np.uint8)
        self.sendIdx = 0
        
    def handle_msg(self, msg):
        temp = pmt.symbol_to_string(msg)
        out = np.frombuffer(base64.binascii.a2b_base64(temp.encode("ascii")), dtype=np.int8)
        self.toSend = np.append(self.toSend, out)

    def work(self, input_items, output_items):
        toSendSize = self.toSend.size
        if toSendSize == 0:
            output_items[0][0] = 80
            return 0
        
        print("sending stuff now")
        output_items[0][0] = self.toSend[sendIdx]
        if sendIdx == toSendSize:
            sendIdx = 0
            self.toSend = np.array([], dtype=np.int8)
        else:
            sendIdx += 1

        return 1
