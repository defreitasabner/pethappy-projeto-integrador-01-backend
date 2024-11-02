class PetMock(object):

    def cadastrar_minimo_dados_necessarios(cliente_id):
        return {
            "nome": "Imunizado",
            "data_nascimento": "2020-04-23T03:00:00.000Z",
            "sexo": "M",
            "raca": "Vira-lata",
            "tutor_id": cliente_id,
            "categoria_id": 1,
            "porte_id": 2
        }
    
    def cadastrar_dados_necessarios_com_veterinario(cliente_id):
        return {
            "nome": "Imunizado",
            "data_nascimento": "2020-04-23",
            "sexo": "M",
            "raca": "Vira-lata",
            "tutor_id": cliente_id,
            "categoria_id": 1,
            "porte_id": 2,
            "alimentos": "Pote de ração cheio de manhã e de tarde.",
            "medicamentos": "Comprimido junto com a ração da tarde",
            "cuidados_especiais": "Fica ansioso com outros cachorros.",
            "veterinario": "Arnaldo César Coelho 11934564242",
        }