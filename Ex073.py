
times = ("Atlético", "Flamengo", "Palmeiras","Bragantino","Corinthians", "Fortaleza","Internacional","Fluminense","América","Ceará", "Athletico-PR", "Santos", "Cuiabá", "Atlético-GO", "São Paulo", "Bahia", "Juventude", "Grêmio", "Sport Recife", "Chapecoense")

print(f"Os cinco primeiros colocados foram {times[:5]}")
print(f"Os últimos quatro colocados da tabela são {times[-4:]}")
print(f"Os times em ordem alfabética são {sorted(times)}")
for pos, time in enumerate(times):
    if time == "Chapecoense":
        print(f"A Chapecoense está em {pos + 1}º lugar")