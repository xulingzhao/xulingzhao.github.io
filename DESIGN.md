# Xuling Zhao / leo — 网站设计与维护约定

最后更新：2026-10-15。本文记录用户已确认的选择和当前实际进度，是本个人网站后续工作的第一阅读入口。网站内容为英文，维护文档与协作沟通可用中文。

## 接手时先做什么

1. 阅读本文件和 `AGENTS.md`，检查当前分支、`git status` 与实际配置。目标开发分支为 `redesign`，保留已有未提交修改。
2. 根据本次任务阅读下方链接的栏目指南与参考源码。不要重新讨论已经确定的字体、配色、导航等选择，除非用户提出改变。
3. 用户的新指示优先；修改完成后，把新确认的选择、实际进度和参考文件位置更新到本文。详细操作只维护在对应指南里，本文提供入口。
4. 日常开发继续使用 `redesign`；`main` 用于已确认的正式版本。用户已授权本次满意版本推送并进入 `main`。以后 Git 提交、推送与发布按用户本次任务的授权范围执行，不把一次发布视为后续自动发布许可。

## 已确认的视觉风格

- 简约、克制、专业，有艺术感；用户喜欢 Apple 风格的干净布局。保持清晰层级与留白，避免装饰堆积、拥挤卡片和彩色文字。
- **所有文字使用 Fraunces Italic**，包括导航、正文、标题和代码。用户明确不需要另配易读的系统字体。当前本地字体为 `assets/fonts/fraunces-italic.ttf`，CSS 名称为 `Fraunces Home`。
- 白色背景、黑色文字与链接；使用浅灰分隔线及必要的浅灰底。**图片保持原始颜色，不做全站灰度处理。**
- 左上角标识为小写 **leo**，无句点；由 `_data/home.yml` 的 `wordmark` 控制。大标题和学术署名仍为 **Xuling Zhao**，不要自行改成 Leo Zhao。
- 浏览器图标为苹果 emoji **🍎**。保留当前 favicon 设置。
- 内容居中，当前容器最大宽度 1080px（含左右内边距）；以 `assets/css/home.css` 的实际实现为准。沿用已确认的标题比例、细分隔线与桌面/手机排版，不随意更换设计体系。
- 首屏突出姓名，身份使用自然的一句英文，不再拆成生硬的身份与学校两行。避免重复的 “I am… I am… I will…” 或重复身份段落。
- Email 与 GitHub 各占一行，并各自带标签。
- Education 与 Research interests 上下独立成节；不能为了两列布局强行并排。区块标题、学校、专业、日期有明确字号层级。
- 研究兴趣直接列出，不添加 “Currently exploring” 等多余说明。
- Honors & Awards 保留独立、可扩展的完整区块，不因目前只有两条就缩成小角落。
- 头像尚未提供，当前使用 XZ 占位与 “Portrait forthcoming”。它与 leo 页首标识用途不同；不要擅自生成或替换为他人照片。

## 栏目结构与内容边界

始终使用五项导航，顺序为 **About / Publications / Projects / Writing / Notes**。列表、详情、标签和归档页保持同一字体、导航与视觉风格；不要让点击详情后恢复旧模板的 CV、Teaching 等导航。

| 栏目         | 地址             | 内容与当前状态                                                                                  |
| ------------ | ---------------- | ----------------------------------------------------------------------------------------------- |
| About        | `/`              | 已填写简介、教育、研究兴趣、奖项、联系方式；保留论文、项目和 Writing 入口，当前显示暂无内容。   |
| Publications | `/publications/` | 当前没有论文，显示 “No publications yet.”；没有论文时隐藏搜索框。                               |
| Projects     | `/projects/`     | 当前没有可展示的真实项目，显示 “No projects yet.”；未来沿用 Applied / Personal 分类与图文详情。 |
| Writing      | `/blog/`         | 当前没有真实文章，显示 “No articles yet.”；未来收录技术文章和个人想法。                         |
| Notes        | `/notes/`        | 当前没有笔记，显示 “No notes yet.”；未来收录课程、阅读和学习笔记。                              |

空状态保留栏目标题、简短英文提示、导航与页脚，不放模板卡片、虚构成果、空分类列表或无用途的搜索。Writing 的 `/blog/archive/` 已保留同风格实现，空状态下不显示空年份/标签/分类列表。

Projects 分类是已经确定的内容约定，空栏目时不必显示分类：

| 分类                  | 收录范围                                           | 用户给出的例子                          |
| --------------------- | -------------------------------------------------- | --------------------------------------- |
| Applied (`applied`)   | 比赛、课题组、企业合作等有明确目标和交付要求的项目 | 竞赛解决方案、组内大型项目、横向课题    |
| Personal (`personal`) | 自己发起的工具、创意作品和技术探索                 | 个人报纸生成器、ASMR 生成工具、动态名片 |

保留 al-folio 多页面、论文功能与项目图文展示能力。等用户提供真实信息后，参考归档结构编写；不要把示例当成用户的经历，不编造作者、结果、合作方、项目链接或发表情况。必要信息缺失时先完成可确定的部分，再简短询问。

## 已确认的个人信息

- 学术姓名：Xuling Zhao；中文姓名：赵旭令（仅维护资料，公开页面保持英文）；英文昵称/标识：leo。
- 当前本科：南京大学人工智能学院。首页表述：**I’m an undergraduate at the School of Artificial Intelligence, Nanjing University.**
- Education：Nanjing University；Undergraduate in Artificial Intelligence；Sep. 2023 – Jun. 2027 (expected)。
- 后续去向：已确定赴浙江大学计算机学院攻读直博。首页表述：**I will pursue a direct-entry PhD at the College of Computer Science and Technology, Zhejiang University.** 未提供入学时间，不编造，也不写成已经在读。
- 研究兴趣：Machine learning；Diffusion language models。尚未确定更窄的方向，不擅自恢复 optimization 等旧草案表述。
- 奖项：2025、2024 年 People's Scholarship，Nanjing University；用户明确暂时不写等级。按年份倒序，可继续增加条目。
- Email：xl.zhao2035@gmail.com。
- GitHub：https://github.com/xulingzhao。

个人信息源在 `_data/home.yml`、`_data/socials.yml`；基本站点元信息在 `_config.yml`。优先更新数据，避免在多处硬编码同一信息。

## 文件与参考入口

| 用途                          | 入口                                                                                                            |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 所有个人页面的样式            | `assets/css/home.css`                                                                                           |
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

本次本地清理：删除 CV、Teaching、People、Books、News、Repositories、插件目录与下拉菜单等旧页面及其集合；删除无用演示媒体和模板专用自动化；参考资料保留于排除构建的 `docs/`。404 已沿用本站风格。新增 `test/site-routes.json` 与 `bin/check-site.py`，新建页面时须更新清单。详细边界见 [CLEANUP.md](docs/CLEANUP.md)。本地与生产配置构建均通过，输出仅含 7 个允许页面；已验证站内链接、桌面/手机显示和旧 CV 地址返回 404。目录实际占用从约 672 MiB 降至约 264 MiB（包含保留的 Git 历史与依赖），释放约 408 MiB。此次清理整理为本地 Git 提交，推送由用户执行；尚未推送或上线。

已完成：统一首页与分页面视觉；统一项目/文章详情和 Writing 归档；个人信息与奖项；leo 标识；四栏目空状态；参考归档与维护文档。

发布进度：用户已将满意版本推送到 `main` / `redesign`，`Deploy site` 已成功构建并写入 `gh-pages`。首次 Pages 误选源码分支导致缺少主题 gem；用户已切换为 `gh-pages` 根目录。2026-10-15 的 Pages 发布已成功（run `38697059164`），正式首页返回 HTTP 200，个人信息与空状态内容已核对。日常开发仍在 `redesign`，推送使用 1Password 中的 `github-xulingzhao` SSH 密钥。

等待用户提供：真实头像、论文、Applied / Personal 项目材料、技术文章/个人想法、课程或阅读笔记。后续以用户提供的信息逐项补充，并保持已经认可的风格。

以后可直接给协作者这句话：

> 请先阅读项目根目录的 DESIGN.md 和 AGENTS.md，检查当前分支与改动，按已确认的设计和内容约定继续本次任务；完成后同步更新 DESIGN.md 中实际变化的进度与约定。
