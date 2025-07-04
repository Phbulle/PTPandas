import sys
from antlr4 import *
from src.generated.PTPandasLexer import PTPandasLexer
from src.generated.PTPandasParser import PTPandasParser
from src.PTPandasVisitorImpl import PTPandasVisitorImpl

def main(argv):
    # Pega o nome do arquivo de entrada da linha de comando
    input_stream = FileStream(argv[1], encoding='utf-8')

    # 1. Análise Léxica
    lexer = PTPandasLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 2. Análise Sintática
    parser = PTPandasParser(stream)
    tree = parser.programa() # 'programa' é a regra inicial da nossa gramática

    # 3. Tradução (usando o padrão Visitor)
    if parser.getNumberOfSyntaxErrors() == 0:
        # Se não houveram erros, cria nosso visitor customizado
        visitor = PTPandasVisitorImpl()
        
        # Visita a árvore, o que irá gerar o código Python
        codigo_python = visitor.visit(tree)
        
        print("--- CÓDIGO PYTHON GERADO ---")
        print(codigo_python)
        print("----------------------------\n")
        
        print("--- SAÍDA DA EXECUÇÃO ---")
        # Executa o código gerado
        # Usamos um dicionário global para que o pandas seja importado corretamente
        try:
            exec(codigo_python, globals())
        except Exception as e:
            print(f"Erro durante a execução do código gerado: {e}")
            
    else:
        print(f"Encontrados {parser.getNumberOfSyntaxErrors()} erros de sintaxe.")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print("Uso: python main.py <arquivo.ptp>")