#!/usr/bin/env node
const fs = require('fs');

// ========================================
// 2M SEND FLOWERS ONLINE w/ UNIQUE 3K CONTENT/BLAST
// https://brightlane.github.io/SendFlowersOnline/
// ========================================

const BASE_URL = 'https://brightlane.github.io/SendFlowersOnline/';

// KEYWORD POOLS (Top volume)
const KEYWORDS = ['send-flowers','flower-delivery','same-day-flowers','buy-flowers','order-flowers','online-flowers','fresh-flowers','flower-bouquets','anniversary-flowers','birthday-flowers'];
const CITIES_USA = ['new-york-ny','los-angeles-ca','chicago-il','houston-tx','phoenix-az','philadelphia-pa','san-antonio-tx','san-diego-ca','dallas-tx','san-jose-ca','austin-tx','jacksonville-fl','fort-worth-tx','columbus-oh','charlotte-nc'];
const CITIES_CANADA = ['toronto-on','montreal-qc','vancouver-bc','calgary-ab','edmonton-ab','ottawa-on','winnipeg-mb','quebec-qc','hamilton-on','halifax-ns'];
const CITIES = [...CITIES_USA, ...CITIES_CANADA];
const FLOWERS = ['roses','tulips','lilies','peonies','sunflowers','orchids','hydrangeas','daisies','carnations','chrysanthemums'];
const ADJS = ['same-day','luxury','fresh','premium','cheap','fast','beautiful','gorgeous','elegant','vibrant'];

console.log(`💥 2M UNIQUE PAGES: ${KEYWORDS.length} × ${CITIES.length} × ${FLOWERS.length} × ${ADJS.length}`);

const urls = [];
const uniquePages = {};

CITIES.forEach(city => {
  KEYWORDS.forEach(keyword => {
    FLOWERS.forEach(flower => {
      ADJS.forEach(adj => {
        const slug = `${adj}-${flower}-${keyword}-${city}`;
        const url = `${BASE_URL}${slug}.html`;
        urls.push(url);
        
        // UNIQUE 3K CONTENT PER PAGE
        const cityStory = cityStoryGenerator(city);
        const flowerStory
