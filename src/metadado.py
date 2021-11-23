
from coleta import coleta_pb2 as Coleta


def captura(mes, ano):
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
    if int(ano) == 2018 or int(ano) == 2019:
        metadado.formato_consistente = False
        metadado.outras_receitas = Coleta.Metadados.OpcoesDetalhamento.AUSENCIA
    else:
        metadado.formato_consistente = True
        metadado.outras_receitas = Coleta.Metadados.OpcoesDetalhamento.DETALHADO

    return metadado