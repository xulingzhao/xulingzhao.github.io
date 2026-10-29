---
layout: default
title: A calmer reading list
permalink: /blog/2026/a-calmer-reading-list/
date: 2026-10-14 00:00:00 +0800
description: A small deduplication rule for a more deliberate daily edition.
excerpt: A small deduplication rule for a more deliberate daily edition.
article_kind: Technical exploration
tags: [javascript, information-design]
categories: [technical]
featured: false
thumbnail: assets/img/projects/morning-paper.svg
cover_alt: Source cards assembled into a newspaper with a landscape illustration.
cover_caption: An illustration from the fictional Morning Paper concept, not a product screenshot.
next_article: /blog/2026/room-for-unfinished-ideas/
next_article_title: Room for unfinished ideas
---

{% capture article_body %}

## Start with a rule you can explain

Imagine collecting five links for a morning reading edition. Two feeds recommend the same article, while another source uses a similar headline for a completely different piece. Before choosing a ranking model or building a new interface, there is a smaller question to answer: what counts as a duplicate?

For a first prototype, I would use exact URL equality after trimming surrounding whitespace. This is deliberately limited. It is easy to inspect, it preserves input order, and it does not merge different articles simply because their titles resemble each other.

## A small implementation

The following function assumes that every item has a string `url` field. It keeps the first occurrence of each trimmed URL and leaves the original items unchanged.

```javascript
function uniqueByUrl(items) {
  const seen = new Set();

  return items.filter((item) => {
    const key = item.url.trim();
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}
```

A short example makes the rule visible:

```javascript
const items = [
  { title: "A quiet interface", url: "/notes/quiet" },
  { title: "The same article", url: " /notes/quiet " },
  { title: "A quiet interface", url: "/notes/another" },
];

uniqueByUrl(items).map((item) => item.url);
// ["/notes/quiet", "/notes/another"]
```

The second entry disappears because its trimmed URL matches the first. The third remains, even though its title is identical to the first title. The identity rule is about links, not wording.

## The boundaries matter

| Situation                    | Result under this rule |
| ---------------------------- | ---------------------- |
| The same URL appears twice   | Keep the first item    |
| Different URLs share a title | Keep both items        |
| A query parameter differs    | Keep both items        |
| The input is empty           | Return an empty list   |

This function does not resolve redirects, remove tracking parameters, validate addresses, or check whether a page exists. Adding those behaviors would change the rule. In particular, removing query parameters without understanding their meaning could merge distinct resources.

> A useful first version makes its assumptions easy to find.

## What I would try next

For the fictional [Morning Paper project]({{ '/projects/morning-paper/' | relative_url }}), I would display a small preview of removed duplicates before generating an edition. That would make an automatic step inspectable without asking the reader to manage every item manually.

Only after observing real duplicate patterns would I add more normalization. The value of this first step is not sophistication; it is a clear behavior that a reader or future maintainer can predict.

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
