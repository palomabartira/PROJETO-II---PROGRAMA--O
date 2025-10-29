class Sapatos:
    """Essa classe tem como objetivo mostrar as opções de sapatos presentes no catálogo.
    Para isso, cria uma lista e dentro dela coloca um dicionário para organizar as informações sobre
    o produto."""
   
    catalogo = [
        {"id": 1, "nome": "🩰 Papete Casual", "preco": 64.90},
        {"id": 2, "nome": "👠 Salto Alto", "preco": 79.90},
        {"id": 3, "nome": "👟 Tênis Casual", "preco": 59.90},
        {"id": 4, "nome": "🥾 Sapatênis Casual", "preco": 80.90},
        {"id": 5, "nome": "👞 Tênis Slip On", "preco": 189.90},
        {"id": 6, "nome": "👟 Tênis Academia e Corrida Gel", "preco": 61.90},
        {"id": 7, "nome": "👟 Tênis Hylane Skatista", "preco": 77.90},
        {"id": 8, "nome": "🥿 Sapatilha Mocassim Fino", "preco": 49.90},
        {"id": 9, "nome": "🥿 Sapatilha Feminina Salomé", "preco": 63.90},
        {"id": 10, "nome": "🥿 Sandália Chinelo", "preco": 62.90},
        {"id": 11, "nome": "🩰 Sandália Infantil Tratora Flatform", "preco": 189.90},
        {"id": 12, "nome": "👢 Bota de Couro", "preco":149.90},
        {"id": 13, "nome": "👡 Sandália Plataforma Original", "preco": 74.90},
        {"id": 14, "nome": "🩰 Sandália Rasteira com Strass Brilho", "preco": 45.90},
        {"id": 15, "nome": "🩰 Sandália Saltinho Baixo com Strass Brilho", "preco": 44.90},
        {"id": 16, "nome": "🩰 Chinelo com Flor em Relevo", "preco": 49.90},
        {"id": 17, "nome": "🩰 Papete de Luxo no Formato de Gladiadora", "preco": 189.90},
        {"id": 18, "nome": "🩰 Rasteirinha Glitter Strass", "preco": 45.90},
        {"id": 19, "nome": "👡 Sandália de Strass com Enfeite de Coração", "preco": 52.90},
        {"id": 20, "nome": "🩰 Sandália Ajustável", "preco": 39.90},
        ]

    @staticmethod
    def verProdutos():
        """Percorre a lista de dicionários 'Sapatos.catalogo', imprimindo o
        ID, nome e preço de cada produto para o usuário."""
        print("-" * 10, "👠 CATÁLOGO 👠", "-" * 10)
        for produto in Sapatos.catalogo:
            print(f"ID: {produto['id']} - {produto['nome']} - R$ {produto['preco']}")
                    
        print("\n✨ Escolha seu estilo e retorne para o menu para adicionar no carrinho! ✨\n")