from modelos.restaurante import Restaurante

restaurante_mega_pizza = Restaurante('Mega pizza', 'Italiana')
restaurante_sushi_hokkai = Restaurante('sushi hokkai', 'Japonesa')
restaurante_san_rafael = Restaurante('san rafael', 'brasileira')

restaurante_sushi_hokkai.alterar_estado()
restaurante_mega_pizza.receber_avalicao('Teo', 3)
restaurante_mega_pizza.receber_avalicao('João', 6)
restaurante_mega_pizza.receber_avalicao('Giovana', 1)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()