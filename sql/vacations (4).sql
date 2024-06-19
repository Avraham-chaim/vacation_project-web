-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 22, 2024 at 01:56 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vacations`
--
CREATE DATABASE IF NOT EXISTS `vacations` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `vacations`;

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `country_id` int(11) NOT NULL,
  `country_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`country_id`, `country_name`) VALUES
(1, 'United States'),
(2, 'Canada'),
(3, 'Australia'),
(4, 'Germany'),
(5, 'France'),
(6, 'Brazil'),
(7, 'Japan'),
(8, 'China'),
(9, 'Africa'),
(10, 'Netherlands'),
(12, 'Israel'),
(14, 'Greece'),
(15, 'Norway'),
(16, 'Maldives'),
(17, 'Japan'),
(18, 'Switzerland'),
(19, 'Caribbean'),
(20, 'Rome');

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `user_id` int(11) NOT NULL,
  `vacation_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `role_name`) VALUES
(1, 'User'),
(2, 'Admin');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `First_name` varchar(30) NOT NULL,
  `Last_name` varchar(40) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `password` varchar(15) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `First_name`, `Last_name`, `Email`, `password`, `role_id`) VALUES
(35, 'yair', 'hcohen', 'yy@gmail.com', 'f94f07baccc55b', 2),
(50, 'shalom', 'chen', 'shalom@gmail.com', '2285b241ee7738', 1);

-- --------------------------------------------------------

--
-- Table structure for table `vacations`
--

CREATE TABLE `vacations` (
  `vacation_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  `vacation_description` varchar(1000) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `price` int(11) NOT NULL,
  `vacation_photo_filename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vacations`
--

INSERT INTO `vacations` (`vacation_id`, `country_id`, `vacation_description`, `start_date`, `end_date`, `price`, `vacation_photo_filename`) VALUES
(1, 20, 'Rome, Italy, a city of ancient marvels, boasts iconic landmarks like the Colosseum and the Roman Forum, offering glimpses into its imperial past. The Pantheon and St. Peter\'s Basilica showcase architectural brilliance and religious significance. With its winding streets and hidden treasures, Rome remains an eternal magnet for history lovers and adventurers.', '2024-11-15', '2024-11-20', 1900, '2d2b2ea9-1d4c-4f30-a91b-5141adf8342f.jpg'),
(2, 2, 'Escape to the tranquil beaches of Bali, Indonesia, where pristine shores meet turquoise waters, creating a haven for relaxation and rejuvenation. With its diverse coastline, Bali offers an array of beach experiences, from the vibrant surf breaks of Kuta to the secluded coves of Nusa Dua. Whether you\'re seeking thrilling water sports or simply craving a serene sunbathing session, Bali\'s beaches provide the perfect setting for unwinding amidst breathtaking natural beauty.', '2024-06-10', '2024-06-17', 3200, '8f37e1f1-d725-498f-878d-e74278373393.jpg'),
(3, 9, 'Embark on an unforgettable safari adventure in Kruger National Park, South Africa, where the wild reigns supreme. Spanning vast savannas and dense forests, Kruger is home to a remarkable array of wildlife, including the Big Five: lions, elephants, buffaloes, leopards, and rhinoceroses. Guided game drives offer intimate encounters with these majestic creatures, while walking safaris provide a deeper connection to the untamed wilderness. With its awe-inspiring landscapes and abundant biodiversity, Kruger National Park promises an immersive safari experience like no other.', '2024-08-05', '2024-08-15', 4800, '9625c5ed-4c70-4f87-9ec3-32e3f4005339.jpg'),
(4, 18, '\nIndulge in the ultimate skiing experience amidst the breathtaking beauty of the Swiss Alps in Switzerland. With its pristine slopes, picturesque villages, and towering peaks, the Swiss Alps offer a playground for winter sports enthusiasts of all levels. From the world-renowned resorts of St. Moritz and Zermatt to hidden gems like Verbier and Davos, there\'s a ski destination to suit every taste. Whether carving through fresh powder, enjoying après-ski in cozy mountain chalets, or simply basking in the stunning alpine scenery, a ski holiday in the Swiss Alps promises thrills, relaxation, and unforgettable memories.', '2024-11-20', '2024-11-28', 3700, '8938103a-1bd0-4844-a91a-093f7880e1af.jpg'),
(5, 17, 'Immerse yourself in the rich cultural tapestry of Kyoto, Japan, a city steeped in tradition and history. From the iconic temples and shrines of Kinkaku-ji and Fushimi Inari Taisha to the serene bamboo groves of Arashiyama, Kyoto offers a captivating glimpse into Japan\'s ancient past. Wander through the narrow streets of Gion, where geishas gracefully glide by traditional tea houses, or explore the bustling markets of Nishiki Market, where centuries-old culinary traditions thrive. With its vibrant festivals, elegant tea ceremonies, and exquisite traditional arts such as ikebana and calligraphy, Kyoto invites visitors to experience the essence of Japanese culture in every corner.', '2024-07-12', '2024-07-19', 2900, 'd67094d5-6058-40ce-8c86-0e4c1c6f51d7.jpg'),
(6, 19, '\nEmbark on a spectacular Caribbean cruise adventure, where each day unveils a new paradise island to explore. Set sail from vibrant ports like Miami or San Juan and venture into the azure waters of the Caribbean Sea. Discover the pristine beaches and lush rainforests of destinations like Barbados, St. Lucia, and Antigua, where snorkeling, diving, and zip-lining adventures await. Indulge in the vibrant culture and colorful architecture of historic cities like Old San Juan and Willemstad, Curacao. With onboard entertainment, gourmet dining, and luxurious amenities, a Caribbean cruise offers the perfect blend of relaxation and adventure for travelers of all ages.', '2024-07-08', '2024-07-22', 5500, 'bd53fe88-24f3-49a7-b833-0ce32b82c906.jpg'),
(7, 1, 'Embark on an unforgettable hiking adventure in the iconic Rocky Mountains of the USA. Explore winding trails through alpine meadows, dense forests, and towering peaks. From the majestic vistas of Rocky Mountain National Park to the rugged beauty of Glacier National Park, each step offers breathtaking views and encounters with wildlife. With its boundless wilderness and natural wonders, a hike in the Rockies promises an unforgettable outdoor experience.', '2024-09-15', '2024-09-23', 3000, '846728ef-bf99-40cf-97d2-87631e6c19cf.jpg'),
(9, 16, 'Escape to the ultimate tropical paradise in the Maldives, where pristine beaches, turquoise waters, and luxurious overwater bungalows await. With its serene beauty and endless opportunities for relaxation and adventure, the Maldives promises an unforgettable getaway.', '2024-11-10', '2024-11-17', 6000, 'b9dd340e-85cf-43f8-8dfa-4ef5eee36ff8.jpg'),
(11, 15, '\nEmbark on a mesmerizing journey to witness the Northern Lights in Tromsø, Norway. Located within the Arctic Circle, Tromsø offers prime viewing opportunities for this breathtaking natural phenomenon. Marvel at the dancing curtains of green, purple, and blue lights as they illuminate the night sky in a dazzling display of colors. Whether you choose to chase the auroras by dog sled, snowmobile, or simply from the comfort of a cozy cabin, Tromsø promises an unforgettable experience in one of nature\'s most awe-inspiring spectacles.', '2024-12-05', '2024-12-12', 4500, '372b6006-d1ac-472b-9964-e618c98c5594.jpg'),
(12, 14, 'Embark on a captivating journey through ancient history in Athens, Greece. Explore iconic landmarks like the Acropolis and Parthenon, wander through the historic streets of Plaka, and discover treasures at the National Archaeological Museum. Athens offers a rich tapestry of Greek history and culture at every turn.', '2024-09-25', '2024-09-30', 3100, 'c968b647-d92f-47dd-8748-5c6c40eb0b13.jpg'),
(59, 12, 'Experience the best of Israel: from the ancient streets of Jerusalem and vibrant beaches of Tel Aviv to the serene beauty of the Dead Sea and Galilee. With rich history, diverse landscapes, and vibrant culture, Israel promises an unforgettable vacation for every traveler.', '2024-08-29', '2024-10-31', 2000, '640afa1a-cbaf-43ab-a89b-d60d030d90c6.jpg'),
(69, 2, 'My first visit in Canada!', '2024-07-08', '2024-08-08', 5000, '7773d57e-b1e3-4d12-8528-4ed98fed921f.jpg'),
(70, 5, 'The best country with the best food!', '2024-08-08', '2024-10-20', 8000, 'd98dce2c-f4f9-4727-9e18-f656faae4f75.jpeg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`country_id`);

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `vacation_id` (`vacation_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `vacations`
--
ALTER TABLE `vacations`
  ADD PRIMARY KEY (`vacation_id`),
  ADD KEY `country_id` (`country_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `country_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT for table `vacations`
--
ALTER TABLE `vacations`
  MODIFY `vacation_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `likes`
--
ALTER TABLE `likes`
  ADD CONSTRAINT `likes_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `likes_ibfk_4` FOREIGN KEY (`vacation_id`) REFERENCES `vacations` (`vacation_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);

--
-- Constraints for table `vacations`
--
ALTER TABLE `vacations`
  ADD CONSTRAINT `vacations_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
