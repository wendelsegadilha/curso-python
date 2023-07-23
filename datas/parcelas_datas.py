from datetime import datetime, timedelta

valor_emprestimo = 1_000_000
data_emprestimo = datetime(2020,12,20)
qtd_parcelas = 5 * 12
valor_parcela = valor_emprestimo / qtd_parcelas

for parcela in range(0, qtd_parcelas):
    data_emprestimo = data_emprestimo + timedelta(days=30)
    print(data_emprestimo, valor_parcela)

