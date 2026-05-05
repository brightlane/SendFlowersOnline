#!/usr/bin/env node
const fs = require('fs');

// ========================================
// FULL UNIQUE 3K CONTENT PER PAGE
// Reads sitemap.txt → spits complete HTML files
// ========================================

const CITY_TALES = {
  'los-angeles-ca': 'Beverly Hills brunch, Rodeo Drive displays, Griffith Observatory romance',
  'new-york-ny': 'Manhattan penthouses, Rockefeller rush, 5th Ave sparkle',
  'toronto-on': 'Distillery District dinners, CN Tower proposals, Eaton Centre elegance',
  // 25+ cities...
};

const FLOWER_TALES = {
  'tulips': 'Dutch spring symbol, 12-15 days vase life, perfect 18°C',
  'roses': '12 long-stem passion, daily trim, Hollywood Hills favorite',
  // All flowers...
};

const readUrls = fs.readFileSync('output/sitemap.txt', 'utf8').split('\n').slice(0, 50); // Sample

readUrls.forEach((url, i)
