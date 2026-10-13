---
layout: default
title: about
permalink: /
description: The personal academic website of Xuling Zhao. Research, projects, and ideas.
---

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home">
  <a class="home-skip" href="#home-introduction">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Xuling Zhao, home">xz.</a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}" aria-current="page">About</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/blog/' | relative_url }}">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <section class="home-introduction" id="home-introduction" aria-labelledby="home-name">
    <div class="home-introduction-copy">
      <p class="home-eyebrow">A personal academic website</p>
      <h1 id="home-name">{{ site.first_name }} {{ site.last_name }}</h1>
      <p class="home-bio">{{ site.data.home.introduction }}</p>
      <a class="home-text-link" href="#selected-work">Explore my work <span aria-hidden="true">↗</span></a>
    </div>
    <figure class="home-portrait">
      {% if site.data.home.portrait %}
        <img src="{{ site.data.home.portrait | relative_url }}" alt="Portrait of Xuling Zhao" width="208" height="248" fetchpriority="high">
      {% else %}
        <div class="home-portrait-placeholder" role="img" aria-label="Portrait placeholder for Xuling Zhao"><span aria-hidden="true">XZ</span></div>
        <figcaption>Portrait forthcoming</figcaption>
      {% endif %}
    </figure>
  </section>

  <section class="home-background" aria-label="Academic background">
    <div>
      <h2>Education</h2>
      {% if site.data.home.education.size > 0 %}
        {% for entry in site.data.home.education %}
          <p class="home-background-detail"><strong>{{ entry.institution }}</strong><br>{{ entry.degree }} · {{ entry.years }}</p>
        {% endfor %}
      {% else %}
        <p>Details forthcoming.</p>
      {% endif %}
    </div>
    <div>
      <h2>Research interests</h2>
      {% if site.data.home.research_interests.size > 0 %}
        <p>{{ site.data.home.research_interests | join: ' · ' }}</p>
      {% else %}
        <p>Details forthcoming.</p>
      {% endif %}
    </div>
  </section>

  <section class="home-section" id="selected-work" aria-labelledby="home-publications-title">
    <div class="home-section-heading">
      <div>
        <p class="home-eyebrow">Selected work</p>
        <h2 id="home-publications-title">Publications</h2>
      </div>
      <a class="home-text-link" href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">↗</span></a>
    </div>
    <p class="home-sample-note">Template examples below; personal publications forthcoming.</p>
    <div class="home-publications publications">
      {% bibliography --group_by none --query @book[preview] --max 2 %}
    </div>
  </section>

  <section class="home-section" aria-labelledby="home-projects-title">
    <div class="home-section-heading">
      <div>
        <p class="home-eyebrow">Ideas in practice</p>
        <h2 id="home-projects-title">Projects</h2>
      </div>
      <a class="home-text-link" href="{{ '/projects/' | relative_url }}">All projects <span aria-hidden="true">↗</span></a>
    </div>
    <p class="home-sample-note">Template examples below; personal projects forthcoming.</p>
    <div class="home-project-grid">
      {% assign home_projects = site.projects | where_exp: 'project', 'project.img' | sort: 'importance' %}
      {% for project in home_projects limit: 2 %}
        <a class="home-project" href="{{ project.url | relative_url }}">
          <div class="home-project-image"><img src="{{ project.img | relative_url }}" alt="" loading="lazy" width="640" height="400"></div>
          <div class="home-project-heading"><h3>{{ project.title | capitalize }}</h3><span aria-hidden="true">↗</span></div>
          <p>{{ project.description }}</p>
        </a>
      {% endfor %}
    </div>
  </section>

  <section class="home-writing" aria-labelledby="home-writing-title">
    <div><h2 id="home-writing-title">Beyond the research.</h2><p>Technical articles and personal reflections.</p></div>
    <a class="home-text-link" href="{{ '/blog/' | relative_url }}">Visit the journal <span aria-hidden="true">↗</span></a>
  </section>

  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
