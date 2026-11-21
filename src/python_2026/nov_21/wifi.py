from dataclasses import dataclass


@dataclass
class WiFiUsage:
    client_name: str
    mac_address: str
    tx_bytes: int # out
    rx_bytes: int # in
    tx_packets: int
    rx_packets: int
    ssid: str



def foo():
    return 10, 20



if __name__ == '__main__':
    gg = foo()
    print(gg[0], gg[1])