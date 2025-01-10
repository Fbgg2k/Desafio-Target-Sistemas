### Aqui está o código em Python que calcula a sequência de Fibonacci até que o número informado seja encontrado (ou superado) e verifica se ele pertence à sequência:


def verifica_fibonacci(numero):
    # Inicia os dois primeiros números da sequência
    fib1, fib2 = 0, 1
    
    # Caso especial para número 0
    if numero == 0:
        return True
    
    # Calcula a sequência até encontrar ou ultrapassar o número
    while fib2 <= numero:
        if fib2 == numero:
            return True
        fib1, fib2 = fib2, fib1 + fib2  # Atualiza os valores da sequência
        
    return False

# Entrada do número (pode ser alterado para um valor fixo)
numero_informado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica e exibe o resultado
if verifica_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} NÃO pertence à sequência de Fibonacci.")

### Como funciona o código:
###1. Inicia os primeiros números da sequência: `fib1 = 0` e `fib2 = 1`.
###2. Usa um loop para calcular o próximo número da sequência até que ele seja maior que o número informado.
###3. Em cada iteração:
###   - Verifica se o número atual da sequência (`fib2`) é igual ao número informado.
###   - Atualiza os dois últimos números da sequência para calcular o próximo valor.
###4. Retorna `True` se o número pertence à sequência; caso contrário, `False`.

### Exemplo de execução:

###Entrada:  

###Digite um número para verificar se pertence à sequência de Fibonacci: 21


###Saída:  

###O número 21 pertence à sequência de Fibonacci.


###Entrada:  

###Digite um número para verificar se pertence à sequência de Fibonacci: 22


###Saída:  

###O número 22 NÃO pertence à sequência de Fibonacci.
