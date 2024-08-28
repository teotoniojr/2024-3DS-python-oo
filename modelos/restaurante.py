from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self): 
        return f'{self._nome} | {self._categoria} | {self._avaliacao} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('')
        print(f'{"Nome do restaurante".ljust(25)} | {" Categoria".ljust(25)} | {"Avaliações".ljust(25)} | {"status"}')
        print('------------------------------------------------------------------------------------------')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}' )
        print('------------------------------------------------------------------------------------------')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avalicao(self, cliente, nota):
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliação'
    
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
    
        if 0 <= media < 2:
            return '★'
        elif 2 <= media < 3:
            return '★★'
        elif 3 <= media < 4:
            return '★★★'
        elif 4 <= media < 5:
            return '★★★★'
        elif media == 5:
            return '★★★★★'
        


