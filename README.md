# Exercício 1 - Multiplicação de Números Grandes

<h1 align="center">Estruturas de Dados e Análise de Algoritmos Mestrado Profissional em Computação Aplicada
Prof. Dr. Eng. Eduardo Takeo Ueda</h1>

O algoritmo para multiplicação de dois valores inteiros X[1..n] e Y [1..n], de n algarismos, que aprendemos na época do ensino fundamental, tem complexidade de tempo Θ(n2). Porém, existe um método de divisão e conquista, conhecido como algoritmo de Karatsuba, publicado em 1962, que realiza a mesma tarefa com com- plexidade O(nlog2 3) ∼= O(n1.58).
Implemente os algoritmos de multiplicação tradicional (do ensino fundamental) e de Karatsuba (apresentado a seguir). Seu programa deve receber dois inteiros X[1..n] e Y [1..n], devolver o produto X · Y , e mostrar o tempo de execução dos 2 algoritmos.
Karatsuba (X, Y , n)

1. se(n≤3)retornaX·Y
2. q←⌈n2⌉
3. A←X[q+1..n];B←X[1..q]
4. C←Y[q+1..n];D←Y[1..q]
5. E ← Karatsuba (A, C, ⌊n2 ⌋)
6. F←Karatsuba(B,D,⌈n2⌉)
7. G←Karatsuba(A+B,C+D,⌈n2⌉+1)
8. H←G−F−E
9. R←E×102⌈n2⌉ +H×10⌈n2⌉ +F
10. retorna R


