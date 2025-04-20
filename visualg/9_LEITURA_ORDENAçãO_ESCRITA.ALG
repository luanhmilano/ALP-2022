Algoritmo "Leitura_ordenação_escrita"
// Desenvolver um programa que leia quatro notas bimestrais de oito alunos e apresente no final os registros
// desses alunos ordenados alfabeticamente pelo campo nome de forma ascendente.

tipo
cadaluno = registro
            nome: caractere
            turma: caracter
            sala: inteiro
            notas: vetor[1..4] de real
            fimregistro

Var
aluno: vetor[1..8] de cadaluno
i, j: inteiro
x: cadaluno

Inicio
para i de 1 até 8 faça
     leia(aluno[i].nome)
     leia(aluno[i].turma)
     leia(aluno[i].sala)
     para j de 1 ate 4 faca
          leia(aluno[i].notas[j])
     fimpara
fimpara

para i de 1 até 7 passo 1 faca
     para j de i+1 até 8 passo 1 faca
          se (aluno[i].nome > aluno[j].nome) entao
             x <- aluno[i]
             aluno[i] <- aluno[j]
             aluno[j] <- x
          fimse
     fimpara
fimpara

para i de 1 ate 8 passo 1 faca
     escreval(aluno[i].nome)
     escreval(aluno[i].turma)
     escreval(aluno[i].sala)
     para j de 1 ate 4 passo 1 faca
          escreval(aluno[i].notas[j])
     fimpara
fimpara

Fimalgoritmo