from __future__ import annotations

from .factors import score_snapshot
from .models import MarketSnapshot, TrendScore


def rank_candidates(snapshots: list[MarketSnapshot], limit: int = 10) -> list[TrendScore]:
    scored = [score_snapshot(snapshot) for snapshot in snapshots]
    return sorted(scored, key=lambda item: item.score, reverse=True)[:limit]
