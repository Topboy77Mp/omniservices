#!/bin/bash

# 🚀 OMNISERVISE - SCRIPT DE DÉPLOIEMENT COMPLET
# Ce script guide pas à pas pour déployer sur GitHub et Render

echo "╔════════════════════════════════════════════════════════════╗"
echo "║   🚀 OMNISERVISE - SCRIPT DE DÉPLOIEMENT COMPLET           ║"
echo "║   E-Commerce 41 produits × 7 catégories                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 1. Vérifier que nous sommes dans le bon dossier
echo -e "${BLUE}📁 Vérification du répertoire...${NC}"
if [ ! -f "index.html" ]; then
  echo -e "${RED}❌ Erreur: index.html non trouvé!${NC}"
  echo "    Assurez-vous d'être dans le dossier OMNISERVISE"
  exit 1
fi
echo -e "${GREEN}✓ Répertoire OK${NC}"
echo ""

# 2. Vérifier Git
echo -e "${BLUE}🔀 Vérification de Git...${NC}"
if ! command -v git &> /dev/null; then
  echo -e "${YELLOW}⚠️  Git n'est pas installé${NC}"
  echo "    Installez Git: sudo apt-get install git"
  exit 1
fi
echo -e "${GREEN}✓ Git trouvé${NC}"
echo ""

# 3. Initialiser Git
echo -e "${BLUE}📝 Étape 1: Initialiser Git localement${NC}"
if [ ! -d ".git" ]; then
  git init
  git config user.name "OMNISERVISE Developer"
  git config user.email "dev@omniservise.tg"
  git add .
  git commit -m "Initial commit: OMNISERVISE v1.0 - 41 produits, 7 catégories"
  echo -e "${GREEN}✓ Repository Git initialisé${NC}"
else
  echo -e "${YELLOW}⚠️  Git est déjà initialisé${NC}"
fi
echo ""

# 4. Afficher les instructions GitHub
echo -e "${BLUE}🐙 Étape 2: Créer repository sur GitHub${NC}"
echo ""
echo "   1. Aller à: https://github.com/new"
echo "   2. Repository name: ${GREEN}omniservise${NC}"
echo "   3. Description: ${GREEN}E-commerce platform - 41 products${NC}"
echo "   4. Visibilité: ${GREEN}Public${NC}"
echo "   5. Cliquer: ${GREEN}Create repository${NC}"
echo ""
echo -e "${YELLOW}⏸️  Appuyez sur ENTRÉE une fois le repo créé...${NC}"
read

# 5. Demander l'URL du repo
echo ""
echo -e "${BLUE}🔗 Étape 3: Connecter vers GitHub${NC}"
echo ""
echo "   Aller à votre repository GitHub et copier l'URL HTTPS"
echo "   Exemple: https://github.com/VOTRE_USERNAME/omniservise.git"
echo ""
read -p "   Entrez l'URL du repository (ou appuyez sur ENTRÉE pour passer): " repo_url

if [ -z "$repo_url" ]; then
  echo ""
  echo -e "${YELLOW}ℹ️  Vous devrez ajouter le remote manuellement:${NC}"
  echo "   ${GREEN}git remote add origin https://github.com/VOTRE_USERNAME/omniservise.git${NC}"
else
  git remote add origin "$repo_url" 2>/dev/null || echo "Le remote existe déjà"
  echo -e "${GREEN}✓ Remote ajouté${NC}"
fi

echo ""
echo -e "${BLUE}📤 Pousser vers GitHub...${NC}"
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
  echo -e "${GREEN}✓ Code poussé sur GitHub!${NC}"
else
  echo -e "${YELLOW}⚠️  Erreur lors du push${NC}"
  echo "   Vérifiez l'URL du repository"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║             ✅ GIT & GITHUB - COMPLÉTÉ!                    ║"
echo "║                                                            ║"
echo "║  Prochaine étape: Déployer sur Render                     ║"
echo "║  1. Aller à: https://render.com                          ║"
echo "║  2. Sign up avec GitHub                                   ║"
echo "║  3. New → Web Service                                     ║"
echo "║  4. Sélectionner repository omniservise                   ║"
echo "║  5. Build: npm install                                    ║"
echo "║  6. Start: npm start                                      ║"
echo "║  7. Cliquer Create & Deploy                               ║"
echo "║                                                            ║"
echo "║  ⏱️  Attendre 2-5 minutes pour le déploiement            ║"
echo "║                                                            ║"
echo "║  📖 Pour plus d'infos: QUICK_START.md                     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Afficher des infos supplémentaires
echo -e "${BLUE}📊 Infos du Projet:${NC}"
echo "   Produits: 41"
echo "   Catégories: 7"
echo "   Pages HTML: 9"
echo "   Images: 102+"
echo "   Taille: ~15 MB"
echo ""

echo -e "${GREEN}🎉 C'est parti!${NC}"
echo ""
