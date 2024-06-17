--  creates a trigger that decreases the quantity of an item after adding a new order
CREATE trigger decrease_quantity AFTER INSERT ON orders
for each row
    update items
    set quantity = quantity - new.number
    WHERE name = NEW.item_name;

