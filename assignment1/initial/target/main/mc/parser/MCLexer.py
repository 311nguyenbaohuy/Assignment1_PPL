# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0166\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6")
        buf.write("\13\u0082\n\13\r\13\16\13\u0083\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\7\r\u008e\n\r\f\r\16\r\u0091\13\r\3\16\3")
        buf.write("\16\3\16\3\16\7\16\u0097\n\16\f\16\16\16\u009a\13\16\3")
        buf.write("\17\3\17\3\17\3\17\7\17\u00a0\n\17\f\17\16\17\u00a3\13")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\7\20\u00ab\n\20\f\20")
        buf.write("\16\20\u00ae\13\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\6/\u012e\n/\r/\16/")
        buf.write("\u012f\3\60\3\60\3\61\3\61\5\61\u0136\n\61\3\61\3\61\7")
        buf.write("\61\u013a\n\61\f\61\16\61\u013d\13\61\3\62\3\62\3\62\5")
        buf.write("\62\u0142\n\62\3\62\5\62\u0145\n\62\3\62\3\62\3\62\5\62")
        buf.write("\u014a\n\62\3\62\3\62\3\62\5\62\u014f\n\62\3\63\3\63\5")
        buf.write("\63\u0153\n\63\3\64\3\64\3\64\3\64\7\64\u0159\n\64\f\64")
        buf.write("\16\64\u015c\13\64\3\64\3\64\3\65\3\65\7\65\u0162\n\65")
        buf.write("\f\65\16\65\u0165\13\65\3\u00ac\2\66\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\2a\2c\61e\62g\63i\64\3\2\16\5\2\13\f\17\17\"\"\13\2%")
        buf.write("&))\60\60<<AB^^``bb\u0080\u0080\t\2$$^^ddhhppttvv\6\2")
        buf.write("\n\f\16\17$$^^\b\2$$ddhhppttvv\3\2^^\4\2\f\f\17\17\3\2")
        buf.write("\62;\4\2GGgg\3\2\63;\5\2C\\aac|\6\2\62;C\\aac|\2\u0176")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3")
        buf.write("\2\2\2\5p\3\2\2\2\7r\3\2\2\2\tt\3\2\2\2\13v\3\2\2\2\r")
        buf.write("x\3\2\2\2\17z\3\2\2\2\21|\3\2\2\2\23~\3\2\2\2\25\u0081")
        buf.write("\3\2\2\2\27\u0087\3\2\2\2\31\u0089\3\2\2\2\33\u0092\3")
        buf.write("\2\2\2\35\u009b\3\2\2\2\37\u00a6\3\2\2\2!\u00b4\3\2\2")
        buf.write("\2#\u00b8\3\2\2\2%\u00bd\3\2\2\2\'\u00c5\3\2\2\2)\u00cb")
        buf.write("\3\2\2\2+\u00d2\3\2\2\2-\u00d9\3\2\2\2/\u00df\3\2\2\2")
        buf.write("\61\u00e8\3\2\2\2\63\u00eb\3\2\2\2\65\u00f0\3\2\2\2\67")
        buf.write("\u00f4\3\2\2\29\u00fa\3\2\2\2;\u00fd\3\2\2\2=\u0102\3")
        buf.write("\2\2\2?\u0108\3\2\2\2A\u010a\3\2\2\2C\u010c\3\2\2\2E\u010e")
        buf.write("\3\2\2\2G\u0111\3\2\2\2I\u0114\3\2\2\2K\u0116\3\2\2\2")
        buf.write("M\u0119\3\2\2\2O\u011b\3\2\2\2Q\u011d\3\2\2\2S\u011f\3")
        buf.write("\2\2\2U\u0121\3\2\2\2W\u0124\3\2\2\2Y\u0127\3\2\2\2[\u0129")
        buf.write("\3\2\2\2]\u012d\3\2\2\2_\u0131\3\2\2\2a\u0133\3\2\2\2")
        buf.write("c\u014e\3\2\2\2e\u0152\3\2\2\2g\u0154\3\2\2\2i\u015f\3")
        buf.write("\2\2\2kl\7o\2\2lm\7c\2\2mn\7k\2\2no\7p\2\2o\4\3\2\2\2")
        buf.write("pq\7*\2\2q\6\3\2\2\2rs\7+\2\2s\b\3\2\2\2tu\7]\2\2u\n\3")
        buf.write("\2\2\2vw\7_\2\2w\f\3\2\2\2xy\7}\2\2y\16\3\2\2\2z{\7\177")
        buf.write("\2\2{\20\3\2\2\2|}\7=\2\2}\22\3\2\2\2~\177\7.\2\2\177")
        buf.write("\24\3\2\2\2\u0080\u0082\t\2\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\u0085\3\2\2\2\u0085\u0086\b\13\2\2\u0086\26\3\2")
        buf.write("\2\2\u0087\u0088\t\3\2\2\u0088\30\3\2\2\2\u0089\u008f")
        buf.write("\7$\2\2\u008a\u008b\7^\2\2\u008b\u008e\t\4\2\2\u008c\u008e")
        buf.write("\n\5\2\2\u008d\u008a\3\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\32\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0098\7$\2")
        buf.write("\2\u0093\u0094\7^\2\2\u0094\u0097\n\6\2\2\u0095\u0097")
        buf.write("\n\7\2\2\u0096\u0093\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\34\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\7\61")
        buf.write("\2\2\u009c\u009d\7\61\2\2\u009d\u00a1\3\2\2\2\u009e\u00a0")
        buf.write("\n\b\2\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a4\u00a5\b\17\2\2\u00a5\36\3\2")
        buf.write("\2\2\u00a6\u00a7\7\61\2\2\u00a7\u00a8\7,\2\2\u00a8\u00ac")
        buf.write("\3\2\2\2\u00a9\u00ab\13\2\2\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ae\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ad\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\7")
        buf.write(",\2\2\u00b0\u00b1\7\61\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3")
        buf.write("\b\20\2\2\u00b3 \3\2\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\u00b7\7v\2\2\u00b7\"\3\2\2\2\u00b8\u00b9")
        buf.write("\7x\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc")
        buf.write("\7f\2\2\u00bc$\3\2\2\2\u00bd\u00be\7d\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7p\2\2\u00c4&\3")
        buf.write("\2\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8")
        buf.write("\7q\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7v\2\2\u00ca(\3")
        buf.write("\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7i\2\2\u00d1*\3\2\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7t\2\2\u00d7\u00d8\7p\2\2\u00d8,\3\2\2\2\u00d9\u00da")
        buf.write("\7d\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7c\2\2\u00dd\u00de\7m\2\2\u00de.\3\2\2\2\u00df\u00e0")
        buf.write("\7e\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7w\2\2\u00e6\u00e7\7g\2\2\u00e7\60\3\2\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7h\2\2\u00ea\62\3\2\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\64\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7t\2\2\u00f3\66\3\2\2\2\u00f4\u00f5")
        buf.write("\7y\2\2\u00f5\u00f6\7j\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7n\2\2\u00f8\u00f9\7g\2\2\u00f98\3\2\2\2\u00fa\u00fb")
        buf.write("\7f\2\2\u00fb\u00fc\7q\2\2\u00fc:\3\2\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7w\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101<\3\2\2\2\u0102\u0103\7h\2\2\u0103\u0104")
        buf.write("\7c\2\2\u0104\u0105\7n\2\2\u0105\u0106\7u\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107>\3\2\2\2\u0108\u0109\7-\2\2\u0109@\3\2\2")
        buf.write("\2\u010a\u010b\7,\2\2\u010bB\3\2\2\2\u010c\u010d\7#\2")
        buf.write("\2\u010dD\3\2\2\2\u010e\u010f\7~\2\2\u010f\u0110\7~\2")
        buf.write("\2\u0110F\3\2\2\2\u0111\u0112\7#\2\2\u0112\u0113\7?\2")
        buf.write("\2\u0113H\3\2\2\2\u0114\u0115\7>\2\2\u0115J\3\2\2\2\u0116")
        buf.write("\u0117\7>\2\2\u0117\u0118\7?\2\2\u0118L\3\2\2\2\u0119")
        buf.write("\u011a\7?\2\2\u011aN\3\2\2\2\u011b\u011c\7/\2\2\u011c")
        buf.write("P\3\2\2\2\u011d\u011e\7\'\2\2\u011eR\3\2\2\2\u011f\u0120")
        buf.write("\7\61\2\2\u0120T\3\2\2\2\u0121\u0122\7(\2\2\u0122\u0123")
        buf.write("\7(\2\2\u0123V\3\2\2\2\u0124\u0125\7?\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126X\3\2\2\2\u0127\u0128\7@\2\2\u0128Z\3\2\2")
        buf.write("\2\u0129\u012a\7@\2\2\u012a\u012b\7?\2\2\u012b\\\3\2\2")
        buf.write("\2\u012c\u012e\t\t\2\2\u012d\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("^\3\2\2\2\u0131\u0132\7\60\2\2\u0132`\3\2\2\2\u0133\u0135")
        buf.write("\t\n\2\2\u0134\u0136\7/\2\2\u0135\u0134\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u013b\t\13\2")
        buf.write("\2\u0138\u013a\t\t\2\2\u0139\u0138\3\2\2\2\u013a\u013d")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("b\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\5]/\2\u013f")
        buf.write("\u0141\5_\60\2\u0140\u0142\5]/\2\u0141\u0140\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u0145\5a\61\2")
        buf.write("\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u014f\3")
        buf.write("\2\2\2\u0146\u0147\5_\60\2\u0147\u0149\5]/\2\u0148\u014a")
        buf.write("\5a\61\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014f\3\2\2\2\u014b\u014c\5]/\2\u014c\u014d\5a\61\2\u014d")
        buf.write("\u014f\3\2\2\2\u014e\u013e\3\2\2\2\u014e\u0146\3\2\2\2")
        buf.write("\u014e\u014b\3\2\2\2\u014fd\3\2\2\2\u0150\u0153\5;\36")
        buf.write("\2\u0151\u0153\5=\37\2\u0152\u0150\3\2\2\2\u0152\u0151")
        buf.write("\3\2\2\2\u0153f\3\2\2\2\u0154\u015a\7$\2\2\u0155\u0156")
        buf.write("\7^\2\2\u0156\u0159\t\4\2\2\u0157\u0159\n\5\2\2\u0158")
        buf.write("\u0155\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7$\2\2\u015eh\3")
        buf.write("\2\2\2\u015f\u0163\t\f\2\2\u0160\u0162\t\r\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164j\3\2\2\2\u0165\u0163\3\2\2\2\25\2")
        buf.write("\u0083\u008d\u008f\u0096\u0098\u00a1\u00ac\u012f\u0135")
        buf.write("\u013b\u0141\u0144\u0149\u014e\u0152\u0158\u015a\u0163")
        buf.write("\3\b\2\2")
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
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13
    LINE_COMMENT = 14
    BLOCK_COMMENT = 15
    INTTYPE = 16
    VOIDTYPE = 17
    BOOLEANTYPE = 18
    FLOATTYPE = 19
    STRINGTYPE = 20
    RETURN = 21
    BREAK = 22
    CONTINUE = 23
    IF = 24
    ELSE = 25
    FOR = 26
    WHILE = 27
    DO = 28
    TRUE = 29
    FALSE = 30
    ADD_OP = 31
    MUL_OP = 32
    NOT_OP = 33
    OR_OP = 34
    NOT_EQUAL_OP = 35
    LESS_OP = 36
    LESS_EQUAL_OP = 37
    ASSIGN_OP = 38
    SUB_OP = 39
    MODULUS_OP = 40
    DIV_OP = 41
    AND_OP = 42
    EQUAL_OP = 43
    GREATER_OP = 44
    GREATER_EQUAL_OP = 45
    INTLIT = 46
    FLOATLIT = 47
    BOOLLIT = 48
    STRINGLIT = 49
    ID = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", 
            "'int'", "'void'", "'boolean'", "'float'", "'string'", "'return'", 
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'while'", 
            "'do'", "'true'", "'false'", "'+'", "'*'", "'!'", "'||'", "'!='", 
            "'<'", "'<='", "'='", "'-'", "'%'", "'/'", "'&&'", "'=='", "'>'", 
            "'>='" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LSB", "RSB", "LP", "RP", "SEMI", "COMMA", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "LINE_COMMENT", 
            "BLOCK_COMMENT", "INTTYPE", "VOIDTYPE", "BOOLEANTYPE", "FLOATTYPE", 
            "STRINGTYPE", "RETURN", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
            "WHILE", "DO", "TRUE", "FALSE", "ADD_OP", "MUL_OP", "NOT_OP", 
            "OR_OP", "NOT_EQUAL_OP", "LESS_OP", "LESS_EQUAL_OP", "ASSIGN_OP", 
            "SUB_OP", "MODULUS_OP", "DIV_OP", "AND_OP", "EQUAL_OP", "GREATER_OP", 
            "GREATER_EQUAL_OP", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "ID" ]

    ruleNames = [ "T__0", "LB", "RB", "LSB", "RSB", "LP", "RP", "SEMI", 
                  "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "LINE_COMMENT", "BLOCK_COMMENT", "INTTYPE", "VOIDTYPE", 
                  "BOOLEANTYPE", "FLOATTYPE", "STRINGTYPE", "RETURN", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "FOR", "WHILE", "DO", "TRUE", 
                  "FALSE", "ADD_OP", "MUL_OP", "NOT_OP", "OR_OP", "NOT_EQUAL_OP", 
                  "LESS_OP", "LESS_EQUAL_OP", "ASSIGN_OP", "SUB_OP", "MODULUS_OP", 
                  "DIV_OP", "AND_OP", "EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                  "INTLIT", "Point", "Exponent", "FLOATLIT", "BOOLLIT", 
                  "STRINGLIT", "ID" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


