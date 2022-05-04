--Exerc�cios

USE TSQL2012;

--1. Construa duas consultas que retornem o N�mero do Produto (productid),
--Nome (productname) e Pre�o (unitprice) onde os pre�os estejam entre 19 e 22.
--Construir a 1�. consulta, utilizando o operador AND.
--Na 2�. Consulta, que dever� retornar exatamente as mesmas colunas e linhas,
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

--2. Construa duas consultas que retornem o N�mero do Produto (productid),
--Nome (productname) e Pre�o (unitprice) onde os pre�os sejam quaisquer um a seguir:
--18 ou 10 ou 21,35. A 1�. consulta, utilizar o operador OR.
--Na 2�. Consulta, que dever� retornar exatamente as mesmas colunas e linhas,
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

--3. Retorne o N�mero do Empregado (empid), T�tulo (titleofcourtesy), a Data de Nascimento (birthdate)
--e concatenar as colunas nome (firstname) e sobrenome (lastname) 
--em apenas uma coluna apelidada de Nome Completo, 
--apenas para os empregados que nasceram em qualquer dia e m�s desde 1947 at� 1965. 
--(tabela HR.Employees)

SELECT	empid as 'Numero Empregado',
		titleofcourtesy as 'Titulo',
		birthdate as 'Data Nascimento',
		firstname + lastname as 'Nome Completo'
FROM HR.Employees
WHERE birthdate BETWEEN '1947/01/01' AND '1965/31/12'

--4. Retorne a Cidade (city), Regi�o (region) e Pa�s (country)
--dos empregados da cidade de Seattle ou do pa�s UK.

SELECT	city as 'Cidade',
		region as 'Regi�o',
		country as 'Pa�s'
FROM HR.Employees
WHERE city = 'Seattle' or country = 'UK'

--5. Retorne o N�mero do Empregado (empid), Nome (firstname) e Data de Contrata��o (hiredate)
--dos empregados contratados em qualquer dia e m�s de 2002 ou de 2004.

SELECT	empid as 'Numero Empregado',
		firstname as 'Nome',
		hiredate as 'Data Contrata��o'
FROM HR.Employees
WHERE (hiredate BETWEEN '2002/01/01' AND '2002/31/12') 
	OR (hiredate BETWEEN '2004/01/01' AND '2004/31/12')

--6. Retorne todas as colunas dos �ltimos 20 registros de Clientes (tabela Sales.Customers),
--ou seja, do maior N�mero do Cliente (custid) para o menor.

SELECT TOP(20) *
FROM Sales.Customers
ORDER BY custid DESC

--7. Primeiramente fa�a uma query para visualizar os pa�ses distintos existentes na tabela anterior.
--Agora construa uma consulta que retorne o N�mero do Cliente (custid),
--o Nome do Contato (contactname), Cidade (city) e Pa�s (country),
--apenas para os clientes da Am�rica do Sul,
--lembrando que apenas pelo campo Pa�s conseguiremos essa filtragem. Ordene pelo Pa�s.

SELECT	custid as 'Numero Cliente',
		contactname as 'Nome do Contato',
		city as 'Cidade',
		country as 'Pa�s'
FROM Sales.Customers
WHERE country IN ('Argentina', 'Brazil', 'Venezuela')
ORDER BY country

--8. Retorne o N�mero do Cliente (custid), o Nome do Contato (contactname)
--e o Fax onde esta �ltima coluna N�O seja NULL.
--Ordene do maior N�mero do Cliente ao menor.

SELECT	custid as 'Numero Cliente',
		contactname as 'Nome Contato',
		fax
FROM Sales.Customers
WHERE fax IS NOT NULL
ORDER BY custid DESC

--9. Retorne o N�mero do Cliente (custid), Cidade (city) e o Pa�s (country) onde a Regi�o (region) seja NULL.
--Ordene de forma ascendente para o Pa�s e descendente para a Cidade.

SELECT	custid as 'Numero Cliente',
		city as 'Cidade',
		country as 'Pais'
FROM Sales.Customers
WHERE region IS NULL
ORDER BY country ASC, city DESC