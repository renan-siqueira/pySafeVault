# pySafeVault

**pySafeVault** is a simple, yet powerful Python-based tool designed to securely encrypt folders, files, or data.

Leveraging state-of-the-art cryptographic methods, **pySafeVault** ensures your data remains safe and confidential.

For more details, check [pySafeVault Wiki](https://github.com/renan-siqueira/pySafeVault/wiki).

---

## Table of Contents

- [About](https://github.com/renan-siqueira/pySafeVault/wiki)
- [Installation & Setup](https://github.com/renan-siqueira/pySafeVault/wiki/0.-Installation-&-Setup)
- [Usage Guide](https://github.com/renan-siqueira/pySafeVault/wiki/1.-Usage-Guide)
- [Automated Testing Guide](https://github.com/renan-siqueira/pySafeVault/wiki/2.-Automated-Testing-Guide)
- [Contribution and Community Guidelines](https://github.com/renan-siqueira/pySafeVault/wiki/Contribution-and-Community-Guidelines)
- [License & Copyright](https://github.com/renan-siqueira/pySafeVault/wiki/License-and-Copyright)

---

## Features

- **Advanced Encryption:** Using AES with CBC mode for strong encryption.

- **Secure Key Derivation:** Using PBKDF2 with SHA256.

- **Data Compression:** Built-in zipping functionality before encryption.

---

## Installation & Setup

For detailed instructions on how to clone the repository, set up a virtual environment, and install dependencies, check out our [Installation Guide](https://github.com/renan-siqueira/pySafeVault/wiki/0.-Installation-&-Setup) in the wiki.

### Basic Steps:

1. Clone the repository: `https://github.com/renan-siqueira/pySafeVault.git`

2. Navigate to the project directory: `cd pySafeVault`

3. Create a virtual environment: `python -m venv venv`

4. Activate the virtual environment:

    - On Windows: ``.\venv\Scripts\activate`

    - On macOS and Linux: `source venv/bin/activate`

5. Install the required packages: `pip install -r requirements.txt`

---

## Usage Guide

After setting up, you can run the `main.py` script to start:

```bash
python main.py
```

Follow the on-screen instructions to encrypt or decrypt your desired files.

For detailed usage instructions, see our [Usage Guide](https://github.com/renan-siqueira/pySafeVault/wiki/1.-Usage-Guide) on the wiki.

---

## Tests

We've incorporated unit tests to ensure the integrity and reliability of **pySafeVault**. 

To run the tests:

```bash
pytest
```

More about our testing methodology can be found in our [Automated Testing Guide Wiki Page](https://github.com/renan-siqueira/pySafeVault/wiki/2.-Automated-Testing-Guide).

---

## Contribution & Community

We welcome and appreciate contributions from the community. 

If you're interested in contributing, check our [Contribution and Community Guidelines](https://github.com/renan-siqueira/pySafeVault/wiki/Contribution-and-Community-Guidelines).

---

## License & Copyright

**pySafeVault** is licensed under the **MIT License**. 

Check our [License and Copyright](https://github.com/renan-siqueira/pySafeVault/wiki/License-and-Copyright) Wiki Page for more details.
