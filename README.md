# 🤖 Web Scraping MatrizCast

Este projeto foi desenvolvido em Python para criar um processo automático de coleta de perfis no LinkedIn a partir de um tema definido pelo usuário. O objetivo deste programa é automatizar a seleção de convidados para partipar do [MatrizCast](https://www.youtube.com/c/MatrizCast), o podcast de educação da [Escola Matriz](https://trakto.link/escolamatriz)

## 🧐 O que é o Web Scraping?

Web Scraping é um método automatizado para coleta de dados na web. Os dados na web estão armazenados de forma não estruturada e, este processo, também tem como objetivo armazená-los de forma estruturada, para que seja possível aplicar técnicas como, por exemplo, de Ciência de Dados.

## 🔍 Porque buscar perfis do Linkedin?

O MatrizCast, é um podcast de educação que já entrevistou mais de 80 profissionais com o objetivo de orientar os jovens sobre o futuro do mercado de trabalho. O processo de busca por estes possíveis entrevistados é feito pela rede social LinkedIn. Todo este processo é feito manualmente, primeiro é definido um tema, depois é feita a pesquisa no LinkedIn e o convite é enviado para todos os selecionados.

Partindo deste ponto o objetivo foi aplicar o conhecimento aprendido sobre Web Scraping para automatizar essa busca, já que o programa pergunta qual o tema (ou temas) de interesse e retorna um arquivo .csv com as informações de nome, headline e url de cada perfil no LinkedIn.
 
 ## ▶️ Para rodar o projeto
 
 O arquivo .py está disponível neste repositório e você pode rodar o programa a partir de uma IDE, como o PyCharm, ou pelo terminal através do comando `python matrizcast_scraping.py`
 
 É necessário também que você tenha instalado as bibliotecas selenium e parsel, que podem ser instaladas pelos comandos `pip install selenium` e `pip install parse`.
 
 
