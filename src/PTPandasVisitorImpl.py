from src.generated.PTPandasParser import PTPandasParser
from src.generated.PTPandasVisitor import PTPandasVisitor

# Herda da classe Visitor gerada pelo ANTLR
class PTPandasVisitorImpl(PTPandasVisitor):
    
    # O Visitor não precisa de um __init__ por enquanto,
    # mas poderia ser usado para inicializar variáveis de controle.

    # Método visitPrograma: é chamado para a regra principal 'programa'
    # ctx (contexto) é o nó da árvore que estamos visitando
    def visitPrograma(self, ctx:PTPandasParser.ProgramaContext):
        # Sempre começamos o script importando o pandas
        codigo_final = ["import pandas as pd"]
        
        # Itera sobre todos os comandos filhos do nó 'programa'
        for comando_ctx in ctx.comando():
            # Visita cada comando. Isso vai chamar o método correspondente
            # (ex: visitCarregarCmd), que retornará uma string de código.
            linha_codigo = self.visit(comando_ctx)
            codigo_final.append(linha_codigo)
        
        # Junta todas as linhas de código geradas com quebras de linha
        return "\n".join(codigo_final)

    # Método para o comando 'carregar'
    # O nome do método é 'visit' + nome da regra com a primeira letra maiúscula
    def visitCarregarCmd(self, ctx:PTPandasParser.CarregarCmdContext):
        # Pega o texto dos tokens da regra
        nome_variavel = ctx.ID().getText()
        caminho_arquivo = ctx.STRING().getText()
        
        # Remove as aspas da string lida
        caminho_arquivo_limpo = caminho_arquivo.strip('"')

        # Monta a linha de código Python
        # Ex: minhas_vendas = pd.read_csv("dados/vendas.csv")
        return f'{nome_variavel} = pd.read_csv("{caminho_arquivo_limpo}")'

    # Método para o comando 'mostrar'
    def visitMostrarCmd(self, ctx:PTPandasParser.MostrarCmdContext):
        nome_variavel = ctx.ID().getText()
        
        # Verifica se a parte opcional '(CABECALHO DE)?' existe
        if ctx.CABECALHO():
            # Se existe, gera o código para .head()
            return f'print({nome_variavel}.head())'
        else:
            # Se não, apenas imprime o DataFrame inteiro
            return f'print({nome_variavel})'