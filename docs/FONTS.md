# 中英文字体

当前约定：英文保持 Fraunces Italic，中文使用霞鹜文楷（LXGW WenKai）常规字重正体。公开页面依然沿用黑色文字、白底和原有布局；博客允许中文及混排。

## 接入方式

`assets/css/home.css` 引入本地分包 CSS，将字体栈设为 `"Fraunces Home", "LXGW WenKai", Georgia, serif`。浏览器优先使用 Fraunces 已有的英文字符，缺少的中文字符使用文楷。`font-synthesis: weight` 保留原来的粗体合成能力，并禁止为中文生成假斜体；Fraunces 文件本身是真正的斜体，不受影响。不要把英文整体改成 `font-style: normal`。数学公式是例外：MathJax 节点不套正文强制字体，保留数学符号、上下标与分数所需的字体；公式里的中文文字仍使用文楷。

直接输入中文即可，标题、正文、摘要和代码共用这套规则。中文文章应标记 `lang: zh-CN`，详见 [Writing 指南](WRITING.md)。当前没有为了演示字体新增公开文章。

## 来源和许可

- 中文字体作者项目：[lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai)。
- 网页分包项目：[chawyehsu/lxgw-wenkai-webfont](https://github.com/chawyehsu/lxgw-wenkai-webfont)。
- 固定 npm 包版本：`lxgw-wenkai-webfont@1.7.0`，包内字体版本 `v1.250`。
- 原始包：`https://registry.npmjs.org/lxgw-wenkai-webfont/-/lxgw-wenkai-webfont-1.7.0.tgz`，下载时已校验 registry 公布的 SHA-512 完整性。
- 本站只提取 `lxgwwenkai-regular.css` 中的中文字符声明及其引用的 88 个 WOFF2 文件，约 4.40 MiB；没有引入其余字重、等宽版本或 npm 运行依赖。
- 字体遵循 [SIL OFL 1.1](../assets/fonts/lxgw-wenkai/OFL.txt)，网页打包代码附 [MIT 许可](../assets/fonts/lxgw-wenkai/LICENSE)。字体二进制与许可原样保留；CSS 的 unicode-range 限定为汉字、中文标点、全角字符与注音，避免改变原有英文、数学符号、箭头和 emoji 的字体回退。
- Fraunces 及其 [OFL](../assets/fonts/Fraunces-OFL.txt) 保持原样。

分包 CSS 的 `unicode-range` 让浏览器只获取实际需要的字符分包，而非一次下载全部中文字体。所有文件由本站提供，不依赖字体 CDN 或访客预先安装字体；加载过程中使用后备字体（`font-display: swap`）。

## 以后更新

不要直接覆盖为未固定版本的 CDN 链接。更新时核对原作者许可和包完整性，保留完整 CSS 与其全部引用文件，并同步来源、版本和许可。验证英文首页布局不变，以及中文标题、标点、正文、代码和手机换行；不要只看 CSS 中声明的字体名称，要检查浏览器实际使用的字体。
