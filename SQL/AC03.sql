--AC03.

--Parte 1: Banco de Dados Concession�ria
-- 1. Recriar toda a estrutura de tabelas 
-- (abrir o script Carga Consessionaria, 
-- DROP nos objetos que j� haviam criado e executar o script 
-- para que crie novamente as tabelas com dados originais).

use master
go

if exists (select * from sys.databases where name = 'Concessionaria')
drop database Concessionaria
go

create database Concessionaria
go

use Concessionaria
go


CREATE TABLE Ano
( 
idAno tinyint identity(1,1)
, descricao smallint not null 
, constraint pkAno primary key (idAno)
)
go


CREATE TABLE Fabricante
( 
idFabricante       tinyint identity(1,1)
, Nome               varchar(50) not null 
, endereco           varchar(100) null 
, cidade             varchar(50) not null 
, UF                 char(2) null 
, telefone           varchar(20) null 
, contato            varchar(50) not null
, constraint pkFabricante primary key (idFabricante)
)
go

CREATE TABLE Mes
( 
idMes              tinyint identity (15, 3) 
, descricao        tinyint  not null 
, constraint pkMes primary key (idMes)
)
go

CREATE TABLE Modelo
( 
idModelo           smallint identity(1,1)
, descricao          varchar(50) not null 
, constraint pkModelo primary key (idModelo)
)
go

CREATE TABLE Veiculo
( 
idVeiculo          smallint identity(1,1)
, descricao          varchar(50) not null
, valor              decimal(9,2)not null
, dataCompra date not null
, idModelo           smallint null 
, idFabricante       tinyint  null 
, idAnoFabricacao    tinyint  null 
, constraint pkVeiculo primary key (idVeiculo)
, constraint fkVeiculo_idModelo foreign key (idModelo) references Modelo(idModelo)
, constraint fkVeiculo_idFabricante foreign key (idFabricante) references Fabricante(idFabricante)
, constraint fkVeiculo_idAnoFabricacao foreign key (idAnoFabricacao) references Ano(idAno)
)
go

CREATE TABLE VendasAnuais
( 
idVendas           int identity (1,1)
, qtd                smallint not null 
, idVeiculo          smallint  null 
, idAnodaVenda       tinyint  null 
, idMesdaVenda       tinyint  null 
, constraint pkVendasAnuais primary key (idVendas)
, constraint fkVendasAnuais_idVeiculo foreign key (idVeiculo) references Veiculo(idVeiculo)
, constraint fkVendasAnuais_idAnodaVenda foreign key (idAnodaVenda) references Ano(idAno)
, constraint fkVendasAnuais_idMesdaVenda foreign key (idMesdaVenda) references Mes(idMes)
)
go

/*
-- Selects
select * from Fabricante
select * from Modelo
select * from Ano
select * from Mes
select * from VendasAnuais
select * from Veiculo
select * from Ano

use master
go

Use Concessionaria
go

*/


-- Fabricante
insert Fabricante (nome, endereco, cidade, uf, telefone, contato) values
  ('Honda', 'Rua da Consolacao, 125', 'Sao Paulo', 'SP', '26454128', 'Ismael Santos')
, ('Yamaha', 'Rua Ipiranga, 820', 'Sao Paulo', 'SP', '24456200', 'Ana Cristina')
, ('Suzuki', 'Av. Rio Branco, 1250', 'Rio de Janeiro', 'RJ', '37785511', 'Marcelo Faria')
, ('Dafra', 'Av. Rodolfo Paiva, 340', 'Rio de Janeiro', 'RJ', '43326667', 'Antonio Brandao')
, ('Kawasaki', 'Rua Joaquim Floriano, 678', 'Sao Paulo', 'SP', '24527272', 'Monica Bahia')
, ('Ducati', 'Rua das Flores, 620', 'Curitiba', 'PR', '62331111', 'Paula Beltr�o')
, ('BMW', 'Rua Antonio Bandeiras, 890', 'Sao Paulo', 'SP', '27783535', 'Hans Miller')
, ('Harley-Davidson', 'Rua das Gaivotas, 81', 'Joinville', 'SC', '32662112', 'Adolfo Siqueira')
, ('Kasinski', 'Av. Brasil, 545', 'Recife', 'PE', '4112-8878', 'Silvia Telles')

-- Modelo
insert Modelo values ('GS'), ('R'), ('K'), ('GT'), ('GTR'), ('GTS'), ('STD'), ('L'), ('LS')

-- Ano
declare @anoFinal smallint = year(getdate())
declare @anoInicial smallint = (@anoFinal - 10)
while @anoFinal >= @anoInicial
begin
insert Ano values (@anoFinal)
set @AnoFinal -= 1
end



-- Mes
declare @mesFinal smallint = 12, @mesInicial smallint = 1
while @mesFinal >= @mesInicial
begin
insert mes values (@mesFinal)
set @mesFinal -= 1
end

----------------------------------------------------------------------------
-- Veiculo / Vendas Anuais
----------------------------------------------------------------------------
-- drop procedure InserirVeiculoVendas
go
create procedure InserirVeiculoVendas @valor int, @ano int, @veiculo varchar(20), @fabricante varchar(30), @modelo varchar(20), @qtdModelo tinyint
as
begin
   set nocount on
   
   declare @idAno tinyint, @idMes tinyint = (select min(idMes) from Mes)
   declare @qtd1 int, @qtd2 int, @qtd3 int, @idFabricante tinyint, @idModelo tinyint
   declare @randMes tinyint, @randDia tinyint, @dataCompra varchar(8), @anoData varchar(4)

-- Valores Iniciais
select   @idFabricante = (select idFabricante from Fabricante where nome = @fabricante)
, @idModelo = (select idModelo from Modelo where descricao = @modelo)
, @idAno = (select idAno from ano where descricao = @ano)
, @idMes = (select min(idMes) from Mes)

-- Percorrendo do ano fornecido at� o �ltimo Ano
   while @idAno <= (select max(idAno) from Ano)
   begin

-- Montando uma data v�lida
select @anoData = cast(descricao as varchar(4)) from ano where idAno = @idAno
select @randMes = cast((rand() * 50) as tinyint), @randDia = cast((rand() * 20) as tinyint)
select @dataCompra = (cast(@anoData as varchar(4))+ replicate('0', 2 - len(@randMes)) + cast(@randMes as varchar) + replicate('0', 2 - len(@randDia)) + cast(@randDia as varchar))

while isdate(@dataCompra) = 0
begin
select @randMes = cast((rand() * 50) as tinyint), @randDia = cast((rand() * 20) as tinyint)
select @dataCompra = (cast(@ano as varchar)+ replicate('0', 2 - len(@randMes)) + cast(@randMes as varchar) + replicate('0', 2 - len(@randDia)) + cast(@randDia as varchar))
end

      -- Inclus�o de Ve�culo
      insert Veiculo (descricao, valor, idModelo, idFabricante, idAnoFabricacao, dataCompra) values (@veiculo, @valor, @idModelo, @idFabricante, @idAno, @dataCompra) 

      if @qtdModelo >= 2
         insert Veiculo (descricao, valor, idModelo, idFabricante, idAnoFabricacao, dataCompra) values (@veiculo, cast(@valor * 1.0025 as int) , @idModelo + 1, @idFabricante, @idAno, @dataCompra) 

      if @qtdModelo = 3
         insert Veiculo (descricao, valor, idModelo, idFabricante, idAnoFabricacao, dataCompra) values (@veiculo, cast(@valor * 1.0045 as int) , @idModelo + 2, @idFabricante, @idAno, @dataCompra) 


  -- Inclus�o de Vendas Anuais
      while @idMes <= (select max(idMes) from Mes)
      begin
         select @qtd1 = cast(rand() * 1000 as int), @qtd2 = cast(rand() * 1000 as int), @qtd3 = cast(rand() * 1000 as int)

         -- VendasAnuais
         insert VendasAnuais values
         (@qtd1, (select idVeiculo from Veiculo where idFabricante = @idFabricante and idAnoFabricacao = @idAno and idModelo = @idModelo and descricao = @veiculo), @idAno, @idMes) 
               
         if @qtdModelo >= 2
            insert VendasAnuais values
            (@qtd2, (select idVeiculo from Veiculo where idFabricante = @idFabricante and idAnoFabricacao = @idAno and idModelo = @idModelo + 1 and descricao = @veiculo), @idAno, @idMes) 

         if @qtdModelo = 3
            insert VendasAnuais values  
            (@qtd3, (select idVeiculo from Veiculo where idFabricante = @idFabricante and idAnoFabricacao = @idAno and idModelo = @idModelo + 2 and descricao = @veiculo), @idAno, @idMes) 

         select @idMes = min(idMes) from Mes where idMes > @idMes
      end

      select @valor = @valor * 1.0065, @idAno += 1, @idMes = (select min(idMes) from Mes)
   end
end
go

-- Honda
declare @Ano01 smallint = (select min(descricao) from Ano)
declare @Ano02 smallint = (@Ano01 + 1), @Ano03 smallint = (@Ano01 + 2), @Ano04 smallint = (@Ano01 + 3), @Ano05 smallint = (@Ano01 + 4), @Ano06 smallint = (@Ano01 + 5)
declare @Ano07 smallint = (@Ano01 + 6), @Ano08 smallint = (@Ano01 + 7), @Ano09 smallint = (@Ano01 + 8), @Ano10 smallint = (@Ano01 + 9)

exec InserirVeiculoVendas 4700, @Ano01, 'CG 125', 'Honda', 'STD', 3
exec InserirVeiculoVendas 5350, @Ano03, 'CG 150', 'Honda', 'STD', 3
exec InserirVeiculoVendas 9300, @Ano07, 'CB 300', 'Honda', 'LS', 1

-- Yamaha
exec InserirVeiculoVendas 5200, @Ano02, 'XTZ 125', 'Yamaha', 'STD', 3
exec InserirVeiculoVendas 8200, @Ano04, 'XTZ 250', 'Yamaha', 'L', 2
exec InserirVeiculoVendas 21400, @Ano08, 'XT 660', 'Yamaha', 'STD', 1

-- Suzuki
exec InserirVeiculoVendas 27000, @Ano06, 'Bandit 650', 'Suzuki', 'GT', 3

-- Dafra
exec InserirVeiculoVendas 5250, @Ano01, 'Kansas 150', 'Dafra', 'LS', 1
exec InserirVeiculoVendas 3200, @Ano03, 'Zig 50', 'Dafra', 'STD', 1
exec InserirVeiculoVendas 10500, @Ano05, 'CityCom 300', 'Dafra', 'STD', 1

-- Kasinski
exec InserirVeiculoVendas 7500, @Ano02, 'Comet 250', 'Kasinski', 'GT', 2

-- BMW
exec InserirVeiculoVendas 37000, @Ano10, 'F800', 'BMW', 'GS', 2

-- Kawasaki
exec InserirVeiculoVendas 28000, @Ano10, 'Versys 650', 'Kawasaki', 'STD', 1

-- Harley-Davidson
exec InserirVeiculoVendas 45000, @Ano09, 'Fat Boy', 'Harley-Davidson', 'STD', 1

INSERT INTO Ano (descricao) VALUES (2022),(2023),(2024),(2025),(2026),(2027),(2028),(2029),(2030),(2031),(2032)

-- Selects
select * from Fabricante
select * from Modelo
select * from Ano
select * from Mes
select * from VendasAnuais
select * from Veiculo
------------------------------------
USE Concessionaria

-- 2. Adicionar os fabricantes a seguir com todos dados: FIAT, GM e VW.

SELECT * FROM Fabricante

INSERT INTO Fabricante (Nome, endereco, cidade, UF, telefone, contato) 
VALUES ('FIAT', 'Avenida Corifeu, 5541','S�o Paulo', 'SP', '37672600', 'Jos� Maria')
INSERT INTO Fabricante (Nome, endereco, cidade, UF, telefone, contato) 
VALUES ('GM', 'Av. Goi�s, 1805','S�o Caetano', 'SP', '42347700', 'Mark Reuss')
INSERT INTO Fabricante (Nome, endereco, cidade, UF, telefone, contato) 
VALUES ('VW', 'Avenida Comendador, 1889','S�o Paulo', 'SP', '54285745', 'Pablo Di Si')

-- 3. Adicionar os modelos: Standard, Premium, Executive.

SELECT * FROM Modelo
INSERT INTO Modelo (descricao) VALUES ('Standard'), ('Premium'), ('Executive')

--4. Adicionar os Ve�culos: 
-- Artic (Fiat - Standard - ano 2025,
-- Voltz (GM - Executive - ano 2027),
-- Zeo (Volks - Premium - ano 2028),
-- Bjorn (GM - Premium - ano 2028),
-- Duntzen (Fiat - Standard � ano 2026),
-- Tungsten (Volks - Executive - ano 2027).

SELECT * FROM Veiculo

INSERT INTO Veiculo (descricao, valor, dataCompra, idFabricante, idModelo, idAnoFabricacao)
VALUES ('Artic', 5000.00, '24/10/2021', 10, 10, 15),
		('Voltz', 6000.00, '24/10/2021', 11, 12, 17),
		('Zeo', 7000.00, '24/10/2021', 12, 11, 18),
		('Bjorn', 8000.00, '24/10/2021', 11, 11, 18),
		('Duntzen', 9000.00, '24/10/2021', 10, 10, 16),
		('Tungsten', 4000.00, '24/10/2021', 12, 12, 17)

-- 5. Adicionar tr�s Vendas para cada ve�culo para o ano de 2029 em meses distintos.

SELECT * FROM VendasAnuais

INSERT INTO VendasAnuais (qtd, idVeiculo, idAnodaVenda, idMesdaVenda)
VALUES (412, 112, 19, 15),
		(645, 112, 19, 18),
		(456, 112, 19, 21),
		(564, 113, 19, 24),
		(634, 113, 19, 27),
		(345, 113, 19, 30),
		(757, 114, 19, 33),
		(457, 114, 19, 36),
		(544, 114, 19, 39),
		(656, 115, 19, 42),
		(864, 115, 19, 45),
		(356, 115, 19, 48),
		(354, 116, 19, 27),
		(364, 116, 19, 30),
		(634, 116, 19, 39),
		(856, 117, 19, 15),
		(253, 117, 19, 21),
		(544, 117, 19, 24)

-- 6. Alterar a fabrica��o dos ve�culos Zeo e Bjorn para o ano de 2026. Os demais ve�culos alterar para 2030.

SELECT * FROM Veiculo
SELECT * FROM Ano

BEGIN TRAN
UPDATE Veiculo SET idAnoFabricacao = 16
WHERE descricao IN ('Zeo', 'Bjorn')
COMMIT TRAN

BEGIN TRAN
UPDATE Veiculo SET idAnoFabricacao = 20
WHERE descricao NOT IN ('Zeo', 'Bjorn')
COMMIT TRAN

--7. Alterar as Vendas dos Ve�culos Premium para janeiro de 2030,
--	Standard para Dezembro de 2031 e Executive para outubro de 2032.

SELECT * FROM Veiculo
SELECT * FROM ANO
SELECT * FROM Mes

SELECT * FROM VendasAnuais VA
JOIN Veiculo V ON V.idVeiculo = VA.idVeiculo
WHERE V.idModelo IN (SELECT idModelo FROM Modelo WHERE descricao LIKE 'Premium')

BEGIN TRAN
UPDATE VendasAnuais SET idAnodaVenda = 20, idMesdaVenda = 48
OUTPUT	deleted.idAnodaVenda,
		inserted.idAnodaVenda,
		deleted.idMesdaVenda,
		inserted.idMesdaVenda
FROM VendasAnuais VA
JOIN Veiculo V ON V.idVeiculo = VA.idVeiculo
WHERE V.idModelo IN (SELECT idModelo FROM Modelo WHERE descricao LIKE 'Premium')
--ROLLBACK TRAN
COMMIT TRAN
-----------
SELECT * FROM VendasAnuais VA
JOIN Veiculo V ON V.idVeiculo = VA.idVeiculo
WHERE V.idModelo IN (SELECT idModelo FROM Modelo WHERE descricao LIKE 'Standard')

BEGIN TRAN
UPDATE VendasAnuais SET idAnodaVenda = 21, idMesdaVenda = 15
OUTPUT	deleted.idAnodaVenda,
		inserted.idAnodaVenda,
		deleted.idMesdaVenda,
		inserted.idMesdaVenda
WHERE idVeiculo IN (SELECT idVeiculo FROM Veiculo 
					WHERE idModelo = (SELECT idModelo FROM Modelo
									WHERE descricao = 'Standard')
					)
--ROLLBACK TRAN
COMMIT TRAN
------------------
SELECT * FROM VendasAnuais VA
JOIN Veiculo V ON V.idVeiculo = VA.idVeiculo
WHERE V.idModelo IN (SELECT idModelo FROM Modelo WHERE descricao LIKE 'Executive')

BEGIN TRAN
UPDATE VendasAnuais SET idAnodaVenda = 22, idMesdaVenda = 21
OUTPUT	deleted.idAnodaVenda,
		inserted.idAnodaVenda,
		deleted.idMesdaVenda,
		inserted.idMesdaVenda
WHERE idVeiculo IN (SELECT idVeiculo FROM Veiculo 
					WHERE idModelo = (SELECT idModelo FROM Modelo
									WHERE descricao = 'Executive')
					)
--ROLLBACK TRAN
COMMIT TRAN

--Parte 2: Banco de Dados PEDIDOS
USE PEDIDOS
--	8. Deletar todos os REGISTROS da Tabela Itens de Pedido que sejam associados a produtos com a palavra
--		CANETA em qualquer parte do campo Observa��o (Utilizar Subquery).

SELECT * FROM TB_ITENSPEDIDO
SELECT * FROM TB_PRODUTO

BEGIN TRAN
DELETE FROM TB_ITENSPEDIDO
WHERE ID_PRODUTO IN (SELECT ID_PRODUTO FROM TB_PRODUTO
					WHERE DESCRICAO LIKE ('%CANETA%')
					)
--ROLLBACK TRAN
COMMIT TRAN

--9. Apagar todos os EMPREGADOS que possuam de 1 a 3 DEPENDENTES. Lembre-se de tratar a quest�o da
--   Foreign Key.
SELECT * FROM TB_EMPREGADO
SELECT * FROM TB_DEPENDENTE

BEGIN TRAN
DELETE FROM TB_DEPENDENTE
OUTPUT deleted.CODFUN,
		deleted.NOME
WHERE CODFUN IN (SELECT CODFUN FROM TB_EMPREGADO 
				WHERE NUM_DEPEND BETWEEN 1 AND 3)
--ROLLBACK TRAN
COMMIT TRAN
GO

BEGIN TRAN
DELETE FROM TB_EMPREGADO
WHERE NUM_DEPEND BETWEEN 1 AND 3
COMMIT TRAN
GO

--10. Atualizar os sal�rios dos EMPREGADOS que possuam C�digos de Supervidores �MPARES, aumentando em
--  12%. E retirar 08% do Bonus Mensal dos empregados que possuam COD_CARGO e COD_DEPTO PARES.
SELECT * FROM TB_EMPREGADO
WHERE (COD_SUPERVISOR % 2) != 0

BEGIN TRAN
UPDATE TB_EMPREGADO SET SALARIO *= 1.12
OUTPUT	deleted.SALARIO,
		inserted.SALARIO
WHERE (COD_SUPERVISOR % 2) != 0
--ROLLBACK TRAN
COMMIT TRAN
--------------
SELECT * FROM TB_EMPREGADO
WHERE (COD_CARGO % 2) = 0 AND (COD_DEPTO % 2) = 0

BEGIN TRAN
UPDATE TB_EMPREGADO SET PREMIO_MENSAL *= 0.92
OUTPUT deleted.PREMIO_MENSAL,
		inserted.PREMIO_MENSAL
WHERE (COD_CARGO % 2) = 0 AND (COD_DEPTO % 2) = 0
--ROLLBACK TRAN
COMMIT TRAN
