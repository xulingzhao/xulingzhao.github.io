---
layout: default
title: Morning Paper
permalink: /projects/morning-paper/
description: A personal newspaper assembled from the sources you choose.
img: assets/img/projects/morning-paper.svg
importance: 2
category: personal
context: Self-initiated reading tool
role: Product concept & prototyping
timeline: An imagined weekend experiment
status: Fictional concept
hero_alt: Source cards assembled into a newspaper with a landscape image and article columns.
hero_caption: Concept illustration of a generated reading edition, with placeholder content.
next_project: /projects/campus-flow/
next_project_title: Campus Flow
---

{% capture project_body %}

## A small reading ritual

Morning Paper is an imagined personal tool for turning a scattered reading list into one quiet daily edition. Instead of opening a stream of tabs, the reader chooses a few feeds and saved links, then receives a finite page to read over coffee.

There is no client brief or competition deadline. This example starts with a personal question: could choosing what to read feel more deliberate, and a little more enjoyable?

## From sources to an edition

The proposed pipeline collects headlines and excerpts from chosen sources, merges duplicate links, and groups the result into a small set of topics. Every item keeps its source, date, and original link so that the reader can inspect the context.

The edition is designed as a reading aid, rather than a substitute for the original articles. A short selection of items, generous spacing, and a visible end make the experience feel closer to a newspaper than an endless feed.

1. **Choose the inputs.** Maintain a small list of feeds, saved links, and topics worth following.
2. **Assemble the edition.** Deduplicate entries and arrange brief, source-linked summaries into an editorial layout.
3. **Keep room for judgment.** Let the reader remove an item, adjust a topic, or save a link for another day before exporting.

## The proposed prototype

A first version would pair a feed parser with a lightweight page template and a print stylesheet. The intended output is a responsive reading page with a printable edition; the mockup above shows the direction, not a running service.

The most interesting experiment is editorial: how much should be automated, and where should a person stay in control? If generated summaries were added, they would need clear attribution and a way to compare them with the source.

## Reflection & next steps

This project is a place to explore information design and small-scale automation without committing to a large product. A next iteration would try a few reading sessions, note what gets skipped, and reduce the edition until each item earns its place.

There is no live demo or downloadable tool yet. This fictional case study serves as a starting structure for a future self-initiated project.

{% endcapture %}

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home project-detail-page">
  <a class="home-skip" href="#project-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home"><img src="{{ '/assets/img/favicon.png' | relative_url }}" alt="" width="40" height="40"></a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/projects/' | relative_url }}" aria-current="true">Projects</a>
      <a href="{{ '/blog/' | relative_url }}">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <article id="project-content" aria-labelledby="project-title">
    <header class="project-detail-introduction">
      <a class="home-text-link" href="{{ '/projects/' | relative_url }}#{{ page.category }}">← All {{ page.category }} projects</a>
      <p class="home-eyebrow">{{ page.category }} · Fictional case study</p>
      <h1 id="project-title">{{ page.title }}</h1>
      <p class="home-bio">{{ page.description }}</p>
      <p class="home-sample-note">An imagined project for this portfolio. The brief, process, and deliverables are illustrative.</p>
    </header>

    <dl class="project-facts">
      <div><dt>Context</dt><dd>{{ page.context }}</dd></div>
      <div><dt>Role</dt><dd>{{ page.role }}</dd></div>
      <div><dt>Timeline</dt><dd>{{ page.timeline }}</dd></div>
      <div><dt>Status</dt><dd>{{ page.status }}</dd></div>
    </dl>

    <figure class="project-cover">
      <img src="{{ page.img | relative_url }}" alt="{{ page.hero_alt }}" width="1280" height="800" fetchpriority="high">
      <figcaption>{{ page.hero_caption }}</figcaption>
    </figure>

    <div class="project-prose">{{ project_body | markdownify }}</div>

  </article>

  <nav class="project-detail-navigation" aria-label="More projects">
    <a class="home-text-link" href="{{ '/projects/' | relative_url }}">← All projects</a>
    <a class="home-text-link" href="{{ page.next_project | relative_url }}">{{ page.next_project_title }} <span aria-hidden="true">↗</span></a>
  </nav>
  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
