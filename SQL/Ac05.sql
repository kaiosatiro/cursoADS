/*
2100194 ..... Carolina Aparecida
2100264 ..... Victor Ezemplari
2101700 ..... Ricardo Tadeu
2020021 ..... Carlos Roberto
2020019 ..... Caio Satiro
*/


--Na base Concession�ria, utilize fun��es de agrega��o para solucionar as seguintes quest�es:
USE Concessionaria
--1. Qual o n�mero de registros existentes na tabela VendasAnuais ?

SELECT COUNT(idVendas) [QTD REGISTROS]
FROM VendasAnuais

--2. Qual o acumulado da quantidade de vendas Totais at� o momento ?

SELECT SUM(qtd) [VALOR ACUMULADO]
FROM VendasAnuais

--3. Quais as quantidades de vendas Totais at� o momento para: menor venda, m�dia de vendas e a maior venda?

SELECT MIN(qtd) [QTD MENOR VENDAS],
		AVG(qtd) [QTD MEDIA DE VENDAS],
		MAX(qtd) [QTD MAIOR VENDAS]
FROM VendasAnuais

--4. Extraia a soma das vendas anuais por ano em ordem descendente.

SELECT SUM(qtd) AS SOMA,
		idAnodaVenda AS ANO
FROM VendasAnuais
GROUP BY idAnodaVenda
ORDER BY idAnodaVenda DESC
--ORDER BY 1 DESC

--5. Traga a soma das vendas anuais para o ve�culo/modelo CG 125 STD
-- (as informa��es do ve�culo devem constar na query).

SELECT	SUM(qtd) AS SOMA,
		VA.idAnodaVenda,
		V.descricao,
		V.idAnoFabricacao,
		V.idFabricante,
		V.idModelo,
		V.idVeiculo,
		V.valor,
		V.dataCompra
FROM VendasAnuais VA
JOIN Veiculo V ON V.idVeiculo = VA.idVeiculo
WHERE V.descricao LIKE '%CG 125%' AND V.idModelo = (SELECT idModelo FROM Modelo WHERE descricao LIKE '%STD%')
GROUP BY VA.idAnodaVenda, V.descricao, V.idFabricante, V.idAnoFabricacao, V.idModelo, V.idVeiculo, V.valor, V.dataCompra

--6. Traga as primeiras datas (ANOS) de FABRICA��O de todos os ve�culos e modelos,
--ordenados pelo nome do fabricante (ascendente), ano (descendente),
--Ve�culo (ascendente) e Modelo (descendente) 
--Toda as informa��es solicitadas, inclusive ordena��o, devem constar na query.

SELECT		F.Nome [NOME FABRICANTE],
			A.descricao AS [ANO DE FABRICA�AO],
			V.descricao AS VEICULO,
			M.descricao AS MODELO			
FROM Veiculo V
JOIN Ano A ON A.idAno = V.idAnoFabricacao
JOIN Fabricante F ON F.idFabricante = V.idFabricante
JOIN Modelo M ON M.idModelo = V.idModelo
GROUP BY A.descricao, V.descricao, M.descricao, F.Nome
ORDER BY F.Nome ASC, A.descricao DESC, V.descricao ASC, M.descricao DESC

--7. Extraia a menor, maior, m�dia e a soma das vendas de cada m�s do ano de 2011, a 2020, em ordem ascendente.

SELECT MIN(qtd) MENOR,
		AVG(qtd) MEDIA,
		MAX(qtd) MAIOR,
		M.descricao,
		A.descricao
FROM VendasAnuais V
JOIN Ano A ON A.idAno = V.idAnodaVenda
JOIN MES M ON M.idMes = V.idMesdaVenda
WHERE A.descricao BETWEEN '2011' AND '2020'
GROUP BY A.descricao, M.descricao
ORDER BY A.descricao ASC, M.descricao ASC

--8. Retorne a mesma consulta anterior, mas somente os registros que tiverem m�dia de vendas superior a 500.

SELECT MIN(qtd) MENOR,
		AVG(qtd) MEDIA,
		MAX(qtd) MAIOR,
		M.descricao,
		A.descricao
FROM VendasAnuais V
JOIN Ano A ON A.idAno = V.idAnodaVenda
JOIN MES M ON M.idMes = V.idMesdaVenda
WHERE A.descricao BETWEEN '2011' AND '2020'
GROUP BY A.descricao, M.descricao
HAVING AVG(qtd) > 500
ORDER BY A.descricao ASC, M.descricao ASC
