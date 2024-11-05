# 4G Router Manager

A Python utility for managing and resetting 4G routers' IP addresses. This tool provides an easy way to monitor, log, and reset your router's IP address through different methods, with multiple practical applications.

## 🌟 Features

- Automatic IP address monitoring
- Multiple IP reset methods:
  - Full router restart
  - 4G connection cycling
- Detailed logging system
- Real-time status updates
- IP change verification
- Error handling and recovery

## 🔧 Technical Details

- **Language**: Python 3.6+
- **Dependencies**: requests
- **Platform**: Cross-platform (Windows, Linux, MacOS)
- **License**: MIT

## 📋 Requirements

- Python 3.6 or higher
- Access to a 4G router's admin interface
- Router credentials (admin username and password)
- Network connectivity

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/vgvr0/4G-Router-Manager.git
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Use Cases and Examples

### 1. IP Rotation and Management
```python
# Basic IP reset
router = Router4GIPReset("192.168.1.1", "admin", "password")
success, result = router.reset_ip_via_connection()

# For API rate limit management
if response.status_code == 429:  # Too many requests
    router.reset_ip_via_connection()
```

### 2. Network Monitoring
```python
# Check connection status
status = router.check_connection_status()
print(f"Current connection status: {status}")

# Monitor current IP
current_ip = router.get_current_ip()
print(f"Current IP: {current_ip}")
```

### 3. Scheduled Resets
```python
import schedule

def daily_reset():
    router = Router4GIPReset("192.168.1.1", "admin", "password")
    router.reset_ip_via_connection()

# Schedule daily reset at 3 AM
schedule.every().day.at("03:00").do(daily_reset)
```

### 4. Automatic Connection Recovery
```python
def auto_recovery():
    router = Router4GIPReset("192.168.1.1", "admin", "password")
    
    if not router.check_connection_status():
        print("Connection lost, attempting recovery...")
        router.reset_ip_via_restart()
```

### 5. Dynamic DNS Integration
```python
def update_dynamic_dns():
    router = Router4GIPReset("192.168.1.1", "admin", "password")
    new_ip = router.get_current_ip()
    update_dns_service(new_ip)
```

### 6. Data Usage Monitoring
```python
def monitor_data_usage():
    router = Router4GIPReset("192.168.1.1", "admin", "password")
    status = router.check_connection_status()
    
    if status.get('data_used') > DATA_LIMIT:
        send_alert("Data limit reached")
```

### 7. Business Continuity
```python
# Automatic backup system
def backup_connection():
    primary_router = Router4GIPReset("192.168.1.1", "admin", "pass1")
    backup_router = Router4GIPReset("192.168.1.2", "admin", "pass2")
    
    if not primary_router.check_connection_status():
        backup_router.reset_ip_via_restart()
```

### 8. Development and Testing
```python
# Testing applications with different IPs
def test_with_different_ips():
    router = Router4GIPReset("192.168.1.1", "admin", "password")
    
    for _ in range(5):
        router.reset_ip_via_connection()
        run_tests()
```

### 9. Monitoring System Integration
```python
from prometheus_client import start_http_server, Gauge

# Monitoring metrics
uptime = Gauge('router_uptime', 'Router uptime in seconds')
signal_strength = Gauge('signal_strength', '4G signal strength')

def collect_metrics():
    router = Router4GIPReset("192.168.1.1", "admin", "password")
    status = router.check_connection_status()
    
    uptime.set(status['uptime'])
    signal_strength.set(status['signal'])
```

### 10. Maintenance Automation
```python
def maintenance_routine():
    router = Router4GIPReset("192.168.1.1", "admin", "password")
    status = router.check_connection_status()
    
    if status.get('issues'):
        router.reset_ip_via_connection()
        if not router.check_connection_status():
            router.reset_ip_via_restart()
```

## ⚠️ Important Considerations

1. Adjust waiting times according to your router model
2. Handle credentials securely
3. Consider your Internet Service Provider's policies
4. Implement robust error handling
5. Respect service platforms' terms of service
6. Monitor data usage and connection limits
7. Test thoroughly in your specific environment

## 🔒 Security Notes

- Store credentials securely
- Use environment variables for sensitive data
- Implement rate limiting for reset attempts
- Monitor and log all operations
- Regular security audits recommended

## 📝 Topics

- Network Management
- Python
- 4G Router
- IP Address Management
- Network Automation
- System Administration
- Network Security
- API Integration
- Business Continuity
- Development Tools

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 📞 Support

If you encounter any issues or have questions:
1. Check the issues section
2. Review the documentation
3. Open a new issue with detailed information
4. Contact the maintainers

## 🎯 Future Developments

- GUI interface
- REST API implementation
- Additional router models support
- Extended monitoring capabilities
- Docker containerization
- Cloud integration features
