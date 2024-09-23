class FuncionarioMock(object):

    CADASTRAR_DADOS_VALIDOS = {
        "usuario": {
            "username": "rogerinho",
            "password": "12345678",
            "email": "rogerinho_do_inga@xpto.com"
        },
        "pessoa": {
            "nome": "Rogerinho do Ingá",
            "endereco": {
                "cidade": "Niterói",
                "bairro": "Ingá",
                "rua": "Rua Qualquer",
                "numero": "42",
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

    CADASTRAR_DADOS_INVALIDOS = {
        "pessoa": {
            "nome": "Shrek",
        }
    }

    ATUALIZAR_EMAIL = {
        "usuario": {
            "email": "atualizado@email.com"
        }
    }