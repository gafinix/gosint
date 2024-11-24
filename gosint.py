from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>OSINT Information Gathering Tool</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; margin: 0; padding: 20px; }
        .container { max-width: 700px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px 0px #888888; }
        h1 { color: #333333; }
        .result { margin-top: 20px; padding: 10px; background-color: #e7f3fe; border: 1px solid #b3d8ff; border-radius: 5px; }
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <div class="container">
        <h1>OSINT Information Gathering Tool</h1>
        <form method="POST">
            <label for="query">Enter Mobile Number, Email, or Social Media Username:</label><br><br>
            <input type="text" id="query" name="query" required style="width: 100%; padding: 10px;">
            <br><br>
            <input type="submit" value="Search" style="padding: 10px 20px;">
        </form>
        {% if results %}
            <div class="result">
                <h2>Results:</h2>
                {% for result in results %}
                    <p>{{ result|safe }}</p>
                {% endfor %}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

# Function to simulate phone number analysis
def analyze_phone(phone):
    if re.match(r'^\+?\d{10,15}$', phone):
        return f"<span class='success'>Phone number format is valid.</span>"
    return f"<span class='error'>Invalid phone number format.</span>"

# Function to simulate email analysis
def analyze_email(email):
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return f"<span class='success'>Email format is valid.</span>"
    return f"<span class='error'>Invalid email format.</span>"

# Function to simulate social media analysis
def analyze_social(username):
    if len(username) > 2:
        return f"<span class='success'>Valid username.</span>"
    return f"<span class='error'>Username too short.</span>"

@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    if request.method == "POST":
        query = request.form["query"].strip()
        results = []

        if "@" in query:  # Email input
            results.append(analyze_email(query))
        elif query.startswith("+") or query.isdigit():  # Phone input
            results.append(analyze_phone(query))
        else:  # Assume social media username
            results.append(analyze_social(query))
        
        # Add real OSINT APIs here in the future
        # Example: results.append(external_osint_api(query))

    return render_template_string(HTML_TEMPLATE, results=results)

if __name__ == "__main__":
    app.run(debug=True)
