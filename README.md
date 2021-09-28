# Exercício 1 - Multiplicação de Números Grandes

<h1 align="center">Estruturas de Dados e Análise de Algoritmos Mestrado Profissional em Computação Aplicada
Prof. Dr. Eng. Eduardo Takeo Ueda</h1>

O algoritmo para multiplicação de dois valores inteiros X[1..n] e Y [1..n], de n algarismos, que aprendemos na época do ensino fundamental, tem complexidade de tempo Θ(n2). Porém, existe um método de divisão e conquista, conhecido como algoritmo de Karatsuba, publicado em 1962, que realiza a mesma tarefa com com- plexidade O(nlog2 3) ∼= O(n1.58).
Implemente os algoritmos de multiplicação tradicional (do ensino fundamental) e de Karatsuba (apresentado a seguir). Seu programa deve receber dois inteiros X[1..n] e Y [1..n], devolver o produto X · Y , e mostrar o tempo de execução dos 2 algoritmos.
Karatsuba (X, Y , n)

```
se(n≤3)retornaX·Y
q←⌈n2⌉
A←X[q+1..n];B←X[1..q]
C←Y[q+1..n];D←Y[1..q]
E ← Karatsuba (A, C, ⌊n2 ⌋)
F←Karatsuba(B,D,⌈n2⌉)
G←Karatsuba(A+B,C+D,⌈n2⌉+1)
H←G−F−E
R←E×102⌈n2⌉ +H×10⌈n2⌉ +F
retorna R


