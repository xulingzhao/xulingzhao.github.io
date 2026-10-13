---
layout: default
permalink: /publications/
title: Publications
description: Research publications by Xuling Zhao.
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home publications-page">
  <a class="home-skip" href="#publications-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Xuling Zhao, home">xz.</a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}" aria-current="page">Publications</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/blog/' | relative_url }}">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <section class="publications-introduction" id="publications-content" aria-labelledby="publications-title">
    <p class="home-eyebrow">Research &amp; scholarship</p>
    <h1 id="publications-title">Publications</h1>
    <p class="home-bio">Research, in print.</p>
    <p class="home-sample-note">Template examples below; personal publications forthcoming.</p>
  </section>

{% if site.bib_search %}
  <div class="publications-search" role="search" aria-label="Filter publications">
    <label for="bibsearch">Search publications</label>
    {% include bib_search.liquid %}
  </div>
  {% endif %}

  <section class="home-publications publications publications-list" aria-label="Publications by year">
    {% bibliography %}
  </section>

  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
