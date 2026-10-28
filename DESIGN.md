# Xuling Zhao / leo — 网站设计与维护约定

最后更新：2026-10-28。本文记录用户已确认的选择和当前实际进度，是本个人网站后续工作的第一阅读入口。网站界面和个人介绍保持英文，博客允许中文及中英文混排；维护文档与协作沟通可用中文。

## 接手时先做什么

1. 阅读本文件和 `AGENTS.md`，检查当前分支、`git status` 与实际配置。目标开发分支为 `redesign`，保留已有未提交修改。
2. 根据本次任务阅读下方链接的栏目指南与参考源码。不要重新讨论已经确定的字体、配色、导航等选择，除非用户提出改变。
3. 用户的新指示优先；修改完成后，把新确认的选择、实际进度和参考文件位置更新到本文。详细操作只维护在对应指南里，本文提供入口。
4. 日常开发继续使用 `redesign`；`main` 用于已确认的正式版本。用户已授权本次满意版本推送并进入 `main`。以后 Git 提交、推送与发布按用户本次任务的授权范围执行，不把一次发布视为后续自动发布许可。

## 已确认的视觉风格

- 简约、克制、专业，有艺术感；用户喜欢 Apple 风格的干净布局。保持清晰层级与留白，避免装饰堆积、拥挤卡片和彩色文字。
- **英文继续使用 Fraunces Italic，中文使用霞鹜文楷正体**，覆盖标题、正文和代码中的相应字符。英文不替换为系统字体。Fraunces 文件为 `assets/fonts/fraunces-italic.ttf`，CSS 名称为 `Fraunces Home`；霞鹜文楷使用 `assets/fonts/lxgw-wenkai/` 中自托管的常规字重 WOFF2 分包，版本与许可见 [字体说明](docs/FONTS.md)。按字符自动回退，禁止浏览器将中文合成为斜体，不需要逐字添加 span。
- 白色背景、黑色文字与链接；使用浅灰分隔线及必要的浅灰底。**图片保持原始颜色，不做全站灰度处理。**
- 唯一点缀色为头像的苹果红 `#c82d28`（CSS 变量 `--home-accent`），只用于非文字元素：最新一条 News 左侧留白中的小红点、文章页顶部 2px 阅读进度条、选中文字的浅红底。文字和链接仍为黑色，不扩大使用范围。
- 动效克制：首屏内容加载时依次上浮淡入；下方区块滚动进入视口时淡入（支持 `animation-timeline` 的浏览器，前 140px 内完成，避免停在半透明）；链接下划线自左向右划出；悬停头像时以脚为轴轻摆。`prefers-reduced-motion` 时全部关闭。
- 左上角标识为小写 **leo**，无句点；由 `_data/home.yml` 的 `wordmark` 控制。大标题和学术署名仍为 **Xuling Zhao**，不要自行改成 Leo Zhao。
- 浏览器图标为苹果 emoji **🍎**。保留当前 favicon 设置。
- 内容居中，当前容器最大宽度 1080px（含左右内边距）；以 `assets/css/home.css` 的实际实现为准。沿用已确认的标题比例、细分隔线与桌面/手机排版，不随意更换设计体系。
- 首屏突出姓名，身份使用自然的一句英文，不再拆成生硬的身份与学校两行。避免重复的 “I am… I am… I will…” 或重复身份段落。
- Email、GitHub、OpenReview 各占一行，并各自带标签；OpenReview 显示姓名而非带数字的 ID。CV 等用户做好 PDF 后再加。
- 首页各节保持单栏、标题在上：用户试看过“左标题右内容”的两栏排版，认为不协调，已撤回，不要再改成两栏。区块标题、学校、专业、日期有明确字号层级。
- 不再设单独的 Research interests 区块：研究方向写在 Education 对应学校下，以小号大写 “INTEREST” 标签引出，不添加 “Currently exploring” 等多余说明。
- Honors & Awards 保留独立、可扩展的完整区块，不因目前只有两条就缩成小角落。
- 首页顺序：简介 → Education → Honors & Awards → News。News 与奖项共用“日期列 + 内容”网格（桌面 90px、手机 64px），两节正文左缘对齐；News 按日期倒序，显示月份与年份。
- 首页暂不放 Publications / Projects / Writing 导引，避免喧宾夺主；等有几个代表项目后再考虑恢复。导航仍保留五项。
- 头像使用用户提供的卡通形象（红苹果穿黑西装），必须是全身像，不要裁成半身。已去除灰色背景，文件为透明 WebP `assets/img/avatar.webp`（286 × 840，约 26 KB），直接站在白底上，不加框；桌面高 400px、手机高 200px。原图背景色 `#6b625c`。社交分享卡片另用正方形完整图 `assets/img/og-avatar.jpg`（600 × 600）。它与 leo 页首标识用途不同；不要擅自生成或替换为他人照片。

## 栏目结构与内容边界

始终使用五项导航，顺序为 **About / Publications / Projects / Writing / Notes**。列表、详情、标签和归档页保持同一字体、导航与视觉风格；不要让点击详情后恢复旧模板的 CV、Teaching 等导航。

| 栏目         | 地址             | 内容与当前状态                                                                                                |
| ------------ | ---------------- | ------------------------------------------------------------------------------------------------------------- |
| About        | `/`              | 已填写简介、头像、教育（含研究方向）、奖项、News、联系方式；暂不放论文、项目和 Writing 导引（通过导航进入）。 |
| Publications | `/publications/` | 当前没有论文，显示 “No publications yet.”；没有论文时隐藏搜索框。                                             |
| Projects     | `/projects/`     | 当前没有可展示的真实项目，显示 “No projects yet.”；未来沿用 Applied / Personal 分类与图文详情。               |
| Writing      | `/blog/`         | 已有《理解 KL 散度》（2026-10-15）；收录技术文章和个人想法。                                                  |
| Notes        | `/notes/`        | 当前没有笔记，显示 “No notes yet.”；未来收录课程、阅读和学习笔记。                                            |

空状态保留栏目标题、简短英文提示、导航与页脚，不放模板卡片、虚构成果、空分类列表或无用途的搜索。Writing 的 `/blog/archive/` 使用同风格实现，已有文章时显示真实年份、标签与分类。

Projects 分类是已经确定的内容约定，空栏目时不必显示分类：

| 分类                  | 收录范围                                           | 用户给出的例子                          |
| --------------------- | -------------------------------------------------- | --------------------------------------- |
| Applied (`applied`)   | 比赛、课题组、企业合作等有明确目标和交付要求的项目 | 竞赛解决方案、组内大型项目、横向课题    |
| Personal (`personal`) | 自己发起的工具、创意作品和技术探索                 | 个人报纸生成器、ASMR 生成工具、动态名片 |

保留 al-folio 多页面、论文功能与项目图文展示能力。等用户提供真实信息后，参考归档结构编写；不要把示例当成用户的经历，不编造作者、结果、合作方、项目链接或发表情况。必要信息缺失时先完成可确定的部分，再简短询问。

## 已确认的个人信息

- 学术姓名：Xuling Zhao；中文姓名：赵旭令（仅维护资料，个人介绍页面保持英文）；英文昵称/标识：leo。
- 当前本科：南京大学人工智能学院。首页表述：**I’m an undergraduate at the School of Artificial Intelligence, Nanjing University.**
- Education（新在前）：Zhejiang University；Direct-entry PhD, College of Computer Science and Technology；PIL Lab；Interest: Diffusion language models；Incoming。Nanjing University；Undergraduate in Artificial Intelligence；LAMDA8 Group（用户在 LAMDA 8 组做过工作）；Interest: Optimization；Sep. 2023 – Jun. 2027 (expected)。
- News：Sep 2026，Admitted to the direct-entry PhD program at the College of Computer Science and Technology, Zhejiang University.（月份由用户确认）。
- 后续去向：已确定赴浙江大学计算机学院攻读直博。该信息由 Education 与 News 表达；首页简介第二句改为 **My research interests are optimization and diffusion language models.**，避免三处重复。未提供入学时间，Education 中显示 Incoming；不编造，也不写成已经在读。
- 研究兴趣（用户 2026-10-28 确认）：Optimization 对应南大，Diffusion language models 对应浙大。不再使用 Machine learning 的笼统表述。
- 奖项：2025、2024 年 People's Scholarship，Nanjing University；用户明确暂时不写等级。按年份倒序，可继续增加条目。
- Email：xl.zhao2035@gmail.com。
- GitHub：https://github.com/xulingzhao。
- OpenReview：https://openreview.net/profile?id=~Xuling_Zhao1（`_data/socials.yml` 的 `openreview_id`）。尚无论文，暂无 Google Scholar。

个人信息源（含 Education、News、奖项）在 `_data/home.yml`、`_data/socials.yml`；基本站点元信息在 `_config.yml`。优先更新数据，避免在多处硬编码同一信息。

## 文件与参考入口

| 用途                          | 入口                                                                                                            |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 所有个人页面的样式            | `assets/css/home.css`，由 `assets/css/main.scss` 内联进 `<head>`；页面不要再单独引用                            |
| 五个主页面                    | `_pages/about.md`、`publications.md`、`projects.md`、`blog.md`、`notes.md`                                      |
| 个人论文                      | `_bibliography/publications.bib`，目前为空；[论文维护指南](docs/PUBLICATIONS.md)                                |
| 论文模板/引用参考             | `docs/publication-examples/papers.bib`，仅供字段参考，不参与构建                                                |
| 未来真实项目                  | `_projects/`；[项目维护指南](docs/PROJECTS.md)                                                                  |
| 未来真实文章                  | `_posts/`；[Writing 维护指南](docs/WRITING.md)                                                                  |
| 已确认风格的项目/文章详情参考 | [参考索引](docs/site-reference/README.md)：两个项目、两篇文章的完整源码                                         |
| 原版 al-folio 功能示例        | [九个项目](docs/project-examples/README.md)、[33 篇文章](docs/writing-examples/README.md)                       |
| Notes                         | 目前只有 `_pages/notes.md` 空状态；尚未建立笔记集合或详情页。收到真实材料后按内容需要扩展，并沿用本站详情风格。 |

四份个人风格参考是此前为演示制作的虚构内容，已从 `_projects/`、`_posts/` 移到 `docs/site-reference/`，不生成公开详情页，不进入站点搜索、RSS 或列表。示意图归档于 `docs/site-reference/project-images/`，不对外发布。原版 42 份示例另行完整保留，不能直接搬回列表造成旧样式复现。

个人论文独立文件与项目/文章空集合会自动控制空状态；添加真实条目后沿用已有列表实现，不必另造一个首页。Notes 的内容结构则需要届时实现。新增内容时同步检查首页、列表、详情、返回链接和 Writing 归档。

## 本地运行与验证

仓库：`xulingzhao/xulingzhao.github.io`。当前是 al-folio v1，运行组件由 gems 提供，不能套用旧版 al-folio 的操作经验。保留已锁定依赖，按实际配置运行。

在项目根目录启动：

```bash
bash bin/serve-local
```

看到 `Server running` 后打开 **http://127.0.0.1:4000/al-folio/**。`/al-folio/` 是当前本地 baseurl，不要擅自去掉。终端保持打开；停止按 **Control + C**，下次仍运行同一命令。修改 `_config.yml` 后需要重启；一般内容修改会自动重建。

环境说明、完整目录与重装方法见 [LOCAL_DEVELOPMENT.md](docs/LOCAL_DEVELOPMENT.md)。当前使用 Homebrew Ruby、`vendor/` 中的项目依赖；Python 3 仅用于静态输出检查，不再需要 `.venv/` 或 nbconvert；启动脚本处理 OneDrive 文件监听并禁用本地外部文章抓取，不要求 Docker。

每次改动按范围验证：相关文件格式、`npm run lint:style-contract`、`git diff --check`、本地 Jekyll 构建；涉及排版时查看桌面和手机，涉及导航时检查完整点击路径。不要为普通文案修改安装整套额外工具。测试日志、截图与依赖放在已忽略的本地目录，不混入 Git 提交。

正式网站目标地址为 **https://xulingzhao.github.io/**。`.github/workflows/deploy.yml` 使用 `_config.yml,_config.production.yml` 构建，后者只覆盖正式 URL 与空 baseurl；本地继续使用 `/al-folio/`。向 `main` 推送会触发部署工作流：`Deploy site` 构建并写入 `gh-pages`，然后由 Pages 发布。仓库 Settings → Pages 必须选择 **Deploy from a branch → gh-pages → /(root)**，不能选择源码 `main`。部署结果需查看这两个工作流，不把本地提交或推送成功当成网站已经上线。模板专用的 Lighthouse、Docker 发布、CV 生成等任务已删除；部署只保留 `Deploy site`，其中包含格式、样式边界、公开路由和本地链接检查。

`DESIGN.md` 和 `docs/` 均排除在网站构建之外。`AGENTS.md` 已指向本文；新增个人设计决策写在这里，不把本站偏好混进上游通用架构说明。运行时组件归属、覆写限制与插件配置仍遵循 `AGENTS.md` 和架构文档。

## 当前进度与下一步

2026-10-28（四）：视觉润色——头像抠图为透明全身像；加入苹果红点缀（News 红点、阅读进度条、选中色）；加入首屏上浮、滚动淡入、下划线划出与头像悬停轻摆，均尊重减少动态效果设置。生产构建（含 PurgeCSS）保留全部新规则，站点检查通过；首页、文章页及其他页面在桌面/手机检查无遮挡。阅读进度条与滚动淡入在不支持滚动驱动动画的浏览器（如当前 Firefox）中不显示，内容正常。

2026-10-28（三）：开启社交分享卡片（`serve_og_meta`，默认图 `og-avatar.jpg`；首页 `title` 改为 `About`，分享标题为 “Xuling Zhao | About”）；联系方式加入 OpenReview；Writing 页 Articles 标题旁加入 RSS（`/feed.xml`）；简介第二句去重；头像框放大为 2:3 全身像。导航五项与 News 全量显示保持不变。

2026-10-28（二）：首页顺序调整为 Education → Honors & Awards → News；删除 Research interests 区块，研究方向并入 Education；浙大加入 PIL Lab；换上用户提供的头像；首页与站点描述改为 optimization and diffusion language models。试过的两栏排版已撤回。本地预览的桌面/手机截图已检查。

2026-10-28：首页新增 News 区块（首条为浙大直博录取，Sep 2026），Education 增加 Zhejiang University 与 LAMDA8 Group，移除首页的 Publications / Projects / Writing 导引及其专用样式（`.home-writing`、`.home-collection-empty`）。手机端奖项年份列由 52px 调为 64px，与 News 对齐。生产构建（含 PurgeCSS）与站点检查通过，桌面/手机截图已检查。

2026-10-26：GitHub 将 `ubuntu-latest` 切换到 Ubuntu 26.04 后，该系统不提供 Ruby 3.3.5，`Deploy site` 因此失败；部署工作流已固定为 `ubuntu-24.04`。另发现 `home.css` 并入 `main.css` 后，Sass 压缩出的单独 `:is(a,b)` 规则会被 PurgeCSS 整条删除，导致文章正文宽度和段距丢失；已改写为普通选择器列表。`home.css` 中不要再写单独的 `:is(...) {}` 规则（`:is(...) h2` 这类带后代的不受影响）。经过 PurgeCSS 的生产构建与线上 8 个页面在桌面和手机宽度下对比一致（手机文章页仅 36 个抗锯齿像素差异）。

2026-10-24：修复线上打开页面时先闪现 al-folio 导航栏的问题。原因是 `home.css` 写在各页正文里，晚于主题样式加载。现由 `assets/css/main.scss` 覆盖主题同名文件，在末尾内联 `home.css`，个人样式随 `<head>` 中的 `main.css` 一起阻塞首次绘制；已移除 8 个页面中的 `<link>`。升级 `al_folio_core` 时需同步该文件的主题部分。生产构建与站点检查通过；8 个页面在桌面和手机宽度下与线上版本像素一致；人为延迟样式时首帧不再出现旧导航。同日清理 OneDrive 恢复的 145 个旧模板文件（与 Git 历史中删除前版本逐字节一致）、9 个未被引用的文楷分包、`.venv/`、旧 `_site/` 与 `.bundle/` 中的截图、日志和临时构建；`.bundle/` 只保留 `github-xulingzhao.pub` 与 `local-preview.yml`。目录从约 697 MiB 降至约 273 MiB。若 OneDrive 再次恢复旧文件，`git status` 会出现大量未跟踪项，可先用 `git clean -nd` 核对后删除。

2026-10-16：根据用户提供的原稿加入首篇真实 Writing 文章《理解 KL 散度》，发布日期 2026-10-15，地址 `/blog/2026/understanding-kl-divergence/`。保留正文与公式，添加六节目录及附录跳转，沿用霞鹜文楷 / Fraunces；数学公式保留 MathJax 专用数学字体，避免符号损坏。文章有 29 个独立公式块，长公式在手机上局部横向滚动。预计阅读时间 18 分钟，列表与详情统一使用 `reading_time`。公开页面清单增至 8 页；本地、生产构建、公式完整性及桌面/手机阅读路径已检查。文章与中文字体修改已合并到 `main` 并推送。

2026-10-16：加入霞鹜文楷中文字体支持，英文 Fraunces Italic 和既有布局保持不变；博客允许中文及混排。没有新增公开示例文章。已验证桌面/手机混排和实际字体，英文首页排版不变且不下载中文字体分包；本地与生产输出检查通过。字体修改与首篇文章一并纳入本次本地发布准备，推送由用户执行。

本次本地清理：删除 CV、Teaching、People、Books、News、Repositories、插件目录与下拉菜单等旧页面及其集合；删除无用演示媒体和模板专用自动化；参考资料保留于排除构建的 `docs/`。404 已沿用本站风格。新增 `test/site-routes.json` 与 `bin/check-site.py`，新建页面时须更新清单。详细边界见 [CLEANUP.md](docs/CLEANUP.md)。本地与生产配置构建均通过，输出仅含 7 个允许页面；已验证站内链接、桌面/手机显示和旧 CV 地址返回 404。目录实际占用从约 672 MiB 降至约 264 MiB（包含保留的 Git 历史与依赖），释放约 408 MiB。此前清理已提交为 `233c5b9` 并合并到本地 `main`；线上发布状态以 GitHub Actions 为准。

已完成：统一首页与分页面视觉；统一项目/文章详情和 Writing 归档；个人信息与奖项；leo 标识；四栏目空状态；参考归档与维护文档。

发布进度：用户已将满意版本推送到 `main` / `redesign`，`Deploy site` 已成功构建并写入 `gh-pages`。首次 Pages 误选源码分支导致缺少主题 gem；用户已切换为 `gh-pages` 根目录。2026-10-15 的 Pages 发布已成功（run `38697059164`），正式首页返回 HTTP 200，个人信息与空状态内容已核对。日常开发仍在 `redesign`，推送使用 1Password 中的 `github-xulingzhao` SSH 密钥。

等待用户提供：论文、Applied / Personal 项目材料、技术文章/个人想法、课程或阅读笔记。后续以用户提供的信息逐项补充，并保持已经认可的风格。

以后可直接给协作者这句话：

> 请先阅读项目根目录的 DESIGN.md 和 AGENTS.md，检查当前分支与改动，按已确认的设计和内容约定继续本次任务；完成后同步更新 DESIGN.md 中实际变化的进度与约定。
