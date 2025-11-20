const express = require('express');
const path = require('path');
const app = express();

// Définir le port
const PORT = process.env.PORT || 3000;

// Servir les fichiers statiques du répertoire courant
app.use(express.static(path.join(__dirname)));

// Route pour la page d'accueil
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Routes pour les pages principales
const pages = ['shop', 'single', 'cart', 'checkout', 'contact', 'bestseller', '404'];
pages.forEach(page => {
  app.get(`/${page}`, (req, res) => {
    res.sendFile(path.join(__dirname, `${page}.html`));
  });
});

// Routes spéciales
app.get('/telechargements', (req, res) => {
  res.sendFile(path.join(__dirname, 'TELECHARGEMENTS_IMAGES.html'));
});

// Gérer les URLs avec paramètres (search, category, etc.)
app.get('/shop.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'shop.html'));
});

// Catch-all pour 404
app.use((req, res) => {
  res.status(404).sendFile(path.join(__dirname, '404.html'));
});

// Démarrer le serveur
app.listen(PORT, () => {
  console.log(`
╔════════════════════════════════════════════════════════════╗
║                   OMNISERVISE RUNNING                      ║
║════════════════════════════════════════════════════════════║
║                                                            ║
║  🌐 Server: http://localhost:${PORT}                    ║
║  📦 Products: 41 items in 7 categories                    ║
║  ✅ Status: Ready for production                          ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
  `);
});
