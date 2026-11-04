
# 📘 Tarefa: Jogo da Forca

## 🎯 Objetivo

Pratique strings, listas, seleção aleatória, laços de repetição e condicionais ao criar um jogo da Forca em que o jogador tenta adivinhar uma palavra antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Preparação da palavra e do jogo

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher uma palavra secreta e preparar as variáveis que representam o estado do jogo.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista `words`.
- Inicializar uma coleção para registrar as letras já tentadas e um contador de palpites incorretos.
- Definir o limite de palpites incorretos permitido.
- Exibir o progresso da palavra, mostrando as letras ainda não adivinhadas como `_` e as letras corretas nas posições correspondentes.

### 🛠️ Palpites e resultado da partida

#### Descrição
Implemente o loop principal para receber palpites, atualizar o estado do jogo e encerrar a partida quando a palavra for descoberta ou o limite de erros for atingido.

#### Requisitos
O programa concluído deve:

- Solicitar ao jogador um palpite de letra e informar se ela aparece na palavra secreta.
- Atualizar e exibir o progresso após cada palpite.
- Contar palpites incorretos sem ultrapassar o limite definido.
- Encerrar a partida quando todas as letras da palavra forem adivinhadas ou quando o limite de palpites incorretos for atingido.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra secreta.