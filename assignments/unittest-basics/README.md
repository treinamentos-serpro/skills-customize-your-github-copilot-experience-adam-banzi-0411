# 📘 Assignment: Automated Testing with unittest

## 🎯 Objective

Aprenda a criar e executar testes automatizados com o módulo `unittest` da biblioteca padrão do Python. Você vai verificar resultados, cobrir casos de entrada diferentes e confirmar o tratamento de erros sem instalar dependências externas.

## 📝 Tasks

### 🛠️ Verificar resultados com assertEqual

#### Descrição
Complete os testes de `add_numbers()` no código inicial, substituindo cada `pass` por uma ou mais verificações que comparem o resultado obtido com o esperado.

#### Requisitos
O programa concluído deve:

- Usar `self.assertEqual()` para comparar os resultados.
- Testar a soma de números positivos.
- Testar a soma envolvendo zero e números negativos.

### 🛠️ Testar resultados booleanos

#### Descrição
Complete os testes de `is_even()` para verificar tanto os casos em que a função retorna `True` quanto aqueles em que retorna `False`.

#### Requisitos
O programa concluído deve:

- Usar `self.assertTrue()` para verificar um número par.
- Usar `self.assertFalse()` para verificar um número ímpar.
- Incluir pelo menos um caso de borda, como zero ou um número negativo.

### 🛠️ Verificar erros e executar a suíte

#### Descrição
Complete os testes de `safe_divide()` para conferir um resultado válido e verificar que a função sinaliza uma divisão por zero.

#### Requisitos
O programa concluído deve:

- Usar `self.assertEqual()` para verificar o resultado de uma divisão válida.
- Usar `self.assertRaises()` para confirmar que dividir por zero levanta `ValueError`.
- Executar todos os testes e confirmar que a suíte termina sem falhas usando:

  ```bash
  python starter-code.py
  ```
