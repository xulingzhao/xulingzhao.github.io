---
layout: default
permalink: /blog/
title: Writing
description: Technical articles and personal reflections by Xuling Zhao.
nav: true
nav_order: 1
pagination:
  enabled: true
  collection: posts
  permalink: /page/:num/
  per_page: 5
  sort_field: date
  sort_reverse: true
  trail:
    before: 1 # The number of links before the current page
    after: 3 # The number of links after the current page
---

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home writing-page">
  <a class="home-skip" href="#writing-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home">{{ site.data.home.wordmark }}</a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/blog/' | relative_url }}" aria-current="page">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <section class="collection-introduction" id="writing-content" aria-labelledby="writing-title">
    <p class="home-eyebrow">Beyond the research</p>
    <h1 id="writing-title">Writing</h1>
    {% if site.posts.size > 0 %}<p class="home-bio">Technical articles and personal reflections.</p>{% endif %}
  </section>

{% if site.posts.size > 0 %}
{% assign featured_posts = site.posts | where: 'featured', true %}
{% assign current_page = paginator.page | default: 1 %}
{% if current_page == 1 and featured_posts.size > 0 %}
    <section class="writing-featured" aria-labelledby="featured-title">
      <h2 id="featured-title">Featured</h2>
      <div class="writing-featured-grid">
        {% for post in featured_posts %}
          {% assign post_link = post.url | relative_url %}
          {% if post.redirect contains '://' %}
            {% assign post_link = post.redirect %}
          {% elsif post.redirect != blank %}
            {% assign post_link = post.redirect | relative_url %}
          {% endif %}
          <a class="writing-feature" href="{{ post_link }}">
            <h3>{{ post.title }} <span aria-hidden="true">↗</span></h3>
            <p>{{ post.description }}</p>
          </a>
        {% endfor %}
      </div>
    </section>
{% endif %}

  <section class="writing-archive" aria-labelledby="articles-title">
    <div class="home-section-heading">
      <h2 id="articles-title">Articles</h2>
      <a class="home-text-link" href="{{ '/blog/archive/' | relative_url }}">Browse the archive <span aria-hidden="true">↗</span></a>
    </div>
    {% if page.pagination.enabled %}
      {% assign postlist = paginator.posts %}
    {% else %}
      {% assign postlist = site.posts %}
    {% endif %}
    <ul class="writing-list">
      {% for post in postlist %}
        {% assign post_link = post.url | relative_url %}
        {% if post.redirect contains '://' %}
          {% assign post_link = post.redirect %}
        {% elsif post.redirect != blank %}
          {% assign post_link = post.redirect | relative_url %}
        {% endif %}
        {% if post.external_source == blank %}
          {% assign read_time = post.content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
        {% else %}
          {% assign read_time = post.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
        {% endif %}
        {% assign year = post.date | date: '%Y' %}
        <li>
          <article class="writing-article{% if post.thumbnail %} has-thumbnail{% endif %}">
            <div class="writing-article-copy">
              <p class="writing-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%B %-d, %Y' }}</time><span aria-hidden="true"> · </span>{{ read_time }} min read{% if post.external_source %}<span aria-hidden="true"> · </span>{{ post.external_source }}{% endif %}</p>
              <h3><a href="{{ post_link }}">{{ post.title }} <span aria-hidden="true">↗</span></a></h3>
              <p class="writing-description">{{ post.description }}</p>
              <div class="writing-tags">
                <a href="{{ '/blog/archive/' | relative_url }}#year-{{ year }}">{{ year }}</a>
                {% for tag in post.tags %}
                  <a href="{{ '/blog/archive/' | relative_url }}#tag-{{ tag | slugify }}">#{{ tag }}</a>
                {% endfor %}
                {% for category in post.categories %}
                  <a href="{{ '/blog/archive/' | relative_url }}#category-{{ category | slugify }}">{{ category }}</a>
                {% endfor %}
              </div>
            </div>
            {% if post.thumbnail %}
              <a class="writing-thumbnail" href="{{ post_link }}" aria-label="Read {{ post.title | escape }}"><img src="{{ post.thumbnail | relative_url }}" alt="" width="320" height="240" loading="lazy"></a>
            {% endif %}
          </article>
        </li>
      {% else %}
        <li class="writing-empty">Articles will appear here.</li>
      {% endfor %}
    </ul>
  </section>

{% if page.pagination.enabled and paginator.total_pages > 1 %}
    <nav class="writing-pagination" aria-label="Writing pages">
      <div>{% if paginator.previous_page %}<a href="{{ paginator.previous_page_path | relative_url }}" rel="prev">← Previous</a>{% endif %}</div>
      <span>Page {{ paginator.page }} of {{ paginator.total_pages }}</span>
      <div>{% if paginator.next_page %}<a href="{{ paginator.next_page_path | relative_url }}" rel="next">Next →</a>{% endif %}</div>
    </nav>
{% endif %}

{% else %}
  <section class="collection-empty" aria-label="Writing status"><p>No articles yet.</p></section>
{% endif %}

  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
