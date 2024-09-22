frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

parte_1 = frase[:31]
parte_2 = frase[32:]
frase_a = parte_1.replace("difícil", "fácil")
frase_b = parte_2.replace("mala", "buena")

print(frase_a + " " + frase_b)