Programa em Python que calcula o percentual de representação de cada estado no faturamento total da distribuidora:

```python
def calcular_percentuais(faturamento_por_estado):
    # Calcula o valor total do faturamento
    total = sum(faturamento_por_estado.values())
    
    # Calcula o percentual de cada estado
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_por_estado.items()}
    
    return total, percentuais

# Faturamento mensal por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula e exibe os resultados
total, percentuais = calcular_percentuais(faturamento)

print(f"Faturamento total: R${total:.2f}\n")
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
```

### **Como o programa funciona:**
1. Cria um dicionário `faturamento` para armazenar os valores de faturamento de cada estado.
2. Calcula o total do faturamento somando os valores do dicionário com `sum(faturamento.values())`.
3. Calcula o percentual de cada estado dividindo seu valor pelo total e multiplicando por 100.
4. Exibe os percentuais formatados com duas casas decimais.

---

### **Saída esperada:**

```
Faturamento total: R$180759.98

Percentual de representação por estado:
SP: 37.53%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
Outros: 10.98%
```

### **Personalização:**
- Para entrada dinâmica de valores, substitua o dicionário fixo por entradas solicitadas ao usuário.
- O programa é flexível e pode ser facilmente adaptado para outros estados ou valores de faturamento.