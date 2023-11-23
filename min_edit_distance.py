from time import perf_counter

def minEditDistance(word1: str, word2: str) -> int:
    matriz = [ [0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)] 

    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if i == 0:
                matriz[0][j] = j #Se i=0, preenche a primeira linha
            elif j == 0:
                matriz[i][0] = i #Se j=0, preenche a primeira coluna
            elif word1[i-1] == word2[j-1]:
                matriz[i][j] = matriz[i-1][j-1] # Caso das diagonais, quando o char em questão é igual na posição de matriz.
            else:
                matriz[i][j] = 1 + min(matriz[i-1][j], matriz[i][j-1], matriz[i-1][j-1]) #Caso as duas letras atualmente sendo comparadas sejam diferentes, 
                                                                                         #descobre qual o menor número entre o número acima, à esquerda e na diagonal e soma 1.

    return matriz[len(word1)][len(word2)]

def get_pairs() -> int:
    pairs = int(input("Quantidade de pares a serem digitados: "))
    return pairs

def get_Strings(pairs: int):
    x_str = []
    y_str = []
    for i in range(pairs):
        x_str.append(input(f"String do par {i+1}: "))
        y_str.append(input(f"String do par {i+1}: "))

    return x_str, y_str


pairs = get_pairs() 
tuple_of_strings = get_Strings(pairs) # Forma uma tupla com duas listas, com cada um dos resultados dos pares. --> (['a', 'b', 'c'], ['a', 'b', 'c'])


for i in range(pairs):
    start = perf_counter()
    print(minEditDistance(tuple_of_strings[0][i], tuple_of_strings[1][i])) #A cada iteração, mostra a distância mínima entre cada um dos pares inseridos pelo usuário.
    end = perf_counter()
    print((end - start) * 1000) #Mostra o tempo de execução para achar a distância mínima de cada par.