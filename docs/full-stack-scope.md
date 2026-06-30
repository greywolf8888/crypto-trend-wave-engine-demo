# Full-Stack Scope

I use this repository to map to the backend and research-core side of my full-stack work.
The companion workbench demo shows how I expose research outputs through a
read-only product surface.

## What This Repository Shows

| Layer | My implementation focus |
| --- | --- |
| Domain modeling | Typed Python objects for market snapshots, scores, and risk boundaries. |
| Data engineering | Synthetic fixture loading with a clear public/private data boundary. |
| Research logic | Deterministic reduced factors and explicit scoring components. |
| Risk workflow | Demo-only boundary output before any execution concept. |
| Reporting | Markdown output that a human can inspect and archive. |
| Testing | Standard-library unit tests and CI. |
| Documentation | Architecture, case study, walkthrough, release notes, and sanitization policy. |

## What I Deliberately Did Not Publish

- Exchange adapters and credentials.
- Private production thresholds.
- Account snapshots or live order logs.
- Runtime caches and historical private reports.
- Any route that could mutate account state.

## How It Pairs With The Workbench Demo

The backend research demo answers: "How do I score and review candidates?"

The workbench demo answers: "How do I turn research outputs into a readable,
read-only product experience?"

Together they show the span from research logic to full-stack presentation while
keeping private material out of public GitHub.

## 中文摘要

我用这个仓库展示我的后端和研究内核能力；配套工作台仓库展示我如何把研究输出产品化。
两个仓库合在一起覆盖从数据、模型、风控、测试到可视化展示的全栈链路。
