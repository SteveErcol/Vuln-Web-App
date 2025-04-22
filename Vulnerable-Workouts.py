from flask import Flask, request, redirect, render_template_string, url_for, session
import webbrowser
import threading
from werkzeug.serving import is_running_from_reloader
import json
import os

app = Flask(__name__)
app.secret_key = 'key'

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
                font-size: 3rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
                text-transform: uppercase;
            }
            .container {
                padding: 40px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <nav>
             <a href="{{ url_for('home') }}">Home</a>
                <a href="{{ url_for('workouts') }}">Workouts</a>
                <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
                <a href="{{ url_for('shop') }}">Shop</a>
                <a href="{{ url_for('about') }}">About Us</a>
                <a href="{{ url_for('cart') }}" title="View Cart">
                    🛒 ({{ session.get('cart')|length if session.get('cart') else 0 }})
                </a>
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
                text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
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
             <a href="{{ url_for('home') }}">Home</a>
                <a href="{{ url_for('workouts') }}">Workouts</a>
                <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
                <a href="{{ url_for('shop') }}">Shop</a>
                <a href="{{ url_for('about') }}">About Us</a>
                <a href="{{ url_for('cart') }}" title="View Cart">
                    🛒 ({{ session.get('cart')|length if session.get('cart') else 0 }})
                </a>
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


# Product catalog
products = {
    1: {"name": "Brotein 5000", "price": "$29.99", "image": "brotein.png", "desc": "You can never have enough protein."},
    2: {"name": "Da Juice", "price": "$24.99", "image": "juice.png", "desc": "Functional heart? Who needs it. We just want gains."},
    3: {"name": "Chalk", "price": "$49.99", "image": "chalk.png", "desc": "Bathe in it if it'll get you muscles."},
    4: {"name": "Tae Bo: Volume 47", "price": "$29.99", "image": "tae.png", "desc": "Billy Blanks hasn't aged a day and will still kick your butt."},
    5: {"name": "Welcome to Biami", "price": "$79.99", "image": "biami.png", "desc": "For a limited time only."},
    6: {"name": "Golden Dumbells", "price": "$499.99", "image": "db.png", "desc": "These are the only things that will outshine your guns."},
    7: {"name": "Travel Mirror", "price": "$139.99", "image": "mirror.png", "desc": "Because you should admire your gains anywhere."},
    8: {"name": "Influencer Starter Kit", "price": "$599.99", "image": "kit.png", "desc": "You won't look ridiculous carrying this around the gym. Trust us."}
}
# Shop Page
@app.route("/shop")
def shop():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gear For Muscles</title>
        <style>
            body { font-family: Arial; 
            margin: 0; 
            background: #f5f5f5; 
            padding: 50px; 
            }
            nav { 
            background: rgba(0,0,0,0.6); 
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
            max-width: 1200px; 
            margin: 40px auto; 
            padding: 0 20px; 
            }
            h1 { 
            font-size: 3rem; 
            text-align: center; 
            margin-bottom: 20px; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
            }
            p { 
            text-align: center; 
            margin-bottom: 40px; 
            }
            .grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 30px; 
            }
            .product-card { 
            background: white; 
            border-radius: 10px; 
            box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
            overflow: hidden; text-align: center; 
            transition: transform 0.3s ease; 
            }
            .product-card:hover { 
            transform: translateY(-5px);
            }
            .product-card img { 
            width: 100%; 
            height: 200px; 
            object-fit: cover; 
            }
            .product-details { 
            padding: 15px; 
            }
            .product-details h3 { 
            margin: 0; 
            font-size: 1.2rem; 
            }
            .price { 
            margin: 10px 0; 
            color: #007BFF; 
            font-weight: bold; 
            }
            .btn { 
            padding: 6px 12px;
            font-size: 0.9rem; 
            background-color: #007BFF; 
            color: white; border: none; 
            border-radius: 5px; 
            cursor: pointer; 
            transition: background 0.3s ease; 
            margin: 5px; 
            }
            .btn:hover { 
            background-color: #0056b3; 
            }
        </style>
    </head>
    <body>
        <nav>
             <a href="{{ url_for('home') }}">Home</a>
                <a href="{{ url_for('workouts') }}">Workouts</a>
                <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
                <a href="{{ url_for('shop') }}">Shop</a>
                <a href="{{ url_for('about') }}">About Us</a>
                <a href="{{ url_for('cart') }}" title="View Cart">
                    🛒 ({{ session.get('cart')|length if session.get('cart') else 0 }})
                </a>
        </nav>

        <div class="container">
            <h1>Gear for Muscles</h1>
            <p>For when pure grit isn't enough.</p>
            <div class="grid">
                {% for id, product in products.items() %}
                <div class="product-card">
                    <img src="{{ url_for('static', filename='shop/' + product.image) }}" alt="{{ product.name }}">
                    <div class="product-details">
                        <h3>{{ product.name }}</h3>
                        <div class="price">{{ product.price }}</div>
                        <a href="{{ url_for('product_detail', product_id=id) }}" class="btn">View Details</a>
                        <a href="{{ url_for('add_to_cart', product_id=id) }}" class="btn">Add to Cart</a>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </body>
    </html>
    ''', products=products)

# Product Detail Page

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = products.get(product_id)
    if not product:
        return "Product not found.", 404
    return render_template_string('''
     <!DOCTYPE html>
    <html>
    <head>
        <title>{{ product.name }}</title>
        <style>
            body { 
            font-family: Arial, sans-serif; 
            text-align: center;
            background-color: #f5f5f5; 
            padding: 50px; margin: 0; 
            }
            nav { background-color: rgba(0,0,0,0.6); 
            padding: 10px; display: flex; 
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
            max-width: 800px; 
            margin: auto; 
            background: white; 
            padding: 30px; 
            border-radius: 10px; 
            box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
            }
            img { 
            width: 100%; 
            max-height: 400px; 
            object-fit: contain; 
            margin-bottom: 20px; 
            }
            h1 { 
            margin-bottom: 10px; 
            }
            .price { 
            font-size: 1.2rem; 
            color: #007BFF; 
            font-weight: bold; 
            margin-bottom: 20px; 
            }
            .btn { 
            padding: 10px 20px; 
            background-color: #007BFF; 
            color: white; border: none; 
            border-radius: 5px; 
            cursor: pointer; 
            text-decoration: none; 
            display: inline-block; 
            }
            .btn:hover { 
            background-color: #0056b3; 
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('home') }}">Home</a>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
        </nav>

        <div class="container">
            <h1>{{ product.name }}</h1>
            <img src="{{ url_for('static', filename='shop/' + product.image) }}" alt="{{ product.name }}">
            <p>{{ product.desc }}</p>
            <div class="price">{{ product.price }}</div>
            <a href="{{ url_for('add_to_cart', product_id=product_id) }}" class="btn">Add to Cart</a>
            <a href="{{ url_for('shop') }}" class="btn" style="background-color: gray;">Back to Shop</a>
        </div>
    </body>
    </html>
    ''', product=product, product_id=product_id)

# Add to Cart Function
@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    if product_id not in products:
        return "Product not found.", 404
    cart = session.get("cart", [])
    cart.append(product_id)
    session["cart"] = cart
    return redirect(url_for("cart"))

# Cart Page
@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    cart_items = [products[int(id)] for id in cart]

    # Price strings to floats
    total = sum(float(item['price'].replace('$', '')) for item in cart_items)

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Your Cart</title>
        <style>
            body { 
            font-family: Arial, sans-serif; 
            background-color: #f5f5f5; 
            margin: 0; 
            padding: 50px; 
            }
            nav { 
            background-color: rgba(0,0,0,0.6); 
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
            max-width: 800px; 
            margin: auto; 
            background: white; 
            padding: 30px; 
            border-radius: 10px; 
            box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
            }
            h1 { 
            margin-bottom: 20px; 
            }
            ul { 
            list-style: none; 
            padding: 0; 
            }
            li { 
            padding: 10px 0; 
            border-bottom: 1px solid #ccc; 
            font-size: 1.1rem; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            }
            .cart-item { 
            display: flex; 
            justify-content: space-between; 
            width: 100%; 
            align-items: center; 
            }
            form { 
            display: inline; 
            }
            .btn { 
            padding: 8px 14px; 
            background-color: #007BFF; 
            color: white; 
            border: none; 
            border-radius: 5px; 
            text-decoration: none; 
            font-size: 0.95rem; 
            cursor: pointer; 
            }
            .btn:hover { 
            background-color: #0056b3; 
            }
            .btn-remove { 
            background-color: red; 
            }
            .btn-remove:hover { 
            background-color: darkred; 
            }
            .total { 
            text-align: right; 
            font-size: 1.2rem; 
            font-weight: bold; 
            margin-top: 20px; 
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('home') }}">Home</a>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
            <a href="{{ url_for('cart') }}" title="View Cart">
                🛒 ({{ session.get('cart')|length if session.get('cart') else 0 }})
            </a>
        </nav>

        <div class="container">
            <h1>Your Cart</h1>
            <ul>
                {% for item in cart_items %}
                <li>
                    <span class="cart-item">
                        {{ item.name }} - {{ item.price }}
                        <form method="POST" action="{{ url_for('remove_from_cart', product_id=loop.index0 + 1) }}">
                            <button type="submit" class="btn btn-remove">X</button>
                        </form>
                    </span>
                </li>
                {% endfor %}
            </ul>

            <div class="total">Total: ${{ "%.2f"|format(total) }}</div>

            <br>
            <a href="{{ url_for('end') }}" class="btn">Checkout</a>
            <a href="{{ url_for('shop') }}" class="btn">Back to Shop</a>
        </div>
    </body>
    </html>
    ''', cart_items=cart_items, total=total)

#Surprise Page (Go back to your lesson)
@app.route("/end")
def end():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>The End</title>
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
            .container {
                padding: 40px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('home') }}">Home</a>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
            <a href="{{ url_for('cart') }}" title="View Cart">
                 🛒 ({{ session.get('cart')|length if session.get('cart') else 0 }})
            </a>
        </nav>
        <div class="container">
            <h1>None of this is real.</h1>
            <p>This is all an illusion. There is no cart. There never was. Go back to where the actual lesson is.</p>
            <img src="{{ url_for('static', filename='shop/magic.gif') }}" alt="Magic" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
        </div>
    </body>
    </html>
    ''')

# Item Removal
@app.route("/remove-from-cart/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", [])
    if product_id in cart:
        cart.remove(product_id)
        session["cart"] = cart
    return redirect(url_for("cart"))

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
            .container {
                padding: 40px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="{{ url_for('home') }}">Home</a>
            <a href="{{ url_for('workouts') }}">Workouts</a>
            <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
            <a href="{{ url_for('shop') }}">Shop</a>
            <a href="{{ url_for('about') }}">About Us</a>
            <a href="{{ url_for('cart') }}" title="View Cart">
                 🛒 ({{ session.get('cart')|length if session.get('cart') else 0 }})
            </a>
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


# Progress Pics
@app.route("/progress-pics", methods=["GET", "POST"])
def progress_pics():
    error = ""
    comments = load_comments()
    verified = False
    images = [img for img in os.listdir(app.config['UPLOAD_FOLDER']) if
              img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    if 'age' in request.form:
        age = request.form.get("age", "")
        if age:
            verified = True


    # Comments
    elif 'comment' in request.form and 'image' in request.form:
        image_name = request.form.get("image")
        comment = request.form.get("comment", "").strip()
        if image_name in images and comment:
            comments.setdefault(image_name, []).append(comment)
            save_comments(comments)
            verified = True  # allow user to stay in after commenting

    # Show Gallery
    if verified or request.method == "POST" and 'comment' in request.form:
        return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Look at Our Muscles</title>
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
                    margin: 0 20px;
                    font-weight: bold;
                    font-size: 1rem;
                }
                nav a:hover {
                    text-decoration: underline;
                }
                header {
                    background-color: transparent;
                    padding: 40px 20px;
                    text-align: center;
                }
                header h1 {
                    margin: 0;
                    font-size: 3rem;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
                }
                header p {
                    color: #ccc;
                    margin-top: 10px;
                }
                .container {
                    max-width: 1200px;
                    margin: 40px auto;
                    padding: 0 20px;
                }
                .gallery {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 30px;
                }
                .photo-card {
                    background: white;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                    overflow: hidden;
                    display: flex;
                    flex-direction: column;
                    transition: transform 0.3s ease;
                }
                .photo-card:hover {
                    transform: translateY(-5px);
                }
                .photo-card img {
                    width: 100%;
                    height: auto;
                    display: block;
                }
                .card-body {
                    padding: 20px;
                    flex: 1;
                }
                form {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }
                input[type="text"] {
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    padding: 10px;
                    background-color: rgba(0, 0, 0, 0.6);
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background 0.3s ease;
                }
                button:hover {
                    background-color: #0056b3;
                }
                .comments {
                    margin-top: 15px;
                }
                .comments p {
                    background-color: transparent;
                    padding: 8px;
                    border-radius: 5px;
                    margin: 5px 0;
                    font-size: 0.95rem;
                    color: #000000;
                }
            </style>
        </head>
        <body>
            <nav>
                <a href="{{ url_for('home') }}">Home</a>
                <a href="{{ url_for('workouts') }}">Workouts</a>
                <a href="{{ url_for('progress_pics') }}">Progress Pics</a>
                <a href="{{ url_for('shop') }}">Shop</a>
                <a href="{{ url_for('about') }}">About Us</a>
                <a href="{{ url_for('cart') }}" title="View Cart">
                    🛒 ({{ session.get('cart')|length if session.get('cart') else 0 }})
                </a>
            </nav>

            <header>
                <h1>Look at Our Muscles</h1>
                <p>Muscles for One. Muscles for All.</p>
            </header>

            <div class="container">
                <div class="gallery">
                    {% for img in images %}
                    <div class="photo-card">
                        <img src="{{ url_for('static', filename='uploads/' + img) }}" alt="Progress Pic">
                        <div class="card-body">
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
                    </div>
                    {% endfor %}
                </div>
            </div>
        </body>
        </html>
        ''', images=images, comments=comments)

    # Age Verification Page
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
        </style>
    </head>
    <body>
        <div class="card">
            <h2>For Legal Purposes</h2>
            <p>Please enter your age</p>
            <form method="POST">
                <input type="text" name="age" placeholder="e.g., 25">
                <button type="submit">Enter</button>
            </form>
        </div>
    </body>
    </html>
    ''', error=error)


# Browser open on launch
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


if __name__ == "__main__":
    if not is_running_from_reloader():
        threading.Timer(1.25, open_browser).start()
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)

