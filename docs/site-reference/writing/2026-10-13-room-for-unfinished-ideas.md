---
layout: default
title: Room for unfinished ideas
permalink: /blog/2026/room-for-unfinished-ideas/
date: 2026-10-13 00:00:00 +0800
description: On keeping a small space for curiosity before it becomes a project.
excerpt: On keeping a small space for curiosity before it becomes a project.
article_kind: Personal reflection
tags: [creativity, learning]
categories: [reflections]
featured: false
next_article: /blog/2026/a-calmer-reading-list/
next_article_title: A calmer reading list
---

{% capture article_body %}

## Before the project has a name

Imagine a notebook filled with small observations: an interface that asks one question too many, a sound that makes a room feel calmer, a sentence that could become the beginning of an essay. None of these is a project yet. They are simply things worth noticing.

It is tempting to give every idea a title, a deadline, and a list of features. That can be helpful when work has a clear purpose. But I would like a different space for the ideas whose purpose is still taking shape.

## A note can be enough

In this imagined practice, an idea begins as a short note with three parts: what caught my attention, why it matters to me, and one small thing I could try. The next step might be a sketch, a paragraph, or a tiny program. It does not need to become a product.

- **Notice something specific.** A concrete observation is easier to return to than a vague ambition.
- **Keep the question open.** Write down what is uncertain before choosing a solution.
- **Try something small.** Make the next experiment short enough that curiosity can carry it.

This would not replace a plan for an applied project with real responsibilities. It would sit beside that work: a place where uncertainty is part of the reason to begin.

## Let the page have an end

I like the idea of a reading list or notebook that eventually says, “That is enough for today.” A finite page makes choosing part of the experience. The things left out can wait without disappearing.

> An unfinished idea can remain useful without becoming an obligation.

The same principle could shape a personal website. A few carefully chosen projects can say more than a crowded collection of every experiment. A short reflection can be worth sharing even when it does not end with a lesson.

## A possible ritual

If I were to test this practice, I would reserve a brief weekly session for revisiting a few notes. I would choose one to develop, let some rest, and remove the ones that no longer feel interesting. The aim would be to protect attention, not to measure productivity.

A future version of [Morning Paper]({{ '/projects/morning-paper/' | relative_url }}) could leave room for one such note beside the day's reading. That possibility is still only a sketch, which is an appropriate place for this essay to end.

{% endcapture %}

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home writing-detail-page">
  <a class="home-skip" href="#article-content">Skip to content</a>
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

  <article id="article-content" aria-labelledby="article-title">
    <header class="writing-detail-introduction">
      <a class="home-text-link" href="{{ '/blog/' | relative_url }}">← All writing</a>
      <p class="home-eyebrow">{{ page.article_kind }} · Illustrative essay</p>
      <h1 id="article-title">{{ page.title }}</h1>
      <p class="home-bio">{{ page.description }}</p>
      {% assign read_time = article_body | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
      <p class="writing-meta"><time datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date: '%B %-d, %Y' }}</time> · {{ read_time }} min read</p>
      <p class="home-sample-note">A fictional sample written for this portfolio, not a record of personal experience or completed work.</p>
    </header>

    {% if page.thumbnail %}
      <figure class="writing-cover">
        <img src="{{ page.thumbnail | relative_url }}" alt="{{ page.cover_alt | escape }}" width="1280" height="800" fetchpriority="high">
        <figcaption>{{ page.cover_caption }}</figcaption>
      </figure>
    {% endif %}

    <div class="writing-prose">{{ article_body | markdownify }}</div>

    <div class="writing-tags writing-detail-tags" aria-label="Article topics">
      {% assign year = page.date | date: '%Y' %}
      <a href="{{ '/blog/archive/' | relative_url }}#year-{{ year }}">{{ year }}</a>
      {% for tag in page.tags %}<a href="{{ '/blog/archive/' | relative_url }}#tag-{{ tag | slugify }}">#{{ tag }}</a>{% endfor %}
      {% for category in page.categories %}<a href="{{ '/blog/archive/' | relative_url }}#category-{{ category | slugify }}">{{ category }}</a>{% endfor %}
    </div>

  </article>

  <nav class="writing-detail-navigation" aria-label="More writing">
    <a class="home-text-link" href="{{ '/blog/' | relative_url }}">← All writing</a>
    {% if page.next_article %}<a class="home-text-link" href="{{ page.next_article | relative_url }}">{{ page.next_article_title }} <span aria-hidden="true">↗</span></a>{% endif %}
  </nav>
  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
