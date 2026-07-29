from flask import Flask, render_template_string, request, redirect, url_for, flash
from secure_auth import SecureAuth

app = Flask(__name__)
app.secret_key = 'cloudexify_super_secret_session_key'  
auth_system = SecureAuth()

# Modern Cybersecurity Dashboard UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CloudExify Secure Auth Portal</title>
    <style>
        * { box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #0f172a; color: #f8fafc; margin: 0; padding: 40px 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .container { background: #1e293b; padding: 35px; border-radius: 12px; width: 100%; max-width: 450px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5); border: 1px solid #334155; }
        h2 { color: #38bdf8; text-align: center; margin-bottom: 5px; font-size: 1.6rem; }
        p.subtitle { text-align: center; color: #94a3b8; font-size: 0.85rem; margin-bottom: 25px; }
        .form-group { margin-bottom: 20px; }
        label { font-size: 0.85rem; color: #cbd5e1; display: block; margin-bottom: 6px; font-weight: 600; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border-radius: 6px; border: 1px solid #475569; background: #0f172a; color: #f8fafc; font-size: 0.95rem; outline: none; transition: border-color 0.2s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #38bdf8; }
        button { width: 100%; padding: 12px; border: none; border-radius: 6px; background: #0284c7; color: #ffffff; font-weight: bold; font-size: 1rem; cursor: pointer; transition: background 0.2s; }
        button:hover { background: #0369a1; }
        .btn-secondary { background: #475569; margin-top: 10px; }
        .btn-secondary:hover { background: #334155; }
        hr { border: 0; height: 1px; background: #334155; margin: 25px 0; }
        
        /* Flash Alerts */
        .alert { padding: 12px; border-radius: 6px; font-size: 0.88rem; margin-bottom: 20px; text-align: center; font-weight: 500; }
        .alert-success { background: #064e3b; color: #34d399; border: 1px solid #059669; }
        .alert-error { background: #7f1d1d; color: #fca5a5; border: 1px solid #dc2626; }
        
        .policy-box { background: #0f172a; padding: 10px 14px; border-radius: 6px; border-left: 3px solid #38bdf8; font-size: 0.78rem; color: #94a3b8; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🛡️ Auth Security Portal</h2>
        <p class="subtitle">CloudExify Cybersecurity Internship Month 1</p>

        <!-- Flash Messages Display -->
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        <!-- Registration Form -->
        <form action="/register" method="POST">
            <h3 style="color: #cbd5e1; margin-bottom: 15px; font-size: 1.1rem;">Create Account</h3>
            
            <div class="policy-box">
                Password must contain: 8+ chars, Uppercase, Lowercase, Number, and Special character.
            </div>

            <div class="form-group">
                <label>Username</label>
                <input type="text" name="username" placeholder="e.g. hammad" required autocomplete="off">
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" name="password" placeholder="••••••••••••" required>
            </div>
            <button type="submit">Register User</button>
        </form>

        <hr>

        <!-- Login Form -->
        <form action="/login" method="POST">
            <h3 style="color: #cbd5e1; margin-bottom: 15px; font-size: 1.1rem;">Authenticate</h3>
            <div class="form-group">
                <label>Username</label>
                <input type="text" name="username" placeholder="Enter username" required autocomplete="off">
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" name="password" placeholder="Enter password" required>
            </div>
            <button type="submit" class="btn-secondary">Login</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/register', methods=['POST'])
def register():
    uname = request.form.get('username', '').strip()
    pwd = request.form.get('password', '')

    res = auth_system.register(uname, pwd)
    
    if "successful" in res.lower():
        flash(res, "success")
    else:
        flash(res, "error")
        
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    uname = request.form.get('username', '').strip()
    pwd = request.form.get('password', '')

    res = auth_system.login(uname, pwd)
    
    if "successful" in res.lower():
        flash(res, "success")
    else:
        flash(res, "error")
        
    return redirect(url_for('home'))

if __name__ == '__main__':
    print("[+] Starting Security Portal on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)