#Nome: Oliver Kieran Galvão McCormack      TIA: 42122058

#Nome: PEDRO LOUREIRO MORONE BRANCO VOLPE  TIA: 42131936

import random

def numerosSorteados(nsorteados): # GERA OS NUMEROS SORTEADOS SEM REPETIÇÃO
    for i in range(len(nsorteados)):
        nsorteados[i] += random.randint(1,60)
        j = 0
        while j < i:
            if nsorteados[j] == nsorteados[i]:
                    nsorteados[i] = random.randint(1,60)
                    j = 0
            else:
                j += 1
    nsorteados.sort() # COLOCAMOS UM .SORT(), MESMO QUE ELE NÃO SEJA NECESSARIO, APENAS PARA MELHOR VISUALIZAÇÃO
                      # SENDO ASSIM DECIDIMOS MANTE-LO COMO UM METODO PYTHON
    return nsorteados

def geraApostas(): # Geração de todas as apostas de todos os participantes e escreve no arquivo participantes.txt
    aposta = [0]*6
    apostas = open('participantes.txt','w')
    for j in range(100000):
        
        for i in range(6):
            aposta[i] = random.randint(1,60)
            l = 0
            while l < i:
                if aposta[l] == aposta[i]:
                    aposta[i] = random.randint(1,60)
                    l = 0
                else:
                    l += 1
        aposta.sort() # COLOCAMOS UM .SORT(), MESMO QUE ELE NÃO SEJA NECESSARIO, APENAS PARA MELHOR VISUALIZAÇÃO
                      # SENDO ASSIM DECIDIMOS MANTE-LO COMO UM METODO PYTHON
        for n in range(len(aposta)-1):
            apostas.write(f'{aposta[n]}' + ' ')
        apostas.write(f'{aposta[n+1]}')
            
        
        apostas.write('\n')
    apostas.close()

def ganhadores(ns): # Verificação de quantos ganhadores houveram de cada tipo (sena, quina e quadra)
    apostas = open('participantes.txt','r')
    vazio = ''
    aposta = []
    sena = 0
    quina = 0
    quadra = 0
    
    while True:
        linha = apostas.readline()
        if linha == vazio:
            break
        else:
            linha = linha.rstrip()
            aposta.append(linha)

    for j in range(100000):
        info = []
        info = aposta[j].split(' ')
        vet = [0]*6
       
        for p in range(6):          # ADICIONAMOS A LISTA INFO[p], EM UM VETOR PARA MELHOR MANIPULAÇÃO 
            vet[p] += int(info[p])

        co = 0
        for t in range(len(vet)):   # INTERSECÇÃO ENTREO O VETOR "VET" E O VETOR DE NUMEOROS SORTEADOS,
                                    # RESULTANDO O NUMEROS DE VALORES IGUAIS 
            for h in range(len(ns)):
                if vet[t] == ns[h]:
                    co += 1 
        acertos = co

        if acertos == 6:            # USAMOS A CONTAGEM DE VALORES IGUAIS PARA DIVIDI-LOS ENTRE 6(SENA),5(QUINA) E 4(QUADRA)
            sena += 1
            
        elif acertos == 5:
            quina += 1
            
        elif acertos == 4:
            quadra += 1
            
            
    return sena,quina,quadra

def dividePremio(sena, quina, quadra, premio): #Divisão do prêmio de acordo com a proporção estabelecida no enunciado para cada tipo de ganhador
    c = 0     # VARIAVEL PARA CASO OCORRA ACUMULO
    sg = 0    # SENA GANHOU
    quig = 0  # QUINA GANHOU
    quag = 0  # QUADRA GANHOU
    if sena > 0 and quina > 0 and quadra > 0:
        sg = (premio*0.62)
        quig = (premio*0.19)
        quag = (premio*0.19)
    elif sena > 0 and quina > 0 and quadra == 0:
        sg = (premio*0.62)
        quig = (premio*0.38)
    elif sena > 0 and quina == 0 and quadra > 0:
        sg = (premio*0.62)
        quag = (premio*0.38)
    elif sena > 0 and quina == 0 and quadra == 0:
        sg = premio
    elif sena == 0 and quina > 0 and quadra > 0:
        quig = (premio*0.50)
        quag = (premio*0.50)
    elif sena == 0 and quina > 0 and quadra == 0:
        quig = premio
    elif sena == 0 and quina == 0 and quadra > 0:
        quag = premio
    else:
        c = premio
    
    return sg,quig,quag,c

def geraSaida(premio,ns,sena,quina,quadra,sg,quig,quag,c): # ESSA FUNÇAO REALIZA A GRAVAÇÃO DOS RESULTADOS EM UM ARQUIVO "SAIDA"
    saida = open('arquivo_de_saída.txt','w',encoding="utf-8")
    if c == 0:
        n = 'Não acumula!'
    else:
        n = 'Acumula:', c
        
    if sena == 0:      # DIVISÃO DA SENA 
        ds = sg
    else:
        ds = sg//sena

    if quina == 0:     # DIVISÃO QUINA 
        dqui = quig
    else:
        dqui = quig // quina

    if quadra == 0:    # DIVISÃO QUADRA
        dqua = quag
    else:
        dqua = quag // quadra
        
    saida.write(f'CONCURSO MEGA SENA DA VIRADA\n')
    saida.write(f'PRÊMIO: {premio}\n')
    saida.write(f'NÚMEROS SORTEADOS\n')
    saida.write(f'{ns[0]} {ns[1]} {ns[2]} {ns[3]} {ns[4]} {ns[5]}\n')
    saida.write(f'GANHADORES:\n')
    saida.write(f'FAIXA   |  GANHADORES   |       PREMIO         | DIVISAO\n')
    saida.write(f'SENA    | {sena}        |    {sg}              | {ds}\n')
    saida.write(f'QUINA   | {quina}       |    {quig}            | {dqui}\n')
    saida.write(f'QUADRA  | {quadra}      |    {quag}            | {dqua}\n')
    saida.write(f'{n}')

    saida.close()

def main(): # É O MAIN (ONDE CHAMAMOS AS FUNÇÕES)
    nsorteados = [0]*6

    premio = float(input('Digite o valor do premio:'))

    ns = numerosSorteados(nsorteados)
    
    geraApostas()

    sena,quina,quadra = ganhadores(ns)

    sg, quig, quag, c = dividePremio(sena, quina, quadra, premio)

    geraSaida(premio, ns, sena, quina, quadra, sg, quig, quag, c)
    
main()