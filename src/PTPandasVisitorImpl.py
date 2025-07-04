from src.generated.PTPandasParser import PTPandasParser
from src.generated.PTPandasVisitor import PTPandasVisitor

class PTPandasVisitorImpl(PTPandasVisitor):

    def visitPrograma(self, ctx:PTPandasParser.ProgramaContext):
        codigo_final = ["import pandas as pd"]
        for comando_ctx in ctx.comando():
            linha_codigo = self.visit(comando_ctx)
            codigo_final.append(linha_codigo)
        return "\n".join(codigo_final)

    def visitCarregarCmd(self, ctx:PTPandasParser.CarregarCmdContext):
        nome_variavel = ctx.ID().getText()
        caminho_arquivo = ctx.STRING().getText().strip('"')
        return f'{nome_variavel} = pd.read_csv("{caminho_arquivo}")'

    def visitMostrarCmd(self, ctx:PTPandasParser.MostrarCmdContext):
        nome_variavel = ctx.ID().getText()
        if ctx.CABECALHO():
            return f'print("\\n--- MOSTRAR CABECALHO DE {nome_variavel} ---\\n", {nome_variavel}.head())'
        else:
            return f'print("\\n--- MOSTRAR {nome_variavel} ---\\n", {nome_variavel})'

    # --- NOVO MÉTODO PARA O COMANDO FILTRAR ---
    def visitFiltrarCmd(self, ctx:PTPandasParser.FiltrarCmdContext):
        # A regra é: FILTRAR ID ONDE expressao EM ID
        # ID(0) é a variável de origem, ID(1) é a de destino
        variavel_origem = ctx.ID(0).getText()
        variavel_destino = ctx.ID(1).getText()

        # Agora, vamos processar a 'expressao'
        expressao_ctx = ctx.expressao()
        
        # Pega o nome da coluna (que é uma STRING)
        coluna = expressao_ctx.STRING().getText() # Mantém as aspas
        
        # Pega o operador (ex: '>')
        op = expressao_ctx.operador().getText()
        
        # Pega o valor (pode ser NUMERO ou STRING)
        valor = expressao_ctx.valor().getText()

        # Monta a linha de código Python final
        # Ex: funcionarios_seniores = funcionarios[funcionarios["idade"] > 30]
        return f'{variavel_destino} = {variavel_origem}[{variavel_origem}[{coluna}] {op} {valor}]'