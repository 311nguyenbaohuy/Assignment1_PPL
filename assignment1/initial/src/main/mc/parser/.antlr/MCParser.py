# Generated from /home/huy/Documents/PPL/Ass1/assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u0167\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\5\2J\n")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3T\n\3\r\3\16\3U")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\5\6_\n\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\7\no\n\n\f\n")
        buf.write("\16\nr\13\n\3\13\3\13\5\13v\n\13\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\7\r\177\n\r\f\r\16\r\u0082\13\r\3\16\3\16\5\16")
        buf.write("\u0086\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\7\20\u0092\n\20\f\20\16\20\u0095\13\20\5\20\u0097")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00a1")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\7\23\u00ab")
        buf.write("\n\23\f\23\16\23\u00ae\13\23\5\23\u00b0\n\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\5\25\u00b7\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u00c2\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u00d3\n\27\3\30\3\30\6\30\u00d7\n\30\r\30\16")
        buf.write("\30\u00d8\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\5\34\u00f1\n\34\3\34\3\34\3\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0100\n\36")
        buf.write("\3\37\3\37\5\37\u0104\n\37\3 \3 \3 \7 \u0109\n \f \16")
        buf.write(" \u010c\13 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u011a")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\5\"\u013a\n\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u014b\n\"\f\"")
        buf.write("\16\"\u014e\13\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\7")
        buf.write("#\u015c\n#\f#\16#\u015f\13#\3$\3$\3$\3$\5$\u0165\n$\3")
        buf.write("$\2\4BD%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDF\2\4\3\2\60\63\4\2\22\22\24\26")
        buf.write("\2\u0175\2I\3\2\2\2\4S\3\2\2\2\6W\3\2\2\2\bY\3\2\2\2\n")
        buf.write("^\3\2\2\2\f`\3\2\2\2\16c\3\2\2\2\20g\3\2\2\2\22l\3\2\2")
        buf.write("\2\24u\3\2\2\2\26w\3\2\2\2\30{\3\2\2\2\32\u0085\3\2\2")
        buf.write("\2\34\u0087\3\2\2\2\36\u0096\3\2\2\2 \u00a0\3\2\2\2\"")
        buf.write("\u00a2\3\2\2\2$\u00af\3\2\2\2&\u00b1\3\2\2\2(\u00b6\3")
        buf.write("\2\2\2*\u00c1\3\2\2\2,\u00d2\3\2\2\2.\u00d4\3\2\2\2\60")
        buf.write("\u00de\3\2\2\2\62\u00e8\3\2\2\2\64\u00eb\3\2\2\2\66\u00ee")
        buf.write("\3\2\2\28\u00f4\3\2\2\2:\u00ff\3\2\2\2<\u0103\3\2\2\2")
        buf.write(">\u0105\3\2\2\2@\u0119\3\2\2\2B\u0139\3\2\2\2D\u014f\3")
        buf.write("\2\2\2F\u0164\3\2\2\2HJ\5\22\n\2IH\3\2\2\2IJ\3\2\2\2J")
        buf.write("K\3\2\2\2KL\5\n\6\2LM\7\3\2\2MN\7\4\2\2NO\7\5\2\2OP\5")
        buf.write("> \2PQ\7\2\2\3Q\3\3\2\2\2RT\5<\37\2SR\3\2\2\2TU\3\2\2")
        buf.write("\2US\3\2\2\2UV\3\2\2\2V\5\3\2\2\2WX\t\2\2\2X\7\3\2\2\2")
        buf.write("YZ\t\3\2\2Z\t\3\2\2\2[_\5\b\5\2\\_\7\23\2\2]_\5\16\b\2")
        buf.write("^[\3\2\2\2^\\\3\2\2\2^]\3\2\2\2_\13\3\2\2\2`a\5\b\5\2")
        buf.write("ab\5\20\t\2b\r\3\2\2\2cd\5\b\5\2de\7\6\2\2ef\7\7\2\2f")
        buf.write("\17\3\2\2\2gh\7\64\2\2hi\7\6\2\2ij\7\60\2\2jk\7\7\2\2")
        buf.write("k\21\3\2\2\2lp\5\24\13\2mo\5\24\13\2nm\3\2\2\2or\3\2\2")
        buf.write("\2pn\3\2\2\2pq\3\2\2\2q\23\3\2\2\2rp\3\2\2\2sv\5\26\f")
        buf.write("\2tv\5\34\17\2us\3\2\2\2ut\3\2\2\2v\25\3\2\2\2wx\5\b\5")
        buf.write("\2xy\5\30\r\2yz\7\n\2\2z\27\3\2\2\2{\u0080\5\32\16\2|")
        buf.write("}\7\13\2\2}\177\5\32\16\2~|\3\2\2\2\177\u0082\3\2\2\2")
        buf.write("\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\31\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0083\u0086\7\64\2\2\u0084\u0086\5\20\t")
        buf.write("\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086\33\3")
        buf.write("\2\2\2\u0087\u0088\5\n\6\2\u0088\u0089\7\64\2\2\u0089")
        buf.write("\u008a\7\4\2\2\u008a\u008b\5\36\20\2\u008b\u008c\7\5\2")
        buf.write("\2\u008c\u008d\5> \2\u008d\35\3\2\2\2\u008e\u0093\5 \21")
        buf.write("\2\u008f\u0090\7\13\2\2\u0090\u0092\5 \21\2\u0091\u008f")
        buf.write("\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0096\u008e\3\2\2\2\u0096\u0097\3\2\2\2\u0097\37\3\2")
        buf.write("\2\2\u0098\u0099\5\b\5\2\u0099\u009a\7\64\2\2\u009a\u00a1")
        buf.write("\3\2\2\2\u009b\u009c\5\b\5\2\u009c\u009d\7\64\2\2\u009d")
        buf.write("\u009e\7\6\2\2\u009e\u009f\7\7\2\2\u009f\u00a1\3\2\2\2")
        buf.write("\u00a0\u0098\3\2\2\2\u00a0\u009b\3\2\2\2\u00a1!\3\2\2")
        buf.write("\2\u00a2\u00a3\7\64\2\2\u00a3\u00a4\7\4\2\2\u00a4\u00a5")
        buf.write("\5$\23\2\u00a5\u00a6\7\5\2\2\u00a6#\3\2\2\2\u00a7\u00ac")
        buf.write("\5@!\2\u00a8\u00a9\7\13\2\2\u00a9\u00ab\5@!\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00af\u00a7\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0%\3\2\2")
        buf.write("\2\u00b1\u00b2\5\"\22\2\u00b2\u00b3\7\n\2\2\u00b3\'\3")
        buf.write("\2\2\2\u00b4\u00b7\5*\26\2\u00b5\u00b7\5,\27\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7)\3\2\2\2\u00b8\u00b9")
        buf.write("\7\32\2\2\u00b9\u00ba\7\4\2\2\u00ba\u00bb\5@!\2\u00bb")
        buf.write("\u00bc\7\5\2\2\u00bc\u00bd\5*\26\2\u00bd\u00be\7\33\2")
        buf.write("\2\u00be\u00bf\5*\26\2\u00bf\u00c2\3\2\2\2\u00c0\u00c2")
        buf.write("\5:\36\2\u00c1\u00b8\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write("+\3\2\2\2\u00c3\u00c4\7\32\2\2\u00c4\u00c5\7\4\2\2\u00c5")
        buf.write("\u00c6\5@!\2\u00c6\u00c7\7\5\2\2\u00c7\u00c8\5*\26\2\u00c8")
        buf.write("\u00c9\7\33\2\2\u00c9\u00ca\5,\27\2\u00ca\u00d3\3\2\2")
        buf.write("\2\u00cb\u00cc\7\32\2\2\u00cc\u00cd\7\4\2\2\u00cd\u00ce")
        buf.write("\5@!\2\u00ce\u00cf\7\5\2\2\u00cf\u00d0\5<\37\2\u00d0\u00d3")
        buf.write("\3\2\2\2\u00d1\u00d3\5:\36\2\u00d2\u00c3\3\2\2\2\u00d2")
        buf.write("\u00cb\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3-\3\2\2\2\u00d4")
        buf.write("\u00d6\7\36\2\2\u00d5\u00d7\5<\37\2\u00d6\u00d5\3\2\2")
        buf.write("\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\7\35\2\2\u00db")
        buf.write("\u00dc\5@!\2\u00dc\u00dd\7\n\2\2\u00dd/\3\2\2\2\u00de")
        buf.write("\u00df\7\34\2\2\u00df\u00e0\7\4\2\2\u00e0\u00e1\5@!\2")
        buf.write("\u00e1\u00e2\7\n\2\2\u00e2\u00e3\5@!\2\u00e3\u00e4\7\n")
        buf.write("\2\2\u00e4\u00e5\5@!\2\u00e5\u00e6\7\5\2\2\u00e6\u00e7")
        buf.write("\5<\37\2\u00e7\61\3\2\2\2\u00e8\u00e9\7\30\2\2\u00e9\u00ea")
        buf.write("\7\n\2\2\u00ea\63\3\2\2\2\u00eb\u00ec\7\31\2\2\u00ec\u00ed")
        buf.write("\7\n\2\2\u00ed\65\3\2\2\2\u00ee\u00f0\7\27\2\2\u00ef\u00f1")
        buf.write("\5@!\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f3\7\n\2\2\u00f3\67\3\2\2\2\u00f4\u00f5")
        buf.write("\5@!\2\u00f5\u00f6\7\n\2\2\u00f69\3\2\2\2\u00f7\u0100")
        buf.write("\5&\24\2\u00f8\u0100\5\26\f\2\u00f9\u0100\5.\30\2\u00fa")
        buf.write("\u0100\5\60\31\2\u00fb\u0100\5\62\32\2\u00fc\u0100\5\64")
        buf.write("\33\2\u00fd\u0100\5\66\34\2\u00fe\u0100\58\35\2\u00ff")
        buf.write("\u00f7\3\2\2\2\u00ff\u00f8\3\2\2\2\u00ff\u00f9\3\2\2\2")
        buf.write("\u00ff\u00fa\3\2\2\2\u00ff\u00fb\3\2\2\2\u00ff\u00fc\3")
        buf.write("\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100;")
        buf.write("\3\2\2\2\u0101\u0104\5:\36\2\u0102\u0104\5(\25\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0102\3\2\2\2\u0104=\3\2\2\2\u0105")
        buf.write("\u010a\7\b\2\2\u0106\u0109\5<\37\2\u0107\u0109\5> \2\u0108")
        buf.write("\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2")
        buf.write("\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010d\3")
        buf.write("\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\7\t\2\2\u010e?")
        buf.write("\3\2\2\2\u010f\u0110\7\4\2\2\u0110\u0111\5@!\2\u0111\u0112")
        buf.write("\7\5\2\2\u0112\u011a\3\2\2\2\u0113\u0114\5B\"\2\u0114")
        buf.write("\u0115\7\6\2\2\u0115\u0116\5B\"\2\u0116\u0117\7\7\2\2")
        buf.write("\u0117\u011a\3\2\2\2\u0118\u011a\5B\"\2\u0119\u010f\3")
        buf.write("\2\2\2\u0119\u0113\3\2\2\2\u0119\u0118\3\2\2\2\u011aA")
        buf.write("\3\2\2\2\u011b\u011c\b\"\1\2\u011c\u011d\7)\2\2\u011d")
        buf.write("\u013a\5B\"\20\u011e\u011f\7#\2\2\u011f\u013a\5B\"\17")
        buf.write("\u0120\u0121\5D#\2\u0121\u0122\7\'\2\2\u0122\u0123\5D")
        buf.write("#\2\u0123\u013a\3\2\2\2\u0124\u0125\5D#\2\u0125\u0126")
        buf.write("\7&\2\2\u0126\u0127\5D#\2\u0127\u013a\3\2\2\2\u0128\u0129")
        buf.write("\5D#\2\u0129\u012a\7/\2\2\u012a\u012b\5D#\2\u012b\u013a")
        buf.write("\3\2\2\2\u012c\u012d\5D#\2\u012d\u012e\7.\2\2\u012e\u012f")
        buf.write("\5D#\2\u012f\u013a\3\2\2\2\u0130\u0131\5D#\2\u0131\u0132")
        buf.write("\7-\2\2\u0132\u0133\5D#\2\u0133\u013a\3\2\2\2\u0134\u0135")
        buf.write("\5D#\2\u0135\u0136\7%\2\2\u0136\u0137\5D#\2\u0137\u013a")
        buf.write("\3\2\2\2\u0138\u013a\5D#\2\u0139\u011b\3\2\2\2\u0139\u011e")
        buf.write("\3\2\2\2\u0139\u0120\3\2\2\2\u0139\u0124\3\2\2\2\u0139")
        buf.write("\u0128\3\2\2\2\u0139\u012c\3\2\2\2\u0139\u0130\3\2\2\2")
        buf.write("\u0139\u0134\3\2\2\2\u0139\u0138\3\2\2\2\u013a\u014c\3")
        buf.write("\2\2\2\u013b\u013c\f\16\2\2\u013c\u013d\7+\2\2\u013d\u014b")
        buf.write("\5B\"\17\u013e\u013f\f\r\2\2\u013f\u0140\7\"\2\2\u0140")
        buf.write("\u014b\5B\"\16\u0141\u0142\f\f\2\2\u0142\u0143\7*\2\2")
        buf.write("\u0143\u014b\5B\"\r\u0144\u0145\f\13\2\2\u0145\u0146\7")
        buf.write("!\2\2\u0146\u014b\5B\"\f\u0147\u0148\f\n\2\2\u0148\u0149")
        buf.write("\7)\2\2\u0149\u014b\5B\"\13\u014a\u013b\3\2\2\2\u014a")
        buf.write("\u013e\3\2\2\2\u014a\u0141\3\2\2\2\u014a\u0144\3\2\2\2")
        buf.write("\u014a\u0147\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3")
        buf.write("\2\2\2\u014c\u014d\3\2\2\2\u014dC\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014f\u0150\b#\1\2\u0150\u0151\5F$\2\u0151\u015d")
        buf.write("\3\2\2\2\u0152\u0153\f\6\2\2\u0153\u0154\7,\2\2\u0154")
        buf.write("\u015c\5D#\7\u0155\u0156\f\5\2\2\u0156\u0157\7$\2\2\u0157")
        buf.write("\u015c\5D#\6\u0158\u0159\f\4\2\2\u0159\u015a\7(\2\2\u015a")
        buf.write("\u015c\5@!\2\u015b\u0152\3\2\2\2\u015b\u0155\3\2\2\2\u015b")
        buf.write("\u0158\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015eE\3\2\2\2\u015f\u015d\3\2\2")
        buf.write("\2\u0160\u0165\5\"\22\2\u0161\u0165\5\6\4\2\u0162\u0165")
        buf.write("\7\64\2\2\u0163\u0165\5\20\t\2\u0164\u0160\3\2\2\2\u0164")
        buf.write("\u0161\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2")
        buf.write("\u0165G\3\2\2\2\36IU^pu\u0080\u0085\u0093\u0096\u00a0")
        buf.write("\u00ac\u00af\u00b6\u00c1\u00d2\u00d8\u00f0\u00ff\u0103")
        buf.write("\u0108\u010a\u0119\u0139\u014a\u014c\u015b\u015d\u0164")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "';'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'int'", "'void'", "'boolean'", "'float'", "'string'", 
                     "'return'", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'while'", "'do'", "'true'", "'false'", "'+'", 
                     "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", "'='", 
                     "'-'", "'%'", "'/'", "'&&'", "'=='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LB", "RB", "LSB", "RSB", 
                      "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "INTTYPE", "VOIDTYPE", "BOOLEANTYPE", "FLOATTYPE", 
                      "STRINGTYPE", "RETURN", "BREAK", "CONTINUE", "IF", 
                      "ELSE", "FOR", "WHILE", "DO", "TRUE", "FALSE", "ADD_OP", 
                      "MUL_OP", "NOT_OP", "OR_OP", "NOT_EQUAL_OP", "LESS_OP", 
                      "LESS_EQUAL_OP", "ASSIGN_OP", "SUB_OP", "MODULUS_OP", 
                      "DIV_OP", "AND_OP", "EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                      "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ID" ]

    RULE_program = 0
    RULE_body = 1
    RULE_lit = 2
    RULE_primary_type = 3
    RULE_mctype = 4
    RULE_input_ptr_type = 5
    RULE_output_ptr_type = 6
    RULE_element = 7
    RULE_many_decls = 8
    RULE_decl = 9
    RULE_var_decl = 10
    RULE_many_vars = 11
    RULE_var = 12
    RULE_func_decl = 13
    RULE_list_params = 14
    RULE_param_decl = 15
    RULE_call_func = 16
    RULE_list_exprs = 17
    RULE_func_stmt = 18
    RULE_if_stmt = 19
    RULE_match_stmt = 20
    RULE_unmatch_stmt = 21
    RULE_do_while_stmt = 22
    RULE_for_stmt = 23
    RULE_break_stmt = 24
    RULE_continue_stmt = 25
    RULE_return_stmt = 26
    RULE_expr_stmt = 27
    RULE_other = 28
    RULE_stmt = 29
    RULE_block_stmt = 30
    RULE_expr = 31
    RULE_expr1 = 32
    RULE_expr2 = 33
    RULE_op = 34

    ruleNames =  [ "program", "body", "lit", "primary_type", "mctype", "input_ptr_type", 
                   "output_ptr_type", "element", "many_decls", "decl", "var_decl", 
                   "many_vars", "var", "func_decl", "list_params", "param_decl", 
                   "call_func", "list_exprs", "func_stmt", "if_stmt", "match_stmt", 
                   "unmatch_stmt", "do_while_stmt", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "expr_stmt", "other", 
                   "stmt", "block_stmt", "expr", "expr1", "expr2", "op" ]

    EOF = Token.EOF
    T__0=1
    LB=2
    RB=3
    LSB=4
    RSB=5
    LP=6
    RP=7
    SEMI=8
    COMMA=9
    WS=10
    ERROR_CHAR=11
    UNCLOSE_STRING=12
    ILLEGAL_ESCAPE=13
    LINE_COMMENT=14
    BLOCK_COMMENT=15
    INTTYPE=16
    VOIDTYPE=17
    BOOLEANTYPE=18
    FLOATTYPE=19
    STRINGTYPE=20
    RETURN=21
    BREAK=22
    CONTINUE=23
    IF=24
    ELSE=25
    FOR=26
    WHILE=27
    DO=28
    TRUE=29
    FALSE=30
    ADD_OP=31
    MUL_OP=32
    NOT_OP=33
    OR_OP=34
    NOT_EQUAL_OP=35
    LESS_OP=36
    LESS_EQUAL_OP=37
    ASSIGN_OP=38
    SUB_OP=39
    MODULUS_OP=40
    DIV_OP=41
    AND_OP=42
    EQUAL_OP=43
    GREATER_OP=44
    GREATER_EQUAL_OP=45
    INTLIT=46
    FLOATLIT=47
    BOOLLIT=48
    STRINGLIT=49
    ID=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
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

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def many_decls(self):
            return self.getTypedRuleContext(MCParser.Many_declsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 70
                self.many_decls()


            self.state = 73
            self.mctype()
            self.state = 74
            self.match(MCParser.T__0)
            self.state = 75
            self.match(MCParser.LB)
            self.state = 76
            self.match(MCParser.RB)
            self.state = 77
            self.block_stmt()
            self.state = 78
            self.match(MCParser.EOF)
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_body




    def body(self):

        localctx = MCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.stmt()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LB) | (1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.RETURN) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.IF) | (1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.NOT_OP) | (1 << MCParser.SUB_OP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_lit




    def lit(self):

        localctx = MCParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0)):
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

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEANTYPE(self):
            return self.getToken(MCParser.BOOLEANTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primary_type




    def primary_type(self):

        localctx = MCParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primary_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
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

    class MctypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_type(self):
            return self.getTypedRuleContext(MCParser.Primary_typeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def output_ptr_type(self):
            return self.getTypedRuleContext(MCParser.Output_ptr_typeContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_mctype




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mctype)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.primary_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.output_ptr_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Input_ptr_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_type(self):
            return self.getTypedRuleContext(MCParser.Primary_typeContext,0)


        def element(self):
            return self.getTypedRuleContext(MCParser.ElementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_input_ptr_type




    def input_ptr_type(self):

        localctx = MCParser.Input_ptr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_input_ptr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.primary_type()
            self.state = 95
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Output_ptr_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_type(self):
            return self.getTypedRuleContext(MCParser.Primary_typeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_output_ptr_type




    def output_ptr_type(self):

        localctx = MCParser.Output_ptr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_output_ptr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.primary_type()
            self.state = 98
            self.match(MCParser.LSB)
            self.state = 99
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_element




    def element(self):

        localctx = MCParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MCParser.ID)
            self.state = 102
            self.match(MCParser.LSB)
            self.state = 103
            self.match(MCParser.INTLIT)
            self.state = 104
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Many_declsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_many_decls




    def many_decls(self):

        localctx = MCParser.Many_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_many_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.decl()
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 107
                    self.decl() 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MCParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MCParser.Func_declContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decl




    def decl(self):

        localctx = MCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decl)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.func_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_type(self):
            return self.getTypedRuleContext(MCParser.Primary_typeContext,0)


        def many_vars(self):
            return self.getTypedRuleContext(MCParser.Many_varsContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var_decl




    def var_decl(self):

        localctx = MCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.primary_type()
            self.state = 118
            self.many_vars()
            self.state = 119
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Many_varsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_many_vars




    def many_vars(self):

        localctx = MCParser.Many_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_many_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.var()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 122
                self.match(MCParser.COMMA)
                self.state = 123
                self.var()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def element(self):
            return self.getTypedRuleContext(MCParser.ElementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_var




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(MCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def list_params(self):
            return self.getTypedRuleContext(MCParser.List_paramsContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_decl




    def func_decl(self):

        localctx = MCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.mctype()
            self.state = 134
            self.match(MCParser.ID)
            self.state = 135
            self.match(MCParser.LB)
            self.state = 136
            self.list_params()
            self.state = 137
            self.match(MCParser.RB)
            self.state = 138
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Param_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Param_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_params




    def list_params(self):

        localctx = MCParser.List_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 140
                self.param_decl()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 141
                    self.match(MCParser.COMMA)
                    self.state = 142
                    self.param_decl()
                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_type(self):
            return self.getTypedRuleContext(MCParser.Primary_typeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_param_decl




    def param_decl(self):

        localctx = MCParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param_decl)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.primary_type()
                self.state = 151
                self.match(MCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.primary_type()
                self.state = 154
                self.match(MCParser.ID)
                self.state = 155
                self.match(MCParser.LSB)
                self.state = 156
                self.match(MCParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def list_exprs(self):
            return self.getTypedRuleContext(MCParser.List_exprsContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_call_func




    def call_func(self):

        localctx = MCParser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MCParser.ID)
            self.state = 161
            self.match(MCParser.LB)
            self.state = 162
            self.list_exprs()
            self.state = 163
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_exprsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_exprs




    def list_exprs(self):

        localctx = MCParser.List_exprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_list_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LB) | (1 << MCParser.NOT_OP) | (1 << MCParser.SUB_OP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID))) != 0):
                self.state = 165
                self.expr()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 166
                    self.match(MCParser.COMMA)
                    self.state = 167
                    self.expr()
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func(self):
            return self.getTypedRuleContext(MCParser.Call_funcContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_func_stmt




    def func_stmt(self):

        localctx = MCParser.Func_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.call_func()
            self.state = 176
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def match_stmt(self):
            return self.getTypedRuleContext(MCParser.Match_stmtContext,0)


        def unmatch_stmt(self):
            return self.getTypedRuleContext(MCParser.Unmatch_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stmt)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.unmatch_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Match_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def match_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Match_stmtContext)
            else:
                return self.getTypedRuleContext(MCParser.Match_stmtContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def other(self):
            return self.getTypedRuleContext(MCParser.OtherContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_match_stmt




    def match_stmt(self):

        localctx = MCParser.Match_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_match_stmt)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(MCParser.IF)
                self.state = 183
                self.match(MCParser.LB)
                self.state = 184
                self.expr()
                self.state = 185
                self.match(MCParser.RB)
                self.state = 186
                self.match_stmt()
                self.state = 187
                self.match(MCParser.ELSE)
                self.state = 188
                self.match_stmt()
                pass
            elif token in [MCParser.LB, MCParser.INTTYPE, MCParser.BOOLEANTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE, MCParser.RETURN, MCParser.BREAK, MCParser.CONTINUE, MCParser.FOR, MCParser.DO, MCParser.NOT_OP, MCParser.SUB_OP, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT, MCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.other()
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

    class Unmatch_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def match_stmt(self):
            return self.getTypedRuleContext(MCParser.Match_stmtContext,0)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def unmatch_stmt(self):
            return self.getTypedRuleContext(MCParser.Unmatch_stmtContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def other(self):
            return self.getTypedRuleContext(MCParser.OtherContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_unmatch_stmt




    def unmatch_stmt(self):

        localctx = MCParser.Unmatch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_unmatch_stmt)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(MCParser.IF)
                self.state = 194
                self.match(MCParser.LB)
                self.state = 195
                self.expr()
                self.state = 196
                self.match(MCParser.RB)
                self.state = 197
                self.match_stmt()
                self.state = 198
                self.match(MCParser.ELSE)
                self.state = 199
                self.unmatch_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(MCParser.IF)
                self.state = 202
                self.match(MCParser.LB)
                self.state = 203
                self.expr()
                self.state = 204
                self.match(MCParser.RB)
                self.state = 205
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.other()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_while_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_do_while_stmt




    def do_while_stmt(self):

        localctx = MCParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_do_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MCParser.DO)
            self.state = 212 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 211
                self.stmt()
                self.state = 214 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LB) | (1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.RETURN) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.IF) | (1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.NOT_OP) | (1 << MCParser.SUB_OP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID))) != 0)):
                    break

            self.state = 216
            self.match(MCParser.WHILE)
            self.state = 217
            self.expr()
            self.state = 218
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MCParser.FOR)
            self.state = 221
            self.match(MCParser.LB)
            self.state = 222
            self.expr()
            self.state = 223
            self.match(MCParser.SEMI)
            self.state = 224
            self.expr()
            self.state = 225
            self.match(MCParser.SEMI)
            self.state = 226
            self.expr()
            self.state = 227
            self.match(MCParser.RB)
            self.state = 228
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MCParser.BREAK)
            self.state = 231
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MCParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MCParser.CONTINUE)
            self.state = 234
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MCParser.RETURN)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LB) | (1 << MCParser.NOT_OP) | (1 << MCParser.SUB_OP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID))) != 0):
                self.state = 237
                self.expr()


            self.state = 240
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr_stmt




    def expr_stmt(self):

        localctx = MCParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expr()
            self.state = 243
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OtherContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_stmt(self):
            return self.getTypedRuleContext(MCParser.Func_stmtContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MCParser.Var_declContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MCParser.Do_while_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MCParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MCParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MCParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MCParser.Return_stmtContext,0)


        def expr_stmt(self):
            return self.getTypedRuleContext(MCParser.Expr_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_other




    def other(self):

        localctx = MCParser.OtherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_other)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.func_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.do_while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 248
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 249
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 250
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 251
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 252
                self.expr_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def other(self):
            return self.getTypedRuleContext(MCParser.OtherContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MCParser.If_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.other()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.if_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(MCParser.Block_stmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_stmt




    def block_stmt(self):

        localctx = MCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MCParser.LP)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.RETURN) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.IF) | (1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.NOT_OP) | (1 << MCParser.SUB_OP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID))) != 0):
                self.state = 262
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.LB, MCParser.INTTYPE, MCParser.BOOLEANTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE, MCParser.RETURN, MCParser.BREAK, MCParser.CONTINUE, MCParser.IF, MCParser.FOR, MCParser.DO, MCParser.NOT_OP, MCParser.SUB_OP, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT, MCParser.ID]:
                    self.state = 260
                    self.stmt()
                    pass
                elif token in [MCParser.LP]:
                    self.state = 261
                    self.block_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 267
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr1Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr1Context,i)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr




    def expr(self):

        localctx = MCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(MCParser.LB)
                self.state = 270
                self.expr()
                self.state = 271
                self.match(MCParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expr1(0)
                self.state = 274
                self.match(MCParser.LSB)
                self.state = 275
                self.expr1(0)
                self.state = 276
                self.match(MCParser.RSB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(MCParser.SUB_OP, 0)

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr1Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr1Context,i)


        def NOT_OP(self):
            return self.getToken(MCParser.NOT_OP, 0)

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr2Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr2Context,i)


        def LESS_EQUAL_OP(self):
            return self.getToken(MCParser.LESS_EQUAL_OP, 0)

        def LESS_OP(self):
            return self.getToken(MCParser.LESS_OP, 0)

        def GREATER_EQUAL_OP(self):
            return self.getToken(MCParser.GREATER_EQUAL_OP, 0)

        def GREATER_OP(self):
            return self.getToken(MCParser.GREATER_OP, 0)

        def EQUAL_OP(self):
            return self.getToken(MCParser.EQUAL_OP, 0)

        def NOT_EQUAL_OP(self):
            return self.getToken(MCParser.NOT_EQUAL_OP, 0)

        def DIV_OP(self):
            return self.getToken(MCParser.DIV_OP, 0)

        def MUL_OP(self):
            return self.getToken(MCParser.MUL_OP, 0)

        def MODULUS_OP(self):
            return self.getToken(MCParser.MODULUS_OP, 0)

        def ADD_OP(self):
            return self.getToken(MCParser.ADD_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 282
                self.match(MCParser.SUB_OP)
                self.state = 283
                self.expr1(14)
                pass

            elif la_ == 2:
                self.state = 284
                self.match(MCParser.NOT_OP)
                self.state = 285
                self.expr1(13)
                pass

            elif la_ == 3:
                self.state = 286
                self.expr2(0)
                self.state = 287
                self.match(MCParser.LESS_EQUAL_OP)
                self.state = 288
                self.expr2(0)
                pass

            elif la_ == 4:
                self.state = 290
                self.expr2(0)
                self.state = 291
                self.match(MCParser.LESS_OP)
                self.state = 292
                self.expr2(0)
                pass

            elif la_ == 5:
                self.state = 294
                self.expr2(0)
                self.state = 295
                self.match(MCParser.GREATER_EQUAL_OP)
                self.state = 296
                self.expr2(0)
                pass

            elif la_ == 6:
                self.state = 298
                self.expr2(0)
                self.state = 299
                self.match(MCParser.GREATER_OP)
                self.state = 300
                self.expr2(0)
                pass

            elif la_ == 7:
                self.state = 302
                self.expr2(0)
                self.state = 303
                self.match(MCParser.EQUAL_OP)
                self.state = 304
                self.expr2(0)
                pass

            elif la_ == 8:
                self.state = 306
                self.expr2(0)
                self.state = 307
                self.match(MCParser.NOT_EQUAL_OP)
                self.state = 308
                self.expr2(0)
                pass

            elif la_ == 9:
                self.state = 310
                self.expr2(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 330
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 328
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.Expr1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                        self.state = 313
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 314
                        self.match(MCParser.DIV_OP)
                        self.state = 315
                        self.expr1(13)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.Expr1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                        self.state = 316
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 317
                        self.match(MCParser.MUL_OP)
                        self.state = 318
                        self.expr1(12)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.Expr1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                        self.state = 319
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 320
                        self.match(MCParser.MODULUS_OP)
                        self.state = 321
                        self.expr1(11)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.Expr1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                        self.state = 322
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 323
                        self.match(MCParser.ADD_OP)
                        self.state = 324
                        self.expr1(10)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.Expr1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                        self.state = 325
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 326
                        self.match(MCParser.SUB_OP)
                        self.state = 327
                        self.expr1(9)
                        pass

             
                self.state = 332
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(MCParser.OpContext,0)


        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr2Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr2Context,i)


        def AND_OP(self):
            return self.getToken(MCParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(MCParser.OR_OP, 0)

        def ASSIGN_OP(self):
            return self.getToken(MCParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.op()
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 345
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.Expr2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                        self.state = 336
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 337
                        self.match(MCParser.AND_OP)
                        self.state = 338
                        self.expr2(5)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.Expr2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                        self.state = 339
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 340
                        self.match(MCParser.OR_OP)
                        self.state = 341
                        self.expr2(4)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.Expr2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                        self.state = 342
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 343
                        self.match(MCParser.ASSIGN_OP)
                        self.state = 344
                        self.expr()
                        pass

             
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func(self):
            return self.getTypedRuleContext(MCParser.Call_funcContext,0)


        def lit(self):
            return self.getTypedRuleContext(MCParser.LitContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def element(self):
            return self.getTypedRuleContext(MCParser.ElementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_op




    def op(self):

        localctx = MCParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_op)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.call_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.match(MCParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 353
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.expr1_sempred
        self._predicates[33] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




