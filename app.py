from flask import Flask, render_template, request
import client
import server

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    mode = request.args.get('mode', 'insecure')
    step = request.form.get('step') if request.method == 'POST' else None

    if request.method == 'POST':
        original = request.form['original']
        append = request.form.get('append', '')
        mac = request.form.get('mac', '')

        if mode == 'insecure':
            if step == 'generate_mac':
                mac = client.insecure_generate_mac(original)
                result = {
                    'step': 'generate_mac',
                    'original': original,
                    'mac': mac,
                    'mode': mode,
                    'full_output': f"=== Server Simulation ===\nOriginal message: {original}\nMAC: {mac}\nMAC generated successfully."
                }
            elif step == 'forge_mac':
                if not mac:
                    result = {
                        'step': 'forge_mac',
                        'error': 'MAC is required for performing the attack or verification.'
                    }
                else:
                    result = client.insecure_forge_mac(original, append, mac)
                    result['step'] = 'forge_mac'

        else:  # secure mode
            if step == 'generate_mac':
                mac = server.secure_generate_mac(original)
                result = {
                    'step': 'generate_mac',
                    'original': original,
                    'mac': mac,
                    'mode': mode,
                    'full_output': f"=== Server Simulation ===\nOriginal message: {original}\nMAC: {mac}\nMAC generated successfully."
                }
            elif step == 'forge_mac':
                if not mac:
                    result = {
                        'step': 'forge_mac',
                        'error': 'MAC is required for performing the attack or verification.'
                    }
                else:
                    result = server.secure_verify_mac(original, append, mac)
                    result['step'] = 'forge_mac'

    return render_template('index.html', result=result, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
