CREATE DATABASE DB_SGE;

CREATE TABLE ALMACEN1(
	codigo VARCHAR(10) PRIMARY KEY,
	cantidad numeric,
	descripcion VARCHAR(20)
);


CREATE TABLE ALMACEN2(
	codigo VARCHAR(10) PRIMARY KEY,
	cantidad numeric,
	descripcion VARCHAR(20)
);


CREATE TABLE DESPIECE(
    C2 VARCHAR(10),
	C1 VARCHAR(10),
	cantidad numeric,
	FOREIGN KEY (C1) REFERENCES almacen1(codigo),
	FOREIGN KEY (C2) REFERENCES almacen2(codigo),
    PRIMARY KEY(C2,C1)
);



CREATE TABLE MOVIMIENTOS(
	cod_movimiento REAL PRIMARY KEY AUTO_INCREMENT,
	fecha DATE,
	c1 VARCHAR(10),
	c2 VARCHAR(10),
	FOREIGN KEY (c1) REFERENCES ALMACEN1(codigo),
	FOREIGN KEY (c2) REFERENCES ALMACEN2(codigo)
);


INSERT INTO almacen1 VALUES('A0001',10, 'Cuadro de fibra de vidrio');
INSERT INTO almacen1 VALUES('A0002',15, 'Manillar');
INSERT INTO almacen1 VALUES('A0003',22, 'Ruedas de montaña');
INSERT INTO almacen1 VALUES('A0004',8, 'Ruedas de carretera');
INSERT INTO almacen1 VALUES('A0005',5, 'frenos de disco baratos');
INSERT INTO almacen1 VALUES('A0006',10, 'frenos de disco caros');
INSERT INTO almacen1 VALUES('A0007',6, 'frenos de zapata');
INSERT INTO almacen1 VALUES('A0008',3, 'Camara de goma');
INSERT INTO almacen1 VALUES('A0009',12, 'Cuadro de aluminio');
INSERT INTO almacen1 VALUES('A0010',19, 'Manillar ergonómico');
INSERT INTO almacen1 VALUES('A0011',3, 'Cuentakilometros');
INSERT INTO almacen1 VALUES('A0012',7, 'Estuche reparacion de ruedas');
INSERT INTO almacen1 VALUES('A0013',5, 'Guardabarros trasero');
INSERT INTO almacen1 VALUES('A0014',6, 'Sillín con amortiguacion');
INSERT INTO almacen1 VALUES('A0015',8, 'Sillin basico');
INSERT INTO almacen1 VALUES('A0016',2, 'Cuadro de BMX con manillar');
INSERT INTO almacen1 VALUES('A0017',6, 'Ruedas pequeñas');

INSERT INTO almacen2 VALUES('B0001',0, 'Bicicleta TodoTerreno');
INSERT INTO almacen2 VALUES('B0002',0, 'Bicicleta de carretera');
INSERT INTO almacen2 VALUES('B0003',0, 'BMX');
INSERT INTO almacen2 VALUES('B0004',0, 'Bicicleta Urbana');
INSERT INTO almacen2 VALUES('B0005',0, 'Mountain Bike');

INSERT INTO despiece VALUES('B0001','A0001',1);
INSERT INTO despiece VALUES('B0001', 'A0002',1);
INSERT INTO despiece VALUES('B0001', 'A0003',2);
INSERT INTO despiece VALUES('B0001', 'A0006',2);
INSERT INTO despiece VALUES('B0001', 'A0013',1);
INSERT INTO despiece VALUES('B0001', 'A0014',1);

INSERT INTO despiece VALUES('B0003', 'A0015',1);
INSERT INTO despiece VALUES('B0003', 'A0016',1);
INSERT INTO despiece VALUES('B0003', 'A0017',2);