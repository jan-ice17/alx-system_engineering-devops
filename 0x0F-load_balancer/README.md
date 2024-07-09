# ALX System Engineering DevOps

## Project: 0x0F. Load Balancer

### Project Overview

This project aims to improve the web stack by adding redundancy, allowing more traffic management, and increasing infrastructure reliability. It involves setting up a load balancer using HAproxy and configuring multiple web servers to handle HTTP requests.

### Getting Started

To get a copy of this repository and start working on the project, clone the repository using the following command:

```bash
git clone https://github.com/jan-ice17/alx-system_engineering-devops.git
```

### Scripts

- `0-custom_http_response_header`: Configures Nginx on Ubuntu to include a custom HTTP response header.
- `1-install_load_balancer`: Installs and configures HAproxy to distribute traffic using a roundrobin algorithm.
- `2-puppet_custom_http_response_header.pp`: Automates the creation of a custom HTTP response header using Puppet.

### Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted on Ubuntu 16.04 LTS
- All scripts must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any errors
- First line of Bash scripts: `#!/usr/bin/env bash`
- Second line of Bash scripts: Comment explaining the script's functionality

### Usage

1. **Configure Web Servers**:
    - Use the provided Bash scripts to set up Nginx on multiple web servers.
    - Ensure the custom HTTP response header (`X-Served-By`) is correctly configured.

2. **Install and Configure HAproxy**:
    - Run the script to install HAproxy on the load balancer server.
    - Ensure traffic distribution across web servers is set up using the roundrobin algorithm.

3. **Automation with Puppet**:
    - Use the provided Puppet manifest to automate Nginx configuration for HTTP response headers.

### Resources

- [Introduction to Load-Balancing and HAproxy](https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
- [HTTP Header](https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
- [Debian/Ubuntu HAProxy Packages](https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)

### Author

- **Janice Gathoga** (jan-ice17)

Feel free to contribute, raise issues, or contact me for any questions or collaboration opportunities.

---

