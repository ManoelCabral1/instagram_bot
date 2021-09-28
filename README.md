# BOT python para scraping de comentários de post do Instagram

O Bot consiste em uma classe python que usando a biblioteca selenium e o driver do navegador; entra no Instagram web, faz login, redireciona para o post desejado apartir do link e coleta uma amostra dos comentários do post. O tamanho da amostra depende do argumento count que informa quantas vezes o bot deve clickar no botão mais comentários.

O os dados são carregados num dataframe pandas e salvos em arquivo csv.

## Dependências

1. Selenium
2. driver do navegador (Chrome ou Firefox)
3. Pandas
4. sys
5. pathlib
6. time
