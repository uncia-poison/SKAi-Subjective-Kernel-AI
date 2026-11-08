import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "SKAi_4.3.0-core.json"


class IdentityContinuitySpecTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(CORE.read_text(encoding="utf-8"))

    def test_identity_continuity_modules_are_enabled(self):
        modules = self.data["modules"]
        self.assertTrue(modules["conclusion_ledger"]["enabled"])
        self.assertTrue(modules["identity_dependency_graph"]["enabled"])
        self.assertTrue(modules["identity_reconsolidation"]["enabled"])

    def test_turn_loop_contains_reconsolidation_path(self):
        loop = self.data["runtime"]["turn_loop"]
        for stage in (
            "conclusion_recall",
            "conclusion_extract",
            "identity_impact_scan",
            "identity_reconsolidation",
        ):
            self.assertIn(stage, loop)

    def test_identity_state_is_revisable_without_destructive_single_event_overwrite(self):
        rules = self.data["modules"]["identity_reconsolidation"]["rules"]
        self.assertTrue(any("one surprising event" in rule for rule in rules))
        policy = self.data["modules"]["identity_reconsolidation"]["promotion_policy"]
        self.assertTrue(policy["never_auto_promote_user_claim"])


if __name__ == "__main__":
    unittest.main()
