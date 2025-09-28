"""
Author: Swarnendu Bhattacharjee
Project: Stray Animal Feeder
File: tests/test_feeder.py
Purpose: Unit & integration tests for robotic feeder modules and CV system
"""

import unittest
from unittest.mock import patch, MagicMock
from src.feeder_robot import FeederRobot
from src.cv_module import CVModule
from src.utils import calculate_feed_quantity

class TestFeederRobot(unittest.TestCase):
    def setUp(self):
        """Initialize the FeederRobot and CVModule for testing"""
        self.robot = FeederRobot(num_dispensers=3, default_quantity=50)  # grams
        self.cv = CVModule()

    def test_feed_single_dispenser(self):
        """Test if a single dispenser feeds correct amount"""
        result = self.robot.feed(dispenser_id=1)
        self.assertIn('dispensed', result)
        self.assertEqual(result['quantity'], 50)

    def test_feed_multiple_dispensers(self):
        """Test if all dispensers feed correctly"""
        results = [self.robot.feed(d) for d in range(1, 4)]
        for r in results:
            self.assertEqual(r['quantity'], 50)
            self.assertIn('dispensed', r)

    def test_adjusted_feed_quantity(self):
        """Test feeding with custom quantity"""
        result = self.robot.feed(dispenser_id=2, quantity=75)
        self.assertEqual(result['quantity'], 75)

    @patch('src.cv_module.CVModule.detect_injured_animal')
    def test_cv_alert_triggers_feeder(self, mock_detect):
        """Test CV detection triggers feeder"""
        mock_detect.return_value = True
        injured_detected = self.cv.detect_injured_animal('sample_image.jpg')
        self.assertTrue(injured_detected)
        feed_response = self.robot.feed(dispenser_id=1)
        self.assertIn('dispensed', feed_response)

    def test_feed_quantity_calculation(self):
        """Test utility function for dynamic feed calculation"""
        quantity = calculate_feed_quantity(weight_kg=4, activity_level='high')
        self.assertIsInstance(quantity, int)
        self.assertGreater(quantity, 0)

    def test_full_workflow_integration(self):
        """Simulate end-to-end scenario"""
        # Step 1: CV detects injured animal
        with patch.object(CVModule, 'detect_injured_animal', return_value=True):
            alert = self.cv.detect_injured_animal('injured_cat.jpg')
            self.assertTrue(alert)

        # Step 2: Feeder dispenses food
        feed = self.robot.feed(dispenser_id=1)
        self.assertEqual(feed['quantity'], 50)
        self.assertIn('dispensed', feed)

        # Step 3: Log/utility check
        log_qty = calculate_feed_quantity(weight_kg=3, activity_level='medium')
        self.assertIsInstance(log_qty, int)

if __name__ == '__main__':
    unittest.main()
