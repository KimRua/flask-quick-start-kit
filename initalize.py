import os
import sys
import subprocess

def create_virtual_environment():
    """Create a virtual environment for the project."""
    print("Creating virtual environment...")
    try:
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Virtual environment created successfully.")
    except Exception as e:
        print(f"Failed to create virtual environment: {e}")
        sys.exit(1)

def install_requirements():
    """Install required dependencies."""
    print("Installing requirements...")
    try:
        subprocess.check_call([os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "pip"), "install", "-r", "requirement.txt"])
        print("Requirements installed successfully.")
    except Exception as e:
        print(f"Failed to install requirements: {e}")
        sys.exit(1)

def create_project_structure():
    """Create the necessary project structure."""
    print("Setting up project structure...")
    try:
        os.makedirs("app", exist_ok=True)
        with open("run.py", "w") as f:
            f.write("""from app import app\n\nif __name__ == "__main__":\n    app.run(debug=True)\n""")
        with open("app/__init__.py", "w") as f:
            f.write(
                """from flask import Flask\n\napp = Flask(__name__)\n\n# 앱 설정 가져오기\napp.config.from_object('config.Config')\n\n# 라우트 등록\nfrom app import routes\n"""
            )
        with open("app/routes.py", "w") as f:
            f.write(
                """from flask import render_template\nfrom app import app\n\n@app.route("/")\ndef home():\n    return render_template("index.html")\n"""
            )
        with open("config.py", "w") as f:
            f.write(
                """class Config:\n    SECRET_KEY = 'your_secret_key_here'\n    DEBUG = True\n"""
            )
        os.makedirs("app/templates", exist_ok=True)
        with open("app/templates/index.html", "w") as f:
            f.write(
                """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask Quick Start</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
        </head>
        <body>
            <header>
                <h1>Welcome to Flask Quick Start Kit!</h1>
            </header>
            <main>
                <p>This is a simple starter project for Flask.</p>
                <button id="clickMeButton">Click Me</button>
                <p id="message"></p>
            </main>
            <script src="{{ url_for('static', filename='js/script.js') }}"></script>
        </body>
        </html>
        """
            )
        os.makedirs("app/static", exist_ok=True)
        os.makedirs("app/static/css", exist_ok=True)
        os.makedirs("app/static/js", exist_ok=True)
        os.makedirs("app/static/img", exist_ok=True)
        with open("app/static/css/style.css", "w") as f:
            f.write(
                """body {\n    font-family: Arial, sans-serif;\n    margin: 0;\n    padding: 0;\n    background-color: #f8f9fa;\n    color: #333;\n}\n\nheader {\n    background-color: #007bff;\n    color: white;\n    padding: 15px 20px;\n    text-align: center;\n}\n\nmain {\n    padding: 20px;\n}\n\nbutton {\n    background-color: #007bff;\n    color: white;\n    border: none;\n    padding: 10px 20px;\n    font-size: 16px;\n    cursor: pointer;\n}\n\nbutton:hover {\n    background-color: #0056b3;\n}\n\n#message {\n    margin-top: 20px;\n    font-weight: bold;\n    color: #007bff;\n}"""
            )
        with open("app/static/js/script.js", "w") as f:
            f.write(
                """document.getElementById('clickMeButton').addEventListener('click', function() {\n    document.getElementById('message').innerText = 'Button clicked!';\n});"""
            )
        with open("requirement.txt", "w") as f:
            f.write("Flask\n")
        print("Project structure created successfully.")
    except Exception as e:
        print(f"Failed to set up project structure: {e}")
        sys.exit(1)


if __name__ == "__main__":
    print("Initializing Flask Quick Start Kit...")
    create_virtual_environment()
    create_project_structure()
    install_requirements()
    print("Initialization complete. You can now activate the virtual environment and run the project.")
