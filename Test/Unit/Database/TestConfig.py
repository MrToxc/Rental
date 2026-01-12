import unittest
from pathlib import Path

from Database.Config import find_root, find_config


class TestDatabase(unittest.TestCase):

    def test_find_root(self):
        root = find_root()
        self.assertTrue(Path(root).resolve().exists())
        self.assertTrue(Path(root).resolve().is_dir())
        self.assertTrue(Path(root / "rental_config.json").exists())

    def test_find_config(self):
        self.assertTrue(Path(find_config()).exists())

if __name__ == '__main__':
    unittest.main()