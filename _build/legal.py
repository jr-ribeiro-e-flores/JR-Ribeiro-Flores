# -*- coding: utf-8 -*-
"""Textos da Política de Privacidade e dos Termos de Uso."""


def privacy(site):
    e = site["email"]
    ga = bool(site.get("ga_id"))
    cookies = (
        "<p>O site utiliza apenas o armazenamento local do navegador para guardar a sua escolha sobre cookies. "
        "Com o seu consentimento, utilizamos o <strong>Google Analytics</strong>, que coleta dados de navegação "
        "de forma agregada (páginas visitadas, tempo de permanência, tipo de dispositivo e localização aproximada) "
        "para entendermos como o site é utilizado. Você pode aceitar ou recusar no aviso exibido na primeira visita "
        "e alterar a escolha a qualquer momento pelo link “Preferências de cookies”, no rodapé.</p>"
        if ga else
        "<p>Este site <strong>não utiliza cookies</strong> de rastreamento, análise ou publicidade. As fontes e "
        "os ícones são carregados do próprio site, sem envio de informações a terceiros.</p>"
    )
    third = [
        "<li><strong>FormSubmit</strong>, que encaminha as mensagens do formulário ao e-mail do escritório;</li>",
        "<li><strong>Google (Gmail)</strong>, para recebimento e resposta de e-mails;</li>",
        "<li><strong>WhatsApp</strong>, quando você opta por falar conosco por esse canal;</li>",
        "<li><strong>GitHub Pages</strong>, que hospeda o site e pode registrar dados técnicos de acesso, como o endereço IP;</li>",
    ]
    if ga:
        third.append("<li><strong>Google Analytics</strong>, somente se você consentir, para estatísticas de uso do site;</li>")
    return {
        "title": "Política de Privacidade",
        "eyebrow": "LGPD",
        "lead": "Transparência sobre como coletamos, utilizamos e protegemos os seus dados pessoais.",
        "updated": "outubro de 2026",
        "sections": [
            ("quem-somos", "1. Quem somos",
             f"<p>Este site pertence à <strong>{site['name']}</strong>, responsável pelo tratamento dos dados pessoais "
             "coletados por meio dele, nos termos da Lei nº 13.709/2018 (Lei Geral de Proteção de Dados, a LGPD). "
             f"Para qualquer assunto relacionado aos seus dados, fale com a gente pelo e-mail <a href=\"mailto:{e}\">{e}</a>.</p>"),
            ("dados", "2. Quais dados coletamos",
             "<p>Coletamos apenas os dados que você nos envia voluntariamente:</p><ul>"
             "<li><strong>Formulário de contato:</strong> nome, telefone/WhatsApp, e-mail, área de interesse e a descrição que você escrever;</li>"
             "<li><strong>WhatsApp e e-mail:</strong> as informações que você compartilhar nas conversas com o escritório.</li></ul>"
             "<p>Recomendamos não enviar, no primeiro contato, documentos ou informações sensíveis (como dados de saúde). "
             "Se forem necessários para a análise do caso, orientaremos a melhor forma de envio.</p>"),
            ("finalidade", "3. Para que usamos os dados",
             "<ul><li>Responder à sua solicitação e agendar o atendimento;</li><li>Analisar preliminarmente o seu caso;</li>"
             "<li>Prestar os serviços jurídicos, caso você decida nos contratar;</li><li>Cumprir obrigações legais e éticas da advocacia.</li></ul>"
             "<p>Não vendemos, alugamos ou utilizamos seus dados para publicidade de terceiros.</p>"),
            ("base-legal", "4. Base legal",
             "<p>O tratamento é realizado com base no seu <strong>consentimento</strong>, nos <strong>procedimentos preliminares "
             "à contratação</strong> de serviços solicitados por você e, quando aplicável, no <strong>exercício regular de direitos</strong> "
             "e no cumprimento de obrigações legais (art. 7º da LGPD).</p>"),
            ("compartilhamento", "5. Compartilhamento",
             "<p>Para funcionar, o site utiliza serviços de terceiros que podem ter acesso técnico às informações:</p><ul>"
             + "".join(third) + "</ul>"
             "<p>Os dados também poderão ser compartilhados com órgãos públicos ou do Judiciário quando necessário à defesa dos "
             "seus interesses, sempre dentro do serviço contratado, ou por obrigação legal.</p>"),
            ("sigilo", "6. Sigilo profissional",
             "<p>Todas as informações relacionadas ao seu caso são protegidas pelo <strong>sigilo profissional</strong> previsto no "
             "Estatuto da Advocacia (Lei nº 8.906/1994) e no Código de Ética e Disciplina da OAB.</p>"),
            ("seguranca", "7. Segurança",
             "<p>O site funciona exclusivamente com conexão criptografada (HTTPS). Adotamos medidas técnicas e organizacionais "
             "razoáveis para proteger os dados contra acessos não autorizados, perda ou alteração.</p>"),
            ("retencao", "8. Por quanto tempo guardamos",
             "<p>Os dados são mantidos pelo tempo necessário para atender à sua solicitação e, em caso de contratação, pelo período "
             "exigido para o cumprimento de obrigações legais e para a defesa de direitos. Se não houver contratação, os dados do "
             "contato podem ser excluídos mediante solicitação.</p>"),
            ("cookies", "9. Cookies", cookies),
            ("direitos", "10. Seus direitos",
             "<p>Você pode, a qualquer momento, solicitar: confirmação da existência de tratamento, acesso aos dados, correção, "
             "anonimização ou exclusão, portabilidade, informação sobre compartilhamento e revogação do consentimento (art. 18 da LGPD). "
             f"Basta enviar um e-mail para <a href=\"mailto:{e}\">{e}</a>. Você também pode apresentar reclamação à Autoridade "
             "Nacional de Proteção de Dados (ANPD).</p>"),
            ("alteracoes", "11. Alterações",
             "<p>Esta política pode ser atualizada para refletir mudanças no site ou na legislação. A versão vigente estará sempre "
             "disponível nesta página.</p>"),
        ],
    }


def terms(site):
    e = site["email"]
    return {
        "title": "Termos de Uso",
        "eyebrow": "Aviso legal",
        "lead": "Condições de uso deste site e informações importantes sobre o conteúdo publicado.",
        "updated": "outubro de 2026",
        "sections": [
            ("aceitacao", "1. Aceitação",
             f"<p>Ao acessar este site, você concorda com estes Termos de Uso. O site é mantido pela <strong>{site['name']}</strong> "
             "e tem finalidade exclusivamente informativa e institucional.</p>"),
            ("informativo", "2. Caráter informativo",
             "<p>Os artigos e textos publicados têm caráter <strong>informativo e educativo</strong>. Eles não constituem parecer "
             "jurídico, consulta ou recomendação para um caso específico, e não substituem a análise individual de um advogado. "
             "A legislação e o entendimento dos tribunais podem mudar ao longo do tempo.</p>"),
            ("relacao", "3. Relação advogado-cliente",
             "<p>O envio de mensagens pelo formulário, e-mail ou WhatsApp <strong>não estabelece, por si só, relação "
             "advogado-cliente</strong>. A contratação dos serviços depende de análise prévia do caso e de ajuste formal entre as "
             "partes, inclusive quanto aos honorários.</p>"),
            ("publicidade", "4. Publicidade e ética profissional",
             "<p>Este site observa o Código de Ética e Disciplina da OAB e o Provimento nº 205/2021 do Conselho Federal da OAB, "
             "que regulamentam a publicidade na advocacia. Nenhum conteúdo deve ser interpretado como promessa de resultado, "
             "uma vez que cada caso depende de suas circunstâncias e da decisão das autoridades competentes.</p>"),
            ("propriedade", "5. Propriedade intelectual",
             "<p>Textos, marca, brasão, imagens e layout deste site pertencem à Ribeiro &amp; Flores Advocacia ou são utilizados "
             "com autorização. É permitido compartilhar links para os artigos; a reprodução total ou parcial do conteúdo depende "
             "de autorização prévia e da indicação da fonte.</p>"),
            ("links", "6. Links externos",
             "<p>O site pode conter links para serviços de terceiros, como WhatsApp e redes sociais. Não nos responsabilizamos "
             "pelo conteúdo ou pelas práticas de privacidade desses serviços.</p>"),
            ("privacidade", "7. Privacidade",
             "<p>O tratamento de dados pessoais segue a nossa <a href=\"../privacidade/\">Política de Privacidade</a>.</p>"),
            ("contato", "8. Contato",
             f"<p>Dúvidas sobre estes termos podem ser enviadas para <a href=\"mailto:{e}\">{e}</a>.</p>"),
        ],
    }
