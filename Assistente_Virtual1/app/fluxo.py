dados_paciente = {}

def conversa(etapa: str, resposta: str):
    etapa = etapa.lower()

    if etapa == "inicio":
        return{"Pergunta": "Olá, tudo bem? Como posso lhe ajudar hoje?","proxima_etapa": "consulta"}
    
    elif etapa == "consulta":
         return{"Pergunta": "Certo! Você já é paciente da nossa clínica?","proxima_etapa": "verificacao_consulta"}
    
    elif etapa == "verificacao_consulta":
        if resposta.lower() == "sim":
            return {"mensagem": "Perfeito! Vamos buscar seu cadastro.","proxima_etapa": "identificacao_existente"}        

        if resposta.lower() == "não":
            return {"mensagem": "Então faremos um cadastro para o senhor(a).","proxima_etapa": "aviso"}
        
        else:
            return {"mensagem": "Desculpe, não entendi. Responda apenas com 'sim' ou 'não'.","proxima_etapa": "verificacao_consulta"}
        
    elif etapa == "identificacao_existente":
        dados_paciente["identificacao_existente"] = resposta
        return{"pergunta": "Certo! Qual tipo de médico o senhor(a) está precisando neste momento?", "proxima_etapa": "especialidade"}
    
    elif etapa == "aviso":
        return{"mensagem": "Ok! Então precisamos de algumas informações pessoais do senhor(a) para prosseguirmos. Fique tranquilo(a), Seus dados são confidenciais conforme as normas da LGPD.", "proxima_etapa": "cadastro"}
    
    elif etapa == "cadastro":
        return{"pergunta": "Qual o nome completo do senhor(a)?", "proxima_etapa": "nome"}
    
    elif etapa == "nome":
        dados_paciente["nome"] = resposta
        return{"pergunta": "Quantos anos tem?", "proxima_etapa": "idade"}
    
    elif etapa == "idade":
        dados_paciente["idade"] = resposta
        return{"pergunta": "Qual o CPF do senhor(a)?", "proxima_etapa": "cpf"}

    elif etapa == "cpf":
        dados_paciente["cpf"] = resposta
        return{"pergunta": "O senhor(a) poderia me informar um telefone para contato?", "proxima_etapa": "numero"}
    
    elif etapa == "numero":
        dados_paciente["numero"] = resposta
        return{"pergunta": "O senhor(a) tem E-mail?", "proxima_etapa": "verificacao_email"}
    
    elif etapa == "verificacao_email":
        if resposta.lower() == "sim":
            return{"pergunta": "Informe o seu E-mail.", "proxima_etapa": "email"}
       
        elif resposta.lower() == "não":
            dados_paciente["email"] = ""
            return{"pergunta": "O senhor(a) possui algum plano de saúde?","proxima_etapa": "codigo_plano"}
        
        return {"mensagem": "Por favor, responda apenas com 'sim' ou 'não'.","proxima_etapa": "verificacao_email"}
    
    elif etapa == "email":
        dados_paciente["email"] = resposta
        return{"pergunta": "O senhor(a) possui algum plano de saúde?", "proxima_etapa": "verificacao_codigo"}
    
    elif etapa == "verificacao_codigo":
        if resposta.lower() == "sim":
            return {"pergunta": "Por favor, informe o número da sua carteirinha do plano.", "proxima_etapa":"codigo_plano"}

        elif resposta.lower() == "não":
            dados_paciente["codigo_plano"] = ""
            return {"pergunta": "Certo! Qual tipo de médico o senhor(a) está precisando neste momento?", "proxima_etapa": "especialidade"}

        return {"mensagem": "Por favor, responda apenas com 'sim' ou 'não'.", "proxima_etapa": "verificacao_codigo"}

    elif etapa == "codigo_plano":
        dados_paciente["codigo_plano"] = resposta
        return{"pergunta": "Certo! Qual tipo de médico o senhor(a) está precisando neste momento?", "proxima_etapa": "especialidade"}
    
    elif etapa == "especialidade":
        dados_paciente["especialidade"] = resposta
        nome = dados_paciente.get("nome", "")
        return{"mensagem": f"Ok! Ótimo senhor(a) {nome}. Peço que o senhor(a) aguarde por alguns dias, pois os seus dados já foram registrados no nosso sistema. Assim que uma vaga estiver disponível entraremos em contato. Fique tranquilo(a), pois geralmente esse processo de espera leva pouco tempo. Agradecemos sua pela preferência! Até breve.", "proxima_etapa": "fim"}
    
    else:
        return {"mensagem": "Etapa não reconhecida. Comece enviando etapa='inicio'."}