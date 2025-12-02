# ping_monitor.py
import subprocess
import logging
import platform  # ✅ ADDED: needed for OS detection

# Set up logging to file
logging.basicConfig(
    filename="ping_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def is_host_alive(ip: str, timeout: int = 2) -> bool:
    """
    Checks if a host is reachable using the system 'ping' command.
    Returns True if host responds within timeout, else False.
    Works on Windows, Linux, and macOS.
    """
    try:
        # Detect OS
        param = "-n" if platform.system().lower() == "windows" else "-c"  # ✅ fixed typo: .lower()
        # On Windows, timeout is in milliseconds; Unix uses seconds
        timeout_arg = str(timeout * 1000) if platform.system().lower() == "windows" else str(timeout)

        ping_cmd = ["ping", param, "1", "-w", timeout_arg, ip]

        result = subprocess.run(
            ping_cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout + 2  # safety margin
        )
        return result.returncode == 0
    except Exception as e:
        logging.error(f"Error pinging {ip}: {e}")
        return False


def monitor_hosts(host_list):
    """Monitor a list of hosts and log status."""
    for host in host_list:
        status = "UP" if is_host_alive(host) else "DOWN"
        message = f"{host} is {status}"
        print(message)
        logging.info(message)


if __name__ == "__main__":
    # Use localhost for reliable testing
    hosts = ["127.0.0.1", "8.8.8.8"]  # 127.0.0.1 should always work
    monitor_hosts(hosts)