from animal import Cachorro, Cavalo, Preguica, Veterinario

cachorro1 = Cachorro('Sutao', 4)
print(f'Cachorro\n Nome:{cachorro1.nome} \n Idade:{cachorro1.idade}')
print(cachorro1.emitir_som())
print(cachorro1.correr())

print()

cavalo1 = Cavalo('Trovao', 7)
print(f'Cavalo\n Nome:{cavalo1.nome} \n Idade:{cavalo1.idade}')
print(cavalo1.emitir_som())
print(cavalo1.correr())

print()

preguica1 = Preguica('Sonic', 1)
print(f'Preguica\n Nome:{preguica1.nome}\n Idade:{preguica1.idade}')
print(preguica1.emitir_som())
print(preguica1.subir_arvore())

print()

veterinario = Veterinario()
veterinario.examinar(cachorro1)
veterinario.examinar(cavalo1)
veterinario.examinar(preguica1)
