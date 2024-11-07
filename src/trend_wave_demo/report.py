from __future__ import annotations

from .models import TrendScore
from .risk import boundary_for


def render_markdown(scores: list[TrendScore]) -> str:
    lines = [
        "# Demo Candidate Report",
        "",
        "| Symbol | Score | Trend | Flow | Risk Penalty | Demo Boundary |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in scores:
        boundary = boundary_for(item)
        lines.append(
            f"| {item.symbol} | {item.score:.2f} | {item.trend_component:.2f} | "
            f"{item.flow_component:.2f} | {item.risk_penalty:.2f} | "
            f"{boundary.max_position_pct:.1f}% max / {boundary.stop_distance_pct:.1f}% stop |"
        )
    lines.append("")
    lines.append("Synthetic data only. This report is not investment advice.")
    return "\n".join(lines)
