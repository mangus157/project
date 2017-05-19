import socket
import sys
import struct

class NL:
    def __init__(self, protocol, src_ip, dst_ip, version=4, ip_header_length=5, tos=0, total_length=0,\
                 identification=54321, fragment_offset=0, ttl=255, ip_checksum=0):
        self.version_ip_header_length = (version << 4) + ip_header_length
        self.src_ip = socket.inet_aton(src_ip)
        self.dst_ip = socket.inet_aton(dst_ip)
        self.protocol = self.select_proto(protocol.lower())
        try:
            self.ip_header = struct.pack("!2B3H2BH4s4s", self.version_ip_header_length, tos,
                             total_length, identification, fragment_offset, ttl, protocol,
                             ip_checksum, self.src_ip, self.dst_ip)
        except struct.error, msg:
            print msg
            sys.exit()

    def select_proto(self, protocol):
        if protocol == "tcp":
            return socket.IPPROTO_TCP
        elif protocol == "udp":
            return socket.IPPROTO_UDP
        else:
            print "Not supported protocol.."
            sys.exit()

    def make(self):
        return self.ip_header

    def usage(self):
        pass
if __name__ == "__main__":
    pass
