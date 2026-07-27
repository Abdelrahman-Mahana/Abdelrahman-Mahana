import os
import urllib.request
import re

print("Downloading scripts from AVIVASHISHTA29...")

files = [
    "scripts/prep_photo.py",
    "scripts/make_ascii_svg.py",
    "scripts/make_info_card.py",
    "scripts/fetch_contributions.py",
    "scripts/render_heatmap_svg.py",
    "scripts/requirements.txt"
]

base_url = "https://raw.githubusercontent.com/AVIVASHISHTA29/AVIVASHISHTA29/main/"
os.makedirs("scripts", exist_ok=True)
os.makedirs(".github/workflows", exist_ok=True)

for file in files:
    url = base_url + file
    filepath = file
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"Downloaded {file}")
    except Exception as e:
        print(f"Failed to download {file}: {e}")

# Customize fetch_contributions.py
try:
    with open("scripts/fetch_contributions.py", "r") as f:
        content = f.read()
    content = content.replace("AVIVASHISHTA29", "Abdelrahman-Mahana")
    with open("scripts/fetch_contributions.py", "w") as f:
        f.write(content)
    print("Customized fetch_contributions.py")
except Exception as e:
    print("Error customizing fetch_contributions.py:", e)

# Customize prep_photo.py to point to correct photo
try:
    with open("scripts/prep_photo.py", "r") as f:
        content = f.read()
    content = content.replace('os.path.join(HERE, "..", "source-photo.jpg")', 'os.path.join(HERE, "..", "assets ", "me last.png")')
    with open("scripts/prep_photo.py", "w") as f:
        f.write(content)
    print("Customized prep_photo.py")
except Exception as e:
    print("Error customizing prep_photo.py:", e)

# Customize make_info_card.py
try:
    with open("scripts/make_info_card.py", "r") as f:
        content = f.read()

    new_rows = """ROWS = [
    ("host",),
    ("kv", "Role", "Data Scientist & AI Builder"),
    ("kv", "Location", "Egypt"),
    ("gap",),
    ("sec", "Connect"),
    ("bul", "Kaggle: kaggle.com/abdelrahmanmahana"),
    ("bul", "Medium: abdelrahmanmahana.medium.com"),
    ("bul", "Email: abdelrahmanmahana01@gmail.com"),
    ("bul", "Dev.to: dev.to/abdelrahmanmahana"),
    ("gap",),
    ("sec", "Stack"),
    ("kv", "AI/ML", "PyTorch, TensorFlow, OpenCV, Scikit-learn"),
    ("kv", "Core", "Python, C++, Java, JS, HTML/CSS"),
    ("kv", "Cloud", "AWS, GCP, Azure, MongoDB, SQL"),
    ("kv", "Other", "Docker, Git, Django, Hadoop, Flutter"),
]"""
    # Use re.sub to replace the ROWS array
    content = re.sub(r"ROWS\s*=\s*\[.*?\]", new_rows, content, flags=re.DOTALL)
    content = content.replace("avi@github", "abdelrahman@github")
    with open("scripts/make_info_card.py", "w") as f:
        f.write(content)
    print("Customized make_info_card.py")
except Exception as e:
    print("Error customizing make_info_card.py:", e)

print("Setup complete! You can now run the generation scripts.")
