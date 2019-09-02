import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme("aAsVN","aAsVN,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",104))
    def test_line_comment(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("// /* */123a123 \t","<EOF>",105))
    def test_block_comment(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""/*123a123 //
        
        
        
        */""","<EOF>",106))
    def test_line_string(self):
        """test String"""
        quotes = "\""
        content = "\"\\\""
        string = quotes + content + quotes
        self.assertTrue(TestLexer.checkLexeme(string,content + ",<EOF>",107))

    def test_line_String(self):
        """test String"""
        quotes = "\""
        content = "Hello world"
        string = quotes + content + quotes
        self.assertTrue(TestLexer.checkLexeme("int a = 10","int,a,=,10,<EOF>",109))
        #self.assertTrue(TestLexer.checkLexeme(string,string + ",<EOF>",108))