# test_mangacollector.py
"""
Tests for MangaCollector module.
"""

import unittest
from mangacollector import MangaCollector

class TestMangaCollector(unittest.TestCase):
    """Test cases for MangaCollector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaCollector()
        self.assertIsInstance(instance, MangaCollector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaCollector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
