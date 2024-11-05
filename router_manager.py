"""
4G Router Manager
----------------
A Python utility for managing and resetting 4G routers' IP addresses.
Provides methods for IP monitoring, logging, and different reset approaches.

License: MIT
Version: 1.0.0
"""

import requests
from requests.exceptions import RequestException
import time
import logging
from datetime import datetime
from typing import Optional, Tuple, Dict

class Router4GIPReset:
    """
    A class to manage 4G router IP reset operations.
    
    Attributes:
        ip_address (str): Local IP address of the router
        username (str): Router admin username
        password (str): Router admin password
        session (requests.Session): Session object for maintaining connection
        base_url (str): Base URL for router administration
        logger (logging.Logger): Logger instance for operation logging
    """
    
    def __init__(self, ip_address: str, username: str, password: str) -> None:
        """
        Initialize the Router4GIPReset instance.
        
        Args:
            ip_address: Local IP address of the router
            username: Router admin username
            password: Router admin password
        """
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.base_url = f'http://{ip_address}'
        
        # Configure logging
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Configure the logging system."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=f'router_ip_reset_{datetime.now().strftime("%Y%m%d")}.log'
        )
        self.logger = logging.getLogger(__name__)

    def get_current_ip(self) -> Optional[str]:
        """
        Get the current public IP address.
        
        Returns:
            str: Current public IP address or None if retrieval fails
        """
        try:
            response = requests.get('https://api.ipify.org?format=json')
            return response.json()['ip']
        except Exception as e:
            self.logger.error(f"Error getting current IP: {str(e)}")
            return None

    def _login(self) -> bool:
        """
        Attempt to log in to the router.
        
        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            login_url = f'{self.base_url}/login'
            login_data = {
                'username': self.username,
                'password': self.password
            }
            response = self.session.post(login_url, data=login_data)
            response.raise_for_status()
            return True
        except Exception as e:
            self.logger.error(f"Login failed: {str(e)}")
            return False

    def reset_ip_via_restart(self) -> Tuple[bool, Dict[str, str]]:
        """
        Reset IP by restarting the router.
        
        Returns:
            Tuple[bool, Dict[str, str]]: Success status and IP change information
        """
        try:
            old_ip = self.get_current_ip()
            self.logger.info(f"Current IP before reset: {old_ip}")

            if not self._login():
                return False, {"error": "Login failed"}

            # Send restart command
            restart_url = f'{self.base_url}/restart'
            self.session.post(restart_url, data={'action': 'restart'})
            self.logger.info("Restart command sent")
            
            # Wait for router to restart
            print("Waiting for router restart (60 seconds)...")
            time.sleep(60)
            
            # Check new IP
            new_ip = self.get_current_ip()
            self.logger.info(f"New IP after reset: {new_ip}")
            
            return old_ip != new_ip, {
                "old_ip": old_ip,
                "new_ip": new_ip,
                "method": "restart"
            }

        except Exception as e:
            self.logger.error(f"IP reset via restart failed: {str(e)}")
            return False, {"error": str(e)}

    def reset_ip_via_connection(self) -> Tuple[bool, Dict[str, str]]:
        """
        Reset IP by cycling the 4G connection.
        
        Returns:
            Tuple[bool, Dict[str, str]]: Success status and IP change information
        """
        try:
            old_ip = self.get_current_ip()
            self.logger.info(f"Current IP before reset: {old_ip}")
            
            if not self._login():
                return False, {"error": "Login failed"}

            # Disconnect
            disconnect_url = f'{self.base_url}/connection/disconnect'
            self.session.post(disconnect_url)
            self.logger.info("4G connection disconnected")
            time.sleep(5)
            
            # Reconnect
            connect_url = f'{self.base_url}/connection/connect'
            self.session.post(connect_url)
            self.logger.info("4G connection reconnected")
            time.sleep(10)
            
            # Verify IP change
            new_ip = self.get_current_ip()
            self.logger.info(f"New IP after reset: {new_ip}")
            
            return old_ip != new_ip, {
                "old_ip": old_ip,
                "new_ip": new_ip,
                "method": "connection_cycle"
            }

        except Exception as e:
            self.logger.error(f"IP reset via connection cycle failed: {str(e)}")
            return False, {"error": str(e)}

    def check_connection_status(self) -> Dict[str, any]:
        """
        Check the current connection status.
        
        Returns:
            Dict[str, any]: Connection status information
        """
        try:
            if not self._login():
                return {"error": "Login failed"}

            status_url = f'{self.base_url}/status'
            response = self.session.get(status_url)
            return response.json()

        except Exception as e:
            self.logger.error(f"Error checking connection status: {str(e)}")
            return {"error": str(e)}

def main():
    """Main function to demonstrate usage."""
    # Router configuration
    ROUTER_IP = "192.168.1.1"
    USERNAME = "admin"
    PASSWORD = "your_password"
    
    # Initialize router manager
    router = Router4GIPReset(ROUTER_IP, USERNAME, PASSWORD)
    
    # Try connection cycle method first
    print("Attempting IP reset via connection cycling...")
    success, result = router.reset_ip_via_connection()
    
    if not success:
        print("Attempting IP reset via router restart...")
        success, result = router.reset_ip_via_restart()
    
    if success:
        print(f"IP reset successful: {result['old_ip']} -> {result['new_ip']}")
    else:
        print(f"IP reset failed: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
