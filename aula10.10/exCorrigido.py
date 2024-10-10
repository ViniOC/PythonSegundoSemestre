import oracledb

def get_conexao():
    return oracledb.connect(user="rm556182", password="101003", dsn = "oracle.fiap.com.br/orcl")


def insere(carro:dict):
    sql = "insert into tb_carro(modelo,montadora, placa, ano) values (:modelo, :montadora, :placa, :ano) returning id into :id"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            carro['id'] = novo_id
            cur.execute(sql, carro)
            carro['id'] = novo_id.getvalue()[0]
        conn.commit()
        
def recupera_id(id:int):
    sql = "slect id, modelo, montadora, placa, ano from tb_carro where id = :id"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"id": id})
            reg = cur.fetchone
            if len(reg) > 0:
                return{'id': reg[0], 'modelo': reg[1], 'montadora': reg[2], 'placa': reg[3], 'ano': reg[4]}
            else:
                return None