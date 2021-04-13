from Form import TelaInserir


def test_ins():

    assert TelaInserir().test_inserir(listaDados=['Cartão','236.5', '15/04/2021','','200','Sim']) == ('Cartão', 236.5, '15/04/2021', 0, 200.0, 36.5, 'Sim')



