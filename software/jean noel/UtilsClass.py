import os
import sys
import struct

from bluetooth.btcommon import *
import bluetooth._bluetooth as _bt

class Utils():

    def read_local_bdaddr(self):
        hci_sock = _bt.hci_open_dev(0)
        old_filter = hci_sock.getsockopt( _bt.SOL_HCI, _bt.HCI_FILTER, 14)
        flt = _bt.hci_filter_new()
        opcode = _bt.cmd_opcode_pack(_bt.OGF_INFO_PARAM, 
                _bt.OCF_READ_BD_ADDR)
        _bt.hci_filter_set_ptype(flt, _bt.HCI_EVENT_PKT)
        _bt.hci_filter_set_event(flt, _bt.EVT_CMD_COMPLETE);
        _bt.hci_filter_set_opcode(flt, opcode)
        hci_sock.setsockopt( _bt.SOL_HCI, _bt.HCI_FILTER, flt )

        _bt.hci_send_cmd(hci_sock, _bt.OGF_INFO_PARAM, _bt.OCF_READ_BD_ADDR )

        pkt = hci_sock.recv(255)

        status,raw_bdaddr = struct.unpack("xxxxxxB6s", pkt)
        assert status == 0

        t = [ "%X" % ord(b) for b in raw_bdaddr ]
        t.reverse()
        bdaddr = ":".join(t)

        # restore old filter
        hci_sock.setsockopt( _bt.SOL_HCI, _bt.HCI_FILTER, old_filter )
        return [bdaddr]
