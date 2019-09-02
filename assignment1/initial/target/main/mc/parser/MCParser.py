# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\5\5\37\n\5\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\3\3\2\24\25\2%\2\f\3\2\2\2\4\27\3\2")
        buf.write("\2\2\6\31\3\2\2\2\b\36\3\2\2\2\n \3\2\2\2\f\r\5\4\3\2")
        buf.write("\r\16\7\3\2\2\16\17\7\6\2\2\17\20\7\7\2\2\20\22\7\n\2")
        buf.write("\2\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2")
        buf.write("\2\2\24\25\7\13\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\t")
        buf.write("\2\2\2\30\5\3\2\2\2\31\32\5\n\6\2\32\33\7\f\2\2\33\7\3")
        buf.write("\2\2\2\34\37\5\n\6\2\35\37\7\5\2\2\36\34\3\2\2\2\36\35")
        buf.write("\3\2\2\2\37\t\3\2\2\2 !\7\4\2\2!#\7\6\2\2\"$\5\b\5\2#")
        buf.write("\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\7\2\2&\13\3\2\2\2\5")
        buf.write("\22\36#")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "';'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'int'", "'void'", "'boolean'", "'float'", 
                     "'string'", "'return'", "'break'", "'continue'", "'if'", 
                     "'else'", "'for'", "'while'", "'do'", "'true'", "'false'", 
                     "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", 
                     "'='", "'-'", "'%'", "'/'", "'&&'", "'=='", "'>'", 
                     "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "INTLIT", "LB", "RB", 
                      "LSB", "RSB", "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "INTTYPE", "VOIDTYPE", "BOOLEANTYPE", 
                      "FLOATTYPE", "STRINGTYPE", "RETURN", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "FOR", "WHILE", "DO", "TRUE", "FALSE", 
                      "ADD_OP", "MUL_OP", "LOGIC_NOT_OP", "LOGIC_OR_OP", 
                      "NOT_EQUAL_OP", "LESS_OP", "LESS_EQUAL_OP", "ASSIGN_OP", 
                      "SUB_OP", "MODULUS_OP", "DIV_OP", "LOGIC_AND", "EQUAL_OP", 
                      "GREATER_OP", "GREATER_EQUAL_OP", "INT_LIT", "FLOAT_LIT", 
                      "BOOL_LIT", "STRING_LIT" ]

    RULE_program = 0
    RULE_mctype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mctype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    INTLIT=3
    LB=4
    RB=5
    LSB=6
    RSB=7
    LP=8
    RP=9
    SEMI=10
    COMMA=11
    WS=12
    ERROR_CHAR=13
    UNCLOSE_STRING=14
    ILLEGAL_ESCAPE=15
    LINE_COMMENT=16
    BLOCK_COMMENT=17
    INTTYPE=18
    VOIDTYPE=19
    BOOLEANTYPE=20
    FLOATTYPE=21
    STRINGTYPE=22
    RETURN=23
    BREAK=24
    CONTINUE=25
    IF=26
    ELSE=27
    FOR=28
    WHILE=29
    DO=30
    TRUE=31
    FALSE=32
    ADD_OP=33
    MUL_OP=34
    LOGIC_NOT_OP=35
    LOGIC_OR_OP=36
    NOT_EQUAL_OP=37
    LESS_OP=38
    LESS_EQUAL_OP=39
    ASSIGN_OP=40
    SUB_OP=41
    MODULUS_OP=42
    DIV_OP=43
    LOGIC_AND=44
    EQUAL_OP=45
    GREATER_OP=46
    GREATER_EQUAL_OP=47
    INT_LIT=48
    FLOAT_LIT=49
    BOOL_LIT=50
    STRING_LIT=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(MCParser.BodyContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mctype()
            self.state = 11
            self.match(MCParser.T__0)
            self.state = 12
            self.match(MCParser.LB)
            self.state = 13
            self.match(MCParser.RB)
            self.state = 14
            self.match(MCParser.LP)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID:
                self.state = 15
                self.body()


            self.state = 18
            self.match(MCParser.RP)
            self.state = 19
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MctypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mctype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==MCParser.INTTYPE or _la==MCParser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.funcall()
            self.state = 24
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.funcall()
                pass
            elif token in [MCParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(MCParser.INTLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MCParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MCParser.ID)
            self.state = 31
            self.match(MCParser.LB)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID or _la==MCParser.INTLIT:
                self.state = 32
                self.exp()


            self.state = 35
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





