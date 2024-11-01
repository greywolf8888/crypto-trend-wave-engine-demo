from __future__ import annotations

from .models import RiskBoundary, TrendScore


def boundary_for(score: TrendScore) -> RiskBoundary:
    if score.score >= 72:
        return RiskBoundary(5.0, 3.2, ("strong setup", "demo-only sizing"))
    if score.score >= 58:
        return RiskBoundary(3.0, 4.0, ("watchlist setup", "confirmation required"))
    return RiskBoundary(0.0, 0.0, ("research only", "no demo allocation"))
