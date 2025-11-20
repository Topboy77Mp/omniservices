#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour ajouter le widget WhatsApp à toutes les pages HTML
"""

import re
from pathlib import Path

# Contenu du widget WhatsApp
WHATSAPP_WIDGET = '''<!-- WhatsApp Widget Flottant -->
<div id="whatsapp-widget" class="whatsapp-widget">
    <a href="https://wa.me/22892651234?text=Bonjour%20OMNISERVISE%2C%20je%20souhaite%20connaitre%20plus%20d%27informations%20sur%20vos%20produits" 
       target="_blank" 
       rel="noopener noreferrer"
       class="whatsapp-button"
       title="Chat WhatsApp">
        <i class="fab fa-whatsapp"></i>
        <span class="whatsapp-text">Chat</span>
    </a>
    <div class="whatsapp-tooltip">Besoin d'aide? Contactez-nous sur WhatsApp!</div>
</div>

<style>
/* WhatsApp Widget Styles */
.whatsapp-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 999;
    animation: slideIn 0.5s ease-in-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.whatsapp-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: linear-gradient(135deg, #25D366, #20BA5E);
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(37, 211, 102, 0.4);
    transition: all 0.3s ease;
    font-size: 28px;
    border: 3px solid white;
    position: relative;
}

.whatsapp-button:hover {
    transform: scale(1.15);
    box-shadow: 0 8px 20px rgba(37, 211, 102, 0.6);
    width: 150px;
    border-radius: 50px;
    padding-right: 10px;
}

.whatsapp-button:hover .whatsapp-text {
    display: inline;
}

.whatsapp-text {
    display: none;
    font-size: 14px;
    font-weight: bold;
    white-space: nowrap;
}

.whatsapp-button:active {
    transform: scale(0.95);
}

/* Tooltip */
.whatsapp-tooltip {
    position: absolute;
    bottom: 75px;
    right: 0;
    background: #333;
    color: white;
    padding: 10px 15px;
    border-radius: 8px;
    font-size: 12px;
    white-space: nowrap;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
    pointer-events: none;
}

.whatsapp-widget:hover .whatsapp-tooltip {
    opacity: 1;
    visibility: visible;
    bottom: 80px;
}

/* Animation pulsante */
@keyframes pulse {
    0%, 100% {
        box-shadow: 0 4px 12px rgba(37, 211, 102, 0.4);
    }
    50% {
        box-shadow: 0 4px 20px rgba(37, 211, 102, 0.8);
    }
}

.whatsapp-button {
    animation: slideIn 0.5s ease-in-out, pulse 2s ease-in-out infinite;
}

/* Responsive */
@media (max-width: 768px) {
    .whatsapp-widget {
        bottom: 15px;
        right: 15px;
    }

    .whatsapp-button {
        width: 50px;
        height: 50px;
        font-size: 24px;
    }

    .whatsapp-button:hover {
        width: 130px;
    }

    .whatsapp-tooltip {
        font-size: 11px;
    }
}

@media (max-width: 480px) {
    .whatsapp-widget {
        bottom: 10px;
        right: 10px;
    }

    .whatsapp-button {
        width: 45px;
        height: 45px;
        font-size: 20px;
    }

    .whatsapp-button:hover {
        width: 120px;
    }
}

/* Mode Sombre Optionnel */
@media (prefers-color-scheme: dark) {
    .whatsapp-tooltip {
        background: #555;
    }
}
</style>
'''

# Fichiers HTML à traiter
HTML_FILES = [
    'index.html',
    'shop.html',
    'single.html',
    'contact.html',
    'cart.html',
    'checkout.html',
    'bestseller.html',
    '404.html',
    'TELECHARGEMENTS_IMAGES.html',
]

def add_whatsapp_widget(filepath):
    """Ajouter le widget WhatsApp à un fichier HTML"""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Vérifier si le widget est déjà présent
        if 'whatsapp-widget' in content:
            print(f"   ⚠️  {filepath.name} - Widget déjà présent")
            return False
        
        # Chercher la balise </body> pour insérer le widget avant
        if '</body>' not in content:
            print(f"   ⚠️  {filepath.name} - Pas de balise </body>")
            return False
        
        # Insérer le widget avant </body>
        new_content = content.replace('</body>', f'{WHATSAPP_WIDGET}\n</body>')
        
        # Sauvegarder
        filepath.write_text(new_content, encoding='utf-8')
        print(f"   ✓ {filepath.name} - Widget ajouté")
        return True
        
    except Exception as e:
        print(f"   ❌ {filepath.name} - Erreur: {e}")
        return False

# Exécution
print("=" * 60)
print("🔄 AJOUT DU WIDGET WHATSAPP À TOUTES LES PAGES")
print("=" * 60)
print()

success = 0
failed = 0

for filename in HTML_FILES:
    filepath = Path(filename)
    if filepath.exists():
        if add_whatsapp_widget(filepath):
            success += 1
        else:
            failed += 1
    else:
        print(f"   ⚠️  {filename} - Non trouvé")

print()
print("=" * 60)
print(f"✅ RÉSUMÉ: {success} fichiers mis à jour, {failed} erreurs")
print("=" * 60)
print()
print("📍 Widget WhatsApp ajouté avec:")
print("   ✓ Numéro: +228 92 65 12 34")
print("   ✓ Message pré-rempli")
print("   ✓ Icône Font Awesome")
print("   ✓ Animation pulsante")
print("   ✓ Responsive design")
print("   ✓ Tooltip au survol")
print()
