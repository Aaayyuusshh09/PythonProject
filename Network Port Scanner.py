"""
Cybersecurity Project: Network Port Scanner
Covers: socket module, loops, input, functions, error handling
"""

import socket

def scan_port(ip, port):
    """Try connecting to a port on the target IP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # short timeout for speed
        result = sock.connect_ex((ip, port))  # returns 0 if connection successful
        sock.close()
        return result == 0
    except socket.error:
        return False


def port_scanner():
    """Main port scanning function"""
    target = input("Enter target IP address or hostname: ")
    try:
        target_ip = socket.gethostbyname(target)  # convert to IP
    except socket.gaierror:
        print("❌ Invalid hostname.")
        return

    print(f"\n🔍 Scanning target: {target} ({target_ip})")

    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print("\n--- Scan Results ---")
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"✅ Port {port} is OPEN")
        else:
            print(f"❌ Port {port} is CLOSED")


# ---- Run Program ----
if __name__ == "__main__":
    port_scanner()
