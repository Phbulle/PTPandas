# Generated from grammar/PTPandas.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PTPandasParser import PTPandasParser
else:
    from PTPandasParser import PTPandasParser

# This class defines a complete generic visitor for a parse tree produced by PTPandasParser.

class PTPandasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PTPandasParser#programa.
    def visitPrograma(self, ctx:PTPandasParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PTPandasParser#comando.
    def visitComando(self, ctx:PTPandasParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PTPandasParser#filtrarCmd.
    def visitFiltrarCmd(self, ctx:PTPandasParser.FiltrarCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PTPandasParser#expressao.
    def visitExpressao(self, ctx:PTPandasParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PTPandasParser#operador.
    def visitOperador(self, ctx:PTPandasParser.OperadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PTPandasParser#valor.
    def visitValor(self, ctx:PTPandasParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PTPandasParser#carregarCmd.
    def visitCarregarCmd(self, ctx:PTPandasParser.CarregarCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PTPandasParser#mostrarCmd.
    def visitMostrarCmd(self, ctx:PTPandasParser.MostrarCmdContext):
        return self.visitChildren(ctx)



del PTPandasParser