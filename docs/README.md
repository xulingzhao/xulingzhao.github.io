# Website maintenance

Start with [DESIGN.md](../DESIGN.md) for confirmed design and content decisions.

- [Local development and publishing](LOCAL_DEVELOPMENT.md)
- [Publications](PUBLICATIONS.md)
- [Adding an Exploration entry](#exploration)
- [Projects](PROJECTS.md)
- [Writing](WRITING.md)
- [Chinese and English fonts](FONTS.md)
- [Cleanup, storage, and recovery](CLEANUP.md)
- [Personal-style project and article references](site-reference/README.md)
- [Original project examples](project-examples/README.md)
- [Original article examples](writing-examples/README.md)
- [Bibliography field references](publication-examples/README.md)

The remaining technical guides, including [ARCHITECTURE.md](ARCHITECTURE.md), [BOUNDARIES.md](BOUNDARIES.md), and [CUSTOMIZE.md](CUSTOMIZE.md), are retained as upstream plugin documentation. Their generic starter examples and commands are not this site's current operating instructions; use the personal guides above first.

Everything under `docs/` is excluded from public website output. Notes currently has only an empty landing page; its content structure will be designed when real notes are available.

## Exploration

每个真实想法放在 `_explorations/` 中的一个 Markdown 文件里。用稳定、唯一的英文短名作为文件名，例如 `research-question.md`。文件头可以这样写。

```yaml
---
title: "你的研究问题"
date: 2026-11-23
status: Open Question
lang: zh-CN
---
```

填写实际标题和记录日期。`status` 取 `Set Aside`（已搁置）、`Open Question`（留下的问题）或 `Rediscovery`（重新发现）。正文直接用 Markdown 写想法和停下来的理由。重新发现已有工作时，可以在正文链接原论文，说明两条思路的交汇点。

栏目按状态分组，每组按日期倒序排列。读者在 `/exploration/` 点击标题即可展开正文。`research-question.md` 对应的页内地址为 `/exploration/#idea-research-question`。
