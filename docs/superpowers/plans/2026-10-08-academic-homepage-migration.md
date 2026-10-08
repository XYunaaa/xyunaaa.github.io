# Academic Homepage Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** 复用参考网站的 AcadHomepage 模板，将 Xiaoyun Dong 的主页迁移为可手工编辑的 Markdown，并保留旧版本和原项目链接。

**Architecture:** Jekyll 将 `_pages/about.md` 渲染为首页，作者和导航分别由 YAML 配置管理。直接复用参考模板的布局和 Sass；原来的项目子页面及资源继续作为静态文件发布。

**Tech Stack:** Jekyll、Liquid、Sass、GitHub Pages、现有 Ruby、Python 标准库测试、Chrome 预览。

**Spec:** `docs/superpowers/specs/2026-10-08-academic-homepage-migration-design.md`

## Global Constraints

- 当前旧站提交 `a37c1a2115cc211e8ce65654614c8372266ea86a`，已保存本地标签 `homepage-v1-wowchemy`；改版分支为 `redesign/academic`。
- 参考模板提交 `f287176b481843e37366a3d479e457c56d472407`，本地只读副本位于 `/tmp/kyrie-louy-homepage-reference`。
- 保留模板许可、旧项目页面、论文附件及旧页使用的 CSS、JavaScript 和媒体。
- 身份为 Xiaoyun Dong，仓库为 `XYunaaa/xyunaaa.github.io`，站点为 `https://xyunaaa.github.io`，Scholar ID 为 `YK8VvrAAAAAJ`。
- 初稿使用设计中的 11 项公开论文记录，随后由用户手工编辑；不继续扩大检索范围。
- 不添加 Scholar 爬虫、定时任务、引用数同步、访客地图、分析服务或新前端框架。
- 在本地实现和预览；不推送、合并到发布分支或修改远端 Pages 设置。

## Review Focus

1. 旧 `index.html` 与 Markdown 的 `/` 路径冲突：构建输出应只有新版首页。
2. 相对资源路径和旧子页面：首页及 `/research/f1tenth/` 的本地资源均存在，旧页不套新版布局。
3. 390px 手机宽度及键盘操作：无横向溢出，导航和联系方式可访问，按钮有名称和可见焦点。
4. 保留旧锚点：`about`、`news`、`featured`、`publications`、`research` 指向对应内容，章节跳转留在当前页。
5. 参考作者内容或错误发表状态：侧栏是用户本人，三项 arXiv 工作标为预印本，VI-Planning 主论文、Demo 和 Poster分别标注。

## Task 1: 可构建的模板与旧链接

**Files:** 引入 `LICENSE`、`Gemfile`、`Gemfile.lock`、`.gitignore`、`_config.yml`、`_layouts/`、`_includes/`、`_sass/`、`assets/`、`_data/navigation.yml`；创建 `_pages/about.md`、`tests/test_site.py`；移除新版根目录 `index.html`；保留所有旧子页面及其资源。

**Interfaces:** 输入为参考模板与旧站快照；输出为可在 `_site/` 构建出的唯一首页及原静态子页面。Task 2 在同一套模板中补齐内容。

- [x] 使用 using-git-worktrees 技能检查隔离环境，在仓库内的 `.worktrees/academic` 建立 `redesign/academic` worktree；将 `.worktrees/` 忽略，防止构建或提交包含独立 checkout。已有合适的独立 worktree 时复用。
- [x] 在 `tests/test_site.py` 使用 `unittest` 和 `html.parser.HTMLParser` 写小型构建产物检查：`test_homepage_identity` 检查 `_site/index.html` 中侧栏姓名和 Scholar 链接；`test_local_resources_and_anchors` 检查首页的本地 CSS、脚本、图片、链接和章节锚点；`test_legacy_page_export` 检查旧 F1TENTH 页逐字保留及其 CSS、脚本、图片存在。测试以站点根目录为基准解析 URL，跳过外部网址和 `mailto:`，目录链接解析为 `index.html`。

  解析结果提供 `author_name: str`、`links: list[str]`、`ids: set[str]`、`text: str`；本地资源和链接转换为 `_site/` 下的 `Path`。上述三个测试分别使用这些断言：

  ```python
  self.assertEqual(home.author_name, "Xiaoyun Dong")
  self.assertTrue(any("user=YK8VvrAAAAAJ" in url for url in home.links))
  self.assertTrue(all(path.exists() for path in local_targets))
  self.assertTrue({"about", "news", "featured", "publications", "research"} <= home.ids)
  self.assertEqual(exported_legacy.read_bytes(), source_legacy.read_bytes())
  ```

- [x] 运行 `python3 -m unittest discover -s tests -v`，确认缺少 `_site/index.html` 时失败，不能默默跳过构建产物检查。
- [x] 从参考副本引入上列模板文件和本地字体，保留第三方许可证；不复制其 `.git`、个人照片、论文附件、爬虫、工作流或统计配置。
- [x] 设置作者信息和已确认的经历；头像引用已有 `authors/admin/` 文件。首页使用 `permalink: /`，移除旧根首页以消除路径冲突；忽略 `_site/`、`.bundle/`、`vendor/` 和本地临时文件，并在 Jekyll 配置中排除测试、设计文档与 worktree。
- [x] 移除模板对缺失 `compress` 布局的引用、无用统计脚本及嵌套 `<head>`；资源路径使用 Jekyll 的 `relative_url`，避免旧页深层路径导致 404。移除全局 `<base target="_blank">`，保留必要外链的独立目标设置。
- [x] 检查模板在手机上的联系人展示和导航行为；给菜单按钮添加可访问名称，保留可见焦点，只修改相关布局、样式或现有脚本。
- [x] 配置模板现有的 GitHub Pages 构建依赖，去掉未使用的 `hawkins`；生成适合本机 Ruby 与 Bundler 的锁文件，不盲目沿用要求 Bundler 2.7.1 的上游锁文件。依赖安装到当前 checkout 的 `vendor/bundle`，不修改全局 Ruby 环境。
- [x] 运行 `bundle3.0 exec jekyll build --trace` 与上述 unittest 命令，预期构建成功、无首页冲突或缺失布局，三项检查通过。检查 `git diff homepage-v1-wowchemy -- research publication authors css js en` 确认旧资源未被修改。
- [x] 提交这一独立可构建结果：`feat: adopt AcadHomepage template and preserve legacy pages`。

## Task 2: 内容初稿、预览与维护说明

**Files:** 补齐 `_pages/about.md`、`_config.yml`、`_data/navigation.yml`；按需修改 `_sass/_page.scss`、`_sass/_buttons.scss` 和相关布局；扩展 `tests/test_site.py`；创建 `README.md`。

**Interfaces:** 使用 Task 1 的构建命令和 `_site/` 产物；输出为完整内容初稿、桌面与手机预览、手工维护说明。

- [ ] 在 `tests/test_site.py` 加入 `test_publication_types`：检查三个设计中明确的 arXiv 链接、预印本标注及 VI-Planning 的主论文、Demo、Poster 标注。复用 HTML 解析结果，不要求未来始终只有 11 项论文。

  ```python
  for paper_id in ("2607.12214", "2607.09764", "2605.07910"):
      self.assertIn("https://arxiv.org/abs/" + paper_id, home.links)
  self.assertIn("Preprints", home.text)
  self.assertIn("Demo: VI-Planning", home.text)
  self.assertIn("Poster: VI-Planning", home.text)
  ```

- [ ] 运行新增检查，确认 Task 1 的最小内容首页未包含完整论文时失败。
- [ ] 在 `_pages/about.md` 写入简介、教育与工作经历、已有新闻、设计表中的论文、原项目与已有荣誉；保留毕业论文链接。按年份降序列论文，完整列出已有来源中的作者，突出 Xiaoyun Dong，不猜测共同一作或录用状态。按钮使用本地文字样式，现有代码与 BibTeX 链接继续可用。
- [ ] 为各章节设置稳定锚点并保留 Review Focus 中的旧锚点；导航显示 About、Education & Experience、News、Publications、Projects 和 Honors。删除空 Gallery 占位及参考作者的个人内容，允许真实论文作者列表出现合作者 Yang Lou。
- [ ] 在 README 写明手工修改的三个文件、依赖安装与预览命令、发布前备份旧标签的方法，以及用 `git worktree add --detach` 查看旧版的操作。解释标签不会自动回滚已上线页面；恢复上线版本通过新提交进行。
- [ ] 运行 `bundle3.0 exec jekyll build --trace`、`python3 -m unittest discover -s tests -v` 和 `git diff --check`，预期全部通过；检查首页没有未渲染的 Liquid 标记。
- [ ] 启动本地预览 `bundle3.0 exec jekyll serve --host 127.0.0.1 --port 4000`；用 Chrome 查看 1440px 与 390px 页面，截图保存到 `/tmp`，确认字体、侧栏、论文列表、菜单和项目图像。浏览器检查 `document.documentElement.scrollWidth <= window.innerWidth`，并用键盘验证导航、菜单和联系方式；发现问题只修复相关文件后重跑受影响的检查。
- [ ] 提交完整内容与维护说明：`feat: migrate homepage content to editable Markdown`。
- [ ] 进行一次最终代码与产物审查，验证两个任务覆盖设计中的验收要求；交付分支名、预览地址或截图链接、编辑入口和验证结果，说明论文清单不是完整 Scholar 导出。
- [ ] 发布前向用户报告预览结果。当前阶段保留 `redesign/academic` 分支和旧版标签；新版发布验收后再标记 `homepage-v2-academic`。
