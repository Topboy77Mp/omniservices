#!/bin/bash
# Script de vérification post-réorganisation
# Vérifie que shop.html a été correctement mis à jour

echo "=========================================="
echo "  CONTRÔLE DE QUALITÉ - SHOP.HTML"
echo "=========================================="
echo ""

FILE="/home/backbox/Downloads/Electro-Bootstrap-1.0.0/shop.html"

echo "📋 Vérifications en cours..."
echo ""

# Vérifier que le fichier existe
if [ -f "$FILE" ]; then
    echo "✅ Fichier shop.html trouvé"
else
    echo "❌ Fichier shop.html non trouvé"
    exit 1
fi

# Compter les catégories
BEAUTE=$(grep -c "Beauté & Cosmétiques" "$FILE")
PARFUMS=$(grep -c "Parfums & Eaux" "$FILE")
SOINS=$(grep -c "Soins Personnels" "$FILE")
NATURELS=$(grep -c "Produits Naturels & Herbes" "$FILE")
ALIMENTS=$(grep -c "Aliments & Épices" "$FILE")
VETEMENTS=$(grep -c "Vêtements & Mode" "$FILE")
AUTRES=$(grep -c "Autres Produits" "$FILE")

echo ""
echo "📊 Catégories présentes:"
[ $BEAUTE -gt 0 ] && echo "  ✅ Beauté & Cosmétiques" || echo "  ❌ Beauté & Cosmétiques"
[ $PARFUMS -gt 0 ] && echo "  ✅ Parfums & Eaux" || echo "  ❌ Parfums & Eaux"
[ $SOINS -gt 0 ] && echo "  ✅ Soins Personnels" || echo "  ❌ Soins Personnels"
[ $NATURELS -gt 0 ] && echo "  ✅ Produits Naturels & Herbes" || echo "  ❌ Produits Naturels & Herbes"
[ $ALIMENTS -gt 0 ] && echo "  ✅ Aliments & Épices" || echo "  ❌ Aliments & Épices"
[ $VETEMENTS -gt 0 ] && echo "  ✅ Vêtements & Mode" || echo "  ❌ Vêtements & Mode"
[ $AUTRES -gt 0 ] && echo "  ✅ Autres Produits" || echo "  ❌ Autres Produits"

echo ""
echo "🏷️  Icônes Font Awesome:"
grep -q "fas fa-spa" "$FILE" && echo "  ✅ fa-spa (Beauté)" || echo "  ❌ fa-spa"
grep -q "fas fa-wind" "$FILE" && echo "  ✅ fa-wind (Parfums)" || echo "  ❌ fa-wind"
grep -q "fas fa-tint" "$FILE" && echo "  ✅ fa-tint (Soins)" || echo "  ❌ fa-tint"
grep -q "fas fa-leaf" "$FILE" && echo "  ✅ fa-leaf (Naturels)" || echo "  ❌ fa-leaf"
grep -q "fas fa-pepper-hot" "$FILE" && echo "  ✅ fa-pepper-hot (Aliments)" || echo "  ❌ fa-pepper-hot"
grep -q "fas fa-shirt" "$FILE" && echo "  ✅ fa-shirt (Vêtements)" || echo "  ❌ fa-shirt"
grep -q "fas fa-box" "$FILE" && echo "  ✅ fa-box (Autres)" || echo "  ❌ fa-box"

echo ""
echo "🖼️  Images et contenu:"
IMAGES=$(grep -c "photo/" "$FILE")
PRODUCTS=$(grep -c "product-item rounded" "$FILE")
BUTTONS=$(grep -c "Ajouter au Panier" "$FILE")
BADGES=$(grep -c "product-new" "$FILE")

echo "  📸 Références images: $IMAGES"
echo "  🏷️  Conteneurs produits: $PRODUCTS"
echo "  🛒 Boutons panier: $BUTTONS"
echo "  🎖️  Badges produit: $BADGES"

if [ $IMAGES -eq 41 ] && [ $PRODUCTS -eq 41 ] && [ $BUTTONS -eq 41 ] && [ $BADGES -eq 41 ]; then
    echo ""
    echo "✅ Tous les contrôles sont passés!"
else
    echo ""
    echo "⚠️  Certains éléments pourraient être manquants"
fi

echo ""
echo "=========================================="
echo "  ✨ VÉRIFICATION TERMINÉE"
echo "=========================================="
