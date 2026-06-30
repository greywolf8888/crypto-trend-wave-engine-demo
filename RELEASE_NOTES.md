# Release Notes

## v0.1.1-demo

I published this patch release to turn the demo from a simple public export into
a stronger portfolio artifact for the private `main` branch.

### Highlights

- Rewrote the README in my first-person project voice.
- Added architecture, walkthrough, full-stack scope, case study, and sanitization docs.
- Added a GitHub presentation checklist covering README, topics, release, security, CI, and social preview.
- Added 1280x640 PNG/SVG social preview assets for repository presentation.
- Tightened security documentation and public/private boundary language.
- Normalized generated research notes toward first-person wording.

### 中文摘要

`v0.1.1-demo` 是展示层增强版本。我把 README、架构、案例复盘、脱敏策略、
GitHub 展示清单、社交预览素材和安全边界说明补到更适合作品集展示的状态。

## v0.1.0-demo

I published this release as the public, sanitized demo for the private research
core behind my crypto-market workflow.

### Highlights

- Added an offline trend-wave scoring pipeline built on synthetic market data.
- Added typed domain models for snapshots, scores, and risk boundaries.
- Added demo-only risk boundary output before any execution concept.
- Added Markdown reporting so candidates can be reviewed without a service.
- Added English and Chinese documentation for public readers.
- Added CI and unit tests that run without external dependencies.
- Added a public sanitization policy explaining what I removed before release.

### Public Boundary

I did not include exchange credentials, account data, production
thresholds, live execution routes, private caches, or real trading logs.

### 中文摘要

`v0.1.0-demo` 是我为私有研究内核准备的公开脱敏版本。它包含合成数据、低版本评分、
只读风控边界、Markdown 报告、中英文文档、CI 和测试；不包含密钥、账户、实盘路径、
生产参数或真实交易日志。
