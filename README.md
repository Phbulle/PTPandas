# 🐼 PTPandas: Análise de Dados com Pandas em Português 📊

# Objetivo
O pandas é a biblioteca padrão para análise de dados em Python, mas sua sintaxe, embora poderosa, pode ser verbosa e pouco intuitiva para iniciantes, especialmente para aqueles que não têm o inglês como primeira língua. Comandos como df[df['idade'] > 30] exigem um conhecimento prévio da estrutura da biblioteca que pode ser uma barreira inicial.

O PTPandas nasceu com o objetivo de simplificar este processo. Criamos uma Linguagem de Domínio Específico (DSL) que traduz comandos de análise de dados, escritos em português claro e declarativo, para código pandas funcional. A nossa meta é oferecer uma porta de entrada amigável ao mundo da análise de dados, permitindo que qualquer pessoa, de estudantes a profissionais de outras áreas, possa realizar manipulações de dados de forma rápida e intuitiva.

Dentre as facilidades trazidas pelo PTPandas, destacamos:

Comandos em Português: Utilize CARREGAR, MOSTRAR, FILTRAR, SALVAR, entre outros, para expressar suas intenções de forma natural.

Sintaxe Simplificada: Abstraímos a complexidade de operações comuns. Em vez de aninhar seleções, você escreve de forma linear: FILTRAR dados ONDE "coluna" > valor EM novos_dados.

Foco no Fluxo de Trabalho: A linguagem é projetada para seguir o fluxo de trabalho padrão de um analista: carregar dados, transformar/limpar e salvar/visualizar os resultados.

# Como Executar o Projeto
Para executar o PTPandas, basta ter Python e Java (JDK) instalados em sua máquina. O projeto já inclui todas as ferramentas necessárias.

# 1. Clone o Repositório

Primeiro, clone este repositório para a sua máquina local.
```
git clone https://github.com/Phbulle/PTPandas.git
```

# 2. Instale as Dependências

Este comando irá instalar o pandas e o runtime do ANTLR para Python, que estão listados no arquivo requirements.txt.
```
pip install -r requirements.txt
```

# 3. Gere o Parser a partir da Gramática

Execute o comando abaixo para gerar o código do analisador. Ele usa a ferramenta antlr.jar (já inclusa no projeto) para ler a gramática e criar os arquivos necessários.
```
java -jar antlr.jar -Dlanguage=Python3 -visitor -o src/generated grammar/PTPandas.g4
```

# 4. Execute um Exemplo!

Agora você está pronto! Para executar um script, passe seu caminho como argumento para main.py.

```
python main.py exemplos/analise_rh.ptp
```

# Exemplos de Código
Aqui estão alguns exemplos de scripts que demonstram o poder e a simplicidade do PTPandas.

1. Análise de Vendas de uma Loja
Este exemplo carrega dados de vendas, filtra por um valor específico e salva o resultado.

```
#Carrega o arquivo de vendas para a variável 'vendas'
CARREGAR DADOS DE "dados/vendas.csv" EM vendas

#Mostra as 5 primeiras linhas para uma inspeção rápida
MOSTRAR CABECALHO DE vendas

#Filtra apenas as vendas onde a quantidade foi maior que 10
FILTRAR vendas ONDE "quantidade" > 10 EM vendas_grandes

#Mostra o novo dataframe com as vendas grandes
MOSTRAR vendas_grandes

#Salva o resultado filtrado em um novo arquivo para análise posterior
SALVAR vendas_grandes EM "saida/vendas_acima_de_10.csv"
```

2. Gerenciamento de Recursos Humanos
Este script manipula uma lista de funcionários, selecionando por departamento e idade.

```
#Carrega a base de dados de funcionários
CARREGAR DADOS DE "dados/funcionarios.csv" EM funcionarios

#Filtra todos os funcionários do departamento de "TI"
FILTRAR funcionarios ONDE "departamento" == "TI" EM equipe_ti

#Do pessoal de TI, seleciona apenas os que têm mais de 30 anos
FILTRAR equipe_ti ONDE "idade" > 30 EM ti_seniores

#Mostra o resultado final da equipe sênior de TI
MOSTRAR ti_seniores
```
