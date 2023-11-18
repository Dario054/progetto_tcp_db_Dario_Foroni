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
-- Struttura della tabella `clienti_dario_foroni`
--

CREATE TABLE `clienti_dario_foroni` (
  `id` int(255) NOT NULL,
  `nome` varchar(40) NOT NULL,
  `cognome` varchar(40) NOT NULL,
  `posizione_lavorativa` varchar(40) NOT NULL,
  `data_ass` date NOT NULL,
  `data_n` date NOT NULL,
  `luogo_n` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `clienti_dario_foroni`
--

INSERT INTO `clienti_dario_foroni` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `data_ass`, `data_n`, `luogo_n`) VALUES
(1, 'dario', 'foroni', 'magazziono', '2023-09-04', '2023-08-22', 'Reggio'),
(2, 'samuele', 'zaccarelli', 'magazziono', '2023-09-20', '2023-09-03', 'Carpi');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `clienti_dario_foroni`
--
ALTER TABLE `clienti_dario_foroni`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `clienti_dario_foroni`
--
ALTER TABLE `clienti_dario_foroni`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
