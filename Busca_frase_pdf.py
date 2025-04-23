#pip install PyPDF2

import os
import PyPDF2

def pesquisar_pdfs(pasta, frase_busca, arquivo_log):
    """
    Pesquisa arquivos PDF em uma pasta por uma frase específica e gera um arquivo de log.

    Args:
        pasta (str): Caminho da pasta contendo os arquivos PDF.
        frase_busca (str): Frase a ser pesquisada nos arquivos PDF.
        arquivo_log (str): Caminho do arquivo de log a ser gerado.
    """

    with open(arquivo_log, 'w', encoding='utf-8') as log:
        for arquivo in os.listdir(pasta):
            if arquivo.endswith(".pdf"):
                caminho_arquivo = os.path.join(pasta, arquivo)
                try:
                    with open(caminho_arquivo, 'rb') as arquivo_pdf:
                        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
                        num_paginas = len(leitor_pdf.pages)
                        for pagina in leitor_pdf.pages:
                            texto_pagina = pagina.extract_text()
                            if frase_busca.lower() in texto_pagina.lower():
                                log.write(f"Arquivo: {arquivo}, Páginas: {num_paginas}\n")
                                break  # Interrompe a busca no arquivo se a frase for encontrada
                except Exception as e:
                    log.write(f"Erro ao processar {arquivo}: {e}\n")

# Exemplo de uso
pasta_pdfs = "C:"  # Substitua pelo caminho da sua pasta
frase_procurada = "PROCURAR"  # Substitua pela frase que você deseja procurar
arquivo_resultado = "resultado_pesquisa.log"

pesquisar_pdfs(pasta_pdfs, frase_procurada, arquivo_resultado)

print(f"Pesquisa concluída. Resultados salvos em: {arquivo_resultado}")