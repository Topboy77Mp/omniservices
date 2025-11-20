/*
 * Configuration OMNISERVISE
 * Informations centralisées pour le site
 */

// Configuration générale
const OMNISERVISE_CONFIG = {
    // Informations entreprise
    company: {
        name: "OMNISERVISE",
        tagline: "Votre partenaire de confiance",
        description: "Services et produits de qualité à Lomé, Togo",
        founded: 2024,
        location: "Lomé, Togo"
    },
    
    // Coordonnées de contact
    contact: {
        phone: "(+228) 90 12 34 56",
        email: "info@omniservise.tg",
        address: "Rue de la Paix, Lomé, Togo",
        website: "www.omniservise.tg",
        hours: {
            weekday: "Lun-Ven: 08h00 - 17h00",
            saturday: "Samedi: 09h00 - 14h00",
            sunday: "Dimanche: Fermé",
            timezone: "GMT+0 (Heure d'Afrique de l'Ouest)"
        }
    },
    
    // Réseaux sociaux
    socialMedia: {
        facebook: "https://facebook.com/omniservise",
        twitter: "https://twitter.com/omniservise",
        instagram: "https://instagram.com/omniservise",
        whatsapp: "+22890123456",
        linkedin: "https://linkedin.com/company/omniservise"
    },
    
    // Devises et paiement
    payment: {
        primaryCurrency: "XOF",
        currencySymbol: "FCFA",
        acceptedMethods: [
            "Carte bancaire",
            "Mobile Money (Togocom, MTN)",
            "Virement bancaire",
            "Espèces à la livraison"
        ]
    },
    
    // Livraison
    shipping: {
        domesticDelivery: {
            standard: "2-3 jours",
            express: "24 heures",
            free: true,
            minOrder: 0
        },
        internationalDelivery: {
            available: false,
            message: "Livraison internationale non disponible pour le moment"
        }
    },
    
    // Catégories de produits
    categories: [
        {
            id: 1,
            name: "Accessoires",
            count: 12,
            icon: "fa-box"
        },
        {
            id: 2,
            name: "Services Électroniques",
            count: 8,
            icon: "fa-cogs"
        },
        {
            id: 3,
            name: "Réparation & Maintenance",
            count: 6,
            icon: "fa-tools"
        },
        {
            id: 4,
            name: "Solutions Professionnelles",
            count: 10,
            icon: "fa-briefcase"
        },
        {
            id: 5,
            name: "Produits & Équipements",
            count: 15,
            icon: "fa-laptop"
        }
    ],
    
    // Services clés
    services: [
        {
            title: "Retour Gratuit",
            description: "Garantie de 30 jours satisfait ou remboursé!",
            icon: "fa-sync-alt"
        },
        {
            title: "Livraison Gratuite",
            description: "Livraison gratuite pour toutes les commandes",
            icon: "fa-telegram-plane"
        },
        {
            title: "Support 24/7",
            description: "Nous vous supportons en ligne 24h/24",
            icon: "fa-life-ring"
        },
        {
            title: "Recevez des Cadeaux",
            description: "Cadeaux gratuits sur toute commande > 50€",
            icon: "fa-credit-card"
        },
        {
            title: "Paiement Sécurisé",
            description: "Nous protégeons votre sécurité",
            icon: "fa-lock"
        },
        {
            title: "Service en Ligne",
            description: "Retour gratuit dans les 30 jours",
            icon: "fa-blog"
        }
    ],
    
    // Couleurs de marque
    colors: {
        primary: "#0052a3",        // Bleu professionnel
        secondary: "#f28b00",      // Orange dynamique
        success: "#198754",        // Vert
        danger: "#dc3545",         // Rouge
        warning: "#ffc107",        // Jaune
        info: "#0dcaf0",           // Cyan
        light: "#f8f9fa",          // Gris clair
        dark: "#212529",           // Gris foncé
        togoGreen: "#1d5a3d",      // Vert Togo
        togoYellow: "#fcd116"      // Jaune Togo
    },
    
    // SEO
    seo: {
        title: "OMNISERVISE - Services et Produits à Lomé, Togo",
        description: "Découvrez OMNISERVISE, votre partenaire de confiance pour tous vos services et produits à Lomé, Togo",
        keywords: "OMNISERVISE, services, produits, Lomé, Togo, électronique, réparation",
        author: "OMNISERVISE",
        language: "fr-FR",
        robots: "index, follow"
    },
    
    // FAQ
    faq: [
        {
            question: "Comment puis-je passer une commande?",
            answer: "Parcourez notre catalogue, ajoutez les produits au panier et suivez le processus de paiement."
        },
        {
            question: "Quels modes de paiement acceptez-vous?",
            answer: "Nous acceptons carte bancaire, Mobile Money, virement bancaire et espèces à la livraison."
        },
        {
            question: "Combien de temps prend la livraison?",
            answer: "La livraison standard prend 2-3 jours. L'express est 24h. La livraison est gratuite."
        },
        {
            question: "Puis-je retourner un produit?",
            answer: "Oui, vous avez 30 jours pour retourner un produit (gratuit). Satisfait ou remboursé."
        },
        {
            question: "Comment puis-je vous contacter?",
            answer: "Vous pouvez nous appeler au (+228) 90 12 34 56 ou envoyer un email à info@omniservise.tg"
        },
        {
            question: "Offrez-vous une garantie?",
            answer: "Oui, tous nos produits incluent une garantie. Contactez-nous pour plus de détails."
        }
    ]
};

// Export pour Node.js (si utilisé)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = OMNISERVISE_CONFIG;
}
