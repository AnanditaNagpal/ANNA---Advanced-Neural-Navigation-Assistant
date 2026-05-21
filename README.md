# 🚀 ANNA – GitHub Deployment Guide (Warp Terminal)

A complete step-by-step guide to push your ANNA project to GitHub using Warp Terminal.

---

## ✅ PRE-REQUISITES CHECKLIST

Before you start, make sure you have:
- [ ] Git installed → check with `git --version`
- [ ] A GitHub account → github.com
- [ ] Warp Terminal installed → warp.dev

---

## STEP 1 — Configure Git (one-time setup)

```bash
git config --global user.name "Anandita Nagpal"
git config --global user.email "your-email@example.com"
```

Verify it saved:
```bash
git config --list
```

---

## STEP 2 — Organize Your Project Folder

Make sure your ANNA project folder looks like this before proceeding:

```
ANNA/
├── anna.py
├── voice_module.py
├── gesture_module.py
├── automation.py
├── requirements.txt     ← create this if missing (see below)
├── assets/              ← put screenshots/diagrams here
└── README.md            ← use the README provided
```

### Generate requirements.txt (if you don't have one)

Navigate to your project folder in Warp, activate your venv, then:

```bash
pip freeze > requirements.txt
```

Or manually create it with your known dependencies:
```bash
cat > requirements.txt << EOF
opencv-python
mediapipe
SpeechRecognition
nltk
pyautogui
PyAudio
EOF
```

---

## STEP 3 — Create a .gitignore File

This prevents junk files from being pushed to GitHub:

```bash
cat > .gitignore << EOF
# Virtual environment — anna_env should NOT be pushed to GitHub
anna_env/
venv/
env/
.venv/

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.env

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# NLTK data
nltk_data/
EOF
```

---

## STEP 4 — Initialize Git in Your Project

Navigate to your ANNA folder in Warp:

```bash
cd /path/to/your/ANNA
```

Initialize Git:
```bash
git init
```

You'll see: `Initialized empty Git repository in .../ANNA/.git/`

---

## STEP 5 — Add the README

Copy the provided README.md into your ANNA folder, then confirm it's there:

```bash
ls -la
```

---

## STEP 6 — Create a New Repo on GitHub

1. Go to **github.com** → click the **"+"** icon → **"New repository"**
2. Fill in:
   - **Repository name:** `ANNA`
   - **Description:** `Multimodal HCI system — voice + gesture computer control using OpenCV, MediaPipe, and NLTK`
   - **Visibility:** Public (recommended for portfolio)
   - ❌ Do NOT check "Add a README" (you already have one)
3. Click **"Create repository"**
4. Copy the repo URL — it looks like:
   `https://github.com/YOUR_USERNAME/ANNA.git`

---

## STEP 7 — Stage All Your Files

Back in Warp, inside your ANNA folder:

```bash
git add .
```

Check what's staged:
```bash
git status
```

You should see all your files listed in green.

---

## STEP 8 — Make Your First Commit

```bash
git commit -m "Initial commit: ANNA - Advanced Neural Navigation Assistant"
```

---

## STEP 9 — Link to GitHub & Push

```bash
git remote add origin https://github.com/YOUR_USERNAME/ANNA.git
git branch -M main
git push -u origin main
```

Warp will prompt for your GitHub credentials. Use:
- **Username:** your GitHub username
- **Password:** your GitHub Personal Access Token (NOT your account password)

> 💡 If you don't have a Personal Access Token:
> GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic) → Generate new token
> Check: `repo` scope → Generate → Copy it

---

## STEP 10 — Verify on GitHub

Open your browser and go to:
```
https://github.com/YOUR_USERNAME/ANNA
```

You should see:
- ✅ All your files listed
- ✅ The README rendered beautifully on the page
- ✅ Badges showing Python version, status, etc.

---

## 🔄 Future Updates (How to Push Changes)

Every time you make changes to your project:

```bash
git add .
git commit -m "describe what you changed"
git push
```

---

## 🏷️ Add a GitHub Topic Tag (Optional but Recommended)

On your GitHub repo page:
- Click the ⚙️ gear icon next to "About"
- Add topics: `python`, `computer-vision`, `hci`, `gesture-recognition`, `voice-recognition`, `mediapipe`, `opencv`, `nlp`, `accessibility`

This makes your repo discoverable on GitHub!

---

## 🌟 Make Your Repo Stand Out

- Add screenshots to your `assets/` folder and reference them in README
- Pin this repo on your GitHub profile
- Add it to your LinkedIn and resume as a project link

---

*Guide created for ANNA – B.Tech Project, Manipal University Jaipur*
