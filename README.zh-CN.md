# Crypto Trend Wave Engine

![Status](https://img.shields.io/badge/status-sanitized_release-0f766e)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![CI](https://img.shields.io/badge/ci-unittest-16a34a)
![Mode](https://img.shields.io/badge/mode-offline_research-2563EB)
![License](https://img.shields.io/badge/license-MIT-blue)

[English README](README.md) · [架构说明](docs/architecture.md) · [案例复盘](docs/case-study.md) · [脱敏策略](docs/sanitization-policy.md)

我把这个仓库做成私有 `main` 分支的公开脱敏版本。私有项目体量更大；
这个公开版本只保留适合展示的工程形态：合成数据读取、低版本趋势浪型评分、
显式风控边界、Markdown 报告、测试、CI，以及能解释工作流的文档。

这不是交易机器人发布版。它不连接交易所、不下单、不包含账户数据、API key、
生产阈值、私有日志或实盘执行路径。

![演示报告预览](docs/assets/demo-report-preview.svg)

## 公开版本展示内容

这个公开版本展示我如何组织一个研究密集型后端项目：数据噪声大、策略假设多、
风控要求强，所以代码必须有清晰边界和可复核输出。

| 能力面 | 公开实现 | 体现的能力 |
| --- | --- | --- |
| 数据边界 | `data_samples/` 下的合成 CSV/JSON | 我能把公开样本和私有运行数据隔离。 |
| 领域模型 | 行情快照、评分、风控边界 dataclass | 我会把业务概念显式建模，而不是到处传原始字典。 |
| 评分引擎 | 趋势、流动性、资金流、费率、波动惩罚 | 我能把研究假设落成确定性代码。 |
| 风控层 | 只读仓位上限和止损距离输出 | 我把风险当作产品表面，而不是最后补丁。 |
| 报告层 | Markdown 候选报告 | 输出能被人复核，不只是给脚本消费。 |
| 质量门禁 | 标准库测试和 GitHub Actions | 公开版本不依赖重环境也能验证。 |

## 离线运行

```powershell
$env:PYTHONPATH="src"
python -m trend_wave_demo.cli --sample data_samples/market_snapshot.csv --limit 5
python -m unittest discover -s tests
```

## 仓库结构

| 路径 | 作用 |
| --- | --- |
| `src/trend_wave_demo/` | 离线评分、排序、风控、CLI 和报告代码 |
| `data_samples/` | 合成行情快照和场景样本 |
| `docs/` | 架构、演示 walkthrough、案例复盘、脱敏策略和研究记录 |
| `tests/` | 单元测试和公开 fixture |
| `.github/workflows/` | 轻量 CI |

## 为什么是公开脱敏版本

我在公开前有意降级：

- 用合成样本替换私有行情缓存。
- 移除交易所密钥、账户状态、实盘路径和生产阈值。
- 保留架构、命名、测试风格和文档风格。
- 使用整理后的公开提交历史，而不是暴露私有运行提交。

## 文档入口

- [架构说明](docs/architecture.md)
- [项目 walkthrough](docs/demo-walkthrough.md)
- [全栈能力映射](docs/full-stack-scope.md)
- [案例复盘](docs/case-study.md)
- [脱敏策略](docs/sanitization-policy.md)
- [运行手册](docs/runbook.md)
- [Release notes](RELEASE_NOTES.md)

## 公开边界

我维护这个仓库仅用于作品集展示和技术沟通；我不把它作为投资建议、生产交易系统，
也不把它作为任何交易表现承诺。
