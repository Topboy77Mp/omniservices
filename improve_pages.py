#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'amélioration rapide des pages HTML
Ajoute des images, améliore le contenu, traduit les textes restants
"""

import os
import re
from pathlib import Path

# Dictionnaire de traductions manquantes
TRADUCTIONS = {
    "USD": "XOF",
    "Anglais": "Français",
    "Turkish": "English",
    "Spanol": "Español",
    "Italiano": "Italino",
    "Euro": "XOF (FCFA)",
    "Dolar": "USD (Dollar)",
    "$0.00": "0 XOF",
    "Electro": "OMNISERVISE",
    "Your Site Nom": "OMNISERVISE Lomé",
    "123 Street Nouveau York.USA": "Rue de la Paix, Lomé, Togo 🇹🇬",
    "(+012) 3456 7890": "(+228) 90 12 34 56",
    "Yoursite@ex.com": "info@omniservise.tg",
}

# Fichiers HTML à améliorer
HTML_FILES = [
    "cart.html",
    "cheackout.html", 
    "bestseller.html",
    "404.html"
]

def improve_html_file(filepath):
    """Améliore un fichier HTML"""
    if not os.path.exists(filepath):
        print(f"⚠️  {filepath} n'existe pas")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Appliquer les traductions
    for ancien, nouveau in TRADUCTIONS.items():
        content = content.replace(ancien, nouveau)
    
    # Vérifier si changements ont été faits
    if content == original:
        print(f"✓ {filepath} - Déjà optimisé")
        return False
    
    # Écrire les changements
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filepath} - Mis à jour")
    return True

def main():
    print("=" * 60)
    print("  🚀 AMÉLIORATION RAPIDE DES PAGES HTML")
    print("=" * 60)
    
    base_path = "/home/backbox/Downloads/Electro-Bootstrap-1.0.0"
    os.chdir(base_path)
    
    updated_count = 0
    for html_file in HTML_FILES:
        filepath = os.path.join(base_path, html_file)
        if improve_html_file(filepath):
            updated_count += 1
    
    print("=" * 60)
    print(f"  ✨ {updated_count}/{len(HTML_FILES)} fichiers mis à jour")
    print("=" * 60)

if __name__ == "__main__":
    main()
