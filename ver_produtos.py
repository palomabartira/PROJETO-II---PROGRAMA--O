from produto import Sapato

class Sapatos:
    """ Gerencia o catálogo estático de sapatos disponíveis na loja. """

    catalogo = [
        Sapato(1, "🩰 Papete Casual", 64.90),
        Sapato(2, "👠 Salto Alto", 79.90),
        Sapato(3, "👟 Tênis Casual", 59.90),
        Sapato(4, "🥾 Sapatênis Casual", 80.90),
        Sapato(5, "👞 Tênis Slip On", 189.90),
        Sapato(6, "👟 Tênis Academia e Corrida Gel", 61.90),
        Sapato(7, "👟 Tênis Hylane Skatista", 77.90),
        Sapato(8, "🥿 Sapatilha Mocassim Fino", 49.90),
        Sapato(9, "🥿 Sapatilha Feminina Salomé", 63.90),
        Sapato(10, "🥿 Sandália Chinelo", 62.90),
        Sapato(11, "🩰 Sandália Infantil Tratora Flatform", 189.90),
        Sapato(12, "👢 Bota de Couro", 149.90),
        Sapato(13, "👡 Sandália Plataforma Original", 74.90),
        Sapato(14, "🩰 Sandália Rasteira com Strass Brilho", 45.90),
        Sapato(15, "🩰 Sandália Saltinho Baixo com Strass Brilho", 44.90),
        Sapato(16, "🩰 Chinelo com Flor em Relevo", 49.90),
        Sapato(17, "🩰 Papete de Luxo no Formato de Gladiadora", 189.90),
        Sapato(18, "🩰 Rasteirinha Glitter Strass", 45.90),
        Sapato(19, "👡 Sandália de Strass com Enfeite de Coração", 52.90),
        Sapato(20, "🩰 Sandália Ajustável", 39.90),
        ]

    @staticmethod
    def verProdutos():
        """ Exibe todos os produtos contidos no catálogo da loja. """
        
        print("-" * 10, "👠 CATÁLOGO 👠", "-" * 10)
        for produto in Sapatos.catalogo:
            print(produto.mostrar())
        print("\n✨ Escolha seu estilo e retorne para o menu para adicionar no carrinho!✨\n")