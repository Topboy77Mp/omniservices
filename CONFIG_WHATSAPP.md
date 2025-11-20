# Configuration du Widget WhatsApp OMNISERVISE

## 📍 PARAMÈTRES ACTUELS

```
NUMÉRO_WHATSAPP = +228 92 65 12 34
NUMERO_ENCODE = 22892651234 (sans + ni espaces)

MESSAGE_DEFAUT = "Bonjour OMNISERVISE, je souhaite connaitre plus d'informations sur vos produits"
MESSAGE_ENCODE = "Bonjour%20OMNISERVISE%2C%20je%20souhaite%20connaitre%20plus%20d%27informations%20sur%20vos%20produits"

COULEUR_PRIMAIRE = #25D366 (Vert WhatsApp)
COULEUR_SECONDAIRE = #20BA5E (Vert plus foncé)
COULEUR_TEXTE = #FFFFFF (Blanc)
COULEUR_BORDER = #FFFFFF (Blanc)

POSITION_DESKTOP_BOTTOM = 20px
POSITION_DESKTOP_RIGHT = 20px
POSITION_MOBILE_BOTTOM = 10px
POSITION_MOBILE_RIGHT = 10px

TAILLE_AU_REPOS_DESKTOP = 60px × 60px
TAILLE_AU_REPOS_MOBILE = 45px × 45px
TAILLE_AU_SURVOL_DESKTOP = 150px × 60px
TAILLE_AU_SURVOL_MOBILE = 120px × 45px

ANIMATION_ENTRANCE = slideIn 0.5s ease-in-out
ANIMATION_PULSE = pulse 2s ease-in-out infinite
Z_INDEX = 999
```

## 🔧 COMMENT MODIFIER

### 1. Changer le Numéro WhatsApp

**Fichier à modifier**: Tous les fichiers HTML (index.html, shop.html, etc.)

**Chercher**:
```html
https://wa.me/22892651234?text=
```

**Remplacer par**:
```html
https://wa.me/VOTRE_NUMERO?text=
```

**Exemple**: Pour le numéro +33 1 23 45 67 89
```html
https://wa.me/33123456789?text=
```

### 2. Changer le Message Pré-rempli

**Chercher**:
```html
text=Bonjour%20OMNISERVISE%2C%20je%20souhaite%20connaitre%20plus%20d%27informations%20sur%20vos%20produits
```

**Remplacer par**:
```html
text=VOTRE_MESSAGE_ENCODE
```

**Comment encoder un message**:
- Espaces → %20
- Accent é → %C3%A9
- Accent à → %C3%A0
- Apostrophe ' → %27
- Point d'interrogation ? → %3F
- Virgule , → %2C

**Exemple**: "Bonjour, pouvez-vous m'aider?"
```
Bonjour%2C%20pouvez-vous%20m%27aider%3F
```

### 3. Changer les Couleurs

**Fichier à modifier**: Tous les fichiers HTML (rechercher `<style>`)

**Chercher**:
```css
background: linear-gradient(135deg, #25D366, #20BA5E);
```

**Remplacer par**:
```css
background: linear-gradient(135deg, #YOUR_COLOR1, #YOUR_COLOR2);
```

**Couleurs WhatsApp Alternatives**:
```
Vert clair: #25D366
Vert standard: #128C7E
Vert foncé: #0F7569
```

### 4. Changer la Position

**Fichier à modifier**: Tous les fichiers HTML (rechercher `<style>`)

**Pour déplacer vers le coin inférieur gauche**:
```css
bottom: 20px;
left: 20px;   /* Remplacer "right" par "left" */
```

**Pour déplacer vers le coin supérieur droit**:
```css
top: 20px;    /* Remplacer "bottom" par "top" */
right: 20px;
```

### 5. Changer la Taille

**Chercher**:
```css
width: 60px;
height: 60px;
```

**Remplacer par**:
```css
width: 70px;
height: 70px;
```

## 📝 AJOUTER LE WIDGET À UNE NOUVELLE PAGE

Si vous créez une nouvelle page HTML, ajoutez avant la balise `</body>`:

```html
<!-- WhatsApp Widget Flottant -->
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
/* [Copier le CSS du fichier js/whatsapp-widget.html] */
</style>
```

Ou utiliser le script d'ajout automatisé:
```bash
python3 add_whatsapp_widget.py
```

## 🔍 VÉRIFIER L'INTÉGRATION

### Sur Desktop
1. Ouvrir la page dans un navigateur
2. Voir l'icône verte pulsante en bas-droit
3. Passer la souris → icône s'agrandit
4. Affichage du texte "Chat"
5. Tooltip au survol

### Sur Mobile
1. Ouvrir la page sur smartphone
2. Voir l'icône verte pulsante en bas-droit
3. Appuyer sur l'icône
4. WhatsApp doit s'ouvrir

## 🧪 TESTER LE LIEN

Pour vérifier que le lien fonctionne:
1. Remplacer le numéro par le vôtre
2. Cliquer sur le widget
3. Vérifier que WhatsApp s'ouvre avec le message pré-rempli

## 📊 MONITORING

### Vérifier les Clics
1. WhatsApp Business (optionnel) pour voir les statistiques
2. Analytics Google (optionnel) pour tracker les clics
3. Manuellement: vérifier les messages reçus

### Améliorer le Taux de Conversion
- Répondre rapidement (< 1h)
- Utiliser un message de bienvenue automatisé
- Offrir un code de réduction pour les nouveaux clients
- Segmenter les messages par source (page produit, etc.)

## 🚀 DÉPLOIEMENT

Après modification:
```bash
git add .
git commit -m "Modifier widget WhatsApp"
git push origin main
```

Render redéploiera automatiquement dans 1-2 minutes.

## ❌ DÉPANNAGE

### Le widget n'apparaît pas?
- Vérifier que Font Awesome est chargé
- Ouvrir la console (F12) pour voir les erreurs
- Vérifier que `</body>` existe dans le HTML

### Le lien ne fonctionne pas?
- Vérifier le format du numéro (22892651234 sans + ni espaces)
- Vérifier que WhatsApp est installé
- Essayer sur un navigateur différent

### Le CSS ne s'applique pas?
- Forcer le rafraîchissement (Ctrl+F5)
- Vérifier qu'aucun autre CSS ne le masque
- Vérifier que le style est dans la balise `<style>`

## 📞 CONTACT

Pour toute question sur le widget:
- Voir: GUIDE_WHATSAPP_WIDGET.md (guide complet)
- Consulter: js/whatsapp-widget.html (code source)
- Tester: Directement sur le site

---

**Version**: 1.0  
**Date**: 20 novembre 2025  
**Statut**: ✅ Opérationnel

**Besoin d'aide?** Consulter GUIDE_WHATSAPP_WIDGET.md
