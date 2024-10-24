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
            "veterinario": {
                "pessoa": {
                    "nome": "Arnaldo César Coelho",
                    "endereco": {
                        "cidade": "São Paulo",
                        "bairro": "Consolação",
                        "rua": "Rua Frei Caneca",
                        "numero": "250",
                        "complemento": ""
                    },
                    "telefones": [
                        {
                            "numero": "11934564242",
                            "is_contato_emergencia": True
                        }
                    ]
                },
                "clinica": "Veterinária Coelho"
            },
            "nome": "Imunizado",
            "data_nascimento": "2020-04-23",
            "sexo": "M",
            "raca": "Vira-lata",
            "medicamentos": [],
            "alimentos": [],
            "cuidados_especiais": [],
            "tutor_id": cliente_id,
            "categoria_id": 1,
            "porte_id": 2
        }