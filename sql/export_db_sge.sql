-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 04-03-2019 a las 14:49:50
-- Versión del servidor: 10.1.36-MariaDB
-- Versión de PHP: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_sge`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `almacen1`
--

CREATE TABLE `almacen1` (
  `codigo` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `cantidad` decimal(10,0) DEFAULT NULL,
  `descripcion` varchar(20) COLLATE latin1_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `almacen1`
--

INSERT INTO `almacen1` (`codigo`, `cantidad`, `descripcion`) VALUES
('A0001', '17', 'Cuadro de fibra de v'),
('A0002', '15', 'Manillar'),
('A0003', '22', 'Ruedas de montaña'),
('A0004', '8', 'Ruedas de carretera'),
('A0005', '5', 'frenos de disco bara'),
('A0006', '10', 'frenos de disco caro'),
('A0007', '6', 'frenos de zapata'),
('A0008', '3', 'Camara de goma'),
('A0009', '12', 'Cuadro de aluminio'),
('A0010', '19', 'Manillar ergonómico'),
('A0011', '3', 'Cuentakilometros'),
('A0012', '7', 'Estuche reparacion d'),
('A0013', '5', 'Guardabarros trasero'),
('A0014', '6', 'Sillín con amortigua'),
('A0015', '0', 'Sillin basico'),
('A0016', '0', 'Cuadro de BMX con ma'),
('A0017', '1', 'Ruedas pequeñas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `almacen2`
--

CREATE TABLE `almacen2` (
  `codigo` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `cantidad` decimal(10,0) DEFAULT NULL,
  `descripcion` varchar(20) COLLATE latin1_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `almacen2`
--

INSERT INTO `almacen2` (`codigo`, `cantidad`, `descripcion`) VALUES
('B0001', '0', 'Bicicleta TodoTerren'),
('B0002', '0', 'Bicicleta de carrete'),
('B0003', '1', 'BMX'),
('B0004', '0', 'Bicicleta Urbana'),
('B0005', '0', 'Mountain Bike');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `despiece`
--

CREATE TABLE `despiece` (
  `C2` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `C1` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `cantidad` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `despiece`
--

INSERT INTO `despiece` (`C2`, `C1`, `cantidad`) VALUES
('B0001', 'A0001', '1'),
('B0001', 'A0002', '1'),
('B0001', 'A0003', '2'),
('B0001', 'A0006', '2'),
('B0001', 'A0013', '1'),
('B0001', 'A0014', '1'),
('B0003', 'A0015', '1'),
('B0003', 'A0016', '1'),
('B0003', 'A0017', '2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimientos`
--

CREATE TABLE `movimientos` (
  `cod_movimiento` double NOT NULL,
  `fecha` date DEFAULT NULL,
  `c2` varchar(10) COLLATE latin1_spanish_ci DEFAULT NULL,
  `cantidad` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `movimientos`
--

INSERT INTO `movimientos` (`cod_movimiento`, `fecha`, `c2`, `cantidad`) VALUES
(1, '2019-03-04', 'B0003', '1');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `almacen1`
--
ALTER TABLE `almacen1`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `almacen2`
--
ALTER TABLE `almacen2`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `despiece`
--
ALTER TABLE `despiece`
  ADD PRIMARY KEY (`C2`,`C1`),
  ADD KEY `C1` (`C1`);

--
-- Indices de la tabla `movimientos`
--
ALTER TABLE `movimientos`
  ADD PRIMARY KEY (`cod_movimiento`),
  ADD KEY `c2` (`c2`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `movimientos`
--
ALTER TABLE `movimientos`
  MODIFY `cod_movimiento` double NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `despiece`
--
ALTER TABLE `despiece`
  ADD CONSTRAINT `despiece_ibfk_1` FOREIGN KEY (`C1`) REFERENCES `almacen1` (`codigo`),
  ADD CONSTRAINT `despiece_ibfk_2` FOREIGN KEY (`C2`) REFERENCES `almacen2` (`codigo`);

--
-- Filtros para la tabla `movimientos`
--
ALTER TABLE `movimientos`
  ADD CONSTRAINT `movimientos_ibfk_1` FOREIGN KEY (`c2`) REFERENCES `almacen2` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
