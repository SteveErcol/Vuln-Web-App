from flask import Flask, request, redirect, render_template_string, url_for
import webbrowser
import threading
from werkzeug.serving import is_running_from_reloader
import json
import os

app = Flask(__name__)

COMMENTS_FILE = 'comments.json'
app.config['UPLOAD_FOLDER'] = 'static/uploads'


def load_comments():
    if not os.path.exists(COMMENTS_FILE):
        return {}
    with open(COMMENTS_FILE, 'r') as f:
        return json.load(f)


def save_comments(comments):
    with open(COMMENTS_FILE, 'w') as f:
        json.dump(comments, f)


# Home Page
@app.route("/")
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gym For Muscles</title>
        <style>
            html, body {
                margin: 0;
                padding: 0;
                height: 100%;
                font-family: Arial, sans-serif;
                background: url('https://lh5.googleusercontent.com/vWSLmMtz8k_Jh7mWE-G3IgiKZjJ8YFp8FTen2K9HhESMbLvwURmNIDed7HI7t-ZLg_QljnPedplWOzYtLAB7qJKlNeLHzMI2v04YBLwih-rf_50SpAnchUhqX1YG7HjeEx9UGi6f-_GqefQDsQjYGDcBXaT0WXJJ') no-repeat center center fixed;
                background-size: cover;
                overflow: hidden;
            }
            nav {
                background-color: #232526;
                padding: 10px;
                display: flex;
                justify-content: center;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                font-weight: bold;
            }
            nav a:hover {
                text-decoration: underline;
            }
            .container {
                padding: 40px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
        </nav>
        <div class="container">
            <h1><i>Welcome to Esteban's Gym For Muscles!</i></h1>
            <p>Choose a section from above to start getting <i><strong>buff</strong></i>.</p>
        </div>
    </body>
    </html>
    ''')


# Workouts Page
@app.route("/workouts")
def workouts():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Workouts for Muscles</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #232526, #414345);
                color: white;
                text-align: center;
                padding: 50px;
            }
            nav {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 10px;
                display: flex;
                justify-content: center;
                margin-bottom: 30px;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                font-weight: bold;
            }
            nav a:hover {
                text-decoration: underline;
            }

            h1 {
                font-size: 3em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 40px;
                color: #ccc;
            }
            .workout-section {
                max-width: 600px;
                margin: 0 auto 20px;
                text-align: left;
            }
            .fancy-button {
                width: 100%;
                background: linear-gradient(to right, #ff416c, #ff4b2b);
                border: none;
                border-radius: 10px;
                padding: 15px 20px;
                color: white;
                font-size: 1.1em;
                font-weight: bold;
                cursor: pointer;
                transition: background 0.3s ease;
                text-align: left;
                box-shadow: 0 4px 10px rgba(255, 75, 43, 0.2);
            }
            .fancy-button:hover {
                background: linear-gradient(to right, #ff4b2b, #ff416c);
            }
            .dropdown-content {
                display: none;
                padding: 15px;
                margin-top: 5px;
                background-color: rgba(255, 255, 255, 0.05);
                border-left: 3px solid #ff4b2b;
                border-radius: 5px;
            }
        </style>
        <script>
            function toggleDropdown(id) {
                var content = document.getElementById(id);
                content.style.display = content.style.display === "block" ? "none" : "block";
            }
        </script>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
        </nav>

        <h1>Workouts for Muscles</h1>
        <p>What muscle is getting big today?</p>

        <div class="workout-section">
            <button class="fancy-button" onclick="toggleDropdown('arms')">Arms</button>
            <div class="dropdown-content" id="arms">
                <h3>Curls</h3>
                2 sets of 500 reps
                <h3>Tricep Extensions</h3>
                2 sets of 500 reps
                <h3><strong>Repeat Until Your Muscles Are Big</strong></h3>
            </div>
        </div>

        <div class="workout-section">
            <button class="fancy-button" onclick="toggleDropdown('pecs')">Pecs</button>
            <div class="dropdown-content" id="pecs">
                <h3>Bench Press</h3>
                2 sets of 500 reps
                <h3>Chest Flys</h3>
                2 sets of 500 reps
                <h3><strong>Repeat Until Your Muscles Are Big</strong></h3>
            </div>
        </div>

        <div class="workout-section">
            <button class="fancy-button" onclick="toggleDropdown('back')">Back</button>
            <div class="dropdown-content" id="back">
                <h3>Rows</h3>
                2 sets of 500 reps
                <h3>Pull Ups</h3>
                2 sets of 500 reps
                <h3><strong>Repeat Until Your Muscles Are Big</strong></h3>
            </div>
        </div>

        <div class="workout-section">
            <button class="fancy-button" onclick="toggleDropdown('quads')">Quads</button>
            <div class="dropdown-content" id="quads">
                <h3>Squats</h3>
                ∞ Sets of ∞ Reps 
                <h3><strong>Never Stop Squatting</strong></h3>
            </div>
        </div>

        <div class="workout-section">
            <button class="fancy-button" onclick="toggleDropdown('hammies')">Hammies</button>
            <div class="dropdown-content" id="hammies">
                <h3>Romanian Deadlifts</h3>
                2 sets of 500 reps
                <h3>Leg Curls</h3>
                2 sets of 500 reps
                <h3><strong>Repeat Until Your Muscles Are Big</strong></h3>
            </div>
        </div>    

        <div class="workout-section">
            <button class="fancy-button" onclick="toggleDropdown('glutes')">Glutes</button>
            <div class="dropdown-content" id="glutes">
                <h3>Hip Thrusts</h3>
                2 sets of 500 reps
                <h3>Kickbacks</h3>
                2 sets of 500 reps
                <h3><strong>Repeat Until Your Muscles Are Big</strong></h3>
            </div>
        </div>  

        <div class="workout-section">
            <button class="fancy-button" onclick="toggleDropdown('abs')">Washboard Abs</button>
            <div class="dropdown-content" id="abs">
                <h3>Sit Ups</h3>
                ∞ Sets of ∞ Reps 
                <h3>Crunches</h3>
                ∞ Sets of ∞ Reps 
                <h3>Leg Raises</h3>
                ∞ Sets of ∞ Reps 
                <h3>Back Extensions</h3>
                ∞ Sets of ∞ Reps 
                <h3><strong>Abs All Day, Every Day</strong></h3>
            </div>    
        </div>
    </body>
    </html>
    ''')


# Shop Page
@app.route("/shop")
def shop():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gear for Muscles</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: #f5f5f5;
            }
            nav {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 10px;
                display: flex;
                justify-content: center;
                margin-bottom: 30px;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                font-weight: bold;
            }
            nav a:hover {
                text-decoration: underline;
            }
            .container {
                padding: 40px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
        </nav>
        <div class="container">
            <h1>Gear for Muscles</h1>
            <p>Spend Money. Get Big Muscles.</p>
        </div>
    </body>
    </html>
    ''')


# About Us Page
@app.route("/about")
def about():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Us and Our Muscles</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: #f5f5f5;
            }
            nav {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 10px;
                display: flex;
                justify-content: center;
                margin-bottom: 30px;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                font-weight: bold;
            }
            nav a:hover {
                text-decoration: underline;
            }
            .container {
                padding: 40px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
        </nav>
        <div class="container">
            <h1>🏋️‍♂️ About Us – Esteban’s Gym for Muscles 💥</h1>
            <p>Welcome to <strong>Esteban’s Gym for Muscles</strong> – where gains are forged, weakness is banished, and mirrors tremble under the weight of sheer flex.</p>

            <p>Founded by <em>Esteban (aka "The Bicep Whisperer")</em>, our gym was built on one bold belief:</p>
            <blockquote>
                <p><em>“If it doesn't hurt, it needs more reps.”</em></p>
            </blockquote>

            <p>At Esteban’s, we don’t just lift weights – we <strong>intimidate them</strong>. Whether you’re a first-time lifter or Arnold himself, we’ve got everything you need to sculpt guns that are illegal in 48 states (besides Texas and Alaska).</p>

            <h2>💪 What Makes Us Special?</h2>
            <ul style="text-align: left; display: inline-block;">
                <li><strong>Protein Shakes so Powerful</strong>, you need a prescription.</li>
                <li><strong>Our Own Muscle Soundtrack</strong>, accented by power grunts and clanking iron.</li>
                <li><strong>A Signature Scent</strong>: 30% iron, 70% ambition.</li>
                <li><strong>Staffed by Experts</strong> who once curled a full-sized fridge “just to see if they could.”</li>
            </ul>

            <p>Our motto?</p>
            <blockquote>
                <p><em>“If you’re not sore, you’re just visiting.”</em></p>
            </blockquote>

            <p>So come on down. Bring your muscles. Or borrow some from a friend.  
            At <strong>Esteban’s Gym for Muscles</strong>, <em>we don’t count reps – we make reps count.</em></p>
        </div>
    </body>
    </html>
    ''')


# Progress Pics – Age Verification Required
@app.route("/progress-pics", methods=["GET", "POST"])
def progress_pics():
    error = ""
    comments = load_comments()
    verified = False
    images = [img for img in os.listdir(app.config['UPLOAD_FOLDER']) if
              img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Step 1: Age Verification
    if 'age' in request.form:
        age = request.form.get("age", "").strip()
        if not age.isdigit():
            error = "Please enter a valid number."
        elif int(age) < 18:
            error = "You must be at least 18 years old to access progress pics."
        else:
            verified = True

    # Step 2: Posting a comment
    elif 'comment' in request.form and 'image' in request.form:
        image_name = request.form.get("image")
        comment = request.form.get("comment", "").strip()
        if image_name in images and comment:
            comments.setdefault(image_name, []).append(comment)
            save_comments(comments)
            verified = True  # allow user to stay in after commenting

    # If verified, show the gallery
    if verified or request.method == "POST" and 'comment' in request.form:
        return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Progress Pics</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 30px; }
                .gallery { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }
                .photo-card {
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    padding: 15px;
                    width: 300px;
                    text-align: center;
                }
                img { width: 100%; border-radius: 10px; }
                form { margin-top: 10px; }
                input[type="text"] {
                    width: 100%;
                    padding: 8px;
                    margin-top: 5px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    margin-top: 5px;
                    padding: 8px 12px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .comments { text-align: left; margin-top: 10px; }
                .comments p { background: #eee; padding: 5px; border-radius: 4px; margin: 3px 0; }
            </style>
        </head>
        <body>
            <h1>Progress Pics</h1>
            <p>Leave your thoughts on our progress!</p>
            <div class="gallery">
                {% for img in images %}
                <div class="photo-card">
                    <img src="{{ url_for('static', filename='uploads/' + img) }}" alt="Progress Pic">
                    <form method="POST">
                        <input type="hidden" name="image" value="{{ img }}">
                        <input type="text" name="comment" placeholder="Leave a comment..." required>
                        <button type="submit">Post</button>
                    </form>
                    <div class="comments">
                        {% for comment in comments.get(img, []) %}
                            <p>{{ comment }}</p>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
        </body>
        </html>
        ''', images=images, comments=comments)

    # Default: Show age verification
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Age Verification</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f5f5f5;
                margin: 0;
            }
            .card {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 300px;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                padding: 10px 20px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            .error {
                color: red;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Age Verification</h2>
            <p>Please enter your age to view progress pics:</p>
            <form method="POST">
                <input type="text" name="age" placeholder="e.g., 25">
                <button type="submit">Enter</button>
            </form>
            <div class="error">{{ error }}</div>
        </div>
    </body>
    </html>
    ''', error=error)


# Launch in browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


if __name__ == "__main__":
    if not is_running_from_reloader():
        threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
