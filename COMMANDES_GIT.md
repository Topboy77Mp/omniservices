# 💻 COMMANDES GIT EXACTES - Copier/Coller

Voici toutes les commandes à exécuter pour déployer votre site.

---

## 🚀 DEPLOYMENT EN 3 BLOCS (Copier/Coller)

### BLOC 1: Git Local (Exécuter d'abord)
```bash
cd ~/Downloads/Electro-Bootstrap-1.0.0
git init
git config user.name "Votre Nom"
git config user.email "votre@email.com"
git add .
git status
git commit -m "Initial commit: OMNISERVISE v1.0"
```

### BLOC 2: GitHub (Après créer le repo)
```bash
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/omniservise.git
git push -u origin main
```

### BLOC 3: Render (Via interface web)
1. https://render.com
2. New Web Service
3. Connecter omniservise
4. Build: `npm install`
5. Start: `npm start`
6. Create & Deploy

---

## 🔄 MISES À JOUR (Usage quotidien)

### Mettre à jour le site
```bash
# Ajouter les changements
git add .

# Vérifier
git status

# Commit avec description
git commit -m "Description de vos changements"

# Pousser (Render redéploie automatiquement)
git push origin main
```

### Exemples de commits
```bash
git commit -m "Ajouter nouveau produit"
git commit -m "Corriger description beauté"
git commit -m "Mettre à jour prix"
git commit -m "Améliorer moteur de recherche"
```

---

## 🔀 COMMANDES GIT UTILES

### Voir l'état
```bash
git status
git log --oneline
git remote -v
```

### Annuler des changements
```bash
# Annuler un fichier local
git checkout -- nomfichier.html

# Annuler tous les changements
git reset --hard HEAD
```

### Branches
```bash
git branch              # Liste des branches
git branch -M main     # Renommer en main
git checkout -b develop # Créer branche develop
```

### Fusionner (Avancé)
```bash
git merge develop      # Fusionner develop dans main
git rebase develop     # Réécrire historique
```

---

## 📤 GITHUB CLI (Alternative)

Si vous préférez la CLI GitHub:

```bash
# Installer
brew install gh  # macOS
sudo apt install gh  # Linux
choco install gh  # Windows

# Se connecter
gh auth login

# Créer repo directement
gh repo create omniservise --public --source=. --remote=origin --push
```

---

## 🐛 TROUBLESHOOTING COMMANDES

### "fatal: destination path '.git' already exists"
```bash
# Solution: supprimer et réinitialiser
rm -rf .git
git init
git add .
git commit -m "Initial commit"
```

### "fatal: not a git repository"
```bash
# Vous n'êtes pas dans le bon dossier
cd ~/Downloads/Electro-Bootstrap-1.0.0
git init
```

### "error: The following untracked working tree files would be overwritten"
```bash
# Ajouter les fichiers manquants
git add .
git commit -m "Add missing files"
```

### "permission denied (publickey)"
```bash
# Configurer SSH (optionnel)
ssh-keygen -t ed25519 -C "votre@email.com"
cat ~/.ssh/id_ed25519.pub  # Copier et ajouter à GitHub Settings

# Ou utiliser HTTPS (plus simple)
git remote remove origin
git remote add origin https://github.com/USERNAME/omniservise.git
git push -u origin main
```

### "rejected: failed to push some refs"
```bash
# Pull d'abord
git pull origin main

# Puis push
git push origin main
```

---

## 📋 WORKFLOW TYPIQUE JOUR À JOUR

```bash
# Matin: Voir les derniers changements
git log --oneline -5

# Pendant la journée: Travailler normalement
# ... modifier fichiers ...

# Fin de journée: Sauvegarder les changements
git add .
git commit -m "Description du jour"
git push origin main
```

---

## 🎯 COMMANDES ESSENTIELLES (à mémoriser)

| Commande | Effet |
|----------|-------|
| `git add .` | Ajouter tous les fichiers |
| `git commit -m "..."` | Créer un commit |
| `git push origin main` | Envoyer sur GitHub |
| `git pull origin main` | Récupérer depuis GitHub |
| `git status` | Voir l'état |
| `git log` | Voir l'historique |
| `git branch` | Gérer les branches |

---

## 🚀 DÉPLOIEMENT COMPLET EN UNE FOIS

Si vous connaissez votre URL GitHub:

```bash
#!/bin/bash
cd ~/Downloads/Electro-Bootstrap-1.0.0
git init
git config user.name "Developer"
git config user.email "dev@omniservise.tg"
git add .
git commit -m "OMNISERVISE v1.0"
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/omniservise.git
git push -u origin main
echo "✅ Deployment complet!"
```

Sauvegarder dans `deploy_complete.sh` et exécuter:
```bash
bash deploy_complete.sh
```

---

## 📊 COMMANDES PAR SCENARIO

### Scenario 1: Premier déploiement
```bash
git init
git add .
git commit -m "Initial"
git branch -M main
git remote add origin https://github.com/USERNAME/omniservise.git
git push -u origin main
```

### Scenario 2: Mettre à jour le site
```bash
git add .
git commit -m "Description"
git push origin main
```

### Scenario 3: Ajouter un fichier oublié
```bash
git add fichier_oublie.html
git commit -m "Add missing file"
git push origin main
```

### Scenario 4: Corriger le dernier commit
```bash
git add .
git commit --amend -m "Message corrigé"
git push origin main --force
```

### Scenario 5: Revenir en arrière
```bash
git log  # Trouver le commit
git revert abc123  # abc123 = ID du commit
git push origin main
```

---

## 🔐 SÉCURITÉ GIT

### Ne jamais pousser (ajouter à .gitignore)
- `.env` (variables sensibles)
- `node_modules/` (trop gros)
- `.git/` (déjà ignoré)
- Fichiers temporaires

### Vérifier .gitignore
```bash
cat .gitignore
```

### Secrets: Utiliser variables d'environnement
```bash
# Ne pas faire:
PASSWORD="secret123"  # ❌ Visible sur GitHub

# Faire:
export PASSWORD="secret123"  # ✅ Variable locale
```

---

## 📚 RESSOURCES

- [Git Tutorial](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

## ✅ CHECKLIST GITHUB/GIT

- [ ] Git installé: `git --version`
- [ ] Identité configurée: `git config user.name`
- [ ] Repository initialisé: `.git/` existe
- [ ] Fichiers ajoutés: `git status` OK
- [ ] Commit effectué: `git log` affiche le commit
- [ ] Remote configuré: `git remote -v` affiche origin
- [ ] Push réussi: `git push` sans erreur
- [ ] GitHub.com affiche les fichiers

---

**Version**: 1.0  
**Date**: 20 novembre 2025

**Besoin d'aide?** Voir INDEX_DOCUMENTATION.md
