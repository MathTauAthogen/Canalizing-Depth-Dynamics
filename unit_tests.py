import unittest
import sub_problem_1 as sp1
class TestAttractors(unittest.TestCase):
    def setUp(self):
        pass
    def test_size_2(self):
        self.assertEqual(sp1.get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]]), [[1, 0],[1, 1],[1, 0]])
 
    def test_size_3(self):
        self.assertEqual(sp1.get_attractors_and_bassinets([[0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 1, 0]]), [[2, 4],[1, 1]])
if __name__ == '__main__':
    unittest.main()