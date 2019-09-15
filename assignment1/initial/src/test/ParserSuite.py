import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """void main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """void main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """void main( {}"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_if(self):
        input = """void main( ){ if (a) if (b) if (c) a; else a; else }"""
        expect = "Error on line 1 col 51: }"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_expression_No57(self):
        """expression statement"""
        input = """
        boolean test()
            {
                boolean b;
                b=((a && b)|| (a>=c) ||(d==e) || (a!=3));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))