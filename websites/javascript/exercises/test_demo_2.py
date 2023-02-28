# encoding: utf-8


import unittest
class TestDemo(unittest.TestCase):
    def demo(self , A , B , X):
        if A > 1 and B == 0:
            X = X / A
            if A == 2 or X > 1:
                X = X + 1
                
            return X
          
    ''' Decision Coverage '''
            
    def test_demo_statement_coverag_1(self):        
     '''
    Using statement coverage to test 'demo'
    input, A = 3, B = 0, X = 1
    expect result: X = 1/3
     '''    
     X = self.demo (A=2, B=0 ,X=1)
     self.assertEqual(1/3,X)
    def test_demo_statement_coverag_2(self):
        '''
        Using statement coverage to test 'demo'
        input, A = 2, B = 0, X = 4
        expect result: X = 3

        '''
        X = self.demo (A=2, B=0 ,X=4)
        self.assertEqual(3,X)

        if __name__ == '__main__':
             unittest.main()
