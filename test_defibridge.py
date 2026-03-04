# test_defibridge.py
"""
Tests for DeFiBridge module.
"""

import unittest
from defibridge import DeFiBridge

class TestDeFiBridge(unittest.TestCase):
    """Test cases for DeFiBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeFiBridge()
        self.assertIsInstance(instance, DeFiBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeFiBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
