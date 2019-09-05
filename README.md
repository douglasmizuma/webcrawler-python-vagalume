# webcrawler-python-vagalumeWeb Crawler - Vagalume

Web Crawler - Vagalume

>A ideia do projeto consiste em um Web Crawler para o site de música Vagalume que, ao escolher uma banda, o programa deve trazer todas as músicas daquela banda específica.
>O projeto foi feito em python na versão 3.7.4

Sobre o programa:

>O programa precisa receber o nome de uma banda, esse nome pode estar em um arquivo .txt, em que deve conter somente o nome de uma banda em uma única linha, ou pode ser escrito pelo CMD, tanto depois do começo da execução do programa quanto na linha de comando para executar o programa.
>Após receber a banda ele precisa saber quantas músicas deseja trazer. Só aceita números sem casa decimal ou nenhuma entrada, ou seja, só apertando enter. No caso de nenhuma entrada ele trará todas as músicas.
>Além de imprimir na tela todas as músicas encontradas ele cria um arquivo com o nome da banda em .txt contando as músicas impressas na tela.

Exemplos de uso:

```
C:\Users\Douglas\WebCrawler>python main.py
Insira o nome da banda ou o nome do arquivo com a extenção .txt:
pOkEmOn
Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
a
O valor digitado "a" não é valido.

Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
2.2
O valor digitado "2.2" não é valido.

Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
3,3
O valor digitado "3,3" não é valido.

Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
lalalas
O valor digitado "lalalas" não é valido.

Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
20
(hey You) Free Up Your Mind
12º Abertura - Galactic Battles
2B A Master
A Cidade de Verídian
A Força do Mestre
A Hora Chegou - Adeus de Pikachu
Abertura 1
Abertura 10
Abertura 11
Abertura 12
Abertura 13
Abertura 14
Abertura 15
Abertura 18
Abertura 3
Abertura 4
Abertura 5
Abertura 6
Abertura 7
Abertura 8
```

```
C:\Users\Douglas\WebCrawler>python main.py Marília Mendonça
Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
reais
O valor digitado "reais" não é valido.

Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
50
10 de Setembro
A Culpa É Dele (Part. Maiara e Maraisa)
A Gente Não Se Aguenta
A Gente Não Tá Junto
A Voz do Coração
Aceita Que Dói Menos (Com Trio Parada Dura)
Aí Como Eu Tô Bandida
Alô Porteiro
Amante Fiel (Com Felipe Araújo)
Amante Não Tem Lar
Amigo Emprestado
Apaixonadinha (part. Leo Santana, Didá Banda Feminina)
Até o Tempo Passa
Ausência
Bebaça
Bebi Liguei
Bem Pior Que Eu
Bye Bye
Casa da Mãe Joana (Part. Henrique e Juliano)
Ciumeira
Como Faz Com Ela
Coração Bipolar (Com Zé Henrique e Gabriel)
Coração de Violeiro
Coração Mal Assombrado
Covardia
De Quem É a Culpa?
De Sexta a Sexta
Deu Ocupado de Novo (Part. Zezé di Camargo e Luciano)
Direitos Iguais
Do Copo de Cerveja
Ei Saudade
Ela É Problema Seu
Entre Quatro Paredes
Essas Nossas Brigas
Esse Cara Aqui do Lado
Estranho
Estrelinha
Eu Não Sou Novela
Eu Sei de Cor
Festa das Patroas
Flor E O Beija-Flor
Foi Só Um Caso (Com Chitãozinho e Xororó)
Folgado
Hoje Somos Só Metade
Impasse (Part. Henrique e Juliano)
Incendeia (Com Léo Santana)
Infiel
Ligação Fora de Área
Love à Queima Roupa
Matriz Ou Filial (Com Fátima Leão)
```

```
C:\Users\Douglas\WebCrawler>python main.py Banda.txt
Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
5
100% Casamento
24 Horas de Amor
A Casa ao Lado
A Culpa é Sua
A Dois Graus
```

```
C:\Users\Douglas\WebCrawler>python main.py
Insira o nome da banda ou o nome do arquivo com a extenção .txt:
teste.txt
Digite a quantidade de músicas que deseja listar, ele precisa ser um número inte
iro.
4
Amiga Até o Fim
Anjo da Internet
Aquarela
Bom Dia
```
