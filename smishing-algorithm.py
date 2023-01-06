import smtplib

# Endereço de e-mail e senha do remetente
endereco_email = "atacante@email.com"
senha = "SenhaAtacante"

# Número de telefone do alvo
alvo = "5511999999999"

# Mensagem da mensagem de texto
mensagem = """\
Prezado usuário,

Estamos observando atividades suspeitas em sua conta. Para proteger sua conta, solicitamos que você verifique suas informações de login clicando no link a seguir:

http://sitefalso.com/verificar-conta

Atenciosamente,
Equipe de segurança
"""

# Conexão com o servidor de e-mail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(endereco_email, senha)

# Envio da mensagem de texto
server.sendmail(endereco_email, alvo, mensagem)
server.quit()
