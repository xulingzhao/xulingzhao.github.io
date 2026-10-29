---
layout: default
title: Writing archive
permalink: /blog/archive/
description: Browse writing by year, topic, and category.
---

<div class="academic-home writing-page writing-archive-page">
  <a class="home-skip" href="#archive-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home"><img src="{{ '/assets/img/favicon.png' | relative_url }}" alt="" width="40" height="40"></a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/blog/' | relative_url }}" aria-current="true">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <section class="writing-detail-introduction" id="archive-content" aria-labelledby="archive-title">
    <a class="home-text-link" href="{{ '/blog/' | relative_url }}">← All writing</a>
    <p class="home-eyebrow">The collection</p>
    <h1 id="archive-title">Writing archive</h1>
    {% if site.posts.size > 0 %}<p class="home-bio">Browse by year, topic, or category.</p>{% endif %}
  </section>

{% if site.posts.size > 0 %}
{% assign years = site.posts | group_by_exp: 'post', 'post.date | date: "%Y"' %}
{% assign sorted_tags = site.tags | sort %}
{% assign sorted_categories = site.categories | sort %}
{% assign archive_types = 'Year,Topic,Category' | split: ',' %}
{% for type in archive_types %}
    {% case type %}
      {% when 'Year' %}{% assign groups = years %}{% assign prefix = 'year' %}
      {% when 'Topic' %}{% assign groups = sorted_tags %}{% assign prefix = 'tag' %}
      {% when 'Category' %}{% assign groups = sorted_categories %}{% assign prefix = 'category' %}
    {% endcase %}
    <section class="writing-archive-group" aria-labelledby="archive-{{ prefix }}">
      <h2 id="archive-{{ prefix }}">By {{ type | downcase }}</h2>
      {% for group in groups %}
        {% if type == 'Year' %}
          {% assign group_name = group.name %}{% assign grouped_posts = group.items %}
        {% else %}
          {% assign group_name = group[0] %}{% assign grouped_posts = group[1] %}
        {% endif %}
        <section class="writing-archive-subgroup" aria-labelledby="{{ prefix }}-{{ group_name | slugify }}">
          <h3 id="{{ prefix }}-{{ group_name | slugify }}">{{ group_name | replace: '-', ' ' | capitalize }}</h3>
          <ul>
            {% for post in grouped_posts %}
              {% assign post_link = post.url | relative_url %}
              {% if post.redirect contains '://' %}{% assign post_link = post.redirect %}
              {% elsif post.redirect != blank %}{% assign post_link = post.redirect | relative_url %}{% endif %}
              <li><a href="{{ post_link }}">{{ post.title }}</a><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%b %-d, %Y' }}</time></li>
            {% endfor %}
          </ul>
        </section>
      {% endfor %}
    </section>
{% endfor %}
{% else %}
  <section class="collection-empty" aria-label="Writing status"><p>No articles yet.</p></section>
{% endif %}
  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
