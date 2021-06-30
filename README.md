# Máscaras de validação por expressões regulares

Trabalho desenvolvido na disciplina Teoria da Computação do Programa de Pós-Graduação em Ciência da Computação (PPGCC) da Universidade Federal do Pará (UFPA) em 2021.1.

O trabalho consiste no densenvolvimento de máscaras de validação, através de expressões regulares, que obedecem às especificações prévias de cada campo, conforme descrito abaixo.

## Descrição

Neste trabalho foram desenvolvidas máscaras de validação através de expressões regulares para os campos nome, e-mail, senha, cpf, e telefone. Para a construção das máscaras considera-se os seguintes alfabetos <img src="https://render.githubusercontent.com/render/math?math=\sum=\lbrace a, b, c, ..., z\rbrace">, <img src="https://render.githubusercontent.com/render/math?math=\Gamma=\lbrace A, B, C, ..., Z\rbrace"> e <img src="https://render.githubusercontent.com/render/math?math=N=\lbrace 0, 1, 2, ..., 9\rbrace">.

Abaixo é apresentada a descrição dos campos análisados:

* **Nome** : deve receber o nome e o sobrenome, ambos não vazios, separados por um espaç o; não
deve aceitar caracteres especiais ou numéricos; o primeiro símbolo do nome e do sobrenome
deve ser do alfabeto <img src="https://render.githubusercontent.com/render/math?math=\Gamma">, e os outros símbolos devem ser do alfabeto <img src="https://render.githubusercontent.com/render/math?math=\sum">.

* **E mail** : as sentenças possuem símbolos de <img src="https://render.githubusercontent.com/render/math?math=\sum"> e deve conter exatamente um símbolo “@”; não
devem começar com o símbolo “@”; devem terminar com a sequência “.br”; devem ter, pelo
menos, um símbolo de <img src="https://render.githubusercontent.com/render/math?math=\sum"> entre o símbolo “@” e o “.br”.

* **Senha** : as cadeias podem conter símbolos dos alfabetos <img src="https://render.githubusercontent.com/render/math?math=\sum">, <img src="https://render.githubusercontent.com/render/math?math=\Gamma"> e <img src="https://render.githubusercontent.com/render/math?math=N">; devem, obrigatoriamente,
ter pelo menos um símbolo do alfabeto Γ e um símbolo do alfabeto N; devem ter comprimento
igual a 8.

* **CPF** : as cadeias devem ter o formato xxx.xxx.xxx xx , onde x <img src="https://render.githubusercontent.com/render/math?math=\epsilon"> <img src="https://render.githubusercontent.com/render/math?math=N">.

* **Telefone** : as cadeias devem ter o formato (xx) 9xxxx-xxxx ou (xx) 9xxxxxxxx ou xx 9xxxxxxxx
onde x <img src="https://render.githubusercontent.com/render/math?math=\epsilon"> <img src="https://render.githubusercontent.com/render/math?math=N">.