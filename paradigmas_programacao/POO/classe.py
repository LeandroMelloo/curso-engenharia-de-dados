"""
    objetos: que são os representantes de um modelo (ou ideia) que chamamos de 'classe'
        classe: Produto
            - atributos: características
                - nome
                - preco
                - quantidade
            - métodos: funções
                - __init__

    Para exemplificar, podemos pensar na definição de uma classe para representar um Produto
    em um estoque. E vamos considerar que esse produto tem atributos de nome, preço e quantidade.
    O código abaixo mostra a criação dessa classe no Python
"""

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    """
        E pronto, criamos um objeto da nossa classe Produto. Para conseguirmos observar uma resposta
        clara sobre seus atributos e/ou comportamentos, precisamos criar um método para realizar ações
        com essa classe.
    """
    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco}")
        print(f"Quantidade: {self.quantidade}")

    """
        O trabalho com métodos também permite criar comportamentos e regras utilizando os atributos
        da classe. Por exemplo, podemos criar um método mostrar_valor_total_estoque(), que calcula a
        multiplicação do valor da quantidade e o valor do preço unitário dos produtos disponíveis em
        estoque.
    """
    def mostrar_valor_total_estoque(self):
        valor_total = self.preco * self.quantidade
        print(f"O valor total de estoque deste produto é R${round(valor_total, 2)}")

"""
    A partir desse momento, já temos um modelo do que é um produto.
    E pode-se criar as instâncias desse modelo, que chamamos de objetos.
    Por exemplo, criamos um objeto nomeado p1 que possui os atributos: nome 'Água', preço '1.99',
    e quantidade '20'.
    E agora, podemos instanciar novamente um objeto novo, e chamar esse método da classe.
"""

p1 = Produto("Água", 1.99, 20)
p1.mostrar_info()
p1.mostrar_valor_total_estoque()

p2 = Produto("Refrigerante", 4.99, 25)
p2.mostrar_info()
p2.mostrar_valor_total_estoque()

"""
    Herança:
        Representa a capacidade de criar novas classes a partir de outras classes existentes,
        com a função de estender funcionalidades, e possibilita reutilizar código.
        A herança permite que classes compartilhem comportamentos e atributos comuns,
        ao mesmo tempo que permitem que as classes filhas derivadas possuam novas funcionalidades
        específicas. Por meio da herança, também é possível definir uma ordem de hierarquia entre os
        objetos.

        Retomando ao exemplo da classe Produto, nós poderíamos criar uma classe derivada chamada
        ProdutoPerecivel. Essa classe derivada tem todas as informações da classe pai e possui um
        atributo adicional chamado data_validade para representar o vencimento do produto.
"""
class ProdutoPerecivel(Produto):
    # Adição de um novo atributo "data_validade"
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade

    # Novo comportamento de mostrar a validade do Produto.
    def mostrar_validade(self):
        print(f"O produto vence no dia {self.data_validade}")

    """
        Polimorfismo:
            Representa a capacidade de um objeto ser utilizado com comportamentos de maneiras diferentes,
            a depender do contexto em que é inserido.

            No caso das classes Produto e ProdutoPerecivel, o método mostrar_info() pode ter um
            comportamento diferente na classe derivada ProdutoPerecivel, onde podemos adicionar um
            aviso informando que o produto é perecível.
    """
    def mostrar_info(self):
        super().mostrar_info()
        print("="*30)
        print(f"Esse produto é perecível!")
        print("="*30)

"""
    Ao criar um novo objeto da classe ProdutoPerecivel, podemos utilizar tanto os métodos da classe pai
    (Produto), quanto também o método novo mostrar_validade.
"""
p3 = ProdutoPerecivel('Leite', 7.99, 10, '10/05/2023')
p3.mostrar_info()
p3.mostrar_valor_total_estoque()
p3.mostrar_validade() # Método novo

"""
    A característica de uma classe derivada compartilhar o mesmo nome de uma classe pai facilita a
    aplicação e uso do mesmo método em laços de repetição e outras situações quando precisa-se usar
    objetos distintos de várias classes derivadas. No exemplo abaixo, utilizamos um laço de repetição
    para aplicar o mesmo método mostrar_info() em uma lista com um carrinho de compras dos objetos
    criados.
"""
carrinho_produtos = [
    Produto("Água", 1.99, 20),
    Produto("Refrigerante", 4.99, 25),
    ProdutoPerecivel('Leite', 7.99, 10, '10/05/2023'),
    ProdutoPerecivel('Maçã', 0.99, 15, '28/06/2025')
]

for i in carrinho_produtos:
  i.mostrar_info()
  print("-=" * 30)