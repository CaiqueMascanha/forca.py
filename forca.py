from faker import Faker

class Forca:
    def __init__(self):
        self.fake = Faker('pt_BR')
        self.palavra = self.fake.name().lower()
        self.segredo = ['_' for _ in self.palavra]
        self.tentativas = 6
        self.digitadas = []

    def play(self):
        print(f'{self.segredo}\n')
        self.chute = input('Digite uma letra ou o nome da plavra: ').lower()

        if self.chute not in self.digitadas:
            for i, _ in enumerate(self.palavra):
                if self.chute == self.palavra[i]:
                    self.segredo[i] = self.chute
                
                elif self.chute == self.palavra:
                    self.segredo = self.chute

                elif self.chute in self.digitadas:
                    print(f'Você já digitou esta palavra: {self.chute}')
        else:
            print('Você já digitou essa palavra ou letra, tente novamente!')

        self.digitadas += self.chute

        if self.segredo == self.palavra:
            print('Parabéns, você acertou!!!')
            
        if self.chute != self.palavra and self.chute not in self.palavra and self.chute in self.digitadas:
            self.tentativas -= 1

        





if __name__ == '__main__':
    ...