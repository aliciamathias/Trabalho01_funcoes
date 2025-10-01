# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão

import conversor
def main():
    tipo = input("Digite 'dolar' para converter de real para dólar (Default) ou\n" \
    "'real' para converter de dólar para real: ")
    valor = float(input("Digite o valor: "))
    cotacao = float(input("Digite a cotação do dólar: "))

    if (tipo.lower() == "dolar" or tipo == ""):
        print(f"\n{valor:.2f} reais equivalem a {conversor.real_para_dolar(valor, cotacao):.2f} dólares.")
    elif(tipo.lower() == "real"):
        print(f"{valor:.2f} dólares equivalem a {conversor.dolar_para_real(valor, cotacao):.2f} reais.")

main()