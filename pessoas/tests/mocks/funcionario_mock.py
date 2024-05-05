class FuncionarioMock(object):

    CADASTRAR_DADOS_VALIDOS = {
        "usuario": {
            "username": "abner",
            "password": "12345678",
            "email": "defreitasabner@gmail.com"
        },
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

    ATUALIZAR_EMAIL = {
        "usuario": {
            "email": "atualizado@email.com"
        }
    }