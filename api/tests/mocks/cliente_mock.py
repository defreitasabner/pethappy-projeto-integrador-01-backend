class ClienteMock(object):

    CADASTRAR_DADOS_VALIDOS = {
        "pessoa": {
            "nome": "Cliente Válido da Silva",
            "endereco": {
                "cidade": "Rio de Janeiro",
                "bairro": "Tijuca",
                "rua": "Rua qualquer",
                "numero": "123",
                "complemento": "Casa muito engraçada"
            },    
            "telefones": [
                {
                    "numero": "11234567890",
                    "is_contato_emergencia": True
                }
            ]
        }
    }

    CADASTRAR_DADOS_INVALIDOS = {
        "pessoa": {
            "nome": "",
            "endereco": {
                "cidade": "Rio de Janeiro",
                "bairro": "Tijuca",
                "rua": "Delgado de Carvalho",
                "numero": "123",
                "complemento": ""
            },    
            "telefones": [
                {
                    "numero": "11234567890",
                    "is_contato_emergencia": True
                }
            ]
        }
    }

    ATUALIZAR_ENDERECO = {
        "pessoa": {
            "endereco": {
                "cidade": "São Paulo",
                "bairro": "Centro",
                "rua": "Rua Qualquer",
                "numero": "32",
                "complemento": "Logo ali"
            }
        }
    } 