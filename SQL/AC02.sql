--Exercícios

USE TSQL2012;

--1. Construa duas consultas que retornem o Número do Produto (productid),
--Nome (productname) e Preço (unitprice) onde os preços estejam entre 19 e 22.
--Construir a 1ª. consulta, utilizando o operador AND.
--Na 2ª. Consulta, que deverá retornar exatamente as mesmas colunas e linhas,
--utilizar o predicado BETWEEN. (tabela Production.Products)

SELECT	productid as 'Numero Produto',
		productname as 'Nome Produto',
		unitprice as 'Preco' 
FROM Production.Products
WHERE unitprice >= 19 AND unitprice <= 22;

SELECT	productid as 'Numero Produto',
		productname as 'Nome Produto',
		unitprice as 'Preco' 
FROM Production.Products
WHERE unitprice BETWEEN 19 AND 22;

--2. Construa duas consultas que retornem o Número do Produto (productid),
--Nome (productname) e Preço (unitprice) onde os preços sejam quaisquer um a seguir:
--18 ou 10 ou 21,35. A 1ª. consulta, utilizar o operador OR.
--Na 2ª. Consulta, que deverá retornar exatamente as mesmas colunas e linhas,
--utilizar o predicado IN.

SELECT	productid as 'Numero Produto',
		productname as 'Nome Produto',
		unitprice as 'Preco' 
FROM Production.Products
WHERE unitprice = 18 OR unitprice = 10 OR unitprice = 21.35;

SELECT	productid as 'Numero Produto',
		productname as 'Nome Produto',
		unitprice as 'Preco' 
FROM Production.Products
WHERE unitprice IN (18, 10, 21.35);

--3. Retorne o Número do Empregado (empid), Título (titleofcourtesy), a Data de Nascimento (birthdate)
--e concatenar as colunas nome (firstname) e sobrenome (lastname) 
--em apenas uma coluna apelidada de Nome Completo, 
--apenas para os empregados que nasceram em qualquer dia e mês desde 1947 até 1965. 
--(tabela HR.Employees)

SELECT	empid as 'Numero Empregado',
		titleofcourtesy as 'Titulo',
		birthdate as 'Data Nascimento',
		firstname + lastname as 'Nome Completo'
FROM HR.Employees
WHERE birthdate BETWEEN '1947/01/01' AND '1965/31/12'

--4. Retorne a Cidade (city), Região (region) e País (country)
--dos empregados da cidade de Seattle ou do país UK.

SELECT	city as 'Cidade',
		region as 'Região',
		country as 'País'
FROM HR.Employees
WHERE city = 'Seattle' or country = 'UK'

--5. Retorne o Número do Empregado (empid), Nome (firstname) e Data de Contratação (hiredate)
--dos empregados contratados em qualquer dia e mês de 2002 ou de 2004.

SELECT	empid as 'Numero Empregado',
		firstname as 'Nome',
		hiredate as 'Data Contratação'
FROM HR.Employees
WHERE (hiredate BETWEEN '2002/01/01' AND '2002/31/12') 
	OR (hiredate BETWEEN '2004/01/01' AND '2004/31/12')

--6. Retorne todas as colunas dos últimos 20 registros de Clientes (tabela Sales.Customers),
--ou seja, do maior Número do Cliente (custid) para o menor.

SELECT TOP(20) *
FROM Sales.Customers
ORDER BY custid DESC

--7. Primeiramente faça uma query para visualizar os países distintos existentes na tabela anterior.
--Agora construa uma consulta que retorne o Número do Cliente (custid),
--o Nome do Contato (contactname), Cidade (city) e País (country),
--apenas para os clientes da América do Sul,
--lembrando que apenas pelo campo País conseguiremos essa filtragem. Ordene pelo País.

SELECT	custid as 'Numero Cliente',
		contactname as 'Nome do Contato',
		city as 'Cidade',
		country as 'País'
FROM Sales.Customers
WHERE country IN ('Argentina', 'Brazil', 'Venezuela')
ORDER BY country

--8. Retorne o Número do Cliente (custid), o Nome do Contato (contactname)
--e o Fax onde esta última coluna NÃO seja NULL.
--Ordene do maior Número do Cliente ao menor.

SELECT	custid as 'Numero Cliente',
		contactname as 'Nome Contato',
		fax
FROM Sales.Customers
WHERE fax IS NOT NULL
ORDER BY custid DESC

--9. Retorne o Número do Cliente (custid), Cidade (city) e o País (country) onde a Região (region) seja NULL.
--Ordene de forma ascendente para o País e descendente para a Cidade.

SELECT	custid as 'Numero Cliente',
		city as 'Cidade',
		country as 'Pais'
FROM Sales.Customers
WHERE region IS NULL
ORDER BY country ASC, city DESC