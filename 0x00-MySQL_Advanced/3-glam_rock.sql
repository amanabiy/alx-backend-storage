-- a SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
SELECT DISTINCT `band_name`, IFNULL(`split`, 2020) - `formed` as `lifespan`
FROM `metal_bands` WHERE  style Like '%Glam rock%' ORDER BY `lifespan` DESC