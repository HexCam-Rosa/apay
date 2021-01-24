import numpy as np
from gnuradio import gr

import pmt
import base64


class blk(
    gr.sync_block
):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name="Embedded Python Block",  # will show up in GRC
            in_sig=None,
            out_sig=[np.ubyte],
        )
        self.message_port_register_in(pmt.intern("msg_in"))
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg)

        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        # self.toSend = np.array([], dtype=np.uint8)
        self.toSend = []

    def handle_msg(self, msg):
        # temp = pmt.symbol_to_string(msg)
        # print(temp)
        # out = np.frombuffer(
        #     base64.binascii.a2b_base64(temp.encode("ascii")), dtype=np.ubyte
        # )
        # self.toSend = np.append(self.toSend, out)
        t = pmt.to_python(msg)
        try:
            self.toSend.extend(t)
        except TypeError:
            self.toSend = t

    def work(self, input_items, output_items):
        try:
            toSendSize = len(self.toSend)
        except TypeError:
            toSendSize = 0
        if toSendSize == 0:
            return 0

        for i, byteToSend in enumerate(self.toSend):
            output_items[0][i] = byteToSend
            # for x in range(8):
            #     output_items[0][x + i * 8] = (byteToSend >> x) & 1
            # print(byteToSend)

        self.toSend = []
        return toSendSize
