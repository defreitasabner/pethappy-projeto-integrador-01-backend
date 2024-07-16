class ClienteMock(object):

    CADASTRAR_DADOS_VALIDOS = {
        "pessoa": {
            "nome": "Abner Silveira de Freitas",
            "endereco": {
                "cidade": "Rio de Janeiro",
                "bairro": "Tijuca",
                "rua": "Delgado de Carvalho",
                "numero": "84",
                "complemento": "Na esquina com a rua Barão de Itapagipe"
            },    
            "telefones": [
                {
                    "numero": "21983676303",
                    "is_contato_emergencia": True
                }
            ]
        }
    }

    CADASTRAR_DADOS_INVALIDOS = {
        "pessoa": {
            "nome": "Abner Silveira de Freitas",
        }
    }

    ATUALIZAR_ENDERECO = {
        "pessoa": {
            "endereco": {
                "cidade": "São Paulo",
                "bairro": "Santa Cecília",
                "rua": "Rua Barão de Tatuí",
                "numero": "57",
                "complemento": "Apartamento 81"
            }
        }
    } 