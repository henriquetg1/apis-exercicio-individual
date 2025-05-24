CREATE TABLE IF NOT EXISTS db_order.order_tb (
    id_order VARCHAR(255) PRIMARY KEY,
    id_account VARCHAR(255) NOT NULL,
    dt_date TIMESTAMP NOT NULL,
    db_total NUMERIC(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS db_order.order_item (
    id_order_item VARCHAR(255) PRIMARY KEY,
    id_order VARCHAR(255) NOT NULL,
    id_product VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    db_total NUMERIC(10, 2) NOT NULL,
    
    FOREIGN KEY (id_order) 
    REFERENCES db_order.order_tb(id_order)
);