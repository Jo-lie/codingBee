import unittest
import os

nl=os.linesep

class TestSolutions(unittest.TestCase):

    def test_solution_a1(self):
        from solutions import a1
        expect=('012' + nl + 
                '012' + nl + 
                '012' + nl )
        self.assertEqual(a1.solve(), expect)

    def test_solution_a2(self):
        from solutions import a2
        expect=('000' + nl + 
                '111' + nl + 
                '222' + nl )
        self.assertEqual(a2.solve(), expect)

    def test_solution_a3(self):
        from solutions import a3
        expect=('123' + nl + 
                '456' + nl + 
                '789' + nl )
        self.assertEqual(a3.solve(), expect)

    def test_solution_b(self):
        from solutions import b
        expect=('01234' + nl + 
                '01234' + nl + 
                '01234' + nl )
        self.assertEqual(b.solve(), expect)

    def test_solution_c(self):
        from solutions import c
        expect=('0123' + nl + 
                '0123' + nl + 
                '0123' + nl + 
                '0123' + nl )
        self.assertEqual(c.solve(), expect)

    def test_solution_d(self):
        from solutions import d
        expect=('987' + nl + 
                '654' + nl + 
                '321' + nl )
        self.assertEqual(d.solve(), expect)

    def test_solution_e(self):
        from solutions import e
        expect=('876' + nl + 
                '543' + nl + 
                '210' + nl )
        self.assertEqual(e.solve(), expect)

    def test_solution_f(self):
        from solutions import f
        expect=('121' + nl + 
                '212' + nl + 
                '121' + nl )
        self.assertEqual(f.solve(), expect)

    def test_solution_g(self):
        from solutions import g
        expect=('111' + nl + 
                '101' + nl + 
                '111' + nl )
        self.assertEqual(g.solve(), expect)

if __name__ == '__main__':
    unittest.main()

