#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour mettre à jour les descriptions des produits OMNISERVISE
Remplace les descriptions Apple iPhone par des vraies descriptions adaptées
"""

import re

# Dictionnaire complet des descriptions par catégorie
DESCRIPTIONS = {
    # Beauté & Cosmétiques (4 produits)
    "product-1": {
        "name": "Fond de Teint Hydratant",
        "description": "Fond de teint riche en minéraux naturels avec SPF 20. Couvre les imperfections tout en hydratant la peau. Texture veloutée, longue tenue jusqu'à 12h.",
        "price": "2,500 FCFA"
    },
    "product-2": {
        "name": "Palette Ombres à Paupières",
        "description": "12 teintes sélectionnées pour tous les types de peau. Formule satinée et shimmer combinées. Parfait pour créer des looks de jour et de soirée.",
        "price": "1,800 FCFA"
    },
    "product-3": {
        "name": "Mascara Volume Extrême",
        "description": "Mascara haute définition avec brosse novatrice. Offre un volume spectaculaire sans effet pâteux. Résiste à l'eau, tient 24h.",
        "price": "1,600 FCFA"
    },
    "product-4": {
        "name": "Rouge à Lèvres Longue Tenue",
        "description": "Formule révolutionnaire non-asséchante. 20 teintes disponibles du nude au bordeaux. Tenue jusqu'à 10h sans retouche.",
        "price": "1,400 FCFA"
    },
    
    # Parfums & Eaux (4 produits)
    "product-5": {
        "name": "Eau de Parfum Floral",
        "description": "Senteur délicate à base de fleurs blanches et d'ambre. Longueur en bouche 6-8h. Inspiré des jardins de Grasse.",
        "price": "3,200 FCFA"
    },
    "product-6": {
        "name": "Eau de Toilette Frais",
        "description": "Parfum frais et léger avec notes d'agrumes. Parfait pour l'été et le quotidien. Tenue 4-5h.",
        "price": "2,100 FCFA"
    },
    "product-7": {
        "name": "Eau de Cologne Boisée",
        "description": "Fragrance boisée sophistiquée avec cèdre et vétiver. Idéale pour les hommes modernes. Tenue 4-6h.",
        "price": "2,300 FCFA"
    },
    "product-8": {
        "name": "Eau de Parfum Orientale",
        "description": "Senteur riche aux notes épicées et orientales. Boisée avec ambre et musc blanc. Tenue exceptionnelle 8-10h.",
        "price": "3,500 FCFA"
    },
    
    # Soins Personnels (8 produits)
    "product-9": {
        "name": "Savon Surgras Nature",
        "description": "Savon artisanal surgras enrichi au beurre de karité. Nettoie en douceur, respecte l'épiderme. Parfumé naturellement.",
        "price": "900 FCFA"
    },
    "product-10": {
        "name": "Gel Douche Relaxant",
        "description": "Gel douche doux à base d'huiles essentielles. Forme une mousse généreuse et rafraîchissante. 500ml.",
        "price": "1,200 FCFA"
    },
    "product-11": {
        "name": "Crème Hydratante Visage",
        "description": "Crème riche au beurre de cacao et noix de coco. Hydrate 24h, apaise les rougeurs. Texture légère.",
        "price": "1,800 FCFA"
    },
    "product-12": {
        "name": "Lotion Corporelle Nourrissante",
        "description": "Lotion légère au lait d'amande. Hydrate et nourrit la peau sans résidu gras. Absorbe rapidement.",
        "price": "1,500 FCFA"
    },
    "product-13": {
        "name": "Shampooing Réparateur",
        "description": "Shampooing doux spécialisé pour cheveux fragilisés. Contient huile d'argan et protéines. Restaure la brillance.",
        "price": "1,600 FCFA"
    },
    "product-14": {
        "name": "Après-Shampooing Démêlant",
        "description": "Après-shampooing riche à base de miel et noix de coco. Démêle les cheveux sans casser. 250ml.",
        "price": "1,400 FCFA"
    },
    "product-15": {
        "name": "Masque Capillaire Profond",
        "description": "Masque réparateur intensif au beurre de karité. Traitement hebdomadaire revitalisé. 200ml.",
        "price": "1,900 FCFA"
    },
    "product-16": {
        "name": "Sérumvisage Antioxydant",
        "description": "Sérum concentré à la vitamine C et acide hyaluronique. Éclat immédiat, rides minimisées.",
        "price": "2,200 FCFA"
    },
    
    # Produits Naturels & Herbes (6 produits)
    "product-17": {
        "name": "Huile Essentielle Eucalyptus",
        "description": "Huile essentielle pure et naturelle. Propriétés respiratoires. À diffuser ou diluer. 10ml.",
        "price": "1,500 FCFA"
    },
    "product-18": {
        "name": "Mélange Tisanes Digestifs",
        "description": "Mélange de 5 herbes pour faciliter la digestion. Gingembre, fenouil, menthe. 50g.",
        "price": "800 FCFA"
    },
    "product-19": {
        "name": "Huile de Coco Vierge Bio",
        "description": "Huile de coco première pression à froid. 100% pur et naturel. Multiusage peau/cheveux. 500ml.",
        "price": "2,500 FCFA"
    },
    "product-20": {
        "name": "Beurre de Karité Pur",
        "description": "Beurre de karité non-raffiné provenance Burkina Faso. Nourrissant et réparateur. 100g.",
        "price": "2,000 FCFA"
    },
    "product-21": {
        "name": "Thé Vert Antioxydant",
        "description": "Thé vert premium de la région montagneuse. Riche en polyphénols. 50g (25 sachets).",
        "price": "1,800 FCFA"
    },
    "product-22": {
        "name": "Poudre de Spiruline Bio",
        "description": "Spiruline pure à 100%. Complément alimentaire riche en protéines. 100g.",
        "price": "3,200 FCFA"
    },
    
    # Aliments & Épices (7 produits)
    "product-23": {
        "name": "Miel Pur Africain",
        "description": "Miel récolté à la main, non-chauffé et non-filtré. Riche en enzymes naturelles. 500g.",
        "price": "2,800 FCFA"
    },
    "product-24": {
        "name": "Piment Fort Bio",
        "description": "Piment séché biologique broyé finement. Saveur intense et naturelle. 100g.",
        "price": "650 FCFA"
    },
    "product-25": {
        "name": "Huile d'Arachide Premium",
        "description": "Huile d'arachide première pression. Saveur riche pour cuisiner. 1L.",
        "price": "1,900 FCFA"
    },
    "product-26": {
        "name": "Riz Blanc Complet",
        "description": "Riz blanc long grain de qualité supérieure. Cuit en 20 min. 2kg.",
        "price": "2,200 FCFA"
    },
    "product-27": {
        "name": "Sucre de Canne Complet",
        "description": "Sucre de canne non-raffiné riche en minéraux. Sucre complet authentique. 500g.",
        "price": "850 FCFA"
    },
    "product-28": {
        "name": "Sel Iodé Raffiné",
        "description": "Sel de cuisine iodé pour prévention carence. Granulométrie uniforme. 500g.",
        "price": "400 FCFA"
    },
    "product-29": {
        "name": "Farine de Maïs Complète",
        "description": "Farine de maïs moulue finement à la pierre. Idéale pâtisserie/cuisine. 1kg.",
        "price": "900 FCFA"
    },
    
    # Vêtements & Mode (4 produits)
    "product-30": {
        "name": "Pagne Wax Traditionnel",
        "description": "Pagne wax 100% coton motifs traditionnels. 2m. Teintes assortis à la demande.",
        "price": "3,500 FCFA"
    },
    "product-31": {
        "name": "Cravate Soie Classique",
        "description": "Cravate 100% soie tissée. Nœud facile, entretien simple. Couleurs variées.",
        "price": "2,000 FCFA"
    },
    "product-32": {
        "name": "Turban Coton Ajustable",
        "description": "Turban femme coton bio ajustable. Protège cheveux naturels. Motifs géométriques.",
        "price": "1,500 FCFA"
    },
    "product-33": {
        "name": "Écharpe Laine Premium",
        "description": "Écharpe 100% laine mérinos fine. Chaude et légère. Teintes naturelles.",
        "price": "4,200 FCFA"
    },
    
    # Autres Produits (8 produits)
    "product-34": {
        "name": "Bougie Parfumée Naturelle",
        "description": "Bougie à la cire de soja, senteur lavande. Durée 30h. Contenant réutilisable.",
        "price": "1,800 FCFA"
    },
    "product-35": {
        "name": "Diffuseur Air Ultrasons",
        "description": "Diffuseur ultrasonique brume fraîche. Silencieux, LEDs colorées. 200ml.",
        "price": "2,500 FCFA"
    },
    "product-36": {
        "name": "Savon Naturel Charbon Actif",
        "description": "Savon noir au charbon actif purifiant. Nettoie en profondeur. Artisanal.",
        "price": "1,100 FCFA"
    },
    "product-37": {
        "name": "Miroir Grossissement LED",
        "description": "Miroir LED grossissement 10x portable. Batterie rechargeable. Compact.",
        "price": "3,800 FCFA"
    },
    "product-38": {
        "name": "Brosse Massante Électrique",
        "description": "Brosse électrique 3 vitesses pour cuir chevelu. Vibration infrarouge. Imperméable.",
        "price": "4,500 FCFA"
    },
    "product-39": {
        "name": "Sac Cosmétiques Voyage",
        "description": "Sac organisé pour cosmétiques et toilettes. Imperméable, 5 compartiments. Compact.",
        "price": "2,200 FCFA"
    },
    "product-40": {
        "name": "Peigne Cheveux Démêlant",
        "description": "Peigne anti-casse en matière naturelle. Idéal cheveux frisés/crépus. Massage cuir chevelu.",
        "price": "1,600 FCFA"
    },
    "product-41": {
        "name": "Porte-clés Cuir Naturel",
        "description": "Porte-clés en cuir véritable tanné naturellement. Solide et élégant. Personnalisable.",
        "price": "900 FCFA"
    },
}

def get_product_number(src):
    """Extraire le numéro de produit du src"""
    match = re.search(r'product-(\d+)', src)
    if match:
        return f"product-{match.group(1)}"
    return None

def update_html_file(filepath):
    """Mettre à jour un fichier HTML avec les bonnes descriptions"""
    print(f"\n📝 Traitement de {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = 0
    
    # Pattern pour trouver les blocs produits avec img src="img/product-X.png"
    # On cherche la structure générale autour de l'image
    pattern = r'<img[^>]*src="img/product-(\d+)\.png"[^>]*alt="[^"]*"[^>]*>'
    
    matches = list(re.finditer(pattern, content))
    print(f"   ✓ Trouvé {len(matches)} images de produits")
    
    # Pour chaque match, on va chercher le bloc produit complet et mettre à jour
    for match in reversed(matches):  # On fait l'inverse pour ne pas décaler les indices
        product_key = f"product-{match.group(1)}"
        
        if product_key not in DESCRIPTIONS:
            print(f"   ⚠️ Pas de description pour {product_key}")
            continue
        
        desc = DESCRIPTIONS[product_key]
        start = match.start()
        
        # Chercher le début du bloc contenant (chercher le <div class="product-item" ou équivalent)
        block_start = content.rfind('<div class="product-item', 0, start)
        if block_start == -1:
            block_start = content.rfind('<div class="col-', 0, start)
        
        # Chercher la fin du bloc (</div> correspondant)
        block_end = content.find('</div>', start) + 6
        block_end = content.find('</div>', block_end) + 6
        block_end = content.find('</div>', block_end) + 6
        
        if block_start == -1 or block_end == -1:
            continue
        
        block = content[block_start:block_end]
        
        # Remplacer les descriptions génériques dans ce bloc
        # Chercher h5 avec le titre
        new_block = re.sub(
            r'<h5[^>]*>([^<]*Apple[^<]*|[^<]*Catégorie[^<]*|[^<]*Product[^<]*)</h5>',
            f'<h5>{desc["name"]}</h5>',
            block
        )
        
        # Remplacer la description (généralement dans un <p> ou <small>)
        new_block = re.sub(
            r'<p[^>]*>Apple iPhone[^<]*</p>',
            f'<p>{desc["description"]}</p>',
            new_block
        )
        
        # Remplacer le prix
        new_block = re.sub(
            r'₵[\d,]+',
            f'{desc["price"]}',
            new_block
        )
        
        if new_block != block:
            content = content[:block_start] + new_block + content[block_end:]
            changes += 1
            print(f"   ✓ {product_key}: {desc['name']}")
    
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {changes} produits mis à jour")
        return True
    else:
        print(f"   ⚠️ Aucun changement effectué")
        return False

# Fichiers à traiter
files_to_update = [
    '/home/backbox/Downloads/Electro-Bootstrap-1.0.0/index.html',
    '/home/backbox/Downloads/Electro-Bootstrap-1.0.0/shop.html',
    '/home/backbox/Downloads/Electro-Bootstrap-1.0.0/bestseller.html',
]

print("=" * 60)
print("🔄 MISE À JOUR DES DESCRIPTIONS PRODUITS OMNISERVISE")
print("=" * 60)

total_changes = 0
for filepath in files_to_update:
    try:
        if update_html_file(filepath):
            total_changes += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")

print("\n" + "=" * 60)
print(f"✅ TERMINÉ: {total_changes} fichiers mis à jour")
print("=" * 60)
