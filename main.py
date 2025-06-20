# A - Lista Encadeada Simples
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

# Lista não circular
class FilaTriagem:
    def __init__(self):
        self.head = None
        self.contadorV = 0
        self.contadorA = 200

    # B - função inserirSemPrioridade(nodo)

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    # C - função inserirComPrioridade(nodo)
    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo

        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    # D - Função inserir

    # Solicitar a cor A ou V
    def inserir(self):
        cor = ''
        while cor not in ('A', 'V'):
            cor = input("Selecione a cor do cartão - A ou V: ").strip().upper()

        # selecionando a cor
        if cor == 'V':
            self.contadorV += 1
            num = self.contadorV
            nodo = Nodo(num, 'V')
            if not self.head:
                self.head = nodo
            else:
                self.inserirSemPrioridade(nodo)

        else:
            self.contadorA += 1
            num = self.contadorA
            nodo = Nodo(num, 'A')
            if not self.head:
                self.head = nodo
            else:
                self.inserirComPrioridade(nodo)
        print(f'>Paciente {cor}{num} inserido na fila.')

    # E - Função imprimir lista de espera
    def imprimirListaEspera(self):
        if not self.head:
            print("Lista vazia!")
            return
        print("Pacientes na fila de espera: ")
        atual = self.head
        while atual:
            print(f"[{atual.cor}{atual.numero}]", end=" ")
            atual = atual.proximo
        print("\n")

    # F - função atenderPaciente()
    def atenderPaciente(self):
        if not self.head:
            print("Não há pacientes registrados!")
            return
        paciente = self.head
        self.head= paciente.proximo
        print(f"Paciente {paciente.cor}{paciente.numero}, comparecer a sala de atendimento.")

# G - menu para utilização
def menu():
    fila = FilaTriagem()
    while True:
        #a.	Deve-se apresentar as opções (1 – adicionar paciente a fila, 2 – mostrar pacientes na fila, 3 – chamar paciente, 4 – sair)
        print("Selecione uma das opções abaixo:")
        print("1 – Adicionar paciente a fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair ")
        escolha = input().strip()
        #b. Se escolhida a opção 1, chamar a função inserir().
        if escolha == '1':
            fila.inserir()
        # c. Se escolhida a opção 2, chamar a função imprimirListaEspera().
        elif escolha == '2':
            fila.imprimirListaEspera()
        #d. Se escolhida a opção 3, chamar a função atenderPaciente().
        elif escolha == '3':
            fila.atenderPaciente()
        #e.	Se escolhida a opção 4, encerrar o programa.
        elif escolha == '4':
            print("Encerrar programa.")
            break
        #f.	Se escolhida uma opção diferente as opções disponíveis, volte para o menu.'
        else:
            print("Selecione uma opção válida!")

if __name__ == "__main__":
    menu()








