# MAC Forgery Lab (with hashpumpy)

This Flask-based project demonstrates a length extension attack on insecure MACs generated with MD5(secret || message), and shows how HMAC prevents such attacks.

## Features

- Insecure mode: Uses `hashlib.md5(secret + message)` — vulnerable to length extension.
- Secure mode: Uses `hmac.new(secret, message, hashlib.md5)` — secure against attack.
- Uses `hashpumpy` to forge a valid MAC without knowing the secret.
- Web interface for input/output.

## Installation

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install flask hashpumpy
```

## How to Use

1. Run the app:

```bash
python app.py
```

2. Open [http://localhost:5000](http://localhost:5000)

3. Steps:
   - Generate MAC for a message
   - Use hashpumpy to forge MAC with appended data
   - Try verifying it in both insecure and secure modes



## Note

This version requires the `hashpumpy` Python library for simulating the attack. Insecure MACs are vulnerable to this method, while HMAC-secured ones are not.

## Team Members
- Mayssoune Hussein Elmasry – 2205251
- Maryam Waheed Zamel – 2205154
- Amina Ahmed Ferra – 2205225