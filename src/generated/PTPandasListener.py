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