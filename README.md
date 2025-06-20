# Atividade 1 – Fila de Triagem com Lista Encadeada

## Descrição
Este projeto implementa um sistema simples de triagem hospitalar usando **lista encadeada não circular** em Python. Cada paciente recebe um cartão numerado verde (V) ou amarelo (A), conforme o grau de urgência, e é inserido em uma fila que prioriza os cartões amarelos e ordena por número dentro de cada cor.

---

## Funcionalidades
- **Inserção de pacientes**  
  - Cartões verdes (V): inseridos ao final da fila  
  - Cartões amarelos (A): inseridos logo após os demais amarelos, antes dos verdes  
  - Numeração automática:  
    - Verdes a partir de 1  
    - Amarelos a partir de 201  
- **Listagem da fila de espera** na ordem de atendimento  
- **Atendimento** (remoção do primeiro da fila)  
- **Menu interativo** para inserir, listar, chamar paciente e sair

---

## Estrutura de Código

- `Nodo` – classe que representa cada cartão (número, cor e ponteiro para o próximo nodo)  
- `FilaTriagem` – classe que gerencia a lista encadeada e os contadores de numeração  
  - `inserirSemPrioridade(nodo)` – adiciona um nodo ao final da lista  
  - `inserirComPrioridade(nodo)` – insere nodo amarelo antes dos verdes  
  - `inserir()` – lê cor do usuário, numera automaticamente, cria e insere o nodo  
  - `imprimirListaEspera()` – exibe todos os cartões na fila  
  - `atenderPaciente()` – remove e chama o primeiro paciente  
- `menu()` – laço principal com as opções:
  1. Adicionar paciente  
  2. Mostrar pacientes  
  3. Chamar paciente  
  4. Sair  

---

## Requisitos
- Python 3.6+  

---

## Como Executar

1. Clone ou faça download deste repositório.  
2. No terminal, navegue até a pasta do projeto.  
3. Execute:

   ```bash
   python nome_do_arquivo.py
