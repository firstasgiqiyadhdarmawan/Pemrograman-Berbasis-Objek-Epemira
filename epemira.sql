-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2020 at 11:11 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `epemira`
--

-- --------------------------------------------------------

--
-- Table structure for table `paslon`
--

CREATE TABLE `paslon` (
  `nopaslon` int(11) NOT NULL,
  `nama_ketua` varchar(255) DEFAULT NULL,
  `nim_ketua` varchar(20) DEFAULT NULL,
  `kelas_ketua` varchar(20) DEFAULT NULL,
  `nama_wakil` varchar(255) DEFAULT NULL,
  `nim_wakil` varchar(20) DEFAULT NULL,
  `kelas_wakil` varchar(20) DEFAULT NULL,
  `visi` varchar(1000) DEFAULT NULL,
  `misi` varchar(1500) DEFAULT NULL,
  `jumlah_suara` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `paslon`
--

INSERT INTO `paslon` (`nopaslon`, `nama_ketua`, `nim_ketua`, `kelas_ketua`, `nama_wakil`, `nim_wakil`, `kelas_wakil`, `visi`, `misi`, `jumlah_suara`) VALUES
(1, 'Rizaldy', '1103194101', 'TK4302', 'Mang Ucup', '1103194065', 'TK4302', 'Meningkatkan kualitas SDM di HMTK', 'memberikan responsi sebelum UTS dan UAS', 0),
(2, 'Alkika', '1103194002', 'TK4302', 'Rifdho', '1103191003', 'TK4302', 'Mempersatukan seluruh angkatan di HMTK', 'mengadakan Makrab dan Fun Futsal antar angkatan', 0);

-- --------------------------------------------------------

--
-- Table structure for table `pemilih`
--

CREATE TABLE `pemilih` (
  `user_id` int(11) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `nim` varchar(20) DEFAULT NULL,
  `kelas` varchar(20) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pemilih`
--

INSERT INTO `pemilih` (`user_id`, `nama`, `nim`, `kelas`, `status`) VALUES
(18, 'ikbal ramdani', '1103194076', 'TK4302', 0),
(19, 'firstasgi qiyadh darmawan', '1103194103', 'TK4302', 0),
(20, 'hanif shafwan mahib', '1103194150', 'TK4302', 0),
(21, 'fakhri arasyid', '1103190057', 'TK4302', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `paslon`
--
ALTER TABLE `paslon`
  ADD PRIMARY KEY (`nopaslon`);

--
-- Indexes for table `pemilih`
--
ALTER TABLE `pemilih`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pemilih`
--
ALTER TABLE `pemilih`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
