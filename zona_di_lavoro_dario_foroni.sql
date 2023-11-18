-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Creato il: Nov 18, 2023 alle 11:56
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `TEPSIT`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `zona_di_lavoro_dario_foroni`
--

CREATE TABLE `zona_di_lavoro_dario_foroni` (
  `id_zona` int(255) NOT NULL,
  `nome_zona` varchar(30) NOT NULL,
  `numero_clienti` int(255) NOT NULL,
  `kfclienti` int(255) DEFAULT NULL,
  `sesso` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `zona_di_lavoro_dario_foroni`
--

INSERT INTO `zona_di_lavoro_dario_foroni` (`id_zona`, `nome_zona`, `numero_clienti`, `kfclienti`, `sesso`) VALUES
(1, 'magazzino', 23, 1, 'maschio');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zona_di_lavoro_dario_foroni`
--
ALTER TABLE `zona_di_lavoro_dario_foroni`
  ADD PRIMARY KEY (`id_zona`),
  ADD KEY `kfclienti` (`kfclienti`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zona_di_lavoro_dario_foroni`
--
ALTER TABLE `zona_di_lavoro_dario_foroni`
  MODIFY `id_zona` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zona_di_lavoro_dario_foroni`
--
ALTER TABLE `zona_di_lavoro_dario_foroni`
  ADD CONSTRAINT `zona_di_lavoro_dario_foroni_ibfk_1` FOREIGN KEY (`kfclienti`) REFERENCES `clienti_dario_foroni` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
