#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour mettre à jour la section tab-6 du shop.html
Ajoute les descriptions appropriées selon les catégories
"""

import re

# Mapping des produits par image
PRODUCTS = {
    'product-3.png': {
        'category': 'Parfums',
        'name': 'Eau de Parfum Luxe Premium',
        'original': '45 000 XOF',
        'sale': '35 000 XOF'
    },
    'product-4.png': {
        'category': 'Vêtements',
        'name': 'Chemise Traditionelle Brodée',
        'original': '28 000 XOF',
        'sale': '21 000 XOF'
    },
    'product-5.png': {
        'category': 'Épices',
        'name': 'Épices Mélange Premium',
        'original': '12 000 XOF',
        'sale': '9 000 XOF'
    },
    'product-6.png': {
        'category': 'Légumes Frais',
        'name': 'Mélange Légumes Biologiques',
        'original': '8 000 XOF',
        'sale': '6 000 XOF'
    },
    'product-7.png': {
        'category': 'Savons Naturels',
        'name': 'Savon Bio à l\'Aloe Vera',
        'original': '5 500 XOF',
        'sale': '4 000 XOF'
    },
    'product-8.png': {
        'category': 'Sauces',
        'name': 'Sauce Tomate Artisanale',
        'original': '4 500 XOF',
        'sale': '3 500 XOF'
    },
    'product-9.png': {
        'category': 'Parfums',
        'name': 'Parfum Floral Élégant',
        'original': '42 000 XOF',
        'sale': '32 000 XOF'
    },
    'product-12.png': {
        'category': 'Vêtements',
        'name': 'Robe Pagne Wax Authentique',
        'original': '32 000 XOF',
        'sale': '24 000 XOF'
    },
    'product-13.png': {
        'category': 'Épices',
        'name': 'Poivre & Herbes Aromatiques',
        'original': '10 000 XOF',
        'sale': '7 500 XOF'
    },
    'product-14.png': {
        'category': 'Légumes Frais',
        'name': 'Fruits & Légumes Sélectionnés',
        'original': '15 000 XOF',
        'sale': '11 000 XOF'
    },
    'product-15.png': {
        'category': 'Savons Naturels',
        'name': 'Savon Shea Butter Premium',
        'original': '6 500 XOF',
        'sale': '5 000 XOF'
    },
    'product-16.png': {
        'category': 'Sauces',
        'name': 'Sauce Pimentée Maison',
        'original': '5 000 XOF',
        'sale': '3 800 XOF'
    },
}

def read_file(filepath):
    """Lit le fichier"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Écrit le fichier"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def update_shop_tab6(filepath):
    """Met à jour la section tab-6"""
    
    content = read_file(filepath)
    
    print("=" * 70)
    print("🔄 MISE À JOUR SHOP.HTML - SECTION TAB-6")
    print("=" * 70)
    print()
    
    # Pour chaque produit, remplacer les infos
    count = 0
    for image_file, product_info in PRODUCTS.items():
        image_num = image_file.replace('product-', '').replace('.png', '')
        
        # Pattern pour trouver et remplacer
        pattern = (
            f'<img src="img/{image_file}"[^>]*>\\s*'
            f'<div class="products-mini-icon[^>]*>.*?</div>\\s*'
            f'</div>\\s*'
            f'</div>\\s*'
            f'<div class="col-7">\\s*'
            f'<div class="products-mini-content p-3">\\s*'
            f'<a href="#" class="d-block mb-2">([^<]*)</a>\\s*'
            f'<a href="#" class="d-block h4">([^<]*)</a>\\s*'
            f'<del class="me-2 fs-5">([^<]*)</del>\\s*'
            f'<span class="text-primary fs-5">([^<]*)</span>'
        )
        
        # Nouvelle valeur
        replacement = (
            f'<img src="img/{image_file}" class="img-fluid w-100 h-100" alt="{product_info["name"]}">\n'
            f'                                                    <div class="products-mini-icon rounded-circle bg-primary">\n'
            f'                                                        <a href="#"><i class="fa fa-eye fa-1x text-white"></i></a>\n'
            f'                                                    </div>\n'
            f'                                                </div>\n'
            f'                                            </div>\n'
            f'                                            <div class="col-7">\n'
            f'                                                <div class="products-mini-content p-3">\n'
            f'                                                    <a href="#" class="d-block mb-2">{product_info["category"]}</a>\n'
            f'                                                    <a href="#" class="d-block h4">{product_info["name"]}</a>\n'
            f'                                                    <del class="me-2 fs-5">{product_info["original"]}</del>\n'
            f'                                                    <span class="text-primary fs-5">{product_info["sale"]}</span>'
        )
        
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
            count += 1
            print(f"✓ {image_file}: {product_info['name']}")
            print(f"  Catégorie: {product_info['category']}")
            print(f"  Prix: {product_info['original']} → {product_info['sale']}")
            print()
    
    write_file(filepath, content)
    
    print("=" * 70)
    print(f"✅ {count} produits mis à jour dans tab-6")
    print("=" * 70)
    print()
    print("📊 Résumé des catégories:")
    print("   • Parfums: Eau de Parfum Luxe Premium, Parfum Floral Élégant")
    print("   • Vêtements: Chemise Traditionelle Brodée, Robe Pagne Wax")
    print("   • Épices: Épices Mélange Premium, Poivre & Herbes")
    print("   • Légumes: Mélange Légumes Biologiques, Fruits & Légumes")
    print("   • Savons: Savon Bio à l'Aloe Vera, Savon Shea Butter")
    print("   • Sauces: Sauce Tomate Artisanale, Sauce Pimentée Maison")
    print()

if __name__ == "__main__":
    filepath = '/home/backbox/Downloads/Electro-Bootstrap-1.0.0/shop.html'
    update_shop_tab6(filepath)
