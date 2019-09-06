# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#body.
    def visitBody(self, ctx:MCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#lit.
    def visitLit(self, ctx:MCParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primary_type.
    def visitPrimary_type(self, ctx:MCParser.Primary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#input_ptr_type.
    def visitInput_ptr_type(self, ctx:MCParser.Input_ptr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#output_ptr_type.
    def visitOutput_ptr_type(self, ctx:MCParser.Output_ptr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#element.
    def visitElement(self, ctx:MCParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl_var.
    def visitDecl_var(self, ctx:MCParser.Decl_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#op.
    def visitOp(self, ctx:MCParser.OpContext):
        return self.visitChildren(ctx)



del MCParser