# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u0165\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6")
        buf.write("\13\u0082\n\13\r\13\16\13\u0083\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\7\f\u008c\n\f\f\f\16\f\u008f\13\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\7\r\u0097\n\r\f\r\16\r\u009a\13\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("+\3+\3+\3,\6,\u011a\n,\r,\16,\u011b\3-\3-\3.\3.\5.\u0122")
        buf.write("\n.\3.\6.\u0125\n.\r.\16.\u0126\3/\3/\3/\5/\u012c\n/\3")
        buf.write("/\5/\u012f\n/\3/\3/\3/\5/\u0134\n/\3/\3/\3/\5/\u0139\n")
        buf.write("/\3\60\3\60\5\60\u013d\n\60\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\62\7\62\u0145\n\62\f\62\16\62\u0148\13\62\3\62\3\62\3")
        buf.write("\63\3\63\7\63\u014e\n\63\f\63\16\63\u0151\13\63\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\64\7\64\u015a\n\64\f\64\16\64")
        buf.write("\u015d\13\64\3\65\3\65\7\65\u0161\n\65\f\65\16\65\u0164")
        buf.write("\13\65\3\u0098\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\2\67\29\34;\35=\36")
        buf.write("?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y\2[\2],_-a.c/e\60g\61i")
        buf.write("\62\3\2\13\5\2\13\f\17\17\"\"\4\2\f\f\17\17\3\2\62;\4")
        buf.write("\2GGgg\f\2%&()\60\60<<AB^^``bb~~\u0080\u0080\t\2$$^^d")
        buf.write("dhhppttvv\6\2\n\f\16\17$$^^\5\2C\\aac|\6\2\62;C\\aac|")
        buf.write("\2\u0172\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5p\3\2\2")
        buf.write("\2\7r\3\2\2\2\tt\3\2\2\2\13v\3\2\2\2\rx\3\2\2\2\17z\3")
        buf.write("\2\2\2\21|\3\2\2\2\23~\3\2\2\2\25\u0081\3\2\2\2\27\u0087")
        buf.write("\3\2\2\2\31\u0092\3\2\2\2\33\u00a0\3\2\2\2\35\u00a4\3")
        buf.write("\2\2\2\37\u00a9\3\2\2\2!\u00b1\3\2\2\2#\u00b7\3\2\2\2")
        buf.write("%\u00be\3\2\2\2\'\u00c5\3\2\2\2)\u00cb\3\2\2\2+\u00d4")
        buf.write("\3\2\2\2-\u00d7\3\2\2\2/\u00dc\3\2\2\2\61\u00e0\3\2\2")
        buf.write("\2\63\u00e6\3\2\2\2\65\u00e9\3\2\2\2\67\u00ee\3\2\2\2")
        buf.write("9\u00f4\3\2\2\2;\u00f6\3\2\2\2=\u00f8\3\2\2\2?\u00fa\3")
        buf.write("\2\2\2A\u00fd\3\2\2\2C\u0100\3\2\2\2E\u0102\3\2\2\2G\u0105")
        buf.write("\3\2\2\2I\u0107\3\2\2\2K\u0109\3\2\2\2M\u010b\3\2\2\2")
        buf.write("O\u010d\3\2\2\2Q\u0110\3\2\2\2S\u0113\3\2\2\2U\u0115\3")
        buf.write("\2\2\2W\u0119\3\2\2\2Y\u011d\3\2\2\2[\u011f\3\2\2\2]\u0138")
        buf.write("\3\2\2\2_\u013c\3\2\2\2a\u013e\3\2\2\2c\u0140\3\2\2\2")
        buf.write("e\u014b\3\2\2\2g\u0155\3\2\2\2i\u015e\3\2\2\2kl\7o\2\2")
        buf.write("lm\7c\2\2mn\7k\2\2no\7p\2\2o\4\3\2\2\2pq\7*\2\2q\6\3\2")
        buf.write("\2\2rs\7+\2\2s\b\3\2\2\2tu\7]\2\2u\n\3\2\2\2vw\7_\2\2")
        buf.write("w\f\3\2\2\2xy\7}\2\2y\16\3\2\2\2z{\7\177\2\2{\20\3\2\2")
        buf.write("\2|}\7=\2\2}\22\3\2\2\2~\177\7.\2\2\177\24\3\2\2\2\u0080")
        buf.write("\u0082\t\2\2\2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2")
        buf.write("\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\3")
        buf.write("\2\2\2\u0085\u0086\b\13\2\2\u0086\26\3\2\2\2\u0087\u0088")
        buf.write("\7\61\2\2\u0088\u0089\7\61\2\2\u0089\u008d\3\2\2\2\u008a")
        buf.write("\u008c\n\3\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0090\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\b\f\2\2\u0091\30")
        buf.write("\3\2\2\2\u0092\u0093\7\61\2\2\u0093\u0094\7,\2\2\u0094")
        buf.write("\u0098\3\2\2\2\u0095\u0097\13\2\2\2\u0096\u0095\3\2\2")
        buf.write("\2\u0097\u009a\3\2\2\2\u0098\u0099\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b")
        buf.write("\u009c\7,\2\2\u009c\u009d\7\61\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u009f\b\r\2\2\u009f\32\3\2\2\2\u00a0\u00a1\7k\2")
        buf.write("\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\34\3\2")
        buf.write("\2\2\u00a4\u00a5\7x\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7k\2\2\u00a7\u00a8\7f\2\2\u00a8\36\3\2\2\2\u00a9\u00aa")
        buf.write("\7d\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0 \3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\"\3\2\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00bd\7i\2\2\u00bd$\3\2\2\2\u00be\u00bf")
        buf.write("\7t\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7w\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7p\2\2\u00c4&\3")
        buf.write("\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7m\2\2\u00ca(\3")
        buf.write("\2\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3\7g\2\2\u00d3*\3")
        buf.write("\2\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7h\2\2\u00d6,\3")
        buf.write("\2\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\u00db\7g\2\2\u00db.\3\2\2\2\u00dc\u00dd")
        buf.write("\7h\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7t\2\2\u00df\60")
        buf.write("\3\2\2\2\u00e0\u00e1\7y\2\2\u00e1\u00e2\7j\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7g\2\2\u00e5\62")
        buf.write("\3\2\2\2\u00e6\u00e7\7f\2\2\u00e7\u00e8\7q\2\2\u00e8\64")
        buf.write("\3\2\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec")
        buf.write("\7w\2\2\u00ec\u00ed\7g\2\2\u00ed\66\3\2\2\2\u00ee\u00ef")
        buf.write("\7h\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2\u00f3\7g\2\2\u00f38\3\2\2\2\u00f4\u00f5")
        buf.write("\7-\2\2\u00f5:\3\2\2\2\u00f6\u00f7\7,\2\2\u00f7<\3\2\2")
        buf.write("\2\u00f8\u00f9\7#\2\2\u00f9>\3\2\2\2\u00fa\u00fb\7~\2")
        buf.write("\2\u00fb\u00fc\7~\2\2\u00fc@\3\2\2\2\u00fd\u00fe\7#\2")
        buf.write("\2\u00fe\u00ff\7?\2\2\u00ffB\3\2\2\2\u0100\u0101\7>\2")
        buf.write("\2\u0101D\3\2\2\2\u0102\u0103\7>\2\2\u0103\u0104\7?\2")
        buf.write("\2\u0104F\3\2\2\2\u0105\u0106\7?\2\2\u0106H\3\2\2\2\u0107")
        buf.write("\u0108\7/\2\2\u0108J\3\2\2\2\u0109\u010a\7\'\2\2\u010a")
        buf.write("L\3\2\2\2\u010b\u010c\7\61\2\2\u010cN\3\2\2\2\u010d\u010e")
        buf.write("\7(\2\2\u010e\u010f\7(\2\2\u010fP\3\2\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111\u0112\7?\2\2\u0112R\3\2\2\2\u0113\u0114")
        buf.write("\7@\2\2\u0114T\3\2\2\2\u0115\u0116\7@\2\2\u0116\u0117")
        buf.write("\7?\2\2\u0117V\3\2\2\2\u0118\u011a\t\4\2\2\u0119\u0118")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011cX\3\2\2\2\u011d\u011e\7\60\2\2\u011e")
        buf.write("Z\3\2\2\2\u011f\u0121\t\5\2\2\u0120\u0122\7/\2\2\u0121")
        buf.write("\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2")
        buf.write("\u0123\u0125\t\4\2\2\u0124\u0123\3\2\2\2\u0125\u0126\3")
        buf.write("\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\\")
        buf.write("\3\2\2\2\u0128\u0129\5W,\2\u0129\u012b\5Y-\2\u012a\u012c")
        buf.write("\5W,\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e")
        buf.write("\3\2\2\2\u012d\u012f\5[.\2\u012e\u012d\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\u0139\3\2\2\2\u0130\u0131\5Y-\2\u0131\u0133")
        buf.write("\5W,\2\u0132\u0134\5[.\2\u0133\u0132\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134\u0139\3\2\2\2\u0135\u0136\5W,\2\u0136\u0137")
        buf.write("\5[.\2\u0137\u0139\3\2\2\2\u0138\u0128\3\2\2\2\u0138\u0130")
        buf.write("\3\2\2\2\u0138\u0135\3\2\2\2\u0139^\3\2\2\2\u013a\u013d")
        buf.write("\5\65\33\2\u013b\u013d\5\67\34\2\u013c\u013a\3\2\2\2\u013c")
        buf.write("\u013b\3\2\2\2\u013d`\3\2\2\2\u013e\u013f\t\6\2\2\u013f")
        buf.write("b\3\2\2\2\u0140\u0146\7$\2\2\u0141\u0142\7^\2\2\u0142")
        buf.write("\u0145\t\7\2\2\u0143\u0145\n\b\2\2\u0144\u0141\3\2\2\2")
        buf.write("\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3")
        buf.write("\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014a\7$\2\2\u014ad\3\2\2\2\u014b\u014f")
        buf.write("\7$\2\2\u014c\u014e\n\b\2\2\u014d\u014c\3\2\2\2\u014e")
        buf.write("\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\7")
        buf.write("^\2\2\u0153\u0154\n\7\2\2\u0154f\3\2\2\2\u0155\u015b\7")
        buf.write("$\2\2\u0156\u0157\7^\2\2\u0157\u015a\t\7\2\2\u0158\u015a")
        buf.write("\n\b\2\2\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015ch\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0162\t\t\2")
        buf.write("\2\u015f\u0161\t\n\2\2\u0160\u015f\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("j\3\2\2\2\u0164\u0162\3\2\2\2\24\2\u0083\u008d\u0098\u011b")
        buf.write("\u0121\u0126\u012b\u012e\u0133\u0138\u013c\u0144\u0146")
        buf.write("\u014f\u0159\u015b\u0162\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LB = 2
    RB = 3
    LSB = 4
    RSB = 5
    LP = 6
    RP = 7
    SEMI = 8
    COMMA = 9
    WS = 10
    LINE_COMMENT = 11
    BLOCK_COMMENT = 12
    INTTYPE = 13
    VOIDTYPE = 14
    BOOLEANTYPE = 15
    FLOATTYPE = 16
    STRINGTYPE = 17
    RETURN = 18
    BREAK = 19
    CONTINUE = 20
    IF = 21
    ELSE = 22
    FOR = 23
    WHILE = 24
    DO = 25
    ADD_OP = 26
    MUL_OP = 27
    NOT_OP = 28
    OR_OP = 29
    NOT_EQUAL_OP = 30
    LESS_OP = 31
    LESS_EQUAL_OP = 32
    ASSIGN_OP = 33
    SUB_OP = 34
    MODULUS_OP = 35
    DIV_OP = 36
    AND_OP = 37
    EQUAL_OP = 38
    GREATER_OP = 39
    GREATER_EQUAL_OP = 40
    INTLIT = 41
    FLOATLIT = 42
    BOOLLIT = 43
    ERROR_CHAR = 44
    STRINGLIT = 45
    ILLEGAL_ESCAPE = 46
    UNCLOSE_STRING = 47
    ID = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", 
            "'int'", "'void'", "'boolean'", "'float'", "'string'", "'return'", 
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'while'", 
            "'do'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", 
            "'='", "'-'", "'%'", "'/'", "'&&'", "'=='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LSB", "RSB", "LP", "RP", "SEMI", "COMMA", "WS", 
            "LINE_COMMENT", "BLOCK_COMMENT", "INTTYPE", "VOIDTYPE", "BOOLEANTYPE", 
            "FLOATTYPE", "STRINGTYPE", "RETURN", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "WHILE", "DO", "ADD_OP", "MUL_OP", "NOT_OP", 
            "OR_OP", "NOT_EQUAL_OP", "LESS_OP", "LESS_EQUAL_OP", "ASSIGN_OP", 
            "SUB_OP", "MODULUS_OP", "DIV_OP", "AND_OP", "EQUAL_OP", "GREATER_OP", 
            "GREATER_EQUAL_OP", "INTLIT", "FLOATLIT", "BOOLLIT", "ERROR_CHAR", 
            "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ID" ]

    ruleNames = [ "T__0", "LB", "RB", "LSB", "RSB", "LP", "RP", "SEMI", 
                  "COMMA", "WS", "LINE_COMMENT", "BLOCK_COMMENT", "INTTYPE", 
                  "VOIDTYPE", "BOOLEANTYPE", "FLOATTYPE", "STRINGTYPE", 
                  "RETURN", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "WHILE", 
                  "DO", "TRUE", "FALSE", "ADD_OP", "MUL_OP", "NOT_OP", "OR_OP", 
                  "NOT_EQUAL_OP", "LESS_OP", "LESS_EQUAL_OP", "ASSIGN_OP", 
                  "SUB_OP", "MODULUS_OP", "DIV_OP", "AND_OP", "EQUAL_OP", 
                  "GREATER_OP", "GREATER_EQUAL_OP", "INTLIT", "Point", "Exponent", 
                  "FLOATLIT", "BOOLLIT", "ERROR_CHAR", "STRINGLIT", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ID" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        elif tk == self.STRINGLIT:
            result = super().emit();
            result.text = result.text[1:-1]
            return result 
        else:
            return super().emit();


