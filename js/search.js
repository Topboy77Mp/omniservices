// Script de recherche et filtrage par catégorie pour index.html
// Ajouter ce script juste avant la fermeture du body

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const categorySelect = document.getElementById('categorySelect');
    const searchBtn = document.getElementById('searchBtn');
    
    if (!searchBtn) return; // Sortir si les éléments n'existent pas
    
    // Fonction pour effectuer la recherche
    function performSearch() {
        const searchQuery = searchInput ? searchInput.value.toLowerCase().trim() : '';
        const selectedCategory = categorySelect ? categorySelect.value : '';
        
        if (!searchQuery && !selectedCategory) {
            alert('Veuillez entrer un terme de recherche ou sélectionner une catégorie');
            return;
        }
        
        // Construire l'URL de redirection vers shop.html
        let url = 'shop.html?';
        const params = [];
        
        if (searchQuery) {
            params.push('search=' + encodeURIComponent(searchQuery));
        }
        
        if (selectedCategory) {
            params.push('category=' + encodeURIComponent(selectedCategory));
        }
        
        url += params.join('&');
        window.location.href = url;
    }
    
    // Événement au clic sur le bouton de recherche
    searchBtn.addEventListener('click', performSearch);
    
    // Événement au Enter dans le champ de recherche
    if (searchInput) {
        searchInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                performSearch();
            }
        });
    }
    
    // Bonus: permettre aussi de rechercher via le sélecteur de catégorie
    if (categorySelect) {
        categorySelect.addEventListener('change', function() {
            if (this.value) {
                // Rediriger directement vers la catégorie
                window.location.href = 'shop.html?category=' + encodeURIComponent(this.value);
            }
        });
    }
});

// Fonction pour afficher les résultats de recherche dans shop.html
function filterProductsBySearch() {
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('search');
    const categoryFilter = urlParams.get('category');
    
    if (!searchQuery && !categoryFilter) {
        return; // Pas de filtrage à faire
    }
    
    const products = document.querySelectorAll('.product-item');
    let visibleCount = 0;
    
    products.forEach(product => {
        const productName = product.querySelector('h4') ? product.querySelector('h4').textContent.toLowerCase() : '';
        const productCategory = product.closest('.category-section');
        const categoryId = productCategory ? productCategory.querySelector('h3') : null;
        const categoryText = categoryId ? categoryId.textContent.toLowerCase() : '';
        
        let matches = true;
        
        // Vérifier le texte de recherche
        if (searchQuery) {
            matches = matches && (productName.includes(searchQuery.toLowerCase()) || categoryText.includes(searchQuery.toLowerCase()));
        }
        
        // Vérifier la catégorie
        if (categoryFilter) {
            const categoryMap = {
                'beaute': 'beauté & cosmétiques',
                'parfums': 'parfums & eaux',
                'soins': 'soins personnels',
                'naturels': 'produits naturels & herbes',
                'aliments': 'aliments & épices',
                'vetements': 'vêtements & mode',
                'autres': 'autres produits'
            };
            matches = matches && categoryText.includes(categoryMap[categoryFilter] || categoryFilter);
        }
        
        // Afficher ou masquer le produit
        if (matches) {
            product.style.display = '';
            visibleCount++;
        } else {
            product.style.display = 'none';
        }
    });
    
    // Afficher un message si aucun résultat
    if (visibleCount === 0 && (searchQuery || categoryFilter)) {
        console.log('Aucun produit ne correspond à votre recherche');
    }
}

// Exécuter le filtrage si la page est shop.html
if (window.location.pathname.includes('shop.html')) {
    document.addEventListener('DOMContentLoaded', filterProductsBySearch);
}
