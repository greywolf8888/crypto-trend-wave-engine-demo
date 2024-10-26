from __future__ import annotations

from .models import MarketSnapshot, TrendScore


def liquidity_component(snapshot: MarketSnapshot) -> float:
    rank_score = max(0.0, 1.0 - (snapshot.volume_rank - 1) / 40)
    return round(rank_score * 30, 2)


def flow_component(snapshot: MarketSnapshot) -> float:
    oi_score = min(max(snapshot.oi_change_pct, -10.0), 15.0) / 15.0
    funding_score = max(0.0, 1.0 - abs(snapshot.funding_rate) / 0.001)
    return round((oi_score * 18) + (funding_score * 12), 2)


def risk_penalty(snapshot: MarketSnapshot) -> float:
    volatility_penalty = max(0.0, snapshot.volatility_pct - 4.0) * 1.8
    crowded_penalty = max(0.0, abs(snapshot.funding_rate) - 0.00035) * 10000
    return round(volatility_penalty + crowded_penalty, 2)


def score_snapshot(snapshot: MarketSnapshot) -> TrendScore:
    trend_component = round(snapshot.trend_strength * 40, 2)
    flow = flow_component(snapshot)
    penalty = risk_penalty(snapshot)
    score = round(liquidity_component(snapshot) + trend_component + flow - penalty, 2)
    return TrendScore(
        symbol=snapshot.symbol,
        score=score,
        trend_component=trend_component,
        flow_component=flow,
        risk_penalty=penalty,
    )
