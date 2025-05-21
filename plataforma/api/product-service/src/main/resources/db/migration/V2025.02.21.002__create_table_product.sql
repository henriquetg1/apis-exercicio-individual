CREATE TABLE product.product (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL,
  price NUMERIC(10,2) NOT NULL CHECK (price > 0),
  unit VARCHAR(50) NOT NULL
);
