#Napoleão de Sousa Carvalho Junior - IFMA Campus Buriticupu
#Código criado com o objetivo de limpar textos, que posteriormente serão usados pelo iramuteq.

#Baixe o Anaconda e adicione o corp01.txt no Jupyter Notebook

def limpar_texto(texto):
    # Trocando hífens por underline
    texto = texto.replace("-", "_")
    # Juntando o texto em um parágrafo
    texto = " ".join(texto.split())
    # Retirando caracteres especiais
    caracteres_especiais = "@$&...=(){}\/\"'!%#:Ⓡ-*"
    for char in caracteres_especiais:
        texto = texto.replace(char, "")
    return texto

def main():
    # Abrindo o arquivo corp01.txt para leitura
    with open("corp01.txt", "r") as arquivo_entrada:
        # Lendo o conteúdo do arquivo
        texto_original = arquivo_entrada.read()

    # Aplicando a limpeza de dados ao texto
    texto_limpo = limpar_texto(texto_original)

    # Escrevendo o texto limpo no arquivo corpalter01.txt
    with open("corpalter01.txt", "w") as arquivo_saida:
        # Escrevendo o texto limpo no arquivo de saída
        arquivo_saida.write(texto_limpo)

if __name__ == "__main__":
    main()
