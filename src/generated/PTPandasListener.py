# Generated from grammar/PTPandas.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PTPandasParser import PTPandasParser
else:
    from PTPandasParser import PTPandasParser

# This class defines a complete listener for a parse tree produced by PTPandasParser.
class PTPandasListener(ParseTreeListener):

    # Enter a parse tree produced by PTPandasParser#programa.
    def enterPrograma(self, ctx:PTPandasParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PTPandasParser#programa.
    def exitPrograma(self, ctx:PTPandasParser.ProgramaContext):
        pass


    # Enter a parse tree produced by PTPandasParser#comando.
    def enterComando(self, ctx:PTPandasParser.ComandoContext):
        pass

    # Exit a parse tree produced by PTPandasParser#comando.
    def exitComando(self, ctx:PTPandasParser.ComandoContext):
        pass


    # Enter a parse tree produced by PTPandasParser#filtrarCmd.
    def enterFiltrarCmd(self, ctx:PTPandasParser.FiltrarCmdContext):
        pass

    # Exit a parse tree produced by PTPandasParser#filtrarCmd.
    def exitFiltrarCmd(self, ctx:PTPandasParser.FiltrarCmdContext):
        pass


    # Enter a parse tree produced by PTPandasParser#expressao.
    def enterExpressao(self, ctx:PTPandasParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by PTPandasParser#expressao.
    def exitExpressao(self, ctx:PTPandasParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by PTPandasParser#operador.
    def enterOperador(self, ctx:PTPandasParser.OperadorContext):
        pass

    # Exit a parse tree produced by PTPandasParser#operador.
    def exitOperador(self, ctx:PTPandasParser.OperadorContext):
        pass


    # Enter a parse tree produced by PTPandasParser#valor.
    def enterValor(self, ctx:PTPandasParser.ValorContext):
        pass

    # Exit a parse tree produced by PTPandasParser#valor.
    def exitValor(self, ctx:PTPandasParser.ValorContext):
        pass


    # Enter a parse tree produced by PTPandasParser#carregarCmd.
    def enterCarregarCmd(self, ctx:PTPandasParser.CarregarCmdContext):
        pass

    # Exit a parse tree produced by PTPandasParser#carregarCmd.
    def exitCarregarCmd(self, ctx:PTPandasParser.CarregarCmdContext):
        pass


    # Enter a parse tree produced by PTPandasParser#mostrarCmd.
    def enterMostrarCmd(self, ctx:PTPandasParser.MostrarCmdContext):
        pass

    # Exit a parse tree produced by PTPandasParser#mostrarCmd.
    def exitMostrarCmd(self, ctx:PTPandasParser.MostrarCmdContext):
        pass



del PTPandasParser