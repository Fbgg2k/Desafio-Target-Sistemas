Programa simples em Python que inverte os caracteres de uma string sem usar funções prontas como `reverse`. O método usado é iterar sobre a string de trás para frente e construir a string invertida manualmente.

```python
def inverter_string(texto):
    texto_invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

# Testando o programa
entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
```

### **Como funciona:**
1. A função `inverter_string` utiliza um laço `for` para percorrer a string da última posição (índice `len(texto) - 1`) até a primeira (índice `0`).
2. Para cada caractere, adiciona-o a uma nova string, chamada `texto_invertido`.
3. O resultado é retornado ao final.

### **Exemplo de execução:**
**Entrada:**  
```
Digite uma string para inverter: exemplo
```

**Saída:**  
```
String invertida: olpmexe
```