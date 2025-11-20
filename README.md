# 🛍️ OMNISERVISE E-Commerce Platform

**Site e-commerce complet avec 41 produits organisés en 7 catégories.**

![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Présentation

OMNISERVISE est une plateforme e-commerce moderne proposant:

- **41 Produits** organisés en **7 catégories**
- 💄 Beauté & Cosmétiques (4 produits)
- 🌬️ Parfums & Eaux (4 produits)
- 💧 Soins Personnels (8 produits)
- 🍃 Produits Naturels & Herbes (6 produits)
- 🌶️ Aliments & Épices (7 produits)
- 👕 Vêtements & Mode (4 produits)
- 📦 Autres Produits (8 produits)

## 🎯 Fonctionnalités

### ✅ Implémentées
- ✓ **Catalogue Produits** - 41 produits avec images, descriptions détaillées et prix
- ✓ **Navigation par Catégories** - Accès rapide aux 7 catégories
- ✓ **Recherche Avancée** - Recherche par nom + filtre par catégorie
- ✓ **Pages Responsives** - Design adapté desktop/mobile
- ✓ **Page Téléchargements** - Télécharger images par catégorie
- ✓ **Localization Française** - 100% en français
- ✓ **Animations** - WOW.js + Animate.css

### 🔄 En Développement
- ⏳ Panier dynamique
- ⏳ Système de commandes
- ⏳ Compte utilisateur

## 📁 Structure du Projet

```
OMNISERVISE/
├── index.html                    # Page d'accueil
├── shop.html                     # Catalogue produits
├── single.html                   # Détail produit
├── cart.html                     # Panier
├── checkout.html                 # Paiement
├── contact.html                  # Contact
├── bestseller.html               # Bestsellers
├── TELECHARGEMENTS_IMAGES.html   # Téléchargements
├── 404.html                      # Page erreur
│
├── css/
│   ├── bootstrap.min.css         # Framework Bootstrap
│   └── style.css                 # Styles personnalisés
│
├── js/
│   ├── main.js                   # Script principal
│   └── search.js                 # Recherche & filtrage
│
├── img/                          # 41 images de produits
│
├── lib/                          # Bibliothèques externes
│   ├── animate/
│   ├── lightbox/
│   ├── owlcarousel/
│   └── wow/
│
├── scss/                         # Fichiers SCSS
│
├── package.json                  # Dépendances Node
├── server.js                     # Serveur Node.js (Render)
├── Procfile                      # Configuration Render
├── render.yaml                   # Configuration déploiement
├── .gitignore                    # Fichiers à ignorer
└── README.md                     # Ce fichier
```

## 🚀 Déploiement

### Sur Render.com

1. **Push sur GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: OMNISERVISE v1.0"
   git branch -M main
   git remote add origin https://github.com/USERNAME/omniservise.git
   git push -u origin main
   ```

2. **Créer service sur Render**
   - Aller à [render.com](https://render.com)
   - Connecter avec GitHub
   - Sélectionner le repository `omniservise`
   - Utiliser la configuration `render.yaml`
   - Service sera automatiquement déployé

3. **Domaine Personnalisé**
   - Ajouter domaine custom: `omniservise.tg`
   - Configurer DNS chez votre registrar

### En Local

```bash
# Installation
npm install

# Démarrage
npm start
# Accès: http://localhost:3000
```

## 🛠️ Technologies

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript (Vanilla)
- **Backend**: Node.js + Express (serveur Render)
- **Animations**: WOW.js, Animate.css
- **Galerie**: Lightbox.js
- **Carousel**: Owl Carousel
- **Icons**: Font Awesome 6.4.0

## 📊 Catégories & Produits

### 💄 Beauté & Cosmétiques (4)
- Fond de Teint Hydratant
- Palette Ombres à Paupières
- Mascara Volume Extrême
- Rouge à Lèvres Longue Tenue

### 🌬️ Parfums & Eaux (4)
- Eau de Parfum Floral
- Eau de Toilette Frais
- Eau de Cologne Boisée
- Eau de Parfum Orientale

### 💧 Soins Personnels (8)
- Savon Surgras Nature
- Gel Douche Relaxant
- Crème Hydratante Visage
- Lotion Corporelle Nourrissante
- Shampooing Réparateur
- Après-Shampooing Démêlant
- Masque Capillaire Profond
- Sérum Visage Antioxydant

### 🍃 Produits Naturels (6)
- Huile Essentielle Eucalyptus
- Mélange Tisanes Digestifs
- Huile de Coco Vierge Bio
- Beurre de Karité Pur
- Thé Vert Antioxydant
- Poudre de Spiruline Bio

### 🌶️ Aliments & Épices (7)
- Miel Pur Africain
- Piment Fort Bio
- Huile d'Arachide Premium
- Riz Blanc Complet
- Sucre de Canne Complet
- Sel Iodé Raffiné
- Farine de Maïs Complète

### 👕 Vêtements & Mode (4)
- Pagne Wax Traditionnel
- Cravate Soie Classique
- Turban Coton Ajustable
- Écharpe Laine Premium

### 📦 Autres Produits (8)
- Bougie Parfumée Naturelle
- Diffuseur Air Ultrasons
- Savon Naturel Charbon
- Miroir Grossissement LED
- Brosse Massante Électrique
- Sac Cosmétiques Voyage
- Peigne Cheveux Démêlant
- Porte-clés Cuir Naturel

## 📱 Pages Disponibles

| Page | Description |
|------|-------------|
| `index.html` | Accueil avec carousel, bestsellers, catégories |
| `shop.html` | Catalogue complet avec recherche & filtres |
| `single.html` | Détail produit avec images gallery |
| `cart.html` | Panier d'achat (en développement) |
| `checkout.html` | Paiement (en développement) |
| `contact.html` | Formulaire contact |
| `bestseller.html` | Produits bestsellers |
| `TELECHARGEMENTS_IMAGES.html` | Télécharger images par catégorie |

## 🔍 Recherche & Filtrage

### Utilisation
1. **Par Texte**: Tapez le nom du produit
2. **Par Catégorie**: Sélectionnez une catégorie
3. **Combiné**: Texte + Catégorie ensemble

### Exemples
- Chercher "Savon" → Affiche tous les savons
- Sélectionner "Beauté" → Affiche beauté uniquement
- "Huile" + "Naturel" → Affiche huiles naturelles

## 📞 Contact

**OMNISERVISE**
- 📧 Email: info@omniservise.tg
- 📞 Tél: +228 XXXX XXXX
- 🌐 Web: https://omniservise.tg

## 📄 License

MIT License - Libre d'utilisation et modification

## 👨‍💻 Développement

```bash
# Mettre à jour les descriptions
python3 update_descriptions.py

# Vérifier la structure
ls -la
```

## 🎉 Prochaines Étapes

- [ ] Panier dynamique avec localStorage
- [ ] Système de commandes
- [ ] Comptes utilisateur
- [ ] Paiement en ligne
- [ ] Admin dashboard
- [ ] Analytics & statistiques

---

**Version**: 1.0  
**Dernière mise à jour**: 20 novembre 2025  
**Statut**: Production Ready ✅
