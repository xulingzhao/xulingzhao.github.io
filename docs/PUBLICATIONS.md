# Publications 维护指南

当前没有个人论文。首页与 Publications 页面显示 “No publications yet.”，没有论文时不显示搜索框。

自己的论文添加到 `_bibliography/publications.bib`。两个页面都会自动读取这个文件；添加首篇 BibTeX 条目后，论文列表会自动出现，首页展示最多两篇。年份分组、图片、摘要与相关链接沿用现有样式和 Jekyll Scholar 配置。

原模板的文献保留在 `docs/publication-examples/papers.bib`，仅用于参考字段写法，完全排除构建；Distill 示例文献另存为同目录的 `distill.bib`。不要把模板条目复制到个人文献文件中充当自己的成果。

不要把他人的参考文献写入个人论文文件；如需正文引用，可新建 `_bibliography/references.bib` 并在引用和文献列表中显式指定。

以后添加论文时，填写真实标题、作者、年份和发表信息；`preview` 可填写 `assets/img/publication_preview/` 中的图片文件名。`pdf`、`html`、`code` 等链接只填写实际存在的资源。
