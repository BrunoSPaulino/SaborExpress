from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça do Sabor", "Gourmet")
restaurante_praca.alternar_status()
restaurante_praca.receber_avaliacao("Guilherme", 2)
restaurante_praca.receber_avaliacao("João", 5)

restaurante_mexicano = Restaurante("Mexicana do Sabor", "Mexicano")
restaurante_mexicano.alternar_status()

restaurante_japones = Restaurante("Japa", "Japonês")


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()