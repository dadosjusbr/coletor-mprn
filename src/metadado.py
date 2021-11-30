from coleta import coleta_pb2 as Coleta


def captura(month, year):
    metadado = Coleta.Metadados()
    metadado.nao_requer_login = True
    metadado.nao_requer_captcha = True
    metadado.acesso = Coleta.Metadados.FormaDeAcesso.RASPAGEM_DIFICULTADA
    metadado.extensao = Coleta.Metadados.Extensao.ODS
    metadado.estritamente_tabular = False
    metadado.tem_matricula = True
    metadado.tem_lotacao = False
    metadado.tem_cargo = True
    metadado.receita_base = Coleta.Metadados.OpcoesDetalhamento.DETALHADO
    metadado.despesas = Coleta.Metadados.OpcoesDetalhamento.DETALHADO
    metadado.formato_consistente = True
    metadado.outras_receitas = Coleta.Metadados.OpcoesDetalhamento.DETALHADO
    # Nessa data, são adicionadas as planilhas de verbas indenizatórias
    if int(year) == 2020 and int(month) == 1:
        metadado.formato_consistente = False
    # Para esses anos, é apenas colocado o total, e não detalhado as verbas indenizatórias
    if int(year) == 2018 or int(year) == 2019:
        metadado.outras_receitas = Coleta.Metadados.OpcoesDetalhamento.SUMARIZADO
        
    return metadado