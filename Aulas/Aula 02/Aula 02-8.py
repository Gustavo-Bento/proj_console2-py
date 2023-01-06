nome = "Gustavo"
idade =19
renda = 3500
entrada = 10000
serasa = False
situacao = True

if (
    (idade>=18)
    and(renda>=2500)
    and(serasa==False)
):
    if(
        (renda>=5000)
        or(entrada>=10000)
    ):
        situacao = True
        print("Aprovado")
    else:
        print("Analisar")
else:
    situacao = False
    print("Reprovado")
    