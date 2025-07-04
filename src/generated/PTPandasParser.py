# Generated from grammar/PTPandas.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,3,3,30,8,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,32,0,9,1,0,0,0,
        2,17,1,0,0,0,4,19,1,0,0,0,6,26,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,
        10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,
        0,1,14,1,1,0,0,0,15,18,3,4,2,0,16,18,3,6,3,0,17,15,1,0,0,0,17,16,
        1,0,0,0,18,3,1,0,0,0,19,20,5,1,0,0,20,21,5,2,0,0,21,22,5,3,0,0,22,
        23,5,8,0,0,23,24,5,4,0,0,24,25,5,7,0,0,25,5,1,0,0,0,26,29,5,5,0,
        0,27,28,5,6,0,0,28,30,5,3,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,
        1,0,0,0,31,32,5,7,0,0,32,7,1,0,0,0,3,11,17,29
    ]

class PTPandasParser ( Parser ):

    grammarFileName = "PTPandas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CARREGAR'", "'DADOS'", "'DE'", "'EM'", 
                     "'MOSTRAR'", "'CABECALHO'" ]

    symbolicNames = [ "<INVALID>", "CARREGAR", "DADOS", "DE", "EM", "MOSTRAR", 
                      "CABECALHO", "ID", "STRING", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_carregarCmd = 2
    RULE_mostrarCmd = 3

    ruleNames =  [ "programa", "comando", "carregarCmd", "mostrarCmd" ]

    EOF = Token.EOF
    CARREGAR=1
    DADOS=2
    DE=3
    EM=4
    MOSTRAR=5
    CABECALHO=6
    ID=7
    STRING=8
    WS=9
    COMENTARIO=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PTPandasParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PTPandasParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PTPandasParser.ComandoContext,i)


        def getRuleIndex(self):
            return PTPandasParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = PTPandasParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.comando()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==5):
                    break

            self.state = 13
            self.match(PTPandasParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def carregarCmd(self):
            return self.getTypedRuleContext(PTPandasParser.CarregarCmdContext,0)


        def mostrarCmd(self):
            return self.getTypedRuleContext(PTPandasParser.MostrarCmdContext,0)


        def getRuleIndex(self):
            return PTPandasParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = PTPandasParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.carregarCmd()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.mostrarCmd()
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


    class CarregarCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARREGAR(self):
            return self.getToken(PTPandasParser.CARREGAR, 0)

        def DADOS(self):
            return self.getToken(PTPandasParser.DADOS, 0)

        def DE(self):
            return self.getToken(PTPandasParser.DE, 0)

        def STRING(self):
            return self.getToken(PTPandasParser.STRING, 0)

        def EM(self):
            return self.getToken(PTPandasParser.EM, 0)

        def ID(self):
            return self.getToken(PTPandasParser.ID, 0)

        def getRuleIndex(self):
            return PTPandasParser.RULE_carregarCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCarregarCmd" ):
                listener.enterCarregarCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCarregarCmd" ):
                listener.exitCarregarCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCarregarCmd" ):
                return visitor.visitCarregarCmd(self)
            else:
                return visitor.visitChildren(self)




    def carregarCmd(self):

        localctx = PTPandasParser.CarregarCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_carregarCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(PTPandasParser.CARREGAR)
            self.state = 20
            self.match(PTPandasParser.DADOS)
            self.state = 21
            self.match(PTPandasParser.DE)
            self.state = 22
            self.match(PTPandasParser.STRING)
            self.state = 23
            self.match(PTPandasParser.EM)
            self.state = 24
            self.match(PTPandasParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MostrarCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(PTPandasParser.MOSTRAR, 0)

        def ID(self):
            return self.getToken(PTPandasParser.ID, 0)

        def CABECALHO(self):
            return self.getToken(PTPandasParser.CABECALHO, 0)

        def DE(self):
            return self.getToken(PTPandasParser.DE, 0)

        def getRuleIndex(self):
            return PTPandasParser.RULE_mostrarCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMostrarCmd" ):
                listener.enterMostrarCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMostrarCmd" ):
                listener.exitMostrarCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMostrarCmd" ):
                return visitor.visitMostrarCmd(self)
            else:
                return visitor.visitChildren(self)




    def mostrarCmd(self):

        localctx = PTPandasParser.MostrarCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mostrarCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(PTPandasParser.MOSTRAR)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 27
                self.match(PTPandasParser.CABECALHO)
                self.state = 28
                self.match(PTPandasParser.DE)


            self.state = 31
            self.match(PTPandasParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





