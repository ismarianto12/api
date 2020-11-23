-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Nov 23, 2020 at 02:53 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django`
--

-- --------------------------------------------------------

--
-- Table structure for table `api_mhs`
--

DROP TABLE IF EXISTS `api_mhs`;
CREATE TABLE IF NOT EXISTS `api_mhs` (
  `id` int(14) NOT NULL AUTO_INCREMENT,
  `nama` varchar(15) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `jalan` varchar(30) DEFAULT NULL,
  `ttl` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `api_mhs`
--

INSERT INTO `api_mhs` (`id`, `nama`, `alamat`, `jalan`, `ttl`) VALUES
(8, '333', 'aa', 'jl', 'aa'),
(9, '333', 'aa', 'jl', 'aa'),
(10, '333', 'aa', 'jl', 'aa'),
(11, '333', 'aa', 'jl', 'aa');

-- --------------------------------------------------------

--
-- Table structure for table `jurusan`
--

DROP TABLE IF EXISTS `jurusan`;
CREATE TABLE IF NOT EXISTS `jurusan` (
  `id` int(14) NOT NULL AUTO_INCREMENT,
  `nama` varchar(40) DEFAULT NULL,
  `kode` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
