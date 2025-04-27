maiormedia=0
menormedia=11
percentual=0
alunosmaior5=0

alunos=[]
quant_alunos=int(input('Digite quantos alunos serão inseridos: '))

for cont in range (quant_alunos):
    dados=[]
    nome=input(f"\nDigite o nome do aluno: ")

    prova=[]
    p1=float(input("Digite a nota da primeira prova teórica: "))
    while p1<0 or p1>10:
        print('Nota Inválida')
        p1=float(input("Digite uma nota entre 0 a 10: "))

    p2=float(input("Digite a nota da segunda prova teórica: "))
    while p2<0 or p2>10:
        print('Nota Inválida')
        p2=float(input("Digite a nota da segunda prova teórica: "))

    projeto=[]
    pj1=float(input('Digite a nota do primeiro projeto: '))
    while pj1<0 or pj1>10:
        print('Nota Inválida')
        pj1=float(input('Digite a nota do primeiro projeto: '))

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
    
    if maiormedia<mediafinal:
        maiormedia=mediafinal

    if menormedia>mediafinal:
        menormedia=mediafinal

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

menu=True
while menu:
    print("-"*50)
    print("\nMenu:")
    print("1 - Mostrar Boletim Completo")
    print("2 - Consultar Aluno")
    print("3 - Mostrar Aluno com Maior Média Final")
    print("4 - Mostrar Aluno com Menor Média Final")
    print("5 - Mostrar Percentual de Alunos com Média Final > 5")
    print("6 - Sair")
    print("-"*50)
    
    opcao = int( input("Digite a opção desejada: "))
    menu=False

    if opcao == 1:
        print("\n>>>Boletim<<<")
        
        for estudante in alunos:
            print("-" * 30)
            print("Nome:", estudante[0])
            print("Notas Teóricas (T1, T2):", estudante[1])
            print("Notas de Projeto (P1, P2):", estudante[2])
            print(f"Média Teórica (MT):{estudante[3][0]:.2f}")
            print(f"Média Prática (MP): {estudante[3][1]:.2f}")
            print(f"Média Final (MF):{ estudante[4]:.2f}")
            print("-" * 30)
            
    elif opcao == 2:
        nomebusca = input(f"\nDigite o nome do aluno para consulta: ").lower()
        existe = False
        for estudante in alunos:
            if estudante[0].lower() == nomebusca:
                print("Nome:", estudante[0])
                print("Notas Teóricas (T1, T2):", estudante[1])
                print("Notas de Projeto (P1, P2):", estudante[2])
                print(f"Média Teórica (MT): {estudante[3][0]:.2f}")
                print(f"Média Prática (MP): {estudante[3][1]:.2f}")
                print(f"Média Final (MF): { estudante[4]:.2f}")
                existe = True
                break
        if not existe:
            print("!"*30)
            print("ALUNO NÃO ENCONTRADO.")
            print("!"*30)

    elif opcao == 3:
        for aluno_maiormedia in alunos:
            if aluno_maiormedia[4] == maiormedia:
                nome_maiormedia = aluno_maiormedia[0] 
        print(f"\na maior media final é de {maiormedia:.2f} do aluno {nome_maiormedia}")
        
    elif opcao == 4:
        for aluno_menormedia in alunos:
            if aluno_menormedia[4] == menormedia:
                nome_menormedia = aluno_menormedia[0]
        print(f"\n A menor média final é de {menormedia:.2f} do aluno {nome_menormedia}")

    elif opcao == 5: 
        for medias in alunos:
            if medias[4]> 5:
                alunosmaior5+=1
                percentual= (alunosmaior5/ quant_alunos)* 100

        print(f"\n O percentual de alunos com média final maior que 5 é de {percentual:.0f}%")
            
    elif opcao == 6:
        print("Saindo...")
        menu=False
    else: 
        print('Opção inválida')
    if opcao!=6:
        menu=True