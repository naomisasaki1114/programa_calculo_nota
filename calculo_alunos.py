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
    dados.append(prova)
    dados.append(projeto)
    dados.append(media)
    dados.append(mediafinal)
    alunos.append(dados)
print(alunos[:])
##MENU DE OPÇÕES
opcao=0
while opcao<6:
    print("-"*50)
    print("\nMenu:")
    print("1 - Mostrar Boletim Completo")
    print("2 - Consultar Aluno")
    print("3 - Mostrar Aluno com Maior Média Final")
    print("4 - Mostrar Aluno com Menor Média Final")
    print("5 - Mostrar Percentual de Alunos com Média Final > 5")
    print("6 - Sair")
    print("-"*50)
    
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("\n>>>Boletim<<<")
        for estudante in alunos:
            print("Nome:", estudante[0])
            print("Notas Teóricas (T1, T2):", estudante[1])
            print("Notas de Projeto (P1, P2):", estudante[2])
            print("Média Teórica (MT):", estudante[3][0])
            print("Média Prática (MP):", estudante[3][1])
            print("Média Final (MF):", estudante[4])
            print("-" * 30)

    elif opcao == "2":
        nomebusca = input("Digite o nome do aluno para consulta: ")
        existe = False
        for estudante in alunos:
            if estudante[0] == nomebusca:
                print("Nome:", estudante[0])
                print("Notas Teóricas (T1, T2):", estudante[1])
                print("Notas de Projeto (P1, P2):", estudante[2])
                print("Média Teórica (MT):", estudante[3][0])
                print("Média Prática (MP):", estudante[3][1])
                print("Média Final (MF):", estudante[4])
                existe = True
                break
        if not existe:
            print("!"*30)
            print("ALUNO NÃO ENCONTRADO.")
            print("!"*30)
            
            #ADICIONAR AS OUTRAS OPÇÕES AQUI
            
            #OPÇÃO FINAL, FIM DO PROGRAMA

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
