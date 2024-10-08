# Crypto Trend Wave Engine Demo

![Status](https://img.shields.io/badge/status-sanitized_demo-0f766e)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![Mode](https://img.shields.io/badge/mode-research_only-2563EB)
![License](https://img.shields.io/badge/license-MIT-blue)

[English README](README.md)

本仓库是私有加密市场研究系统的公开脱敏低版本演示。它只保留可公开展示的
离线评分、合成样本、文档和可测试边界，不包含交易所密钥、账户数据、真实交易日志、
私有运行数据或生产级策略实现。

![演示报告预览](docs/assets/demo-report-preview.svg)

## 演示内容

- 合成行情快照读取。
- 低版本趋势浪型因子评分。
- 只读风控边界检查。
- 候选标的排序与 Markdown 报告输出。
- 面向公开阅读的中英文说明。

## 离线运行

```powershell
$env:PYTHONPATH="src"
python -m trend_wave_demo.cli --sample data_samples/market_snapshot.csv
```

本仓库仅用于公开演示和技术沟通，不构成投资建议，也不是生产交易系统。
