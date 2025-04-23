## 🔍 Pesquisa de Frases em Arquivos PDF
Este script em Python permite pesquisar uma frase específica dentro de arquivos PDF em uma pasta e gerar um arquivo de log com os resultados encontrados.

## 📄 Descrição
O script percorre todos os arquivos PDF em um diretório especificado, procura por uma frase informada em cada arquivo e registra os nomes dos arquivos onde a frase foi encontrada, junto com o número de páginas. Caso ocorra algum erro durante a leitura de um arquivo, o erro também é registrado no log.

## 📦 Requisitos
* Python 3.x
* Biblioteca PyPDF2

Você pode instalar o PyPDF2 com o seguinte comando:

```bash
pip install PyPDF2
```

## ▶️ Como Usar

1. Altere as variáveis pasta_pdfs, frase_procurada e arquivo_resultado no final do script com os valores desejados:

```bash
pasta_pdfs = "C:/CAMINHO/DA/SUA/PASTA"
frase_procurada = "FRASE A SER PESQUISADA"
arquivo_resultado = "nome_do_arquivo_log.log"
```

2. Execute o script:

```bash
python nome_do_arquivo.py
```

3. O script irá gerar um arquivo .log com os resultados da pesquisa no local especificado.

## 📂 Estrutura de Log

O arquivo de log conterá entradas como:

```bash
Arquivo: exemplo.pdf, Páginas: 5
Erro ao processar corrompido.pdf: Could not read malformed PDF file
```

## 🛠️ Função

```bash
pesquisar_pdfs(pasta, frase_busca, arquivo_log)
```

**Parâmetros:**

* pasta: Caminho da pasta que contém os PDFs.

* frase_busca: Frase que será procurada em cada PDF.

* arquivo_log: Caminho do arquivo de saída com os resultados.

## 👩‍💻 Sobre a Autora

<img src="https://avatars.githubusercontent.com/u/180755020?v=4" height="100"/>

Desenvolvido por **Raylaine Barreto** 

- [LinkedIn](https://www.linkedin.com/in/raylaine-barreto)

