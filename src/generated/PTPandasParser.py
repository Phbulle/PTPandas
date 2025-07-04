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
        4,1,19,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,54,8,7,1,7,1,7,1,7,0,
        0,8,0,2,4,6,8,10,12,14,0,2,1,0,3,8,2,0,9,9,17,17,53,0,17,1,0,0,0,
        2,26,1,0,0,0,4,28,1,0,0,0,6,35,1,0,0,0,8,39,1,0,0,0,10,41,1,0,0,
        0,12,43,1,0,0,0,14,50,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,
        1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,
        22,1,1,0,0,0,23,27,3,12,6,0,24,27,3,14,7,0,25,27,3,4,2,0,26,23,1,
        0,0,0,26,24,1,0,0,0,26,25,1,0,0,0,27,3,1,0,0,0,28,29,5,1,0,0,29,
        30,5,16,0,0,30,31,5,2,0,0,31,32,3,6,3,0,32,33,5,13,0,0,33,34,5,16,
        0,0,34,5,1,0,0,0,35,36,5,17,0,0,36,37,3,8,4,0,37,38,3,10,5,0,38,
        7,1,0,0,0,39,40,7,0,0,0,40,9,1,0,0,0,41,42,7,1,0,0,42,11,1,0,0,0,
        43,44,5,10,0,0,44,45,5,11,0,0,45,46,5,12,0,0,46,47,5,17,0,0,47,48,
        5,13,0,0,48,49,5,16,0,0,49,13,1,0,0,0,50,53,5,14,0,0,51,52,5,15,
        0,0,52,54,5,12,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,
        56,5,16,0,0,56,15,1,0,0,0,3,19,26,53
    ]

class PTPandasParser ( Parser ):

    grammarFileName = "PTPandas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'FILTRAR'", "'ONDE'", "'>'", "'<'", "'=='", 
                     "'!='", "'>='", "'<='", "<INVALID>", "'CARREGAR'", 
                     "'DADOS'", "'DE'", "'EM'", "'MOSTRAR'", "'CABECALHO'" ]

    symbolicNames = [ "<INVALID>", "FILTRAR", "ONDE", "OP_MAIOR", "OP_MENOR", 
                      "OP_IGUAL", "OP_DIFERENTE", "OP_MAIOR_IGUAL", "OP_MENOR_IGUAL", 
                      "NUMERO", "CARREGAR", "DADOS", "DE", "EM", "MOSTRAR", 
                      "CABECALHO", "ID", "STRING", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_filtrarCmd = 2
    RULE_expressao = 3
    RULE_operador = 4
    RULE_valor = 5
    RULE_carregarCmd = 6
    RULE_mostrarCmd = 7

    ruleNames =  [ "programa", "comando", "filtrarCmd", "expressao", "operador", 
                   "valor", "carregarCmd", "mostrarCmd" ]

    EOF = Token.EOF
    FILTRAR=1
    ONDE=2
    OP_MAIOR=3
    OP_MENOR=4
    OP_IGUAL=5
    OP_DIFERENTE=6
    OP_MAIOR_IGUAL=7
    OP_MENOR_IGUAL=8
    NUMERO=9
    CARREGAR=10
    DADOS=11
    DE=12
    EM=13
    MOSTRAR=14
    CABECALHO=15
    ID=16
    STRING=17
    WS=18
    COMENTARIO=19

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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.comando()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17410) != 0)):
                    break

            self.state = 21
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


        def filtrarCmd(self):
            return self.getTypedRuleContext(PTPandasParser.FiltrarCmdContext,0)


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
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.carregarCmd()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.mostrarCmd()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.filtrarCmd()
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


    class FiltrarCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTRAR(self):
            return self.getToken(PTPandasParser.FILTRAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PTPandasParser.ID)
            else:
                return self.getToken(PTPandasParser.ID, i)

        def ONDE(self):
            return self.getToken(PTPandasParser.ONDE, 0)

        def expressao(self):
            return self.getTypedRuleContext(PTPandasParser.ExpressaoContext,0)


        def EM(self):
            return self.getToken(PTPandasParser.EM, 0)

        def getRuleIndex(self):
            return PTPandasParser.RULE_filtrarCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFiltrarCmd" ):
                listener.enterFiltrarCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFiltrarCmd" ):
                listener.exitFiltrarCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFiltrarCmd" ):
                return visitor.visitFiltrarCmd(self)
            else:
                return visitor.visitChildren(self)




    def filtrarCmd(self):

        localctx = PTPandasParser.FiltrarCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_filtrarCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(PTPandasParser.FILTRAR)
            self.state = 29
            self.match(PTPandasParser.ID)
            self.state = 30
            self.match(PTPandasParser.ONDE)
            self.state = 31
            self.expressao()
            self.state = 32
            self.match(PTPandasParser.EM)
            self.state = 33
            self.match(PTPandasParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PTPandasParser.STRING, 0)

        def operador(self):
            return self.getTypedRuleContext(PTPandasParser.OperadorContext,0)


        def valor(self):
            return self.getTypedRuleContext(PTPandasParser.ValorContext,0)


        def getRuleIndex(self):
            return PTPandasParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = PTPandasParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(PTPandasParser.STRING)
            self.state = 36
            self.operador()
            self.state = 37
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MAIOR(self):
            return self.getToken(PTPandasParser.OP_MAIOR, 0)

        def OP_MENOR(self):
            return self.getToken(PTPandasParser.OP_MENOR, 0)

        def OP_IGUAL(self):
            return self.getToken(PTPandasParser.OP_IGUAL, 0)

        def OP_DIFERENTE(self):
            return self.getToken(PTPandasParser.OP_DIFERENTE, 0)

        def OP_MAIOR_IGUAL(self):
            return self.getToken(PTPandasParser.OP_MAIOR_IGUAL, 0)

        def OP_MENOR_IGUAL(self):
            return self.getToken(PTPandasParser.OP_MENOR_IGUAL, 0)

        def getRuleIndex(self):
            return PTPandasParser.RULE_operador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador" ):
                listener.enterOperador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador" ):
                listener.exitOperador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador" ):
                return visitor.visitOperador(self)
            else:
                return visitor.visitChildren(self)




    def operador(self):

        localctx = PTPandasParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
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


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(PTPandasParser.NUMERO, 0)

        def STRING(self):
            return self.getToken(PTPandasParser.STRING, 0)

        def getRuleIndex(self):
            return PTPandasParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = PTPandasParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==9 or _la==17):
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
        self.enterRule(localctx, 12, self.RULE_carregarCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(PTPandasParser.CARREGAR)
            self.state = 44
            self.match(PTPandasParser.DADOS)
            self.state = 45
            self.match(PTPandasParser.DE)
            self.state = 46
            self.match(PTPandasParser.STRING)
            self.state = 47
            self.match(PTPandasParser.EM)
            self.state = 48
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
        self.enterRule(localctx, 14, self.RULE_mostrarCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(PTPandasParser.MOSTRAR)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 51
                self.match(PTPandasParser.CABECALHO)
                self.state = 52
                self.match(PTPandasParser.DE)


            self.state = 55
            self.match(PTPandasParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





