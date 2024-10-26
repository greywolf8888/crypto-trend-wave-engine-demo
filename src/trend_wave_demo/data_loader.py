from __future__ import annotations

import csv
from pathlib import Path

from .models import MarketSnapshot


def load_snapshots(path: str | Path) -> list[MarketSnapshot]:
    rows: list[MarketSnapshot] = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                MarketSnapshot(
                    symbol=row["symbol"],
                    close=float(row["close"]),
                    volume_rank=int(row["volume_rank"]),
                    oi_change_pct=float(row["oi_change_pct"]),
                    funding_rate=float(row["funding_rate"]),
                    trend_strength=float(row["trend_strength"]),
                    volatility_pct=float(row["volatility_pct"]),
                )
            )
    return rows
