import pickle

# Carregar os dados dos usuários a partir de um arquivo binário
with open('usuarios.bin', 'rb') as arquivo:
    usuarios = pickle.load(arquivo)


def maior(posI,posJ,usuario):
    
    #seguidores
    
    seguidoresI = len(usuario[posI][2])
    seguidoresJ = len(usuario[posJ][2])
    if seguidoresI <seguidoresJ:return True
    if seguidoresI >seguidoresJ:return False
    #seguindo
    seguindoI = len(usuario[posI][1])
    seguindoJ = len(usuario[posJ][1])
    if seguindoI<seguindoJ:return True
    if seguindoI>seguindoJ:return False
    #nome
    nomeI = (usuario[posI][0])
    nomeJ = (usuario[posJ][0])
    if nomeI>nomeJ:return True
    if nomeI<nomeJ:return False
    print('a')
    return posJ<posI

def merge(usuario, lista, lesq, ldir):
    i = 0
    j =0
    k = 0  
    
    while i<len(lesq) and j<len(ldir):
        if not maior(lesq[i],ldir[j],usuario):
            lista[k]=lesq[i]
            i+=1
        else:
            lista[k]=ldir[j]
            j+=1
        k+=1

    while i < len(lesq):
        lista[k] = lesq[i]
        i += 1
        k += 1

    while j < len(ldir):
        lista[k] = ldir[j]
        j += 1
        k += 1

def mergesort(lista, usuarios):
    if len(lista) > 1:
        meio = len(lista) // 2
        lesq = lista[:meio]
        ldir = lista[meio:]
        mergesort(lesq, usuarios)
        mergesort(ldir, usuarios)
        merge(usuarios, lista, lesq, ldir)

def fazlista(usuarios):
    lista = list(usuarios.keys())
    mergesort(lista, usuarios)
    return lista

def imprime(lista_ordenada,usuarios):
    for chave in lista_ordenada:
        seguindo = len(usuarios[chave][1])
        seguidores = len(usuarios[chave][2])
        print(f'{usuarios[chave][0]} (segue {seguindo}, seguido por {seguidores})')


# Exemplo de uso:
def main():
    lista_ordenada = fazlista(usuarios)
    imprime(lista_ordenada,usuarios)
if __name__=='__main__':
    main()