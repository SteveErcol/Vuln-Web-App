
Esteban's Gym For Muscles – Educational Web App

Esteban's Gym for Muscles is a fitness-themed Flask web application designed to teach developers and learners how to identify, exploit, and patch common web application vulnerabilities.

This app contains both vulnerable and secure versions, making it perfect for secure coding workshops or classroom demos.

-------------------------------------------------------------------------------

What is included in app:

- Home Page
	- Navigation bar with links to all major sections
	- Dynamic cart icon with item count

- Workouts Page
	- Interactive dropdowns for major muscle groups

- Progress Pics Page
	- Age verification required
		- Vulnerable version available to demonstrate input validation issues
	- Preloaded image gallery
	- Comments for each image (stored in comments.json)

- Shop Page
	- 8 themed fitness products with names, prices, and images
	- "Add to Cart" and "View Details" buttons
	- Product detail pop-out pages with full descriptions
	- Fully functioning cart with checkout option

- About Page
	- A little information about the gym for the ambiance

-------------------------------------------------------------------------------

Educational Purpose

- This application is designed for:
	- Secure coding education
- Web vulnerability walkthroughs

- Educators and learners can modify the app to:
	- Inject vulnerabilities (e.g., reflected/stored XSS, IDOR, insecure redirects)
	- Implement fixes and explain secure alternatives
	- Observe how persistent storage (like JSON files) can be manipulated

-------------------------------------------------------------------------------

Project Structure

project/
├── Workouts.py             # Main Flask application - Patched for Insufficient Input Validation
├── Vulnerable-Workouts.py  # Main Flask application - Unpatched for Insufficient Input Validation
├── comments.json           # Stores Progress Pic comments
├── static/
│   ├── uploads/            # Progress pics shown in gallery
│   └── shop/               # Product images for Shop and Cart section
├── README.md               # You are here.

-------------------------------------------------------------------------------

Setup & Usage

1. Clone or Copy Project
   git clone https://github.com/your-username/gym-for-muscles.git
   cd gym-for-muscles

2. Install Dependencies
   pip install flask werkzeug

3. Add Required Directories & Files
   mkdir -p static/uploads static/shop
   Place your product images in static/shop/ (e.g., brotein.png, juice.png, etc.)
   Place any test gallery images in static/uploads/
   Create an empty comments.json if missing:
   {}

4. Run the App
   python vulnerable-workouts.py
   Your browser will open automatically to http://127.0.0.1:5000

-------------------------------------------------------------------------------

Vulnerability Integration (For Instructors)

- You can adapt the project to teach:
	- XSS Attacks (via comments form on Progress Pics)
	- Insufficient Input Validation (already included)
	- Session-based state attacks
	- Unvalidated redirects or IDOR (if extended)


-------------------------------------------------------------------------------

Customization Tips

- Modify product catalog in products = { ... }
- Replace background GIF with another animated source
- Add form validation or Flask-WTF integration
- Add a database to replace JSON storage (e.g., SQLite)

-------------------------------------------------------------------------------

License

This project is for educational purposes only. Feel free to remix, modify, or fork it for your own lessons!

-------------------------------------------------------------------------------

Final Thoughts

I really hope you enjoy exploring Esteban's Gym! Let me know your thoughts.

Now go forth, code secure apps, and never skip leg day. 💪


