# 📤 GitHub Upload - Kompletan Vodič

**Sauber upload na GitHub u 5 koraka.**

---

## ✅ Pre-requisites

- Git instaliran (provjeri: `git --version`)
- GitHub account kreiran
- Repository kreiran na GitHub.com (ili ćemo ga kreirati)

---

## 🔧 Korak 1: Git Initializirati

**U PowerShell (u projektu folderu):**

```powershell
# Provjeri da si u pravom folderu
cd "C:\Users\41765\Desktop\Boks IT Support\3DS MAX"

# Git initializirati (ako još nije)
git init

# Provjeri status
git status
```

---

## 📁 Korak 2: Repository Kreirati na GitHub

1. **Idi na:** github.com
2. **Klikni:** "+" (gore desno) → "New repository"
3. **Repository Name:** `interior-scene-automation`
4. **Description:** `Automatsko rješenje za fotorealistične 3D vizuelizacije koristeći Open Source softvere (Blender + Python). 4K kvaliteta, enterprise-ready.`
5. **Public** ili **Private** (po tvom izboru)
6. **NE** kreiraj README.md (već imamo)
7. **NE** dodaj .gitignore (već imamo)
8. **Klikni:** "Create repository"

---

## 💻 Korak 3: Sve Dodati i Commit

**U PowerShell:**

```powershell
# Dodaj sve fajlove
git add .

# Provjeri šta će biti upload-ovano
git status

# Kreiraj commit
git commit -m "Initial commit: Interior Scene Automation - 4K Quality, Enterprise-ready"
```

---

## 🌐 Korak 4: Connect sa GitHub

**U PowerShell (zamijeni USERNAME sa svojim GitHub username):**

```powershell
# Dodaj remote repository
git remote add origin https://github.com/USERNAME/interior-scene-automation.git

# Provjeri remote
git remote -v
```

**Ako kaže "remote origin already exists":**
```powershell
git remote remove origin
git remote add origin https://github.com/USERNAME/interior-scene-automation.git
```

---

## 🚀 Korak 5: Upload

**U PowerShell:**

```powershell
# Branch imenovati
git branch -M main

# Upload
git push -u origin main
```

**Ako traži username/password:**
- **Username:** Tvoj GitHub username
- **Password:** Personal Access Token (NE koristi GitHub password)

**Kako kreirati Personal Access Token:**
1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. Naziv: `Interior Scene Upload`
5. Scopes: ✅ `repo` (sve podrepo)
6. Generate token
7. **KOPIRAJ TOKEN** (nećeš ga više vidjeti!)
8. Koristi token kao password

---

## ✅ Verification

**Nakon upload-a:**

1. **Idi na:** `https://github.com/USERNAME/interior-scene-automation`
2. **Provjeri:** Sve fajlove su tamo
3. **Provjeri strukturu:**
   ```
   ✅ README.md
   ✅ LICENSE
   ✅ index.html
   ✅ src/create_interior_scene.py
   ✅ web/interior-generator.html
   ✅ docs/
   ✅ .gitignore
   ```

---

## 📝 GitHub Pages Aktivirati (Opciono)

**Ako želiš da web tool bude online:**

1. **Repository** → **Settings**
2. **Pages** (lijevo sidebar)
3. **Source:** `main` branch
4. **Folder:** `/` (root)
5. **Save**

**Čekaj 2-3 minuta** → Website će biti live na:
`https://USERNAME.github.io/interior-scene-automation/`

---

## 🔧 Troubleshooting

### "Authentication failed"
→ Kreiraj Personal Access Token (korak 5 gore)

### "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/USERNAME/interior-scene-automation.git
```

### "Git nije prepoznat"
→ Download Git: git-scm.com/download/win

### "Fatal: not a git repository"
→ `git init` prvo (korak 1)

---

## 📋 Finalni Checklist

- [ ] Git instaliran
- [ ] Repository kreiran na GitHub.com
- [ ] `git init` izvršen
- [ ] `git add .` izvršen
- [ ] `git commit` kreiran
- [ ] `git remote add origin` izvršen
- [ ] `git push` uspješan
- [ ] Sve fajlove vidljivo na GitHub
- [ ] GitHub Pages aktiviran (opciono)

---

## 🎯 Šta će biti Upload-ovano

```
interior-scene-automation/
├── README.md (Bosanski, 4K dokumentacija)
├── LICENSE (MIT)
├── index.html (Pink enterprise guide - Bosanski)
├── DEPLOYMENT_GUIDE.md
├── TROUBLESHOOTING_GUIDE.md
├── GITHUB_UPLOAD.md (ova datoteka)
├── .gitignore
├── src/
│   └── create_interior_scene.py (4K, Blender 4.x compatible)
├── web/
│   └── interior-generator.html
└── docs/
    └── README.md
```

---

**Gotovo!** Projekt je sada na GitHub-u. 🎉

