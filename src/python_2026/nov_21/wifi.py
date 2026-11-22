import json
from dataclasses import dataclass


@dataclass
class WiFiUsage:
    client_name: str
    mac_address: str
    tx_bytes: int  # out
    rx_bytes: int  # in
    tx_packets: int
    rx_packets: int
    ssid: str


def foo():
    # returning two numbers from function
    return 10, 20


def compute_totals(usages: list[WiFiUsage]) -> tuple[int, int]:
    total_tx = sum(u.tx_bytes for u in usages)
    total_rx = sum(u.rx_bytes for u in usages)
    return total_tx, total_rx


def get_largest_uploaders(usages: list[WiFiUsage], n_uploaders: int) -> list[WiFiUsage]:
    sorted_usages = sorted(
        usages,
        key=lambda u: u.tx_bytes,
        reverse=True
    )
    return sorted_usages[:n_uploaders]


def read_wifi_from_json(filename: str) -> list[WiFiUsage]:
    with open(filename, 'r') as file:
        users_data = json.load(file)
        return [WiFiUsage(**user_data) for user_data in users_data]


def display_usages(usages: list[WiFiUsage]):
    for usage in usages:
        print(f"{usage.client_name:20} - {usage.ssid:20}: {usage.tx_bytes//10**6:6} MB out, {usage.rx_bytes//10**6:6} MB in")


if __name__ == '__main__':
    # using 2 outputs
    gg = foo()
    print(gg[0], gg[1])

    wifi_usage = read_wifi_from_json('wifi_usage.json')
    display_usages(get_largest_uploaders(wifi_usage, 5))
