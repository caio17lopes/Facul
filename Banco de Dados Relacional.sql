use aula4;

    
create table cidade (
    id int auto_increment ,
    nome varchar(100) not null,
    uf char(2),
    constraint pkCidade primary key(id)
);

create table cliente (
    id int auto_increment,
    nome varchar(100),
    cidadeId int not null,
    constraint pkCliente primary key (id),
    constraint fkClienteCidade foreign key (cidadeId) references cidade(id)
);
-- sintaxe completa 
insert into cidade (id,nome,uf) values (1,'Bage', 'RS');

-- insert reeduzido lembrando que temn que seguir a ordem das colunas 
insert into cidade values (2, 'Parnaiba', 'PI');

-- insert de algumas colunas 
insert into cidade ( id,nome) values(3,'Imperatriz');

select * from cidade; 

insert into cliente (nome,cidadeid) values('Pedro',1);
insert into cliente (nome,cidadeid) values('Maria',10); -- da erro porque não existe cidade 10 na tabela 

insert into cliente (nome,cidadeid) values ('Nicolas',2), ('Helena',3), ('Beatriz',1);

select * from cliente;

create table funcionario (
    id int auto_increment,
    nome varchar(100),
    cidadeId int not null,
    constraint pkFuncionario primary key (id),
    constraint fkFuncionarioCidade foreign key (cidadeId) references cidade(id)
);

-- Exclusão e inclusão de registros
/* Delete 
	Comando responsavel pela remoção de linahs de uma tabela 
    
Uptade 
	Responsavel por manter a base de dados atualizada, realizando alterações no conteudo ( existente) 
    */
Insert into cidade values  (4,'Curitiba','PR');
Insert into cidade values  (5,'Videira','SC');
Insert into cidade values  (6,'Belo Horizonte','MG');
Insert into cidade values  (7,'São Paulo','SP');
insert into cidade values (3,'Imperatriz','MA');

-- Fazendo Update 
update cidade 
set uf = 'MA'
where id = 3;

-- Fazendo delete 
delete from cidade where id = 3;


-- FAzendo consultas 
select * from cliente
where cidadeid =1;  -- busca todos os lciente que moram na cidade 1

select * from cliente
where cidadeid =1
and salrio > 8000; -- busca clientes na cidade 1 e que tem salario maior que 8000,00

-- Verificação de varias areas
select * from cliente
where cidadeid =1
or cidadeid =2
or cidadeid = 5; -- busca em todas as cidades citadas 


-- Vazendo a vericação por coluna e não por toda a coluna 

select nome, salario from cliente 
where cidadeid = 1
or cidadeid = 3
or cidadeid = 5; -- esse é o metodo de coonsulta padrão 

-- Metodo de busca sem o operador or 
select nome, salario from cliente 
where cidadeid in (1,3,5);

-- Metodo para achar media 
select nome,salario 
from cliente 
where salario >= 5000
and salario <= 10000; -- operadores igual a python 

-- Outro operador para susbstituir o operador and 
select nome,salario 
from cliente 
where salario between 5000 and 10000;

-- Operador para ordenar resultado 

select nome,salario 
from cliente
order by nome asc -- de A a Z 
order by nome desc; -- de Z a A 

select nome,salario 
from cliente 
where salario  between 5000 and 10000
order by salario; -- ele sempre deve ser o utlimo comando e 

-- Posso colocar o order by para executar por coluna como abaixo que vai dar oa mesmo resultado de cima 
select nome,salario 
from cliente 
where salario  between 5000 and 10000
order by 2;


-- AULA 4 JUNÇÃO DE TABELA 
-- SQL Join 

-- Inner Join vai trazer o resultado que for igual as duas tabelas 
-- Self Join faz junçãoi da propria tablea 
-- Cross Join faz cruzam,ento de duas tabelas 
-- Outer Join possui 3 variantes 
-- Left Join pega somente a tabela da esquerda 
-- Right join pega a tabela da direita 
-- Full join pega toda a tabela 

use aula4;
select * from cidade; 
select * from cliente;

-- Inner Join 
select nome 
from cliente 
inner join cidade 
on ClienteCidade = cidade.id;

-- Cross join 
select nomecidade, gerente.nomeEstado
from cidade, estado
order by nomeCidade;

-- Self Join 
select funcionario.nomeFunc, nomeFun
from funcionario 
inner join funcionario gerente -- se quiser todos os funhionario por left join 
on funcionario.gerente = gerent.id; 

-- Full join 



-- Comandos e boas praticas 
/* Outros Comando e boas praticas 
	comandos Alias, limit, distinct, case, union e union all
Boas praticas 
	Não use * (asterisco) no comando select
    Use filtros (where) no delete e no update
    Evite criar insert com varias linhas 
    */
    
-- Exemplo do alias 
select nomefunc as 'Nome do funcionario' from funcionario -- muda o nomeFucn para o apelidado Nome do funcionario, apenas para efeitos de visualização 
where f.cidadeid= 1; -- traz somente da cidade com o apelido 

select * from cidade limit 3; -- limita apenas 3 linhas 

select nomeFucn from funcionario 
union -- ou union all 
select nomeCidade from cidade; -- traz um resultado so em uma lista 

select nomeFunc 'Nome do funcionario',
case 
	when sexoFunc = 'F' then 'Feminino' 
    when sexoFunc = 'M' then 'Masculino' 
end as ' Genero'
from funcionario; -- usando um sistema booleano para como case 
