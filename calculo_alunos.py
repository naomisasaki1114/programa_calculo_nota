alunos=[]
quant_alunos=int(input('Digite quantos alunos serão inseridos: '))

for cont in range (quant_alunos):
    dados=[]
    nome=input("Digite o nome do aluno: ")

    prova=[]
    ##insercao e validacao da primeira prova teorica
    p1=float(input("Digite a nota da primeira prova teórica: "))
    while p1<0 or p1>10:
        print('Nota Inválida')
        p1=float(input("Digite uma nota entre 0 a 10: "))

    ##insercao e validacao da segunda prova teorica
    p2=float(input("Digite a nota da segunda prova teórica: "))
    while p2<0 or p2>10:
        print('Nota Inválida')
        p2=float(input("Digite a nota da segunda prova teórica: "))

    projeto=[]
    #insercao e validacao do primeiro projeto
    pj1=float(input('Digite a nota do primeiro projeto: '))
    while pj1<0 or pj1>10:
        print('Nota Inválida')
        pj1=float(input('Digite a nota do primeiro projeto: '))

    #insercao e validacao do segundo projeto
    pj2=float(input('Digite a nota do segundo projeto: '))
    while pj2<0 or pj2>10:
        print('Nota Inválida')
        pj2=float(input('Digite a nota do segundo projeto: '))

    media=[]
    mediateorica=(0.4*p1)+(0.6*p2)
    mediapratica=(pj1+pj2)/2
    if mediateorica>5 and mediapratica>5:
        mediafinal=0.3*mediapratica + 0.7*mediateorica
    else:
        menor=6
        if menor>mediateorica:
            menor=mediateorica
        if menor>mediapratica:
            menor=mediapratica
        mediafinal=menor

    ##insercao de dados em cada lista
    media.append(mediateorica)
    media.append(mediapratica)
    projeto.append(pj1)
    projeto.append(pj2)
    prova.append(p1)
    prova.append(p2)
    dados.append(nome)
    dados.append(projeto)
    dados.append(media)
    dados.append(mediafinal)
    alunos.append(dados)
print(alunos[:])
