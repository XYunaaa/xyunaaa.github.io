# Xiaoyun Dong · Academic Homepage

站点：<https://xyunaaa.github.io/>。使用参考网站的 AcadHomepage / Jekyll 模板，正文用 Markdown 维护。旧项目页和附件保留原路径。

## 日常编辑

通常只需要改这三个文件：

| 文件 | 修改内容 |
| --- | --- |
| `_pages/about.md` | 简介、经历、新闻、论文、项目、荣誉 |
| `_config.yml` | 姓名、头像、学校、邮箱、GitHub、Google Scholar |
| `_data/navigation.yml` | 顶部导航标题和章节锚点 |

论文清单是简单检索得到的初稿，**不是完整 Google Scholar 导出**；本次 Scholar 访问遇到验证。请手工核对作者、发表状态和链接，新论文按年份加入 `_pages/about.md`。三项 arXiv 工作目前按预印本标注，同一 arXiv ID 的不同标题只保留一条。已有论文作者以公开记录及仓库内 BibTeX 为依据。

添加论文时复制一项 Markdown 条目即可；`**Xiaoyun Dong**` 突出本人，`{: .paper-link}` 提供资源按钮样式。新图片放入 `research/` 或 `publication/`，写清替代文本。保留 `about`、`education`、`news`、`featured`、`publications`、`research`、`honors` 锚点，以免旧链接失效。

## 本地预览与检查

需要 Ruby **3.2 或更高兼容版本**、Bundler 和编译工具。Ubuntu 的系统 Ruby 需要配套开发头文件（`ruby-dev`、`build-essential`）；只安装 Ruby 可执行文件可能无法编译依赖。

在新版 checkout 中运行：

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

打开 <http://127.0.0.1:4000/>。正文保存后会自动重建；修改 `_config.yml` 后重启预览。构建结果在 `_site/`，无需手工编辑或提交该目录。

提交前检查：

```sh
bundle exec jekyll build --trace
python3 -m unittest discover -s tests -v
git diff --check
```

检查覆盖个人信息、论文类型、首页资源与锚点，以及 F1TENTH 旧页面的静态导出。桌面和手机布局、菜单键盘操作仍应在浏览器中查看。

当前机器缺少系统 Ruby 开发头文件，迁移时使用了 `/tmp/xyunaaa-jekyll-ruby` 中的独立 Ruby 3.2 与编译器。该临时环境存在时，可以在命令前加 `conda run --prefix /tmp/xyunaaa-jekyll-ruby --no-capture-output`；环境清理后请按上述要求重新准备 Ruby。

## 版本管理

- `homepage-v1-wowchemy`：改版前的旧站，提交 `a37c1a2115cc211e8ce65654614c8372266ea86a`。
- `redesign/academic`：本次改版分支，当前开发 checkout 在 `.worktrees/academic/`。
- 改版发布并验收后，再创建 `homepage-v2-academic`；以后大改版按版本递增，小修改用含义明确的提交保存。

查看旧版时创建独立 checkout，避免影响当前开发：

```sh
git worktree add --detach /tmp/xyunaaa-homepage-v1 homepage-v1-wowchemy
python3 -m http.server 4001 --bind 127.0.0.1 --directory /tmp/xyunaaa-homepage-v1
```

打开 <http://127.0.0.1:4001/> 即可看旧站。标签只记录已提交内容，**不会自动回滚已上线页面**。如需恢复上线版本，在发布分支创建恢复提交（例如撤销改版合并提交），检查预览后再发布，保留完整历史。

远端备份旧版标签的命令：

```sh
git push origin homepage-v1-wowchemy
```

本次只完成本地迁移与预览，尚未执行远端备份、合并或发布。发布时需要将改版提交合并到 Pages 实际使用的发布分支；确认 GitHub Pages 使用 Jekyll 从该分支根目录构建。如果原设置使用 Actions 上传旧静态产物，需要另行调整构建方式。不要添加 `.nojekyll`，否则 Markdown 首页不会被渲染。

## 模板来源

复用 [kyrie-louy/kyrie-louy.github.io](https://github.com/kyrie-louy/kyrie-louy.github.io) 的 AcadHomepage 模板，参考提交 `f287176b481843e37366a3d479e457c56d472407`。保留 [MIT 许可](LICENSE) 及模板依赖的版权说明。网站未启用 Scholar 爬虫、引用数同步或访客统计。
