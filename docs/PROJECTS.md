# 项目维护指南

网站中的项目内容使用英文。这份指南供你维护网站时查阅，不会出现在公开网站里。

当前没有真实项目，列表与首页显示 “No projects yet.”。下面两个虚构案例仅作为未来写作和详情排版参考，已移出展示集合。总约定见 [DESIGN.md](../DESIGN.md)。

## 现在的结构

- `_pages/projects.md`：Projects 列表，按 Applied / Personal 分类。
- `docs/site-reference/projects/campus-flow.md`：Applied 虚构案例，展示有明确目标和交付要求的项目。
- `docs/site-reference/projects/morning-paper.md`：Personal 虚构案例，展示自己发起的工具和探索。
- `assets/css/home.css`：首页、列表页和新项目详情页共用的风格。
- `docs/site-reference/project-images/`：两个案例的原创 SVG 示意图（不公开发布）。它们不是运行截图或实测结果。
- [project-examples/](project-examples/)：原先 project 1–9 的完整源码，已从展示集合移出；旧演示媒体已清理，恢复说明见 [CLEANUP.md](CLEANUP.md)。

`docs/` 已在 `_config.yml` 的 `exclude` 中，因此这些参考资料不会生成网站页面，也不会进入项目卡片或搜索索引。
两个案例均明确标为虚构，没有真实合作方、成绩、用户数据或已上线产品的含义。

## 如何选择分类

| 分类                  | 放什么                                             | 例子                                    |
| --------------------- | -------------------------------------------------- | --------------------------------------- |
| `applied` → Applied   | 比赛、课题组、企业合作等有明确目标和交付要求的项目 | 竞赛解决方案、组内大型项目、横向课题    |
| `personal` → Personal | 自己发起的工具、创意作品和技术探索                 | 个人报纸生成器、ASMR 生成工具、动态名片 |

分类表达项目的发起方式和约束，不代表技术难度或完成程度。

## 原来的九个示例，哪些内容值得保留

九份正文实际只有两种：project 1、7 多了正文引用；其余七份的正文相同。它们不是九种完全不同的项目架构。

| 原文件                                     | 主要差异与参考价值                                                                       |
| ------------------------------------------ | ---------------------------------------------------------------------------------------- |
| [project 1](project-examples/1_project.md) | 有封面图；正文使用 `cite`；`related_publications: true` 让旧 `page` 布局在文末列出引用。 |
| [project 2](project-examples/2_project.md) | 有封面图；`giscus_comments: true` 是评论的页面开关。                                     |
| [project 3](project-examples/3_project.md) | 长标题、封面图、`redirect` 外部链接；卡片可直接离开本站，旧详情页也会延时跳转。          |
| [project 4](project-examples/4_project.md) | `img` 留空：不提供封面图。新列表已用项目名占位图处理这种情况。                           |
| [project 5](project-examples/5_project.md) | 普通有图项目，主要用来参考图文编排。                                                     |
| [project 6](project-examples/6_project.md) | 另一份无封面项目，与 project 4 的展示机制相同。                                          |
| [project 7](project-examples/7_project.md) | 与 project 1 相同的引用用法，换了封面和排序值。                                          |
| [project 8](project-examples/8_project.md) | 与 project 2 相同的评论用法，换了封面。                                                  |
| [project 9](project-examples/9_project.md) | 普通有图项目，换了封面、说明和排序值。                                                   |

所有示例都演示了三张等宽图片、单张全宽图片、2/3 + 1/3 图片，以及图片说明、图片间插入正文和代码示例。
`figure.liquid` 是 gem 提供的图片组件；原例中 `img-fluid`、`col-sm-*` 等类来自 Bootstrap 兼容层。
归档保留了搬移时的完整内容，包括此前已改成 `applied` / `personal` 的分类。

## 添加一个真正的项目

1. 从 `docs/site-reference/projects/` 复制最接近的案例到 `_projects/`（目录不存在时先创建），例如复制为 `_projects/my-project.md`。
2. 修改文件最上方两个 `---` 之间的配置，并修改正文。
3. 把项目图片放进 `assets/img/projects/`，更新图片路径和说明。
4. 保留样式链接、`.academic-home` 外层、导航和页脚，这样点击进入后仍沿用首页风格。
5. 在本地检查列表 → 详情 → 返回列表的完整路径，并把窗口缩窄检查手机布局。

最常用的配置：

```yaml
layout: default
title: My Project
permalink: /projects/my-project/
description: A short English description of the project.
img: assets/img/projects/my-project.jpg
importance: 3
category: applied
context: Research collaboration
role: Interface design and implementation
timeline: March–June 2026
status: In progress
hero_alt: Describe what the image shows.
hero_caption: Explain the image and its source if needed.
next_project: /projects/morning-paper/
next_project_title: Morning Paper
```

- `permalink` 必须唯一，建议用小写英文和连字符。它决定详情页地址，与文件名可以不同。
- `importance` 越小，越靠前；相同值的顺序不应依赖。首页当前展示前两个有封面的项目。
- `img` 控制列表封面；详情页也通过 `page.img` 使用它。无封面时，列表会自动出现文字占位图；同时删掉详情页的 `<figure class="project-cover">…</figure>`，避免空图片。
- `next_project` / `next_project_title` 控制底部另一项目的入口。没有合适项目时，可以删掉对应的第二个链接，保留 All projects。
- 完成真实替换后，删除详情页的虚构提示，并检查所有信息、图片说明与相关链接均对应真实项目；列表与首页会自动切换为空状态或实际内容。
- `github` 可以选填真实仓库网址，列表会出现 View code。不要为尚不存在的成果添加下载或演示链接。
- 想保留站内详情页时，不要设置 `redirect`。它的用途是跳过详情页前往另一个地址。

正文写在文件前部的 `{% capture project_body %}` 和 `{% endcapture %}` 之间，可直接使用 Markdown 标题、段落、列表和链接。页面通过 `markdownify` 把这段正文渲染到内容区域，避免 Markdown 与 HTML 缩进互相干扰。
两个现有案例已经提供“背景 → 方法 → 交付或原型 → 反思”的结构，你可以自由调整。

## 图片与图文拼排

一张带说明的图片，可以放在正文里：

```html
<figure class="project-cover">
  <img src="{{ '/assets/img/projects/my-project.jpg' | relative_url }}" alt="A meaningful description" loading="lazy" />
  <figcaption>A short caption.</figcaption>
</figure>
```

沿用新样式的 2/3 + 1/3 拼图：

```html
<div class="project-gallery">
  <figure class="project-gallery-wide">
    <img src="{{ '/assets/img/projects/main-view.jpg' | relative_url }}" alt="First image" loading="lazy" />
    <figcaption>The main view.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/projects/detail-view.jpg' | relative_url }}" alt="Second image" loading="lazy" />
    <figcaption>A closer detail.</figcaption>
  </figure>
</div>
```

三张等宽图片：使用三个普通 `<figure>`，不要加 `project-gallery-wide`。
手机上自动变为单列。原图颜色保留，不应用灰度滤镜。
需要原模板的响应式图片处理时，可以参考归档示例中的 `{% include figure.liquid ... %}` 写法，继续使用 gem 提供的组件。

## 引用、评论和旧布局开关

新案例使用 `layout: default` 并自行组织正文，不再套用旧的 `page` 布局。
因此，**只复制 `related_publications: true` 或 `giscus_comments: true` 并不会自动添加相关区域**。

引用可继续使用已有的 Jekyll Scholar 功能，例如正文中的 `{% cite reference-key --file references %}`。
要显示文末参考文献，需要在详情页中明确加入以下内容；他人的参考文献放在 `_bibliography/references.bib`，与自己的 `publications.bib` 分开。

```html
<section class="home-publications publications" aria-labelledby="project-references">
  <h2 id="project-references">References</h2>
  {% bibliography --file references --cited_in_order %}
</section>
```

如果以后需要评论，先配置自己的 Giscus 仓库信息，并按[架构说明](ARCHITECTURE.md#failure-modes-that-produce-no-error-message)确认插件和开关，再在详情页所需位置接入：

```liquid
{% if site.plugins contains 'al_comments' %}
  {% include plugins/al_comments.liquid %}
{% endif %}
```

页面还需要 `giscus_comments: true`。评论服务有独立样式，不会仅靠 Fraunces 页面 CSS 就完全统一；当前两个示例不启用评论。

以后新增项目，优先复制这两个新案例。`docs/project-examples/` 中的原版归档用于参考功能写法；直接搬回 `_projects/` 会恢复旧布局、旧导航，以及示例中可能存在的跳转行为。

新增真实详情页后，把它的 permalink 加入 `test/site-routes.json`，构建后运行输出检查。归档示意图如确需使用，应复制到 `assets/img/projects/` 并更新说明；原案例中的资源路径不会自动恢复。
