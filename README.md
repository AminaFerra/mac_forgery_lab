# MAC Forgery Lab – Length Extension Attack Demonstration & Mitigation

This project demonstrates the security weakness in using naive hash-based MACs (e.g., MAC = hash(secret || message)) and how a length extension attack can be used to forge valid MACs without knowing the secret key. It also shows how to secure the system using HMAC.

## What Is This All About?

A MAC (Message Authentication Code) is used to ensure that a message has not been tampered with and comes from a trusted sender. It's like a digital signature. However, if the MAC is implemented like this:

    MAC = hash(secret || message)

...then it becomes vulnerable to a **Length Extension Attack**. This is a cryptographic flaw where an attacker, who sees a message and its MAC, can add more data to the message and generate a valid MAC for the new message — without knowing the secret.

In this project, you simulate that attack, then fix it using a proper cryptographic method called **HMAC**.

## Features

- Generate MACs using:
  - Insecure MD5(secret || message)
  - Secure HMAC(secret, message)
- Simulate a length extension attack
- Verify success of forgery in insecure mode
- Show that the same attack fails against HMAC
- Simple web interface using Flask

## Project Structure

```
mac_forgery_lab/
├── app.py        # Flask app  
├── server.py     # logic for secure mode
├── client.py     # logic for insecure mode
├── templates/
│   └── index.html      # Frontend HTML page
└── README.md           # Project documentation
```

## How It Works

### Insecure Mode – Attack Simulation

1. **Generate MAC**
   - The user inputs a message.
   - MAC is generated as `MD5(secret || message)`.

2. **Forge MAC**
   - The user supplies:
     - Original message
     - Original MAC
     - Data to append
   - The app:
     - Guesses key lengths
     - Applies MD5 padding manually
     - Constructs forged message and MAC
     - Compares against expected values using the secret key

3. **Verify**
   - If the guessed key length is correct, the forged MAC is accepted.

### Secure Mode – HMAC Mitigation

1. **Generate MAC**
   - The user inputs a message.
   - MAC is generated using `HMAC(secret, message)` with MD5.

2. **Attempted Forgery**
   - The same input as above will fail to validate.
   - HMAC prevents length extension due to its two-pass hashing and key structure.

## Installation

### Using a Virtual Environment (Recommended)

#### 1. Create the environment

```bash
python -m venv venv
```

#### 2. Activate the environment

- **On Windows:**
```bash
venv\Scripts\activate
```

- **On macOS/Linux:**
```bash
source venv/bin/activate
```

#### 3. Install requirements

```bash
pip install flask hashlib hmac struct
```

### Run the Lab

```bash
python app.py
```

Open your browser and go to:  
http://localhost:5000

## Explanation of Code and Sequence

### app.py

- Handles routes for GET and POST.
- `/` route has two modes:
  - **Insecure:** uses MD5(secret || message)
  - **Secure:** uses HMAC(secret, message)
- The logic under `generate_mac` creates a MAC.
- The logic under `forge_mac` tries to forge a new message+MAC.

### index.html

- A styled web interface to:
  - Enter original message, MAC, and appended data
  - Generate MACs
  - Try forging or verifying forged MACs
- Display output in a console-style format.

## Modes of Operation

### Insecure Mode

- Uses MAC = MD5(secret || message)
- Vulnerable to length extension attacks

### Secure Mode

- Uses HMAC with MD5
- Not vulnerable to length extension attacks

## Team Members

- Mayssoune Hussein Elmasry - 2205251
- Maryam Waheed Zamel - 2205154
- Amina Ahmed Ferra - 2205225

## References

- HMAC RFC 2104 – https://datatracker.ietf.org/doc/html/rfc2104