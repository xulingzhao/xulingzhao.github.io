---
layout: default
permalink: /publications/
title: Publications
description: Research publications by Xuling Zhao.
nav: true
nav_order: 2
---

{% capture publication_count %}{% bibliography_count -f publications %}{% endcapture %}
{% assign publication_count = publication_count | plus: 0 %}

<div class="academic-home publications-page">
  <a class="home-skip" href="#publications-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home">{{ site.data.home.wordmark }}</a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}" aria-current="page">Publications</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/blog/' | relative_url }}">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <section class="collection-introduction" id="publications-content" aria-labelledby="publications-title">
    <p class="home-eyebrow">Research &amp; scholarship</p>
    <h1 id="publications-title">Publications</h1>
    {% if publication_count > 0 %}<p class="home-bio">Research, in print.</p>{% endif %}
  </section>

{% if publication_count > 0 %}
{% if site.bib_search %}
  <div class="publications-search" role="search" aria-label="Filter publications">
    <label for="bibsearch">Search publications</label>
    {% include bib_search.liquid %}
  </div>
  {% endif %}

  <section class="home-publications publications publications-list" aria-label="Publications by year">
    {% bibliography -f publications %}
  </section>
  {% else %}
  <section class="collection-empty" aria-label="Publication status">
    <p>No publications yet.</p>
  </section>
  {% endif %}

  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
