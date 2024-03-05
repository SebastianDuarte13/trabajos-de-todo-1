class Producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor
        self.stock_actual = 0

    def actualizar_stock(self, cantidad):
        self.stock_actual += cantidad

    def ganancia_potencial(self):
        return (self.valor_venta - self.valor_compra) * self.stock_actual
