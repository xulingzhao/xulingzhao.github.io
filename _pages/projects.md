---
layout: default
title: Projects
permalink: /projects/
description: Projects and explorations by Xuling Zhao.
nav: true
nav_order: 3
display_categories: [applied, personal]
---

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home projects-page">
  <a class="home-skip" href="#projects-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Xuling Zhao, home">xz.</a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/projects/' | relative_url }}" aria-current="page">Projects</a>
      <a href="{{ '/blog/' | relative_url }}">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <section class="projects-introduction" id="projects-content" aria-labelledby="projects-title">
    <p class="home-eyebrow">Ideas in practice</p>
    <h1 id="projects-title">Projects</h1>
    <p class="home-bio">A space for making and exploring.</p>
    <p class="home-sample-note">Template examples below; personal projects forthcoming.</p>
  </section>

{% assign project_categories = 'All projects' | split: ',' %}
{% if site.enable_project_categories and page.display_categories %}
    {% assign project_categories = page.display_categories %}
{% endif %}
{% for category in project_categories %}
    {% assign sorted_projects = site.projects | sort: 'importance' %}
    {% if site.enable_project_categories and page.display_categories %}
      {% assign sorted_projects = sorted_projects | where: 'category', category %}
    {% endif %}
    {% if sorted_projects.size > 0 %}
      <section class="projects-category" aria-labelledby="{{ category | slugify }}">
        <h2 id="{{ category | slugify }}"><a href="#{{ category | slugify }}">{{ category | capitalize }}</a></h2>
        <div class="home-project-grid">
          {% for project in sorted_projects %}
            <article class="projects-entry">
              <a class="home-project" href="{% if project.redirect %}{{ project.redirect }}{% else %}{{ project.url | relative_url }}{% endif %}">
                {% if project.img %}
                  <div class="home-project-image"><img src="{{ project.img | relative_url }}" alt="" loading="lazy" width="640" height="400"></div>
                {% else %}
                  <div class="home-project-image projects-placeholder" aria-hidden="true"><span>{{ project.title | capitalize }}</span></div>
                {% endif %}
                <div class="home-project-heading"><h3>{{ project.title | capitalize }}</h3><span aria-hidden="true">↗</span></div>
                <p>{{ project.description }}</p>
              </a>
              {% if project.github %}
                <a class="home-text-link projects-code" href="{{ project.github }}">View code <span aria-hidden="true">↗</span></a>
              {% endif %}
            </article>
          {% endfor %}
        </div>
      </section>
    {% endif %}
{% endfor %}

  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
