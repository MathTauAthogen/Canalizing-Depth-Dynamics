import unittest
import find_attractors as fa

class TestAttractors(unittest.TestCase):
    def setUp(self):
        pass

    def test_size_2(self):
        self.assertEqual(fa.get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]]), [[1, 1],[1, 0],[1, 0]])
 
    def test_size_3(self):
        self.assertEqual(fa.get_attractors_and_bassinets([[0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 1, 0]]), [[2, 4],[1, 1]])

if __name__ == '__main__':
    unittest.main()
