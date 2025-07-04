grammar PTPandas;

// 1. ADICIONE 'filtrarCmd' À REGRA 'comando'
programa: comando+ EOF;
comando: carregarCmd | mostrarCmd | filtrarCmd; // Adicionado filtrarCmd

// 2. CRIE A REGRA PARA O COMANDO DE FILTRAGEM
// Ex: FILTRAR funcionarios ONDE "idade" > 30 EM funcionarios_seniores
filtrarCmd: FILTRAR ID ONDE expressao EM ID;

// 3. DEFINA O QUE É UMA 'expressao' DE FILTRO
//    Por enquanto, será simples: "coluna" operador valor
expressao: STRING operador valor;
operador: OP_MAIOR | OP_MENOR | OP_IGUAL | OP_DIFERENTE | OP_MAIOR_IGUAL | OP_MENOR_IGUAL;
valor: NUMERO | STRING;

// -- Regras existentes --
carregarCmd: CARREGAR DADOS DE STRING EM ID;
mostrarCmd: MOSTRAR (CABECALHO DE)? ID;

// --- LEXER ---

// 4. ADICIONE OS NOVOS TOKENS (PALAVRAS-CHAVE)
FILTRAR:    'FILTRAR';
ONDE:       'ONDE';

// 5. ADICIONE OS OPERADORES
OP_MAIOR:       '>';
OP_MENOR:       '<';
OP_IGUAL:       '==';
OP_DIFERENTE:   '!=';
OP_MAIOR_IGUAL: '>=';
OP_MENOR_IGUAL: '<=';

// 6. ADICIONE UM TOKEN PARA NÚMEROS
NUMERO:     [0-9]+ ('.' [0-9]+)?; // Suporta inteiros e decimais

// -- Tokens existentes --
CARREGAR:   'CARREGAR';
DADOS:      'DADOS';
DE:         'DE';
EM:         'EM';
MOSTRAR:    'MOSTRAR';
CABECALHO:  'CABECALHO';
ID:         [a-zA-Z_][a-zA-Z0-9_]*;
STRING:     '"' (~["])* '"';
WS:         [ \t\r\n]+ -> skip;
COMENTARIO: '#' ~[\r\n]* -> skip;