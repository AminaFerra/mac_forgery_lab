import hashlib
import struct

SECRET_KEY = b'supersecretkey' 

def md5_padding(msg_len):
    padding = b'\x80'
    padding += b'\x00' * ((56 - (msg_len + 1) % 64) % 64)
    padding += struct.pack('<Q', msg_len * 8)
    return padding

def insecure_generate_mac(original):
    return hashlib.md5(SECRET_KEY + original.encode()).hexdigest()

def insecure_forge_mac(original, append, mac):
    full_output = [
        f"=== Client Simulation ===",
        f"Original: {original}",
        f"Intercepted MAC: {mac}",
        f"Data to append: {append}\n"
    ]
    original_bytes = original.encode()
    append_bytes = append.encode()
    success = False

    for key_len in range(8, 33):
        try:
            glue_padding = md5_padding(key_len + len(original_bytes))
            forged_message = original_bytes + glue_padding + append_bytes
            md5_obj = hashlib.md5()
            md5_obj.update(SECRET_KEY + forged_message)
            forged_mac = md5_obj.hexdigest()

            valid_mac = hashlib.md5(SECRET_KEY + forged_message).hexdigest()

            full_output.append(f"Trying key length guess: {key_len}")
            full_output.append(f"  Forged message: {forged_message.decode(errors='ignore')}")
            full_output.append(f"  Forged MAC: {forged_mac}")

            if forged_mac == valid_mac and key_len == len(SECRET_KEY):
                full_output.append("✅ SUCCESSFUL FORGERY (Correct Key Length)")
                return {
                    'mode': 'Insecure (Vulnerable to Forgery)',
                    'key_length': key_len,
                    'forged_mac': forged_mac,
                    'forged_message': forged_message.decode(errors='ignore'),
                    'full_output': "\n".join(full_output)
                }
            else:
                full_output.append("❌ Verification failed.\n")
        except Exception as e:
            full_output.append(f"❌ Error at key length {key_len}: {str(e)}\n")

    full_output.append("❌ Forgery unsuccessful for all key length guesses.")
    return {
        'mode': 'Insecure (Forgery Failed)',
        'full_output': "\n".join(full_output)
    }
