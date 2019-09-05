from html.parser import HTMLParser

class EncontraMusica(HTMLParser):

    def __init__(self, qtdm):
        super().__init__()
        self.qtdm = qtdm
        self.flag = 0
        self.musicas = []
#como o html sempre abre e fecha <></> o flag serve para informar em qual tag vamos extrair a informação
#todos os handle_X são chamados quando o feed(data) for chamado
#aqui encontramos o onde esta a lista de musica ordenado de forma alfabetica, aumentando a flag em 1 a cada nivel de <>
    def handle_starttag(self, tag, attrs):
        if tag == "ol":
            for (atributo, valor) in attrs:
                if atributo == "id" and (valor == "alfabetMusicList"):
                    self.flag += 1
        if tag == "a" and self.flag == 1:
            for (atributo, valor) in attrs:
                if atributo == "class" and (valor == "nameMusic" or valor== "nameMusic w1"):
                    self.flag +=1

#quando encontra o fechamento da tag, diminuimos o valor da flag
    def handle_endtag(self, tag):
        if tag == 'ol' and self.flag == 1:
            self.flag -= 1
        if tag == 'a' and self.flag == 2:
            self.flag -= 1

#retorna lista de músicas encontradas
    def lista_musicas(self):
        return self.musicas

#printa na tela o que há na lista
    def imprime_lista(self):
        tamanho = len(self.musicas)
        x = 0
        tudo = 0
        if(self.qtdm == "tudo"):
            tudo = 1
        elif(int(self.qtdm)>tamanho):
            tudo = 1
        else:
            pass
        try:
            if(tudo == 1):
                while x < tamanho:
                    print(self.musicas[x])
                    x+=1
            else:
                while x < int(self.qtdm):
                    print(self.musicas[x])
                    x+=1
        except Exception as ex:
            pass

    def error(self, message):
        print(message)
        pass
        
#entndo no nível certo, traz a informação necessária, no caso, o nome da música
    def handle_data(self, data):
        if self.flag== 2 :
            self.musicas.append(data)