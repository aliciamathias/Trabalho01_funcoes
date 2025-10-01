# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

def dados_usuario():
    usuarios = {
        "admin": "1234",
        "joao": "senha123",
        "maria": "abc@2024"
    }
    return usuarios

def perguntar_usuario_senha():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    return usuario, senha

def verificar_autenticao_usuario(usuario, senha):
    usuarios = dados_usuario()
    if usuarios.get(usuario) == senha:
        print("Autenticação bem-sucedida!")
    else:
        print("Usuário ou senha incorretos.")

usuario, senha = perguntar_usuario_senha()
verificar_autenticao_usuario(usuario, senha)