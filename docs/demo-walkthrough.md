# Demo Walkthrough

This walkthrough explains how I expect a reviewer to read the repository without
needing access to my private project.

## 1. Start With The README

The README explains why this repository exists: it is a sanitized public demo for
the private `main` branch. I use it to show the engineering style behind my
research engine, not to publish a production strategy.

## 2. Inspect The Data Boundary

Open `data_samples/market_snapshot.csv`. The file is intentionally small and
synthetic. It gives the scoring pipeline enough structure to run while avoiding
private account data, live exchange exports, and historical strategy logs.

## 3. Read The Pipeline

The shortest path through the code is:

```text
cli.py -> data_loader.py -> factors.py -> screener.py -> risk.py -> report.py
```

I keep the path direct so a reviewer can understand the demo in minutes.

## 4. Run The Offline Report

```powershell
$env:PYTHONPATH="src"
python -m trend_wave_demo.cli --sample data_samples/market_snapshot.csv --limit 5
```

The output is a Markdown table with score components and a demo-only risk
boundary.

## 5. Verify The Quality Gate

```powershell
python -m unittest discover -s tests
```

I kept the test suite small because this is a low-version public slice, but it
still verifies the core contract: fixture loading, candidate ranking, and risk
boundary behavior.

## 中文摘要

我建议按 README、合成数据、代码流水线、离线报告、测试的顺序阅读。这个 demo 的价值
不在于暴露完整策略，而在于展示我如何把研究流程组织成可读、可测、可脱敏的工程结构。
