# 个人主页模板迁移设计

将 Xiaoyun Dong 的个人主页迁移到参考网站使用的 AcadHomepage 与 Jekyll 模板，保留原有资料、项目页面和附件，以 Markdown 维护内容。视觉沿用参考页的白底、窄侧栏、紧凑正文和蓝色链接。论文只做简单搜索和初步整理，后续由用户手工修改。

## 当前版本与参考模板

- 当前仓库：`XYunaaa/xyunaaa.github.io`，分支 `main`，旧站提交 `a37c1a2115cc211e8ce65654614c8372266ea86a`。
- 旧站是 Hugo 与 Wowchemy 生成的静态文件；当前仓库没有生成它们的源码。
- [参考模板](https://github.com/kyrie-louy/kyrie-louy.github.io)采用 Jekyll、Liquid 和 Sass，参考提交为 `f287176b481843e37366a3d479e457c56d472407`。
- 引入模板时保留其 `LICENSE`、版权说明和依赖自带的许可说明；不用参考作者的照片、论文附件、个人信息和访客统计账号。

## 页面与编辑方式

桌面使用参考模板的双栏布局，左侧展示现有头像、姓名、学校、研究方向、邮箱、GitHub 和用户提供的 [Google Scholar](https://scholar.google.com/citations?user=YK8VvrAAAAAJ&hl=en)。右侧依次展示简介、教育与工作经历、新闻、论文、项目和已有荣誉。手机使用模板的响应式布局。

| 文件或目录 | 作用 |
| --- | --- |
| `_config.yml` | 网站地址、作者信息、联系方式、学校和 Scholar 链接 |
| `_pages/about.md` | 简介、经历、新闻、论文、项目和荣誉 |
| `_data/navigation.yml` | 导航标题及章节锚点 |
| `_layouts/`、`_includes/`、`_sass/`、`assets/` | 复用模板的布局、样式与资源 |
| `authors/`、`publication/`、`research/` 等旧站目录 | 保留已有头像、附件、项目页面及其资源 |
| `README.md` | 手工编辑、预览、发布和查看旧版的方法 |

沿用现有教育经历、工作经历、邮箱和 F1TENTH 项目资料；简介使用不随学年失效的 “Ph.D. student”，不推测新的学历、职位或奖项。研究描述可概括现有场景理解工作与下面的新论文。保留旧章节锚点 `about`、`news`、`featured`、`publications`、`research` 的入口，避免已有链接失效。移除空的 Gallery 占位区。

## 论文初稿

Google Scholar 本次访问返回访问验证，不能据此声称清单完整。首版采用现有主页及搜索中找到、与研究方向和合作者相符的公开记录。每项显示标题、作者、年份、发表渠道和可用链接，突出 Xiaoyun Dong；按年份降序排列。用户可以直接编辑 Markdown 新增、删除和纠正条目。

| 年份 | 条目与来源 | 首版标注 |
| --- | --- | --- |
| 2026 | [Robust 4D Driving Scene Reconstruction from Imperfect Visual Priors](https://arxiv.org/abs/2607.12214) | arXiv 预印本；同一 arXiv ID 的旧标题不重复列出 |
| 2026 | [OmniSCS: Omni Safety-Critical Scenario Synthesis for Autonomous Driving via a Fully Editable Driving World](https://arxiv.org/abs/2607.09764) | arXiv 预印本 |
| 2026 | [One World, Dual Timeline: Decoupled Spatio-Temporal Gaussian Scene Graph for 4D Cooperative Driving Reconstruction](https://arxiv.org/abs/2605.07910) | arXiv 预印本 |
| 2025 | [VI-Planning: Infrastructure-Assisted Real-Time Planning Optimization for Autonomous Driving](https://dblp.org/rec/conf/mobicom/LuWD0LW025) | MobiCom 主论文 |
| 2025 | [Demo: VI-Planning](https://dblp.org/rec/conf/mobicom/LuWD0LW025a) | MobiCom Demo，与主论文分别标注 |
| 2025 | [Poster: VI-Planning](https://dblp.org/rec/conf/mobicom/LuWD0LWW25) | MobiCom Poster，与主论文分别标注 |
| 2022 | [PV-EncoNet: Fast Object Detection Based on Colored Point Cloud](https://doi.org/10.1109/TITS.2021.3114062) | IEEE T-ITS；作者和年份沿用现有 BibTeX |
| 2022 | [SaccadeFork: A lightweight multi-sensor fusion-based target detector](https://doi.org/10.1016/j.inffus.2021.07.004) | Information Fusion |
| 2022 | [Fast 3D Point Cloud Target Tracking based on Polar-Voxel Encoding](https://doi.org/10.1109/SMC53654.2022.9945125) | IEEE SMC；作者顺序按现有 BibTeX 修正 |
| 2021 | [Polarmask-Tracker: Lightweight Multi-Object Tracking and Segmentation Model for Edge Device](https://doi.org/10.1109/ISPA-BDCloud-SocialCom-SustainCom52081.2021.00100) | IEEE ISPA |
| 2020 | [Fast Segmentation-Based Object Tracking Model for Autonomous Vehicles](https://doi.org/10.1007/978-3-030-60239-0_18) | ICA3PP |

不把预印本写成已被会议录用的论文，不推测共同一作、通讯作者或录用消息。不复制同名作者的其他学科论文。现有毕业论文和优秀毕业论文荣誉继续保留在项目或荣誉区。已知的论文页面、代码和 BibTeX 链接继续使用；只有出版商页面时标为 Paper，不暗示为免费 PDF。会议标签和资源按钮采用本地文字样式，减少外部徽章图片请求。

## 构建与旧链接

复用参考模板的 Jekyll 构建方式和 GitHub Pages 依赖。首页源文件由 `_pages/about.md` 的 `permalink: /` 提供，旧根目录 `index.html` 从新版中移除，避免两个文件争用首页路径。旧子页面保持静态 HTML，保留它们使用的 CSS、JavaScript 和媒体文件；Jekyll 的默认布局只用于新首页，不给旧 HTML 套新布局。

修正迁移直接涉及的模板问题：资源路径在旧子页面和首页均能访问；章节导航留在当前页面；移动端导航可用且按钮有可访问名称。构建报错、路径冲突和缺失资源须修复后再提供预览。

首版不引入 Scholar 爬虫、定时任务、引用数同步、访客地图、分析服务或新的前端框架。保留 Scholar 个人链接即可。参考模板未使用的统计脚本和工作流不启用。

## 版本管理与发布

旧站提交标记为 `homepage-v1-wowchemy`，改版在 `redesign/academic` 分支进行。标签只记录已提交文件；发布前将旧版标签备份到远端。小修改使用有明确含义的提交说明，大改版完成并验收后标记 `homepage-v2-academic`，之后按重要版本递增。

查看旧版使用标签创建独立 worktree 或导出快照；恢复上线版本使用新提交保留历史。说明文档应解释标签本身不会自动改变已上线页面。当前授权范围包括本地迁移、内容初稿和预览；远端发布或修改 Pages 设置需用户明确要求。

## 验收

- Jekyll 构建成功，输出只有一个首页，不包含原样的 Liquid 标记。
- 桌面 1440px 与手机 390px 预览正常，没有横向溢出，布局与参考页一致。
- 导航可定位到对应章节，键盘可操作，头像和项目图片有替代文本。
- 个人信息全部为 Xiaoyun Dong，Scholar ID 为 `YK8VvrAAAAAJ`，没有参考作者的个人内容。
- 上表的 11 项论文初稿有正确类型标记，无重复 arXiv 版本；用户可在同一个 Markdown 文件中修改。
- 原项目页面、已知附件、头像、CSS 与 JavaScript 的本地链接仍可访问。
- 旧版本可通过标签恢复，README 中的预览与版本管理命令和实际目录一致。
