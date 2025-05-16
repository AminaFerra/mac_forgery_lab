import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def secure_generate_mac(original):
    return hmac.new(SECRET_KEY, original.encode(), hashlib.md5).hexdigest()

def secure_verify_mac(original, append, mac):
    full_message = (original + append).encode()
    is_valid = (mac == hmac.new(SECRET_KEY, full_message, hashlib.md5).hexdigest())
    verification_text = "✅ MAC verified successfully. Message is authentic." if is_valid else "❌ MAC verification failed (expected in secure mode)."
    return {
        'mode': 'Secure (HMAC)',
        'is_valid': is_valid,
        'combined_message': full_message.decode(errors='ignore'),
        'full_output': f"=== Secure Server Simulation ===\nOriginal message: {original}\nAppended: {append}\nCombined Message: {full_message.decode(errors='ignore')}\nUser-supplied MAC: {mac}\n\n--- Verifying message ---\n{verification_text}"
    }
