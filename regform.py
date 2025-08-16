from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Create folders
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# base.html
with open("templates/base.html", "w", encoding="utf-8") as f:
    f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Miracle Login</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="bg-image"></div>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
""")

# login.html
with open("templates/login.html", "w", encoding="utf-8") as f:
    f.write("""
{% extends "base.html" %}
{% block content %}
<div class="page-box">
    <div class="left-side">
        <h2>Miracle Software Systems</h2>
        <p>A global systems integrator located in Visakhapatnam, Andhra Pradesh.</p>
        <p>We provide:</p>
        <ul>
            <li>Software Development</li>
            <li>Cyber Security</li>
            <li>Web Development</li>
            <li>Mobile App Development</li>
        </ul>
    </div>
    <div class="right-side">
        <form method="post" action="/login">
            <label>Name</label><input name="name" required>
            <label>Constant</label><input name="constant" required>
            <label>Address</label><input name="address" required>
            <label>Email</label><input name="email" type="email" required>
            <label>Phone</label><input name="phone" required>
            <label>Gender</label><input name="gender" required>
            <label>Date of Birth</label><input name="dob" type="date" required>
            <label>Country</label><input name="country" required>
            <label>State</label><input name="state" required>
            <label>City</label><input name="city" required>
            <label>Pincode</label><input name="pincode" required>
            <label>Qualification</label><input name="qualification" required>
            <label>Occupation</label><input name="occupation" required>
            <label>Experience</label><input name="experience" required>
            <label>Skills</label><input name="skills" required>
            <button type="submit">Submit</button>
        </form>
    </div>
</div>
{% endblock %}
""")

# welcome.html
with open("templates/welcome.html", "w", encoding="utf-8") as f:
    f.write("""
{% extends "base.html" %}
{% block content %}
<div class="page-box">
    <div class="left-side">
        <h2>Login Successful</h2>
        <p>Welcome to Miracle Dashboard.</p>
    </div>
    <div class="right-side">
        <h3>Hello, {{ name }} 👋</h3>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Address:</strong> {{ address }}</p>
        <p><strong>Skills:</strong> {{ skills }}</p>
        <a href="/login">Back to Login</a>
    </div>
</div>
{% endblock %}
""")

# style.css (with background image)
with open("static/style.css", "w", encoding="utf-8") as f:
    f.write("""
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(to right, #f0f2f5, #d9e4f5);
    height: 100vh;
    overflow: hidden;
    position: relative;
}
.bg-image {
    background-image: url('miracle.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.2;
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -1;
}
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.page-box {
    display: flex;
    background: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    max-width: 1000px;
    width: 100%;
}
.left-side {
    flex: 1;
    padding-right: 30px;
    border-right: 1px solid #ccc;
}
.right-side {
    flex: 1;
    padding-left: 30px;
}
form {
    display: flex;
    flex-direction: column;
}
label {
    margin-top: 10px;
    font-weight: bold;
}
input {
    padding: 8px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid #aaa;
}
button {
    margin-top: 10px;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
a {
    display: inline-block;
    margin-top: 20px;
    text-decoration: none;
    color: #007bff;
}
""")

# Routes
@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
async def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def handle_login(
    request: Request,
    name: str = Form(...),
    constant: str = Form(...),
    address: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    gender: str = Form(...),
    dob: str = Form(...),
    country: str = Form(...),
    state: str = Form(...),
    city: str = Form(...),
    pincode: str = Form(...),
    qualification: str = Form(...),
    occupation: str = Form(...),
    experience: str = Form(...),
    skills: str = Form(...)
):
    return templates.TemplateResponse("welcome.html", {
        "request": request,
        "name": name,
        "constant": constant,
        "address": address,
        "email": email,
        "phone": phone,
        "gender": gender,
        "dob": dob,
        "country": country,
        "state": state,
        "city": city,
        "pincode": pincode,
        "qualification": qualification,
        "occupation": occupation,
        "experience": experience,
        "skills": skills,
    })