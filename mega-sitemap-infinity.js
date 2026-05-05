#!/usr/bin/env node
const fs = require('fs');

// ========================================
// BILLION+ SITEMAP (Google/Bing Unlimited)
// sitemap.xml → 50K indexes → 50K sitemaps → 50K URLs each = 125 TRILLION!
// ========================================

const BASE_URL = 'https://brightlane.github.io/SendFlowersOnline/';
const MAX_URLS_SITEMAP = 50000;     // Google limit
const MAX_SITEMAPS_INDEX = 50000;    // Index limit
const MAX_INDEXES_TOP = 50000;       // Top index limit = 1.25 TRILLION URLs!

console.log('🌌 Building Billion+ Sitemap Hierarchy...');

// 1. LOAD YOUR 1M+ URLS
const allUrls = fs.readFileSync('output/sitemap.txt', 'utf8')
  .split('\n')
  .filter(u
