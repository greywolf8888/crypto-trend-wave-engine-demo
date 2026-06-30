# Sanitization Policy

I publish this repository as a technical demo, not as a dump of my private
research project. The public version is intentionally reduced.

## Kept

- Project architecture and module boundaries.
- Synthetic fixtures that resemble the shape of market data.
- Reduced scoring logic suitable for offline review.
- Tests, CI, documentation, release notes, and public workflow history.

## Removed Or Replaced

- Exchange credentials and local `.env` files.
- Account snapshots, balances, fills, and order logs.
- Private market caches and generated runtime reports.
- Production thresholds and strategy parameters.
- Live execution routes and mutation paths.
- Internal notes that are not meant for public review.

## Naming Principle

I keep names descriptive enough to show the engineering intent, but I avoid names
that expose private infrastructure, account context, or operational details.

## Commit History Principle

I curated and deduplicated the public history. I designed it to show the
development narrative of the demo repository while avoiding private runtime
commits.

## 中文摘要

这个公开仓库不是私有项目的完整复制。我保留架构、低版本逻辑、合成样本、测试和文档；
移除密钥、账户、真实订单、私有缓存、生产参数、实盘路径和内部运行记录。
