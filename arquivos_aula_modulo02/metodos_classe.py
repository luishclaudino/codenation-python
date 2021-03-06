class Impressora:

    def __init__(self):
        self.a = 10

    @classmethod
    def imprimir_folha(cls):
        print("folha impressa")

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()

    @classmethod
    def imprimir_a(cls):
        print(cls.a)


Impressora.imprimir_folha() #consegue usar o método diretamente sem instanciar

print("=======")
Impressora.imprimir_livro(5)

impressora = Impressora()

impressora.imprimir_folha()

print("======")

# Impressora.imprimir_a()

impressora.imprimir_a() # aqui dá erro pois a variável a está no escopo da instancia (init) e não da classe
