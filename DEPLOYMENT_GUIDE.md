# 🚀 Deployment Guide

**Enterprise-ready deployment instructions for GitHub and production.**

---

## 📋 Prerequisites

- Git installed
- GitHub account
- Repository created on GitHub.com

---

## 🔧 Step 1: Initialize Git Repository

```bash
# In project directory
git init
git add .
git commit -m "Initial commit: Interior Scene Automation"
git branch -M main
```

---

## 🌐 Step 2: Connect to GitHub

```bash
# Replace USERNAME with your GitHub username
git remote add origin https://github.com/USERNAME/interior-scene-automation.git
git push -u origin main
```

**If authentication fails:**
- Create Personal Access Token: GitHub → Settings → Developer settings → Personal access tokens → Generate new token
- Use token as password

---

## 📄 Step 3: Enable GitHub Pages

1. Go to repository → **Settings**
2. Click **Pages** (left sidebar)
3. **Source:** Select `main` branch
4. **Folder:** `/` (root) or `/web`
5. **Save**

**Wait 2-3 minutes** → Site will be live at:
`https://USERNAME.github.io/interior-scene-automation/`

---

## ✅ Verification

- [ ] Repository created
- [ ] Code pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Site accessible via URL
- [ ] All links working

---

## 📧 Next Steps

Send the GitHub Pages URL to end users.

**Production URL Format:**
```
https://USERNAME.github.io/interior-scene-automation/
```

---

**Status:** ✅ Enterprise-ready deployment completed

