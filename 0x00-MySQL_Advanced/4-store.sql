-- a SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order.
CREATE TRIGGER IF NOT EXISTS buy_decrease_item
BEFORE INSERT
ON orders FOR EACH Row
BEGIN
UPDATE items SET quantity = quantity - NEW.number 
WHERE `name` = NEW.item_name
END