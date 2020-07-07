import unittest
import os

nl=os.linesep

class TestSolutions(unittest.TestCase):

    def test_solution_a1(self):
        from solutions import a1
        print('EXERCISE A1')
        print('TASK: print the following pattern.')
        expect=('012' + nl +
                '012' + nl + 
                '012' + nl )
        self.assertEqual(a1.solve(), expect)

    def test_solution_a2(self):
        from solutions import a2
        print('EXERCISE A2')
        print('TASK: print the following pattern.')
        expect=('000' + nl +
                '111' + nl + 
                '222' + nl )
        self.assertEqual(a2.solve(), expect)

    def test_solution_a3(self):
        from solutions import a3
        print('EXERCISE A3')
        print('TASK: print the following pattern.')
        expect=('123' + nl +
                '456' + nl + 
                '789' + nl )
        self.assertEqual(a3.solve(), expect)

    def test_solution_b(self):
        from solutions import b
        print('EXERCISE B')
        print('TASK: print the following pattern.')
        expect=('01234' + nl +
                '01234' + nl + 
                '01234' + nl )
        self.assertEqual(b.solve(), expect)

    def test_solution_c(self):
        from solutions import c
        print('EXERCISE C')
        print('TASK: print the following pattern.')
        expect=('0123' + nl +
                '0123' + nl + 
                '0123' + nl + 
                '0123' + nl )
        self.assertEqual(c.solve(), expect)

    def test_solution_d(self):
        from solutions import d
        print('EXERCISE D')
        print('TASK: print the following pattern.')
        expect=('987' + nl +
                '654' + nl + 
                '321' + nl )
        self.assertEqual(d.solve(), expect)

    def test_solution_e(self):
        from solutions import e
        print('EXERCISE E')
        print('TASK: print the following pattern.')
        expect=('876' + nl +
                '543' + nl + 
                '210' + nl )
        self.assertEqual(e.solve(), expect)

    def test_solution_f(self):
        from solutions import f
        print('EXERCISE F')
        print('TASK: print the following pattern.')
        expect=('121' + nl +
                '212' + nl + 
                '121' + nl )
        self.assertEqual(f.solve(), expect)

    def test_solution_g(self):
        from solutions import g
        print('EXERCISE G')
        print('TASK: print the following pattern.')
        expect=('111' + nl +
                '101' + nl + 
                '111' + nl )
        self.assertEqual(g.solve(), expect)

    def test_solution_h(self):
        from solutions import h
        print('EXERCISE H')
        print('TASK: replace any number between 1 and 21 (including 1 and 21) that is divisible by 3 by the string "bee".')
        expect='1 2 bee 4 5 bee 7 8 bee 10 11 bee 13 14 bee 16 17 bee 19 20 bee '
        self.assertEqual(h.solve(), expect)

    def test_solution_i(self):
        from solutions import i
        print('EXERCISE I')
        print("TASK: print the first 5 lines of the pascal's triangle.")
        expect=('1 ' + nl +
                '1 1 ' + nl +
                '1 2 1 ' + nl +
                '1 3 3 1 ' + nl +
                '1 4 6 4 1 ' + nl)
        self.assertEqual(i.solve(), expect)
        
    def test_solution_j(self):
        from solutions import j
        print('EXERCISE J')
        print("print only the first 6th lines of the pascal's triangle.")
        expect='1 5 10 10 5 1 ' + nl
        self.assertEqual(j.solve(), expect)

    def test_solution_k(self):
        from solutions import k
        print('EXERCISE K')
        print("SIGNATURE: solve(n, s), with a positive number n, and a string s.")
        print("TASK:      the output should be the n-times repetition of the string s (for zero repetitions the empty string should be returned).")
        print("EXAMPLES:  solve(2, 'Xyz') returns 'XyzXyz'; solve(0, 'Xyz') returns ''.")
        self.assertEqual(k.solve(2, 'ToasT'), 'ToasTToasT')
        self.assertEqual(k.solve(4, 'toast'), 'toasttoasttoasttoast')
        self.assertEqual(k.solve(3, 'Xyz'), 'XyzXyzXyz')
        self.assertEqual(k.solve(7, 'xyz'), 'xyzxyzxyzxyzxyzxyzxyz')
        self.assertEqual(k.solve(2, '1+'), '1+1+')
        self.assertEqual(k.solve(22, ''), '')
        self.assertEqual(k.solve(22, '.'), '......................')
        self.assertEqual(k.solve(0, 'toast'), '')
        self.assertEqual(k.solve(0, ''), '')
        self.assertEqual(k.solve(102, 'abc'), 'abc' * 102)

if __name__ == '__main__':
    unittest.main()

