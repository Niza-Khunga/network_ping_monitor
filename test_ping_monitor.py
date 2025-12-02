# test_ping_monitor.py
import pytest
from ping_monitor import is_host_alive

def test_known_good_host():
    """Test that Google DNS (8.8.8.8) is reachable."""
    assert is_host_alive("8.8.8.8") == True

def test_invalid_host():
    """Test that an obviously invalid IP returns False."""
    assert is_host_alive("192.0.2.0") == False  # Reserved for examples