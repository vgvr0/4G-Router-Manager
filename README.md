# 4G Router Manager

A Python utility for managing and resetting 4G routers' IP addresses. This tool provides an easy way to monitor, log, and reset your router's IP address through different methods.

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

## 📖 Usage

Basic usage example:
```python
from router_manager import Router4GIPReset

router = Router4GIPReset(
    ip_address="192.168.1.1",
    username="admin",
    password="your_password"
)

# Reset IP using restart method
router.reset_ip_via_restart()

# Or reset IP using connection cycling
router.reset_ip_via_connection()
```

## ⚠️ Important Notes

- Ensure you have proper authorization to manage the router
- Keep your router credentials secure
- Some features might need to be adjusted based on your specific router model
- Network interruption will occur during IP reset

## 📝 Topics

- Network Management
- Python
- 4G Router
- IP Address Management
- Network Automation
- System Administration
- Network Security

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
