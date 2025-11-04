# 🔄 GitHub Repository - Kompletan Zamjena

**Cilj:** Obriši sve stare fajlove na GitHub-u i zamijeni ih sa novim, čistim verzijama.

---

## ⚠️ VAŽNO

Ovo će **obrisati sve stare fajlove** sa GitHub-a i zamijeniti ih sa novim verzijama.

---

## 🚀 Korak 1: Lokalno Obriši Stare Fajlove

**U PowerShell (u projektu folderu):**

```powershell
# Navigiraj u projekt
cd "C:\Users\41765\Desktop\Boks IT Support\3DS MAX"

# Obriši sve stare dokumentacije
Remove-Item ANLEITUNG.md -ErrorAction SilentlyContinue
Remove-Item BRZI_POCETAK.md -ErrorAction SilentlyContinue
Remove-Item CURSOR_REFACTOR_GUIDE.md -ErrorAction SilentlyContinue
Remove-Item DEPLOYMENT.md -ErrorAction SilentlyContinue
Remove-Item GITHUB_DEPLOYMENT.md -ErrorAction SilentlyContinue
Remove-Item GITHUB_SETUP.md -ErrorAction SilentlyContinue
Remove-Item GITHUB_SETUP_FINAL.md -ErrorAction SilentlyContinue
Remove-Item ONLINE_DEPLOYMENT.md -ErrorAction SilentlyContinue
Remove-Item PROJEKT_BEWERTUNG.md -ErrorAction SilentlyContinue
Remove-Item PROJEKT_STRUKTUR.md -ErrorAction SilentlyContinue
Remove-Item QUICKSTART.txt -ErrorAction SilentlyContinue
Remove-Item README_FINAL.md -ErrorAction SilentlyContinue
Remove-Item STRATESKA_ANALIZA.md -ErrorAction SilentlyContinue
Remove-Item _config.yml -ErrorAction SilentlyContinue
Remove-Item CLEANUP_GITHUB.md -ErrorAction SilentlyContinue
Remove-Item CLEANUP_COMMANDS.md -ErrorAction SilentlyContinue

# Obriši duplicate fajlove (ako postoje u root)
Remove-Item create_interior_scene.py -ErrorAction SilentlyContinue
Remove-Item interior-generator.html -ErrorAction SilentlyContinue
```

---

## 🔧 Korak 2: Git - Obriši Sve i Dodaj Novo

**U PowerShell:**

```powershell
# Dodaj sve promjene (uključujući brisanja)
git add -A

# Provjeri status
git status

# Commit
git commit -m "Complete cleanup: Remove all old files, keep only essential documentation"

# Push na GitHub
git push origin main
```

---

## ✅ Šta će Ostati (Finalna Struktura)

```
interior-scene-automation/
├── README.md                    ✅ Glavna dokumentacija
├── LICENSE                      ✅ MIT License
├── index.html                   ✅ Pink enterprise guide
├── DEPLOYMENT_GUIDE.md          ✅ Deployment
├── TROUBLESHOOTING_GUIDE.md    ✅ Troubleshooting
├── GITHUB_UPLOAD.md            ✅ GitHub guide
├── FULL_REPLACE_GITHUB.md      ✅ (može se obrisati nakon)
├── .gitignore                   ✅ Git ignore
├── src/
│   └── create_interior_scene.py ✅ 4K Script
└── web/
    └── interior-generator.html  ✅ Web tool
```

---

## 🎯 Alternativa: Force Push (Ako ne radi)

**Ako git push ne radi (jer ima konflikata):**

```powershell
# Force push (PREBACUJE sve lokalno na GitHub)
git push -f origin main
```

**⚠️ Oprez:** Force push obriše sve što je na GitHub-u i zamijeni sa lokalnim verzijama.

---

## ✅ Verification

**Nakon push-a:**

1. **Idi na:** https://github.com/ipakja/interior-scene-automation
2. **Provjeri:** Samo essential fajlove vidljive
3. **Provjeri:** Struktura je čista

---

## 📋 Checklista

- [ ] Stare fajlove obrisano lokalno
- [ ] `git add -A` izvršen
- [ ] `git commit` kreiran
- [ ] `git push` uspješan
- [ ] GitHub repository čist
- [ ] Samo essential fajlove vidljivi

---

**Gotovo!** Repository je sada čist i professional. 🎉

