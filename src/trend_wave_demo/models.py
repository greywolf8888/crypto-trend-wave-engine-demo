from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MarketSnapshot:
    symbol: str
    close: float
    volume_rank: int
    oi_change_pct: float
    funding_rate: float
    trend_strength: float
    volatility_pct: float


@dataclass(frozen=True)
class TrendScore:
    symbol: str
    score: float
    trend_component: float
    flow_component: float
    risk_penalty: float


@dataclass(frozen=True)
class RiskBoundary:
    max_position_pct: float
    stop_distance_pct: float
    notes: tuple[str, ...]
