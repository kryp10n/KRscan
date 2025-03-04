# KRscan - Advanced Port Scanner

KRscan is a powerful and efficient command-line port scanner designed for security professionals, network administrators, and penetration testers. It provides advanced scanning features, offering in-depth insights into open ports and running services on target systems.

## Features

- **Fast and Efficient**: Optimized scanning techniques to provide quick results.
- **Customizable Scans**: Supports various scan modes, including SYN scan, UDP scan, and service detection.
- **Banner Grabbing**: Retrieves service banners for better analysis.
- **Interactive CLI**: User-friendly command-line interface with clear output.
- **Multi-threaded**: Enhances performance by scanning multiple ports concurrently.
- **Logging Support**: Saves scan results for later review.

## Installation

Clone the repository and install KRscan using the following commands:

```bash
# Clone the repository
git clone https://github.com/kryp10n/KRscan.git
cd KRscan

# Install dependencies
pip install -r requirements.txt

# Install KRscan as a CLI tool
pip install .
```

## Usage

Once installed, you can run KRscan from anywhere using the command:

```bash
krscan -t <target_ip> -p <ports>
```

### Example Commands

- Scan a single target on common ports:
  ```bash
  krscan -t 192.168.1.1
  ```
- Scan a range of ports:
  ```bash
  krscan -t 192.168.1.1 -p 20-100
  ```
- Perform a UDP scan:
  ```bash
  krscan -t 192.168.1.1 -p 53 -u
  ```

## Roadmap

-

## Disclaimer

KRscan is intended for ethical use only. Unauthorized scanning of systems without explicit permission is illegal and may result in serious consequences.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome! If you'd like to contribute, fork the repository and submit a PR.

## Author

Made by **kryp10n** 🚀

