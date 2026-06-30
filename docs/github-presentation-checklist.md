# GitHub Presentation Checklist

I prepared this repository around the parts of a GitHub project page that a
visitor sees first.

| Surface | What I prepared |
| --- | --- |
| README | First-person project story, architecture diagram, usage, docs index, and public boundary. |
| Description | Short portfolio-oriented summary in `REPOSITORY_DESCRIPTION.md` and GitHub settings. |
| Topics | `crypto`, `python`, `quantitative-research`, `risk-management`, `sanitized-demo`, `trading-demo`. |
| License | MIT license for the public demo code. |
| Security | `SECURITY.md` explains that the demo is offline and sanitized. |
| Release | `v0.1.0-demo` release notes explain what I published and what I removed. |
| Social preview | `docs/assets/social-preview.png` is prepared at 1280x640 for repository preview artwork. |
| CI | `.github/workflows/ci.yml` runs standard-library tests. |

## Notes

GitHub repository settings such as the social preview image usually require a
manual upload in the web UI. I keep the ready-to-upload PNG in `docs/assets/`.

## 中文摘要

我按 GitHub 首页可见区域整理这个仓库：README、简介、topics、license、security、
release、social preview 素材和 CI 都有对应内容。
