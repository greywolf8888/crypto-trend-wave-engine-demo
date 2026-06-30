# Security Boundary

I designed this public demo to stay offline, sanitized, and reviewable without
private credentials.

- I do not require an exchange API key.
- I do not include account snapshots, balances, fills, or live order history.
- I do not implement a production trading endpoint.
- I keep all demo data under `data_samples/` synthetic.
- I keep the scoring logic reduced and unsuitable for live trading decisions.

## Reporting Issues

If you review this repository and notice anything that looks like private data,
credential material, or an unintended live-trading surface, please open an issue
with the file path and line number.

## 中文说明

我让这个公开演示仓库默认离线运行，不需要交易所密钥，不包含账户快照、
真实订单历史或生产交易入口。`data_samples/` 下的数据均为合成样本。
