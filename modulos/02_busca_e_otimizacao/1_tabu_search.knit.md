---
title: "Tabu Search"
---



Neste post, irei aplicar o m�todo de busca Tabu Search na busca da solu��o �tima de um problema do caixeiro viajante.

# Problema do caixeiro viajante

O problema do caixeiro-viajante consiste na procura de um circuito que possua a menor dist�ncia, come�ando numa cidade qualquer, entre v�rias, visitando cada cidade precisamente uma vez e regressando � cidade inicial. [[1]](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante)

Para este exemplo, nosso caixeiro viajante dever� passar por todas as cidades da regi�o do Tri�ngulo Mineiro, representada no mapa abaixo.

![Figura 1: Mapa da regi�o do Tri�ngulo Mineiro e Alto Parana�ba [[2]](https://www-geografia.blogspot.com/2020/04/triangulo-mineiro-minas-gerais.html)](mapa_triangulo_mineiro.PNG) 

A regi�o do Tri�ngulo � formada por 35 munic�pios, listados abaixo [[3]](https://www.mg.gov.br/conteudo/conheca-minas/geografia/regioes-de-planejamento):

* �gua Comprida
* Araguari
* Arapor�
* Cachoeira Dourada
* Campina Verde
* Campo Florido
* Can�polis
* Capin�polis
* Carneirinho
* Cascalho Rico
* Centralina
* Comendador Gomes
* Concei��o das Alagoas
* Conquista
* Delta
* Fronteira
* Frutal
* Gurinhat�
* Indian�polis
* Ipia�u
* Itapajipe
* Ituiutaba
* Iturama
* Limeira do Oeste
* Monte Alegre de Minas
* Pirajuba
* Planura
* Prata
* Santa Vit�ria
* S�o Francisco de Sales
* Tupaciguara
* Uberaba
* Uberl�ndia
* Uni�o de Minas
* Ver�ssimo

# Buscando as dist�ncias entre as cidades do Tri�ngulo Mineiro

Agora precisamos saber as dist�ncias entre essas cidades. Para isso, vamos fazer as consltas no site http://www.distanciasentrecidades.com/ e buscar as informa��es usando o Selenium.



