from __future__ import annotations

import argparse

from .data_loader import load_snapshots
from .report import render_markdown
from .screener import rank_candidates


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the offline trend-wave demo.")
    parser.add_argument("--sample", default="data_samples/market_snapshot.csv")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    snapshots = load_snapshots(args.sample)
    scores = rank_candidates(snapshots, args.limit)
    print(render_markdown(scores))


if __name__ == "__main__":
    main()
