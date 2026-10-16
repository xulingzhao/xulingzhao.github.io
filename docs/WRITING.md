# Writing 维护指南

网站文章可以使用英文、中文或中英文混排。这份中文指南只供维护时查阅，位于不参与网站生成的 `docs/` 目录。

## 当前页面

- `_pages/blog.md`：Writing 文章列表，保留按日期排序、精选开关和每页 5 篇的分页机制。
- `_pages/writing-archive.md`：统一风格的年份、标签和分类索引，地址是 `/blog/archive/`。
- `docs/site-reference/writing/2026-10-14-a-calmer-reading-list.md`：技术文章示例，包含代码、表格、引言和图片。
- `docs/site-reference/writing/2026-10-13-room-for-unfinished-ideas.md`：个人思考示例，包含段落、小标题、列表和引言。
- `assets/css/home.css`：Writing 列表、归档、文章详情，以及其他个人页面的共同样式。

两篇文章都明确标为虚构示例，不代表真实经历或已完成工作。它们使用与首页一致的五项导航。
当前首篇真实文章为《理解 KL 散度》（2026-10-15），源文件 `_posts/2026-10-15-understanding-kl-divergence.md`。两个虚构示例仅作参考，不生成网页；添加第六篇真实文章后，列表会生成下一页。总约定见 [DESIGN.md](../DESIGN.md)。
两篇均设置 `featured: false`，避免在很短的列表里重复展示；以后可把希望置顶的文章改为 `true`。

## 旧示例放在哪里

原来的 **33 篇文章源码完整保留**在 [writing-examples/](writing-examples/README.md)，逐文件核对过，与搬移前完全一致。
旧图片、视频、音频和 Notebook 已清理；文献归档到 `docs/publication-examples/`。归档不是独立运行站点，里面的 Liquid 标签与资源路径仍需放回这个项目环境才能执行。

模板的 Medium / Google Blog 配置也保存在 [external-sources.yml](writing-examples/external-sources.yml)。
站点的 `external_sources` 现在为空，避免示例文章再次混入 Writing。
以后填写自己的来源时，仍需确认抓取到的文章使用了正确布局；本地预览脚本默认不拉取外部来源。

原插件生成的年份、标签和分类页使用旧模板布局。现在文章链接统一指向 `/blog/archive/` 的对应分组，
并关闭了 `jekyll-archives.posts.enabled`，避免生成另一套旧风格页面。图书集合与旧图书归档已删除。

## 示例中真正有用的内容

完整的逐篇对应表在[示例索引](writing-examples/README.md)。复用时可以按目的查找：

| 想做什么       | 值得保留的写法                                                                                |
| -------------- | --------------------------------------------------------------------------------------------- |
| 普通文章       | Markdown 标题、段落、链接、有序和无序列表、任务列表、引用块。                                 |
| 展示代码       | 围栏代码块标注语言；`highlight` 可添加行号；嵌套列表内注意缩进。                              |
| 展示图片       | `thumbnail` 用于列表缩略图；`figure.liquid`、图片说明、拼图、缩放、轮播、前后对比和灯箱。     |
| 公式与图表     | 数学公式、Mermaid、TikZ、Typograms、Chart.js、ECharts、Vega-Lite、Plotly，以及 GeoJSON 地图。 |
| 可交互内容     | 表格搜索与排序、标签页、代码差异、伪代码、Jupyter Notebook 和 marimo。                        |
| 论文式文章     | 正文引用、参考文献、脚注、目录、作者信息；Distill 是一套单独的布局。                          |
| 媒体与外部服务 | 音视频组件、嵌入、评论，以及跳转到 PDF 或外部地址。                                           |

这些功能不需要一次全部启用。先用最普通的文章写清内容，再从原示例复制需要的一个组件。
旧示例是用法参考，不意味着其中的演示代码、远程链接或第三方服务可以直接用于真实项目。

## 如何新增文章

1. 从 `docs/site-reference/writing/` 复制最接近的参考文章到 `_posts/`，文件名使用 `YYYY-MM-DD-english-slug.md`。
2. 修改最上方两个 `---` 之间的配置。
3. 正文放在 `{% capture article_body %}` 和 `{% endcapture %}` 之间，支持 Markdown。
4. 保留后面的样式链接、页面外层、五项导航、正文渲染和页脚。
5. 本地打开 Writing → 文章 → 标签归档 → 返回 Writing，确认整条路径正常。

配置示例：

```yaml
layout: default
title: My New Essay
permalink: /blog/2026/my-new-essay/
date: 2026-10-14 00:00:00 +0800
description: One sentence about the article.
excerpt: One sentence about the article.
article_kind: Technical exploration
tags: [javascript, design]
categories: [technical]
featured: false
```

- `date` 决定排序和年份。日期在未来的文章默认不会显示；时区写 `+0800` 可避免时间理解不一致。
- `permalink` 必须唯一。更改已经对外分享的地址前，要考虑旧链接的去向。
- `excerpt` 明确填写一段短文字，避免自动摘要截断正文的 Liquid `capture` 区块。
- `article_kind` 是详情页的小标题，例如 `Technical exploration` 或 `Personal reflection`。
- `tags` 是主题，`categories` 是较宽的文章类别。新的值会自动出现在同风格的归档页。
- `featured: true` 会在 Writing 第一页的 Featured 区域出现。
- `thumbnail` 可以选填图片路径；有图片时同时填写 `cover_alt` 和 `cover_caption`。当前详情页自动判断是否显示封面。
- `next_article` 和 `next_article_title` 是文末另一篇文章的入口；没有合适文章时，删掉这两个字段即可。
- 不要填写 `redirect`，除非你确实希望读者离开文章详情页。

换成真实内容后，删掉文章中的虚构示例提示，更新正文链接与文末下一篇文章入口；Writing 列表页会自动从空状态切换到文章列表。

## 代码、表格和图片

两个新示例已经实际演示了这些常用写法。代码围栏使用三个反引号并注明语言，例如 `javascript`。
代码仍由 Rouge 渲染，但按当前设计要求，英文使用 Fraunces Italic，中文自动使用霞鹜文楷正体，文字统一为黑色。
代码保留空格和换行，手机上允许长行换行；如果未来想换成等宽字体，可以单独调整 `.writing-prose code` 的规则。

普通 Markdown 表格不需要打开交互表格开关。新文章的表格在小屏幕上可在自身区域横向滚动。
引用块使用 `>`。图片可参考新文章的可选封面，或在正文中加入普通 `<figure>`，也可以复用[项目指南中的拼图写法](PROJECTS.md#图片与图文拼排)。

## 需要额外接入的功能

新文章使用 `layout: default`，不再经过原来的 `post` 或 `distill` 布局。
因此，原 `post` 布局负责的内容不会仅因复制开关而自动出现：

| 原开关 / 功能                | 新文章中的处理                                                                                                        |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `toc.beginning`              | 原 `post` 布局的自动目录不再执行。简单文章可以直接添加指向小标题的链接；复杂目录需单独接入。                          |
| `related_publications: true` | 正文可以使用 `cite`，但文末文献列表需明确加入 bibliography 区域，写法见[项目指南](PROJECTS.md#引用评论和旧布局开关)。 |
| `citation: true`             | 文章自身的引用信息由旧布局插入，新页面需要明确接入 `citation.liquid` 并检查样式。                                     |
| `related_posts`              | 不自动插入原模板的推荐列表；当前用可编辑的 `next_article` 入口代替。                                                  |
| Giscus / Disqus              | 还需要自己的服务配置、插件和页面中的评论组件；参见[项目指南](PROJECTS.md#引用评论和旧布局开关)。                      |
| `layout: distill`            | 会重新使用 Distill 的布局和导航，不能只改一个开关就沿用当前详情风格。                                                 |
| `toc.sidebar`                | 会改变 `default` 布局的网格结构，可能压窄当前页面；需要针对该布局重新检查导航和宽度。                                 |

其他图表、代码、图片和数学功能由各 gem 的资源与开关控制。参考[架构说明](ARCHITECTURE.md#failure-modes-that-produce-no-error-message)，确认插件已加载、站点已启用、文章已选择所需功能。
第三方图表或评论组件可能有自己的字体和颜色，不能假定网站 CSS 会自动统一它们。

## 原示例恢复与依赖

需要参考某个示例时，优先复制其中的正文写法或组件，而不是把整篇旧文章重新放回展示列表。
例如 bibliography 示例用 `post_url` 引用了 Distill 示例；单独恢复它时，必须同步调整这个引用或恢复被引用的文章。
Jupyter 示例需要重新添加 `jekyll-jupyter-notebook`（同时更新 Gemfile 与配置），并安装 nbconvert；Twitter、远程视频和图表数据等依赖网络或外部服务。演示媒体和本地 nbconvert 环境已清理，见 [CLEANUP.md](CLEANUP.md)。需要 Notebook 时再安装 nbconvert，并验证所用远程服务。

修改 `_config.yml` 后，请停止并重新运行 `bash bin/serve-local`。正文修改通常会自动重建。

新增真实文章后，把 permalink（以及实际生成的分页地址）加入 `test/site-routes.json`，构建后运行输出检查。

## 中文与中英文混排

直接输入中文即可，标题、摘要、正文和代码中的中文会自动使用霞鹜文楷；英文仍使用 Fraunces Italic。无需逐字标记或安装电脑字体。以中文为主的文章在 front matter 添加 `lang: zh-CN`，并在正文容器上使用 `lang="{{ page.lang | default: site.lang }}"`，方便浏览器与辅助阅读工具识别语言。导航和首页介绍继续使用英文。字体来源和维护方式见 [FONTS.md](FONTS.md)。

## 数学文章的排版

《理解 KL 散度》可作为真实的中文数学文章参考。正文由 `article_body | markdownify` 渲染；行内数学使用 Kramdown 的 `$$...$$`，独立公式用单独成行的 `$$` 包围，以防 Markdown 吞掉 TeX 转义。数学字形交给 MathJax，不套用正文的强制字体规则。中文公式注释仍可使用文楷。

`.writing-math-page` 提供正文间距、标题层级、六节目录和手机公式局部滚动。目录目标使用显式 HTML 标题 id，避免格式化工具把 Kramdown 属性列表与标题分开。新增章节要同步目录；引用附录应链接到对应 id。

可显式设置 `reading_time`（分钟）以兼顾中文与公式阅读；列表会优先使用该值。纯英文文章不填写时仍沿用原估算。原稿未要求改写时，保留论点和公式，不擅自进行内容重写。
