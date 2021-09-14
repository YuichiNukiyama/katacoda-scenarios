
import unittest
import app

class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.foo(1, 3), 4)

if __name__ == "__main__":
    unittest.main()