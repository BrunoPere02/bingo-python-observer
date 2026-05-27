import random

# ===== PADRÃO OBSERVER =====

# Subject (Sorteador)
class Sorteador:
    def __init__(self):
        self.numeros = list(range(1, 76))
        random.shuffle(self.numeros)
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def sortear(self):
        while self.numeros:
            numero = self.numeros.pop(0)
            print(f"Número sorteado: {numero}")
            for obs in self.observadores:
                if obs.atualizar(numero):
                    return


# Observer (Cartela)
class Cartela:
    def __init__(self):
        self.numeros = self.gerar_cartela()
        self.acertos = set()

    def gerar_cartela(self):
        cartela = []
        colunas = {
            'B': random.sample(range(1, 16), 5),
            'I': random.sample(range(16, 31), 5),
            'N': random.sample(range(31, 46), 5),
            'G': random.sample(range(46, 61), 5),
            'O': random.sample(range(61, 76), 5)
        }
        for i in range(5):
            linha = [
                colunas['B'][i],
                colunas['I'][i],
                'X' if i == 2 else colunas['N'][i],
                colunas['G'][i],
                colunas['O'][i]
            ]
            cartela.append(linha)
        return cartela

    def atualizar(self, numero_sorteado):
        for linha in self.numeros:
            for item in linha:
                if item == numero_sorteado:
                    self.acertos.add(numero_sorteado)
        if self.cartela_cheia():
            print("* Cartela completa! Você venceu!")
            return True
        return False

    def cartela_cheia(self):
        return len(self.acertos) == 24

    def exibir_cartela(self):
        print("Sua cartela:")
        for linha in self.numeros:
            print(linha)


# ===== SIMULAÇÃO DO JOGO =====
cartela = Cartela()
sorteador = Sorteador()
sorteador.adicionar_observador(cartela)
cartela.exibir_cartela()
sorteador.sortear()
