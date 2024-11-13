from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from trend_wave_demo.data_loader import load_snapshots
from trend_wave_demo.risk import boundary_for
from trend_wave_demo.screener import rank_candidates


class CoreDemoTest(unittest.TestCase):
    def test_ranking_uses_synthetic_fixture(self) -> None:
        snapshots = load_snapshots(ROOT / "data_samples" / "market_snapshot.csv")
        ranked = rank_candidates(snapshots, limit=3)
        self.assertEqual(len(ranked), 3)
        self.assertGreaterEqual(ranked[0].score, ranked[-1].score)

    def test_boundary_never_requires_live_access(self) -> None:
        snapshots = load_snapshots(ROOT / "data_samples" / "market_snapshot.csv")
        top = rank_candidates(snapshots, limit=1)[0]
        boundary = boundary_for(top)
        self.assertLessEqual(boundary.max_position_pct, 5.0)


if __name__ == "__main__":
    unittest.main()
