-- This is a MySQL file
-- It is only serve to be a reference to the table inventory

CREATE DATABASE IF NOT EXISTS  furnitures;
USE furnitures;

CREATE TABLE IF NOT EXISTS inventory (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` MEDIUMTEXT NOT NULL,
  `buy_date` DATE NOT NULL,
  `category` MEDIUMTEXT NOT NULL,
  `buy_price` INT NOT NULL,
  `sell_price` INT NOT NULL,
  `stock` INT NOT NULL,
  PRIMARY KEY (`id`));

INSERT INTO inventory (name, buy_date, category, buy_price, sell_price, stock)
VALUES 
('white dinning chair', '2016-12-25', 'chair', 40, 50, 10),
('brown desk', '2017-12-10', 'table', 55, 70, 5),
('red dinning chair', '2018-10-10', 'chair', 50, 60, 10),
('rog chair', '2019-04-03', 'chair', 12, 17, 10),
('white dinning table', '2019-06-06', 'table', 85, 100, 5),
('yellow rog bed', '2020-11-25', 'bed', 210, 300, 3),
('king size bed', '2020-01-18', 'bed', 110, 150, 3),
('oak closet', '2021-02-19', 'cabinet', 80, 120, 3),
('white wardrobe', '2022-04-29', 'cabinet', 60, 100, 3),
('white light', '2023-03-01', 'light', 3, 4, 20),
('yellow dinning chair', '2023-02-08', 'chair', 25, 30, 12),
('soft pink bed', '2022-06-24', 'bed', 22, 27, 6),
('coffee table', '2022-07-29', 'table', 130, 150, 7),
('red wardrobe', '2022-09-28', 'cabinet', 160, 200, 2),
('full size bed', '2021-05-06', 'bed', 35, 46, 5),
('yellow lamp', '2020-09-06', 'light', 69, 89, 10),
('oak desk', '2019-09-18', 'table', 88, 120, 2),
('single size table', '2020-09-10', 'table', 8, 14, 8),
('rocking chair', '2020-08-10', 'chair', 50, 60, 9),
('ceiling lamp', '2021-07-02', 'light', 230, 290, 6);
       



