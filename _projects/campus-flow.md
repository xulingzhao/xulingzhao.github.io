---
layout: default
title: Campus Flow
permalink: /projects/campus-flow/
description: A planning tool for clearer, more reliable campus shuttle journeys.
img: assets/img/projects/campus-flow.svg
importance: 1
category: applied
context: Campus mobility challenge
role: Research & interface design
timeline: An imagined six-week sprint
status: Fictional concept
hero_alt: A campus route map beside comparison charts, using illustrative data.
hero_caption: Concept illustration. Routes, charts, and locations are synthetic.
next_project: /projects/morning-paper/
next_project_title: Morning Paper
---

{% capture project_body %}

## The brief

In this imagined campus mobility challenge, a small research team is asked to help a facilities group compare shuttle routes before a new teaching building opens. The brief has three concrete deliverables: a repeatable comparison method, a working dashboard concept, and a short recommendation report.

The central question is simple: how can planners explain a route choice when a shorter journey for one group creates a longer wait for another?

## An approach built around trade-offs

The proposed workflow starts with a synthetic set of stops, class-change periods, and travel times. A baseline route gives every alternative a consistent point of comparison. Instead of hiding the decision in a single score, the interface separates walking distance, estimated waiting time, and service coverage.

My imagined contribution spans the scenario model and the interface: defining which assumptions a planner can change, sketching the comparison view, and making the reasoning behind each recommendation visible.

1. **Map the constraints.** Record stop locations, vehicle capacity, and the periods that need the most attention.
2. **Compare a few alternatives.** Place route options side by side, with the same inputs and explicit assumptions.
3. **Explain the decision.** Pair each recommendation with its trade-offs and the evidence that would be needed to validate it.

## Deliverables

The fictional handover consists of a scenario workbook, a dashboard prototype, and a decision memo. Together, they let a reviewer follow an input through to a recommendation, rather than relying on a polished final chart alone.

A real implementation would need observed travel times, accessibility requirements, and feedback from riders. The illustration above is a concept sketch; no operational results or measured improvements are claimed here.

## Reflection & next steps

The useful lesson in this example is that a project with a defined client or competition brief needs an understandable handover as much as an interesting model. The next step would be to test whether a planner can explain the difference between two routes without help from the project team.

{% endcapture %}

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home project-detail-page">
  <a class="home-skip" href="#project-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home">{{ site.data.home.wordmark }}</a>
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
