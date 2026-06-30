# Case Study

## Context

I built the private system behind this demo to make crypto-market research more
repeatable. The domain has noisy signals, fast regime changes, and a high cost
for sloppy execution boundaries, so I wanted a workflow where data, assumptions,
risk, and reports are explicit.

## Problem I Solved

Before I formalized the workflow, candidate review could become scattered across
scripts, notes, screenshots, and cached market files. I needed a structure that
could answer four questions consistently:

- Which symbols are worth reviewing?
- Which factors contributed to the score?
- What risk boundary applies before any execution idea?
- Can I reproduce the reasoning later?

## My Technical Approach

I separated the workflow into small stages:

1. Load a market snapshot at the edge.
2. Convert raw rows into explicit domain objects.
3. Score each candidate through reduced factor groups.
4. Rank candidates deterministically.
5. Attach a read-only risk boundary.
6. Render a human-readable report.

My private project extends this with more data adapters and research jobs. The
public demo keeps the same mental model but uses synthetic fixtures and reduced
logic.

## Tradeoffs

I chose clarity over cleverness. I keep the public code intentionally direct because
the repository is a portfolio artifact: a reviewer should see the architecture,
not reverse-engineer a framework.

I also chose not to publish production thresholds. That keeps the repository
useful as a technical sample without turning it into an unsafe trading signal.

## Outcome

I use the demo to show a backend research core that is:

- deterministic enough to test,
- documented enough to review,
- structured enough to extend,
- and sanitized enough to publish.

## 中文摘要

我解决的问题是把分散的候选筛选、评分、风控和报告整理成可复核流程。公开版本保留
架构和工程取舍，但使用合成数据和低版本逻辑，避免泄露私有策略与运行资产。
