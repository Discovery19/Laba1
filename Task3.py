# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1.44 * 1024 * 1024
list_ = 100
lines = 50
symbols_in_line = 25
symbol_size = 4
book = list_ * lines * symbols_in_line * symbol_size
print("Количество книг, помещающихся на дискету:", round(memory / book))
