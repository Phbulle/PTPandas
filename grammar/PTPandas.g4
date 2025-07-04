// Define o nome da gramática. Os arquivos gerados terão esse prefixo.
grammar PTPandas;

// Regras do Parser (Sintático) - começam com letra minúscula

// Um programa é uma sequência de um ou mais comandos, terminando com o fim do arquivo.
programa: comando+ EOF;

// Um comando pode ser um dos tipos abaixo. Adicionaremos mais aqui depois.
comando: carregarCmd | mostrarCmd;

// Define a sintaxe para carregar dados
// Ex: CARREGAR DADOS DE "arquivo.csv" EM variavel
carregarCmd: CARREGAR DADOS DE STRING EM ID;

// Define a sintaxe para mostrar dados
// Ex: MOSTRAR variavel
// Ex: MOSTRAR CABECALHO DE variavel
mostrarCmd: MOSTRAR (CABECALHO DE)? ID;


// Regras do Lexer (Léxico) - definem os 'átomos' (tokens) da linguagem
// Elas devem vir DEPOIS das regras do parser.

CARREGAR:   'CARREGAR';
DADOS:      'DADOS';
DE:         'DE';
EM:         'EM';
MOSTRAR:    'MOSTRAR';
CABECALHO:  'CABECALHO';

// Um identificador (nome de variável)
ID:         [a-zA-Z_][a-zA-Z0-9_]*;

// Uma string de texto entre aspas duplas
STRING:     '"' (~["])* '"';

// Ignorar espaços em branco, tabulações e quebras de linha
WS:         [ \t\r\n]+ -> skip;

// Ignorar comentários que começam com # até o fim da linha
COMENTARIO: '#' ~[\r\n]* -> skip;