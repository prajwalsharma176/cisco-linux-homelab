# Security Policy

## Security Statement

This repository is intended for educational and portfolio purposes.

All sensitive information has been removed or redacted before publication.

Examples include:

* Passwords
* Password hashes
* API tokens
* SSH private keys
* VPN keys
* Authentication secrets
* Personal credentials

Configuration files included in this repository are provided for documentation and learning purposes only.

---

## Credential Handling

This project follows these security practices:

* Passwords are **never hardcoded** in automation scripts.
* Python automation prompts for credentials securely using `getpass()`.
* No credentials are stored in Git.
* Sensitive configuration values are removed before commits.

---

## Responsible Disclosure

If you discover any sensitive information that was accidentally committed to this repository, please do not publicly disclose it.

Instead, open a private GitHub issue or contact the repository owner so the information can be removed promptly.

---

## Security Best Practices

Before publishing any configuration or documentation:

* Remove usernames and password hashes.
* Remove private IP addresses if appropriate.
* Remove public IP addresses.
* Remove API keys and tokens.
* Remove SSH private keys.
* Review all configuration files before committing.

---

## Disclaimer

This repository is a personal Cisco and Linux homelab used for learning networking, Linux system administration, infrastructure automation, and enterprise best practices.

All examples are intended for educational purposes.

