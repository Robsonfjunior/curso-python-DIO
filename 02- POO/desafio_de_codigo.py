class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
      self._nome = nome
      self._numero = numero
      self._plano = plano

    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    @property
    def nome(self):
      return self._nome
      
    @property
    def numero(self):
      return self._numero
      
    @property
    def plano(self):
      return self._plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

print(usuario)