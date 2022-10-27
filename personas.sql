-- phpMyAdmin SQL Dump
-- version 5.0.4deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 27-10-2022 a las 01:54:45
-- Versión del servidor: 8.0.29
-- Versión de PHP: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `personas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `PERSONA`
--

CREATE TABLE `PERSONA` (
  `id` bigint NOT NULL,
  `identificacion` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(80) CHARACTER SET utf8mb3 COLLATE utf8_unicode_ci NOT NULL,
  `apellidos` varchar(80) CHARACTER SET utf8mb3 COLLATE utf8_unicode_ci NOT NULL,
  `edad` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `PERSONA`
--

INSERT INTO `PERSONA` (`id`, `identificacion`, `nombre`, `apellidos`, `edad`) VALUES
(1, '39574152', 'FIGUEROA', 'DIANA MARCELA ', 54),
(2, '28732461', 'GUZMAN LOZANO ', 'MARIA ELVIRA', 12),
(3, '1070588787', 'GUERRA DIAZ', 'JENNI FERNANDA ', 26),
(4, '11307973', 'TORRES', 'JOSE ALDEMAR ', 60),
(5, '39575685', 'GAITAN RODRIGUEZ', 'MARITZA', 17),
(6, '39575685', 'GAITAN RODRIGUEZ', 'ALBA MARITZA', 26),
(7, '52114311', 'ESTUPIÑAN RODRIGUEZ', 'OLGA LUCIA', 8),
(8, '22657111', 'DIAZ', 'ANA GABRIELA ', 9),
(9, '1081182154', 'SANCHEZ', 'PATRICIA ', 15),
(10, '11221932', 'PASTRANA', 'OSCAR', 18),
(11, '1007398205', 'GONZALEZ', 'TATIANA ', 14),
(12, '39582689', 'RAMIREZ TRUJILLO ', 'ALICIA ', 54),
(13, '39582689', 'RAMIREZ', 'ALICIA ', 30),
(14, '1070592466', 'DIAZ LEIVA', 'NATALY', 45),
(15, '79538965', 'BOCANEGRA', 'RUBEN DARIO', 23);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `PERSONA`
--
ALTER TABLE `PERSONA`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `PERSONA`
--
ALTER TABLE `PERSONA`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
