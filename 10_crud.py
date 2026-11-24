import sqlite3
# Conectar ao banco de dados ( ou criar um novo se nao existir)

def conectarBanco() :
    conexao = sqlite3.connect('exemplo.db')
    return conexao

# Vamos criar uma tabela
def criarTabela() :
    conexao = conectarBanco()
    cursor=conexao.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        idade INTEGER
                    )
                   ''')
    conexao.commit()
    conexao.close()

def inserirUsuario(nome,idade):
    conexao = conectarBanco()
    cursor=conexao.cursor()
    cursor.execute('''
                   INSERT INTO usuarios  (nome,idade) VALUES(?,?)
                   ''', (nome, idade))

    conexao.commit()
    conexao.close()
    
def listaUsuarios ():
    conexao = conectarBanco()
    cursor=conexao.cursor()
    cursor.execute('SELECT*FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

#Atualizar dados
def atualizarUsuario(id, novoNome, novaIdade):
    conexao = conectarBanco()
    cursor=conexao.cursor()
    cursor.execute('''
                   UPDATE usuarios SET nome = ?, idade=? WHERE id= ?
                   ''',(novoNome,novaIdade, id))
    conexao.commit()
    conexao.close()

#Vamos excluir um usuário
def excluirUsuario (id):
    conexao = conectarBanco()
    cursor=conexao.cursor()
    cursor.execute('''
                   DELETE FROM usuarios WHERE id = ?
                   ''', (id,))
    conexao.commit()
    conexao.close()
    
#Executar a criação do banco 
criarTabela()
#Vamos inserior um usuário
inserirUsuario("Caio", 39)
inserirUsuario("Lucas", 25)
inserirUsuario("Rafael", 20)
inserirUsuario("Leonardo", 35)
inserirUsuario("Nicole", 16)

#Ver dados armazenados
listaUsuarios()

#Editar um usuario
atualizarUsuario(1, "Henrique", 66)

#Excluir um usuario
excluirUsuario(4)



