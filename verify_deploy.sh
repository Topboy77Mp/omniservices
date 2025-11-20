#!/bin/bash

echo "═══════════════════════════════════════════════════════════"
echo "     ✅ VÉRIFICATION PRE-DEPLOIEMENT OMNISERVISE"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

errors=0

# 1. Vérifier les fichiers HTML principaux
echo "📄 Vérification des fichiers HTML..."
html_files=("index.html" "shop.html" "single.html" "contact.html" "cart.html" "checkout.html" "bestseller.html" "404.html")
for file in "${html_files[@]}"; do
  if [ -f "$file" ]; then
    echo -e "   ${GREEN}✓${NC} $file"
  else
    echo -e "   ${RED}✗${NC} $file MANQUANT"
    ((errors++))
  fi
done
echo ""

# 2. Vérifier les fichiers de configuration
echo "⚙️  Vérification des fichiers de configuration..."
config_files=("package.json" "server.js" "Procfile" "render.yaml" ".gitignore" "README.md" "DEPLOIEMENT.md" "QUICK_START.md")
for file in "${config_files[@]}"; do
  if [ -f "$file" ]; then
    echo -e "   ${GREEN}✓${NC} $file"
  else
    echo -e "   ${RED}✗${NC} $file MANQUANT"
    ((errors++))
  fi
done
echo ""

# 3. Vérifier les dossiers
echo "📁 Vérification des dossiers..."
folders=("css" "js" "img" "lib" "scss")
for folder in "${folders[@]}"; do
  if [ -d "$folder" ]; then
    file_count=$(find "$folder" -type f | wc -l)
    echo -e "   ${GREEN}✓${NC} $folder/ ($file_count fichiers)"
  else
    echo -e "   ${RED}✗${NC} $folder/ MANQUANT"
    ((errors++))
  fi
done
echo ""

# 4. Vérifier les images de produits
echo "🖼️  Vérification des images de produits..."
product_images=$(find img -name "product-*.png" | wc -l)
echo -e "   ${GREEN}✓${NC} $product_images images de produits trouvées"
if [ $product_images -lt 18 ]; then
  echo -e "   ${YELLOW}⚠️  Attention: au moins 18 images requises${NC}"
fi
echo ""

# 5. Vérifier le contenu de package.json
echo "📦 Vérification de package.json..."
if grep -q '"express"' package.json; then
  echo -e "   ${GREEN}✓${NC} Express configuré"
else
  echo -e "   ${RED}✗${NC} Express manquant dans package.json"
  ((errors++))
fi

if grep -q '"start"' package.json; then
  echo -e "   ${GREEN}✓${NC} Script 'start' configuré"
else
  echo -e "   ${RED}✗${NC} Script 'start' manquant"
  ((errors++))
fi
echo ""

# 6. Vérifier server.js
echo "🖥️  Vérification de server.js..."
if grep -q "express()" server.js; then
  echo -e "   ${GREEN}✓${NC} Express initialisé"
else
  echo -e "   ${RED}✗${NC} Express non initialisé"
  ((errors++))
fi

if grep -q "listen(PORT" server.js; then
  echo -e "   ${GREEN}✓${NC} Serveur écoute sur PORT"
else
  echo -e "   ${RED}✗${NC} Serveur non configuré"
  ((errors++))
fi
echo ""

# 7. Vérifier Git
echo "🔀 Vérification de Git..."
if [ -d ".git" ]; then
  echo -e "   ${GREEN}✓${NC} Repository Git initialisé"
else
  echo -e "   ${YELLOW}⚠️  Repository Git pas encore initialisé${NC}"
  echo -e "      Exécuter: git init"
fi
echo ""

# 8. Vérifier les fichiers de recherche
echo "🔍 Vérification de la recherche..."
if [ -f "js/search.js" ]; then
  echo -e "   ${GREEN}✓${NC} js/search.js existe"
  if grep -q "performSearch" js/search.js; then
    echo -e "   ${GREEN}✓${NC} Fonction performSearch trouvée"
  else
    echo -e "   ${RED}✗${NC} Fonction performSearch manquante"
    ((errors++))
  fi
else
  echo -e "   ${RED}✗${NC} js/search.js manquant"
  ((errors++))
fi
echo ""

# 9. Vérifier .gitignore
echo "🚫 Vérification de .gitignore..."
if [ -f ".gitignore" ]; then
  echo -e "   ${GREEN}✓${NC} .gitignore existe"
  if grep -q "node_modules" .gitignore; then
    echo -e "   ${GREEN}✓${NC} node_modules ignorés"
  else
    echo -e "   ${YELLOW}⚠️  node_modules pas ignorés${NC}"
  fi
else
  echo -e "   ${RED}✗${NC} .gitignore manquant"
  ((errors++))
fi
echo ""

# 10. Résumé
echo "═══════════════════════════════════════════════════════════"
if [ $errors -eq 0 ]; then
  echo -e "   ${GREEN}✅ VÉRIFICATION COMPLÈTE - PRÊT POUR DÉPLOIEMENT!${NC}"
else
  echo -e "   ${RED}⚠️  $errors ERREUR(S) DÉTECTÉE(S)${NC}"
fi
echo "═══════════════════════════════════════════════════════════"
echo ""

# 11. Instructions suivantes
echo "📋 PROCHAINES ÉTAPES:"
echo ""
if [ ! -d ".git" ]; then
  echo "1️⃣  Initialiser Git:"
  echo "   git init"
  echo "   git add ."
  echo "   git commit -m 'Initial commit: OMNISERVISE v1.0'"
  echo ""
fi

echo "2️⃣  Créer repository sur GitHub:"
echo "   https://github.com/new"
echo ""

echo "3️⃣  Connecter et pousser:"
echo "   git branch -M main"
echo "   git remote add origin https://github.com/USERNAME/omniservise.git"
echo "   git push -u origin main"
echo ""

echo "4️⃣  Déployer sur Render:"
echo "   https://render.com → New Web Service → Connect GitHub"
echo ""

echo "✅ Voir QUICK_START.md pour les détails complets"
echo ""
