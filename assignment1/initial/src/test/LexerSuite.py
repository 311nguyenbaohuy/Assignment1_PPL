import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
 
    def test_lower_identifier(self):
        """test lower identifiers"""
        testcase = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 101))

    def test_upper_identifier(self):
        """test upper identifier"""
        testcase = "AbC"
        expect = "AbC,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 102))

    def test_ID_with_underscore(self):
        """test ID with underscore"""
        testcase = "_abv__"
        expect = "_abv__,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 103))
    
    def test_one_underscore(self):
        """test underscore ID"""
        testcase = "_"
        expect = "_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 104))

    def test_wrong_ID_1(self):
        """test wrong identifier 1"""
        testcase = "!__"
        expect = "!,__,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 105))

    def test_icon1(self):
        """test error_char 1"""
        testcase = "@__@"
        expect = "Error Token @"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 106))
    
    def test_icon2(self):
        """test error_char 2"""
        testcase = "~__~"
        expect = "Error Token ~"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 107))

    def test_icon3(self):
        """test error_char 3"""
        testcase = "|:3"
        expect = "Error Token |"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 108))

    def test_integer(self):
        """test integer"""
        testcase = "123 001 , 123, 000_000"
        expect = "123,001,,,123,,,000,_000,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 109))

    def test_float(self):
        """test float number"""
        testcase = "1.2e1 10e-1 0.0 1.0e01 0.0e0 0.1e 000.1 123e"
        expect = "1.2e1,10e-1,0.0,1.0e01,0.0e0,0.1,e,000.1,123,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 110))

    def test_error_char(self):
        """test error char"""
        testcase = "#_abc_ "
        expect = "Error Token #"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 111))

    def test_string(self):
        """test simple string"""
        testcase = "\"hello world\""
        expect = "hello world,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 112))
    
    def test_symbolic(sefl):
        """test symbolic"""
        testcase = "+-*/!&|"
        expect = "+,-,*,/,!,Error Token &"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 113))
    
    def test_symbolic_1(sefl):
        """test symbolic 1 """
        testcase = "==!==->=<><=><==>"
        expect = "==,!=,=,-,>=,<,>,<=,>,<=,=,>,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 114))

    def test_symbolic_2(sefl):
        """test symbolic 2 """
        testcase = "[=-=][+-+][=-=][>-<][T-T][:|]"
        expect = "[,=,-,=,],[,+,-,+,],[,=,-,=,],[,>,-,<,],[,T,-,T,],[,Error Token :"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 115))

    def test_symbolic_3(sefl):
        """test symbolic 3 """
        testcase = "[{ hello world "
        expect = "[,{,hello,world,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 116))

    def test_symbolic_4(sefl):
        """test symbolic 4 """
        testcase = "++--||&&**/;,"
        expect = "+,+,-,-,||,&&,*,*,/,;,,,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 117))

    def test_comment(sefl):
        """test line comment"""
        testcase = "// abvc \t \b \n"
        expect = "<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 118))
    
    def test_more_commnet(sefl):
        """test more comment"""
        testcase = """// abv /* abv */ 
                      // avc """
        expect = "<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 119))
    
    def test_block_comment(sefl):
        """test more comment"""
        testcase = """/*/ abv /* abv */ 
                      /*/ avc """
        expect = "/,*,/,avc,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 120))

    def test_block_comment_1(sefl):
        """test block comment_1"""
        testcase = """/*/ abv /*/// abv */ 
                      /*// avc """
        expect = "/,*,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 121))

    def test_block_comment_2(sefl):
        """test block comment_2"""
        testcase = """/*/ abc
                       * abc\n
                       *bc\t \\
                       */ """
        expect = "<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 122))

    def test_wrong_block_comment_3(sefl):
        """test wrong block comment_2"""
        testcase = """/* abv /* abv  
                      /* avc """
        expect = "/,*,abv,/,*,abv,/,*,avc,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 123))

    def test_int_type(sefl):
        """test int type"""
        testcase = "int"
        expect = "int,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 124))
    
    def test_float_type(sefl):
        """test float type"""
        testcase = "float"
        expect = "float,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 125))

    def test_string_type(sefl):
        """test string type"""
        testcase = "string"
        expect = "string,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 126))

    def test_bool_type(sefl):
        """test bool type"""
        testcase = "boolean"
        expect = "boolean,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 127))

    def test_void_type(sefl):
        """test void type"""
        testcase = "void"
        expect = "void,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 128))

    def test_truefalse(sefl):
        """test truefalse"""
        testcase = "truefalse"
        expect = "truefalse,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 129))

    def test_true_false(sefl):
        """test true_false"""
        testcase = "true false"
        expect = "true,false,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 129))