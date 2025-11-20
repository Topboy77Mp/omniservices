# 📚 GUIDE DE DÉPLOIEMENT - OMNISERVISE

## ✅ Étape 1: Préparer le Repository Local

### 1.1 Initialiser Git
```bash
cd ~/Downloads/Electro-Bootstrap-1.0.0
git init
git config user.name "Votre Nom"
git config user.email "votre@email.com"
```

### 1.2 Ajouter les fichiers
```bash
git add .
git status  # Vérifier que les fichiers sont listés
```

### 1.3 Commit initial
```bash
git commit -m "Initial commit: OMNISERVISE v1.0 - 41 produits, 7 catégories"
```

---

## 📤 Étape 2: Créer le Repository sur GitHub

### 2.1 Créer un compte GitHub
- Aller à https://github.com
- S'inscrire ou se connecter
- Vérifier l'email

### 2.2 Créer un nouveau repository
1. Cliquer sur `+` (haut droit) → `New repository`
2. Nom: `omniservise`
3. Description: `E-commerce platform - OMNISERVISE`
4. Visibilité: Public
5. **NE PAS** initialiser avec README/gitignore (.gitignore existe déjà)
6. Cliquer `Create repository`

### 2.3 Connecter le repo local à GitHub
```bash
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/omniservise.git
git push -u origin main
```

### 2.4 Vérifier sur GitHub
- Aller à https://github.com/VOTRE_USERNAME/omniservise
- Les fichiers doivent être visibles

---

## 🚀 Étape 3: Déployer sur Render.com

### 3.1 Créer un compte Render
- Aller à https://render.com
- S'inscrire avec GitHub
- Autoriser l'accès aux repositories

### 3.2 Créer un nouveau service
1. Dashboard → `New +` → `Web Service`
2. Connecter GitHub si demandé
3. Sélectionner repository `omniservise`
4. Configurer:
   - **Name**: `omniservise`
   - **Environment**: Node
   - **Build Command**: `npm install`
   - **Start Command**: `npm start`
   - **Plan**: Free (ou Pro selon les besoins)

### 3.3 Variables d'environnement (Optionnel)
- Ajouter si nécessaire pour production:
  ```
  NODE_ENV = production
  PORT = 3000
  ```

### 3.4 Déployer
1. Cliquer `Create Web Service`
2. Render va:
   - Cloner le repository
   - Installer les dépendances (`npm install`)
   - Lancer le serveur (`npm start`)
3. Attendre 2-5 minutes pour le déploiement

### 3.5 Accéder au site
- URL fournie par Render: `https://omniservise-xxxx.onrender.com`
- Copier l'URL et la tester

---

## 🌐 Étape 4: Ajouter Domaine Personnalisé (Optionnel)

### 4.1 Sur Render
1. Service → `Settings` → `Custom Domain`
2. Entrer: `omniservise.tg`
3. Cliquer `Add Custom Domain`
4. Copier les valeurs DNS

### 4.2 Chez le Registrar (GoDaddy, Namecheap, etc.)
1. Accéder à la gestion DNS de `omniservise.tg`
2. Ajouter les enregistrements DNS fournis par Render
3. Attendre la propagation (15 min - 48h)

### 4.3 Vérifier
- Accéder à `https://omniservise.tg`
- Le site doit charger via Render

---

## 🔄 Étape 5: Workflow de Mise à Jour

### Après chaque modification locale:

```bash
# 1. Vérifier les changements
git status

# 2. Ajouter les fichiers modifiés
git add .

# 3. Créer un commit
git commit -m "Description des changements"

# 4. Pousser vers GitHub
git push origin main
```

**Render se mettra à jour automatiquement** (redéploiement en 1-2 min)

---

## 📊 Structure des Fichiers Importants

```
omniservise/
├── .gitignore              # Fichiers ignorés par Git
├── package.json            # Dépendances Node.js
├── server.js               # Serveur Express
├── Procfile                # Configuration Render
├── render.yaml             # Configuration alternative Render
├── README.md               # Documentation principale
├── DEPLOIEMENT.md          # Ce fichier
│
├── index.html              # Page d'accueil
├── shop.html               # Catalogue produits
├── js/search.js            # Recherche & filtrage
└── ... (autres pages HTML)
```

---

## ✅ Checklist Avant Déploiement

- [ ] Git initialisé: `git init`
- [ ] Fichiers ajoutés: `git add .`
- [ ] Commit effectué: `git commit -m "..."`
- [ ] Repository créé sur GitHub
- [ ] Connexion établie: `git remote add origin ...`
- [ ] Push effectué: `git push -u origin main`
- [ ] Service créé sur Render
- [ ] Déploiement réussi (pas d'erreurs)
- [ ] Site accessible via URL Render
- [ ] Toutes les pages chargent correctement
- [ ] Images visibles
- [ ] Recherche/filtrage fonctionne
- [ ] Responsive design OK (mobile/desktop)

---

## 🐛 Dépannage

### Site ne charge pas
```bash
# 1. Vérifier les logs Render
Render Dashboard → Service → Logs

# 2. Vérifier la syntaxe server.js
node server.js

# 3. Vérifier package.json
cat package.json
```

### Images ne s'affichent pas
- Vérifier les chemins: `/img/product-X.png`
- Les images doivent être dans `/img/`
- Commit les images: `git add img/`

### Recherche ne fonctionne pas
- Vérifier `js/search.js` existe
- Vérifier qu'il est chargé dans HTML: `<script src="js/search.js"></script>`
- Vérifier la console du navigateur (F12 → Console)

### Erreur "Cannot GET /"
- Vérifier que `server.js` est correct
- Vérifier que `index.html` existe à la racine
- Redémarrer le service Render

---

## 🎯 Prochaines Étapes

1. **Panier Dynamique**
   - Sauvegarder panier dans localStorage
   - Afficher nombre d'articles

2. **Paiement**
   - Intégrer Stripe ou PayPal
   - Gérer les commandes

3. **Compte Utilisateur**
   - Inscription/Connexion
   - Historique commandes

4. **Admin Dashboard**
   - Modifier produits
   - Voir les commandes
   - Gérer les stocks

---

## 📞 Support

Pour plus d'info:
- Render Docs: https://render.com/docs
- GitHub Docs: https://docs.github.com
- Express.js: https://expressjs.com

**Version**: 1.0  
**Date**: 20 novembre 2025  
**Statut**: Ready for Production ✅
