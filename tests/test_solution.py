from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        fpath1 = './files/testfile1.txt'
        fpath2 = './files/testfile2.txt'
        solution(fpath1, fpath2)
        with open(fpath2, 'r') as f2:
            text2 = f2.read()
        with open(fpath1, 'r') as f1:
            text1 = f1.read()

        self.assertEqual(text1, text2)