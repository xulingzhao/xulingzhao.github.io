---
layout: default
title: About
permalink: /
description: Xuling Zhao, an Artificial Intelligence undergraduate at Nanjing University, interested in optimization and diffusion language models.
---

<div class="academic-home">
  <a class="home-skip" href="#home-introduction">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home"><img src="{{ '/assets/img/favicon.png' | relative_url }}" alt="" width="40" height="40"></a>
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
      <h1 id="home-name">{{ site.first_name }} {{ site.last_name }}</h1>
      <p class="home-position">{{ site.data.home.introduction }}</p>
      <div class="home-biography">
        <p>{{ site.data.home.focus }}</p>
      </div>
      <dl class="home-contact" aria-label="Contact and profiles">
        <div>
          <dt>Email</dt>
          <dd><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></dd>
        </div>
        <div>
          <dt>GitHub</dt>
          <dd><a href="https://github.com/{{ site.data.socials.github_username }}">{{ site.data.socials.github_username }} <span aria-hidden="true">↗</span></a></dd>
        </div>
        {% if site.data.socials.openreview_id %}
        <div>
          <dt>OpenReview</dt>
          <dd><a href="https://openreview.net/profile?id={{ site.data.socials.openreview_id | url_encode }}">{{ site.first_name }} {{ site.last_name }} <span aria-hidden="true">↗</span></a></dd>
        </div>
        {% endif %}
      </dl>
    </div>
    <figure class="home-portrait">
      {% if site.data.home.portrait %}
        <img src="{{ site.data.home.portrait | relative_url }}" alt="Avatar of Xuling Zhao: a cartoon apple in a black suit" width="136" height="400" fetchpriority="high">
      {% else %}
        <div class="home-portrait-placeholder" role="img" aria-label="Portrait placeholder for Xuling Zhao"><span aria-hidden="true">XZ</span></div>
        <figcaption>Portrait forthcoming</figcaption>
      {% endif %}
    </figure>
  </section>

  <section class="home-section home-profile-section" aria-labelledby="home-education-title">
    <div class="home-section-heading"><h2 id="home-education-title">Education</h2></div>
    <div class="home-education-list">
      {% if site.data.home.education.size > 0 %}
        {% for entry in site.data.home.education %}
          <div class="home-education-entry">
            <h3>{{ entry.institution }}</h3>
            <p>{{ entry.degree }}</p>
            {% if entry.group %}<p class="home-education-group">{{ entry.group }}</p>{% endif %}
            {% if entry.interest %}<p class="home-education-interest"><span>Interest</span>{{ entry.interest }}</p>{% endif %}
            <p class="home-education-years">{{ entry.years }}</p>
          </div>
        {% endfor %}
      {% else %}
        <p>Details forthcoming.</p>
      {% endif %}
    </div>
  </section>

{% if site.data.home.awards.size > 0 %}
  <section class="home-section home-awards" aria-labelledby="home-awards-title">
    <div class="home-section-heading">
      <h2 id="home-awards-title">Honors &amp; Awards</h2>
    </div>
    <ul class="home-award-list">
      {% assign awards = site.data.home.awards | sort: 'year' | reverse %}
      {% for award in awards %}
        <li>
          <span class="home-award-year">{{ award.year }}</span>
          <div>
            <h3>{{ award.title }}{% if award.distinction %} · {{ award.distinction }}{% endif %}</h3>
            <p>{{ award.institution }}</p>
          </div>
        </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

{% if site.data.home.news.size > 0 %}
  <section class="home-section home-news" aria-labelledby="home-news-title">
    <div class="home-section-heading"><h2 id="home-news-title">News</h2></div>
    <ul class="home-news-list">
      {% assign news = site.data.home.news | sort: 'date' | reverse %}
      {% for item in news %}
        <li{% if forloop.first %} class="is-latest"{% endif %}>
          <time class="home-news-date" datetime="{{ item.date | date: '%Y-%m' }}">{{ item.date | date: '%b %Y' }}</time>
          <p>{{ item.text }}</p>
        </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
