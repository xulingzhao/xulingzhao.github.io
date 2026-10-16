# 仓库清理与恢复

2026-10-15 清理基于已确认的五栏目个人网站，保持现有视觉样式与真实个人资料。

## 真正移除的内容

- 删除旧 CV、Teaching、People、Books、News、Repositories、Plugins、Dropdown 页面及 Einstein 备用简介；删除图书、课程、新闻集合和图书归档配置。
- 删除示例照片、论文预览、音视频、PDF、Notebook、Plotly/HTML 演示、CV 数据及模板专用数据。原模板文献移到本文档目录，不再参与文献索引。
- 删除模板截图、Lighthouse 报告、Docker 配置、模板发行/星标/CV/引文/截图机器人及依赖演示页面的上游测试。保留实际部署工作流、样式边界检查，增加本站的公开路由与链接检查。
- 清理旧本地构建副本、临时截图与日志、Jekyll 缓存，以及仅供演示 Notebook 使用的 `.venv/`，同时移除未使用的 Notebook 插件声明。

清理完成时的公开 HTML 只有首页、Publications、Projects、Writing、Notes、Writing 归档和 404，共七页。后续新增的真实文章或项目按实际进度扩展清单。`test/site-routes.json` 列出允许的地址；新增真实页面时明确更新。部署检查拒绝额外 HTML、泄漏的源码目录和失效站内资源链接。404 沿用当前字体和五项导航，不自动跳回首页。

这些是源码与本地构建的清理。正式网站须待用户确认、提交并推送 `main` 后，经过成功部署才会同步删除旧地址；仅本地删除不会修改线上网站。

## 特意保留的内容

- `docs/project-examples/` 九份项目、`docs/writing-examples/` 33 篇文章、`docs/site-reference/` 四份个人风格案例：用于未来写作，完全排除网站构建。
- 两个原创 SVG 示意图移到 `docs/site-reference/project-images/`；原案例源码保留原路径，复用时复制所需图片到公开 assets 并替换为真实内容。
- `docs/publication-examples/` 的两份 BibTeX：字段参考，不是个人论文。
- 技术架构与插件指南、锁定的 gems：保留未来图文、公式、引用等能力；没有为减小体积擅自升级或卸载运行组件。
- `vendor/` 是 Ruby 运行依赖，`node_modules/` 是格式与浏览器验证工具；删除后需要重装。
- `.bundle/github-xulingzhao.pub` 是本机 Git SSH 配置使用的公钥文件；不是临时截图，不能随缓存一起删除。
- `.git/` 保存版本历史。清理没有改写历史，旧文件仍可从 Git 找回，也不会让远端历史对象立即变小。
- 原代码 LICENSE 与字体 OFL 保留。

## 需要找回旧资源时

清理前基线提交为 `8361dfd`。例如把旧图片单独取到临时目录：

```bash
git show 8361dfd:assets/img/6.jpg > /tmp/al-folio-example-6.jpg
```

这不会恢复旧公开页面。需要实际使用时，只取所需文件，检查版权/来源，替换参考路径，再构建验证；不要整批恢复示例集合。

## 后续如何保持整洁

- 截图和临时生产构建放在 `.bundle/`，验证后删除对应文件或子目录；不要整体删除 `.bundle/`。
- `_site/` 与 `.jekyll-cache/` 可在停止本地预览后删除，下次运行会重建。
- 新媒体只加入当前真实内容所需的文件；参考资料继续放 `docs/`。
- 磁盘占用与运行内存不同：本次主要释放磁盘空间，不能把删去的文件大小理解为等量释放 RAM。
