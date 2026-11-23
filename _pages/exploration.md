---
layout: default
title: Exploration
permalink: /exploration/
description: detours and rediscoveries
nav: true
nav_order: 3
statuses:
  - name: Set Aside
    description: Results with modest experimental gains or too little new theory to warrant a paper.
  - name: Open Question
    description: Well-defined conjectures, proof gaps, and technical problems I left open when I stopped working on them.
  - name: Rediscovery
    description: Ideas I worked through before finding the same core insight in an earlier paper.
---

<div class="academic-home">
  <a class="home-skip" href="#exploration-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home"><img src="{{ '/assets/img/favicon.png' | relative_url }}" alt="" width="40" height="40"></a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/exploration/' | relative_url }}" aria-current="page">Exploration</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/blog/' | relative_url }}">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <section class="collection-introduction" id="exploration-content" aria-labelledby="exploration-title">
    <h1 id="exploration-title">{{ page.title }}</h1>
    <p class="home-bio">{{ page.description }}</p>
  </section>

{% for status in page.statuses %}
{% assign status_id = status.name | slugify %}
{% assign entries = site.explorations | where: 'status', status.name | sort: 'date' | reverse %}
  <section class="projects-category exploration-group" aria-labelledby="{{ status_id }}">
    <h2 id="{{ status_id }}"><a href="#{{ status_id }}">{{ status.name }}</a></h2>
    <p class="projects-category-description">{{ status.description }}</p>
    {% for entry in entries %}
      <details class="exploration-entry" lang="{{ entry.lang | default: site.lang | escape }}">
        <summary>{{ entry.title | escape }}</summary>
        <div class="writing-prose" id="idea-{{ entry.slug | slugify }}">{{ entry.content }}</div>
      </details>
    {% endfor %}
  </section>
{% endfor %}

{% if site.explorations.size == 0 %}
  <p class="collection-empty">No entries yet.</p>
{% endif %}

  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
