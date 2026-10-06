# -*- coding: utf-8 -*-
"""Conteúdo do site Ribeiro & Flores Advocacia.

Edite aqui textos, dados de contato, sócios, áreas e artigos.
Depois rode:  python3 _build/build.py
"""
from urllib.parse import quote

# ======================================================================
# CONFIGURAÇÃO GERAL
# ======================================================================
SITE = {
    "name": "Ribeiro & Flores Advocacia",
    "short": "Ribeiro & Flores",
    # Endereço público do site, SEM barra no final.
    # Quando o domínio próprio estiver ativo, troque por "https://ribeiroeflores.adv.br"
    "url": "https://jr-ribeiro-e-flores.github.io/JR-Ribeiro-Flores",
    "phone_display": "(51) 99522-5270",
    "phone_e164": "+5551995225270",
    "whatsapp": "5551995225270",
    "email": "atendimento.ribeiroflores.adv@gmail.com",
    # E-mail que recebe o formulário (FormSubmit).
    "form_email": "atendimento.ribeiroflores.adv@gmail.com",
    "hours_display": "Segunda a sexta, das 8h às 19h",
    "hours_short": "Seg. a sex., 8h às 19h",
    "city": "Canoas",
    "region": "RS",
    "service_area": "Atendimento online em todo o Brasil",
    # Redes sociais (deixe vazio "" para ocultar)
    "instagram": "",
    "linkedin": "",
    "facebook": "",
    # Google Analytics 4: ex. "G-XXXXXXXXXX". Vazio = desativado (sem cookies).
    "ga_id": "",
    # Google Search Console: valor do content da meta tag de verificação. Vazio = não inclui.
    "gsc_verification": "",
    # Mapa: deixe vazio enquanto o atendimento for 100% online.
    "map_embed": "",
    "address": "",
}

WA_DEFAULT = "Olá! Vim pelo site da Ribeiro & Flores Advocacia e gostaria de agendar um atendimento."


def wa(msg=WA_DEFAULT):
    return f"https://wa.me/{SITE['whatsapp']}?text={quote(msg)}"


# ======================================================================
# SÓCIOS
# Campos vazios ("" ou []) são ocultados automaticamente na página.
# ======================================================================
PARTNERS = [
    {
        "key": "josue-ribeiro",
        "name": "Josué Ribeiro",
        "role": "Advogado · Sócio fundador",
        "oab": "",  # ex.: "OAB/RS 000.000"
        "instagram": "josue_vrsilva",
        "photo": "josue",
        "summary": "Advogado fundador da Ribeiro & Flores Advocacia, com atuação pautada na estratégia jurídica, "
                   "na análise técnica e na construção de soluções personalizadas para cada cliente.",
        "bio": [
            "Josué Ribeiro conduz pessoalmente os casos do escritório, do primeiro contato à conclusão. "
            "Sua forma de trabalhar parte de uma escuta atenta: entender o problema por inteiro antes de "
            "propor qualquer caminho.",
            "Sua visão é unir conhecimento técnico, inovação e atendimento humanizado para oferecer uma "
            "experiência jurídica mais eficiente e transparente, com comunicação clara em cada etapa.",
        ],
        "education": [],   # ex.: ["Bacharel em Direito — Universidade X (2015)", "Pós-graduação em ..."]
        "experience": [],  # ex.: ["Advocacia trabalhista desde 2016", ...]
        "areas": ["civil", "empresarial", "consumidor"],
        "highlights": [
            ("Estratégia", "Análise individual de cada caso para definir o caminho jurídico mais adequado."),
            ("Tecnologia", "Atendimento 100% digital, com acompanhamento organizado e ágil."),
            ("Proximidade", "Contato direto com o cliente durante toda a demanda."),
        ],
    },
    {
        "key": "renata-flores",
        "name": "Renata Flores",
        "role": "Advogada · Sócia fundadora",
        "oab": "",
        "instagram": "renata.floresb",
        "photo": "renata",
        "summary": "Advogada sócia fundadora da Ribeiro & Flores Advocacia, com atuação humanizada, ética e "
                   "comprometida com os objetivos de cada cliente.",
        "bio": [
            "Renata Flores atua na construção de uma advocacia próxima, em que o cliente entende o que está "
            "acontecendo com o seu caso e participa das decisões importantes.",
            "Sua atuação representa os valores do escritório: ética, dedicação e compromisso na busca pelas "
            "melhores soluções jurídicas, com atenção às particularidades de cada pessoa.",
        ],
        "education": [],
        "experience": [],
        "areas": ["trabalhista", "previdenciario"],
        "highlights": [
            ("Atendimento humanizado", "Escuta atenta e linguagem acessível, sem juridiquês."),
            ("Ética", "Atuação pautada pelo Código de Ética e Disciplina da OAB."),
            ("Compromisso", "Dedicação e acompanhamento em todas as etapas da demanda."),
        ],
    },
]

# ======================================================================
# ÁREAS DE ATUAÇÃO
# ======================================================================
AREAS = [
    {
        "key": "trabalhista",
        "slug": "direito-trabalhista",
        "name": "Direito Trabalhista",
        "short": "Trabalhista",
        "icon": "briefcase",
        "cover": "trabalhista",
        "seo_title": "Advogado Trabalhista Online",
        "description": "Advogado trabalhista online: rescisão, horas extras, insalubridade, acidente de trabalho e "
                       "verbas rescisórias. Atendimento em todo o Brasil com a Ribeiro & Flores Advocacia.",
        "card": "Defesa de trabalhadores e empresas em rescisões, horas extras, adicionais e acidentes de trabalho.",
        "lead": "Defesa estratégica dos direitos de trabalhadores e empresas, com análise personalizada de cada situação.",
        "intro": [
            "As relações de trabalho envolvem direitos e deveres que precisam ser respeitados dos dois lados. "
            "Quando algo sai do combinado, como verbas não pagas, jornada excessiva ou uma demissão mal conduzida, "
            "é importante entender exatamente o que a lei garante.",
            "A Ribeiro & Flores Advocacia analisa contratos, documentos e a rotina de trabalho para identificar "
            "os direitos envolvidos e construir a solução mais adequada, seja por acordo, seja na Justiça do Trabalho.",
        ],
        "situations": [
            ("Rescisão trabalhista", "Conferência de verbas rescisórias, aviso prévio, FGTS, multa de 40% e seguro-desemprego."),
            ("Horas extras", "Análise da jornada real, do controle de ponto e das diferenças devidas."),
            ("Insalubridade e periculosidade", "Avaliação de atividades expostas a agentes nocivos ou de risco e dos adicionais correspondentes."),
            ("Acidente de trabalho", "Orientação a vítimas de acidentes e doenças ocupacionais: estabilidade, indenizações e benefícios."),
            ("Justa causa", "Análise da validade da dispensa por justa causa e possibilidade de reversão."),
            ("Equiparação salarial", "Diferenças salariais e tratamento desigual entre empregados na mesma função."),
            ("Vínculo de emprego", "Reconhecimento de vínculo em casos de trabalho sem carteira assinada ou \"pejotização\"."),
            ("Assédio no trabalho", "Atuação em situações de assédio moral ou sexual e pedidos de indenização."),
        ],
        "how": [
            ("Entendimento do caso", "Conversamos sobre a sua rotina, o contrato e o que aconteceu."),
            ("Análise de documentos", "Carteira, contracheques, termo de rescisão, FGTS e provas da jornada."),
            ("Cálculo e estratégia", "Estimamos os valores envolvidos e indicamos o melhor caminho: acordo ou ação."),
            ("Acompanhamento", "Conduzimos o caso e informamos você sobre cada andamento."),
        ],
        "faq": [
            ("Qual é o prazo para entrar com uma ação trabalhista?",
             "Em regra, até 2 anos após o fim do contrato de trabalho. Dentro desse prazo, é possível cobrar direitos "
             "referentes aos últimos 5 anos. Por isso, quanto antes a análise for feita, melhor."),
            ("Quais documentos devo separar?",
             "Carteira de trabalho, contracheques, termo de rescisão, extrato do FGTS e qualquer prova da rotina de "
             "trabalho, como mensagens, e-mails, fotos e nomes de testemunhas."),
            ("Preciso ir até o escritório?",
             "Não. Todo o atendimento é online: conversa inicial, envio de documentos e reuniões por vídeo. "
             "Se houver audiência, orientamos você sobre como participar."),
            ("A empresa vai saber que procurei um advogado?",
             "Não. A consulta é protegida pelo sigilo profissional. Nenhuma medida é tomada sem a sua autorização."),
            ("Vocês atendem empresas também?",
             "Sim. Atuamos na defesa de empresas em reclamações trabalhistas e na orientação preventiva sobre "
             "contratações, jornada e desligamentos."),
        ],
        "cta": "Teve algum direito trabalhista desrespeitado?",
    },
    {
        "key": "previdenciario",
        "slug": "direito-previdenciario",
        "name": "Direito Previdenciário",
        "short": "Previdenciário",
        "icon": "shield",
        "cover": "previdenciario",
        "seo_title": "Advogado Previdenciário Online | INSS",
        "description": "Advogado previdenciário online: aposentadoria, benefício negado pelo INSS, auxílio por "
                       "incapacidade, BPC/LOAS e revisões. Atendimento em todo o Brasil.",
        "card": "Aposentadorias, benefícios negados pelo INSS, BPC/LOAS, revisões e planejamento previdenciário.",
        "lead": "Planejamento, orientação e defesa dos seus direitos perante o INSS.",
        "intro": [
            "A aposentadoria e os benefícios previdenciários representam conquistas importantes e, muitas vezes, "
            "a principal fonte de renda de uma família. Um erro no pedido ou no cálculo pode significar anos de "
            "prejuízo.",
            "A Ribeiro & Flores Advocacia analisa o histórico contributivo, os documentos e as regras aplicáveis "
            "para buscar o melhor benefício possível, no INSS ou na Justiça Federal.",
        ],
        "situations": [
            ("Aposentadorias", "Análise de requisitos, tempo de contribuição e regras de transição para o melhor benefício."),
            ("Benefício negado", "Recurso administrativo ou ação judicial quando o INSS indefere o pedido."),
            ("Auxílio por incapacidade", "Benefícios por incapacidade temporária ou permanente negados ou cessados."),
            ("Auxílio-acidente", "Indenização mensal para quem teve redução da capacidade de trabalho após um acidente."),
            ("BPC/LOAS", "Benefício assistencial para idosos e pessoas com deficiência que atendem aos requisitos legais."),
            ("Pensão por morte", "Orientação a dependentes sobre o direito à pensão e a documentação necessária."),
            ("Revisões", "Verificação de erros no cálculo de benefícios já concedidos."),
            ("Planejamento previdenciário", "Organização da vida contributiva para se aposentar no melhor momento."),
        ],
        "how": [
            ("Levantamento", "Analisamos o CNIS, carteiras de trabalho e documentos do seu histórico."),
            ("Diagnóstico", "Identificamos o benefício cabível, as regras aplicáveis e eventuais pendências."),
            ("Pedido ou recurso", "Organizamos o requerimento, o recurso ou a ação judicial."),
            ("Acompanhamento", "Monitoramos o processo e mantemos você informado."),
        ],
        "faq": [
            ("O INSS negou meu benefício. Perdi o direito?",
             "Não necessariamente. É possível apresentar recurso administrativo, em regra no prazo de 30 dias, "
             "fazer novo pedido com documentação completa ou buscar a Justiça Federal."),
            ("Quanto tempo de contribuição preciso para receber auxílio por incapacidade?",
             "Em regra, são exigidas 12 contribuições mensais de carência. Há exceções, como em casos de acidente "
             "de qualquer natureza e de algumas doenças graves previstas em lei."),
            ("Posso revisar minha aposentadoria?",
             "Sim, desde que dentro do prazo legal, que em geral é de 10 anos a partir do primeiro pagamento. "
             "Uma análise do cálculo mostra se a revisão vale a pena."),
            ("O que é o CNIS e por que ele é importante?",
             "É o Cadastro Nacional de Informações Sociais, que reúne seus vínculos e contribuições. Erros ou "
             "lacunas no CNIS são uma das causas mais comuns de benefícios negados ou calculados a menor."),
            ("Atendem segurados de outros estados?",
             "Sim. O atendimento é online, e os processos previdenciários tramitam de forma eletrônica, o que "
             "permite atuar em todo o Brasil."),
        ],
        "cta": "O INSS negou seu benefício?",
    },
    {
        "key": "consumidor",
        "slug": "direito-do-consumidor",
        "name": "Direito do Consumidor",
        "short": "Consumidor",
        "icon": "cart",
        "cover": "consumidor",
        "seo_title": "Advogado do Consumidor Online",
        "description": "Advogado do consumidor: cobrança indevida, nome negativado, fraudes bancárias, contratos "
                       "abusivos e indenizações. Atendimento online em todo o Brasil.",
        "card": "Cobranças indevidas, negativação irregular, fraudes bancárias, contratos abusivos e indenizações.",
        "lead": "Proteção dos seus direitos nas relações de consumo e combate às práticas abusivas.",
        "intro": [
            "As relações de consumo fazem parte do dia a dia de todos. Ainda assim, cobranças indevidas, contratos "
            "desproporcionais, falhas em serviços e fraudes causam prejuízos e muita dor de cabeça.",
            "A Ribeiro & Flores Advocacia atua para restabelecer o equilíbrio nessas relações, com base no Código "
            "de Defesa do Consumidor, buscando a devolução de valores e a reparação dos danos sofridos.",
        ],
        "situations": [
            ("Cobranças indevidas", "Cobranças sem fundamento, valores incorretos e devolução em dobro do que foi pago."),
            ("Negativação indevida", "Nome incluído indevidamente no SPC ou Serasa e pedido de indenização."),
            ("Fraudes bancárias", "Golpes, transações não reconhecidas e empréstimos não contratados."),
            ("Contratos abusivos", "Cláusulas que geram desequilíbrio ou prejuízo ao consumidor."),
            ("Produtos e serviços", "Produtos com defeito, serviços mal prestados e descumprimento de oferta."),
            ("Planos e operadoras", "Problemas com telefonia, internet, companhias aéreas e prestadores de serviço."),
            ("Indenizações", "Reparação de danos materiais e morais causados ao consumidor."),
        ],
        "how": [
            ("Relato e provas", "Você nos conta o que aconteceu e envia faturas, prints e protocolos."),
            ("Análise jurídica", "Avaliamos os direitos envolvidos e o valor que pode ser pleiteado."),
            ("Tentativa de solução", "Quando adequado, buscamos um acordo antes de ir à Justiça."),
            ("Ação judicial", "Se necessário, ingressamos com a ação e acompanhamos até o fim."),
        ],
        "faq": [
            ("Qual o prazo para reclamar de um produto ou serviço com defeito?",
             "Em regra, 30 dias para produtos e serviços não duráveis e 90 dias para os duráveis, contados da "
             "entrega ou, no caso de vício oculto, do momento em que o defeito aparece."),
            ("Comprei pela internet e me arrependi. Posso devolver?",
             "Sim. Nas compras feitas fora do estabelecimento comercial, como internet e telefone, o consumidor pode "
             "desistir em até 7 dias a partir do recebimento, com devolução dos valores pagos."),
            ("Nome negativado indevidamente gera indenização?",
             "Em regra, sim. A exceção mais comum é quando a pessoa já possuía outra negativação legítima anterior. "
             "Nesse caso, pode ser pedido o cancelamento do registro indevido."),
            ("Paguei uma cobrança indevida. Tenho direito à devolução?",
             "Sim. O Código de Defesa do Consumidor prevê a devolução em dobro do valor pago indevidamente, salvo "
             "engano justificável do fornecedor."),
            ("Fui vítima de golpe envolvendo minha conta bancária. O banco pode ser responsabilizado?",
             "Depende do caso. Os bancos respondem por falhas de segurança na prestação do serviço. Cada situação "
             "precisa ser analisada, por isso é importante registrar a ocorrência e reunir os comprovantes logo."),
        ],
        "cta": "Foi prejudicado como consumidor?",
    },
    {
        "key": "civil",
        "slug": "direito-civil",
        "name": "Direito Civil",
        "short": "Civil",
        "icon": "scale",
        "cover": "civil",
        "seo_title": "Advogado Cível Online | Contratos e Indenizações",
        "description": "Advogado cível online: contratos, indenizações, responsabilidade civil, cobranças e conflitos "
                       "patrimoniais. Atendimento personalizado em todo o Brasil.",
        "card": "Contratos, indenizações, responsabilidade civil, cobranças e conflitos patrimoniais.",
        "lead": "Soluções jurídicas para relações pessoais, contratuais e patrimoniais.",
        "intro": [
            "O Direito Civil está presente nas principais relações da vida cotidiana: um contrato de aluguel, a "
            "compra de um imóvel, um acidente de trânsito, uma dívida que não foi paga.",
            "A Ribeiro & Flores Advocacia atua na prevenção e na solução desses conflitos, priorizando caminhos "
            "eficientes, como a negociação e o acordo, sem abrir mão da firmeza quando a via judicial é necessária.",
        ],
        "situations": [
            ("Contratos", "Elaboração, análise e revisão de contratos para dar segurança às partes."),
            ("Indenizações", "Danos materiais e morais decorrentes de situações prejudiciais."),
            ("Responsabilidade civil", "Prejuízos causados por pessoas ou empresas, inclusive acidentes de trânsito."),
            ("Cobranças e obrigações", "Dívidas, pagamentos não realizados e descumprimento de obrigações."),
            ("Locação", "Questões entre locador e locatário: despejo, reajustes, cobrança de aluguéis."),
            ("Conflitos patrimoniais", "Questões envolvendo bens, direitos e relações patrimoniais."),
            ("Negociações e acordos", "Notificações extrajudiciais e acordos formalizados com segurança."),
        ],
        "how": [
            ("Escuta e documentos", "Entendemos os fatos e reunimos contratos, comprovantes e conversas."),
            ("Avaliação de riscos", "Mostramos as possibilidades, os riscos e os custos de cada caminho."),
            ("Solução extrajudicial", "Sempre que possível, buscamos resolver por notificação ou acordo."),
            ("Atuação judicial", "Quando necessário, conduzimos o processo com estratégia e acompanhamento."),
        ],
        "faq": [
            ("Contrato verbal tem validade?",
             "Em muitos casos, sim. O problema costuma ser a prova do que foi combinado. Mensagens, comprovantes de "
             "pagamento e testemunhas ajudam a demonstrar o acordo."),
            ("Qual o prazo para pedir indenização?",
             "Em regra, o prazo para a pretensão de reparação civil é de 3 anos. Alguns casos possuem prazos "
             "específicos, por isso é importante analisar a situação concreta."),
            ("É possível resolver sem entrar na Justiça?",
             "Muitas vezes, sim. Notificações extrajudiciais, negociação e acordos formalizados podem resolver o "
             "conflito de forma mais rápida e econômica."),
            ("Vocês analisam contratos antes da assinatura?",
             "Sim. A revisão prévia é uma das formas mais eficientes de evitar prejuízos e conflitos futuros."),
        ],
        "cta": "Precisa de orientação jurídica?",
    },
    {
        "key": "empresarial",
        "slug": "direito-empresarial",
        "name": "Direito Empresarial",
        "short": "Empresarial",
        "icon": "building",
        "cover": "empresarial",
        "seo_title": "Advogado Empresarial Online | Assessoria para Empresas",
        "description": "Assessoria jurídica empresarial online: contratos, consultoria trabalhista preventiva, "
                       "organização societária, recuperação de crédito e LGPD para empresas de todo o Brasil.",
        "card": "Assessoria preventiva para empresas: contratos, questões societárias, crédito e LGPD.",
        "lead": "Assessoria jurídica preventiva e estratégica para empresas que querem crescer com segurança.",
        "intro": [
            "Empresas de todos os portes enfrentam riscos jurídicos no dia a dia: um contrato mal redigido, uma "
            "contratação feita sem os cuidados necessários, um cliente que não paga.",
            "A Ribeiro & Flores Advocacia assessora empresas na prevenção e na solução de conflitos. Nosso foco é "
            "reduzir riscos antes que eles se transformem em prejuízo, para que você se concentre no crescimento "
            "do negócio.",
        ],
        "situations": [
            ("Contratos empresariais", "Elaboração, revisão e negociação de contratos com clientes, fornecedores e parceiros."),
            ("Consultoria trabalhista preventiva", "Contratações, jornada, rotinas de RH, desligamentos e defesa em reclamações."),
            ("Organização societária", "Constituição de empresas, contrato social, acordo de sócios e alterações."),
            ("Recuperação de crédito", "Notificações, acordos e medidas judiciais contra inadimplentes."),
            ("Proteção de dados (LGPD)", "Adequação de documentos e rotinas à Lei Geral de Proteção de Dados."),
            ("Relações de consumo", "Direitos e deveres perante o CDC e defesa em reclamações de clientes."),
        ],
        "how": [
            ("Diagnóstico", "Conhecemos a operação da empresa e identificamos os principais riscos."),
            ("Plano de ação", "Priorizamos o que precisa ser ajustado: contratos, rotinas e documentos."),
            ("Implementação", "Elaboramos os documentos e orientamos a equipe."),
            ("Acompanhamento", "Atendimento pontual ou assessoria mensal, com contato direto com os sócios."),
        ],
        "faq": [
            ("Empresa pequena precisa de assessoria jurídica?",
             "Sim. Pequenas empresas costumam ser as mais afetadas por um contrato mal feito ou por uma ação "
             "trabalhista. A prevenção custa bem menos do que resolver o problema depois."),
            ("Qual a diferença entre assessoria mensal e atendimento pontual?",
             "No atendimento pontual, cuidamos de uma demanda específica, como um contrato ou uma cobrança. Na "
             "assessoria mensal, acompanhamos a empresa de forma contínua, com orientação sempre que surgir uma dúvida."),
            ("Atendem empresas de outros estados?",
             "Sim. Todo o atendimento é online, com reuniões por vídeo e troca de documentos digital, para empresas "
             "de todo o Brasil."),
            ("Minha empresa precisa se adequar à LGPD?",
             "Toda empresa que trata dados pessoais de clientes, funcionários ou fornecedores está sujeita à LGPD. "
             "A adequação envolve revisar documentos, rotinas e a forma como os dados são coletados e guardados."),
        ],
        "cta": "Vamos conversar sobre a sua empresa?",
    },
]
AREA_BY_KEY = {a["key"]: a for a in AREAS}

# ======================================================================
# ARTIGOS
# O corpo de cada artigo fica em _build/articles/<slug>.html
# ======================================================================
ARTICLES = [
    {
        "slug": "fui-demitido-quais-sao-meus-direitos",
        "body": "demissao-direitos",
        "old": "artigo-demissao-direitos.html",
        "title": "Fui demitido. Quais são meus direitos?",
        "excerpt": "Entenda quais verbas podem ser devidas após o fim do contrato de trabalho e quais cuidados tomar nesse momento.",
        "category": "trabalhista",
        "date": "2026-09-23",
        "related": ["inss-negou-meu-beneficio-o-que-fazer", "quando-procurar-um-advogado"],
    },
    {
        "slug": "inss-negou-meu-beneficio-o-que-fazer",
        "body": "inss-negou-beneficio",
        "old": "artigo-inss-negou-beneficio.html",
        "title": "INSS negou meu benefício. O que fazer?",
        "excerpt": "Conheça os caminhos possíveis quando um benefício previdenciário é indeferido pelo INSS.",
        "category": "previdenciario",
        "date": "2026-09-23",
        "related": ["fui-demitido-quais-sao-meus-direitos", "quando-procurar-um-advogado"],
    },
    {
        "slug": "cobranca-indevida-gera-indenizacao",
        "body": "cobranca-indevida",
        "old": "artigo-cobranca-indevida.html",
        "title": "Cobrança indevida gera indenização?",
        "excerpt": "Saiba quais são os direitos do consumidor diante de cobranças abusivas, negativação irregular ou serviços inadequados.",
        "category": "consumidor",
        "date": "2026-09-23",
        "related": ["contratos-por-que-a-analise-juridica-e-importante", "quando-procurar-um-advogado"],
    },
    {
        "slug": "contratos-por-que-a-analise-juridica-e-importante",
        "body": "analise-de-contratos",
        "old": "artigo-analise-de-contratos.html",
        "title": "Contratos: por que a análise jurídica é importante?",
        "excerpt": "Entenda como uma análise preventiva pode evitar problemas futuros e proteger seus direitos.",
        "category": "civil",
        "date": "2026-09-23",
        "related": ["como-proteger-juridicamente-sua-empresa", "cobranca-indevida-gera-indenizacao"],
    },
    {
        "slug": "como-proteger-juridicamente-sua-empresa",
        "body": "protecao-juridica-empresa",
        "old": "artigo-protecao-juridica-empresa.html",
        "title": "Como proteger juridicamente sua empresa?",
        "excerpt": "A assessoria jurídica preventiva auxilia empresas na redução de riscos e na tomada de decisões mais seguras.",
        "category": "empresarial",
        "date": "2026-09-23",
        "related": ["contratos-por-que-a-analise-juridica-e-importante", "fui-demitido-quais-sao-meus-direitos"],
    },
    {
        "slug": "quando-procurar-um-advogado",
        "body": "quando-procurar-advogado",
        "old": "artigo-quando-procurar-advogado.html",
        "title": "Quando procurar um advogado?",
        "excerpt": "A orientação jurídica no momento certo pode evitar prejuízos e levar a soluções mais eficientes.",
        "category": "orientacao",
        "date": "2026-09-23",
        "related": ["contratos-por-que-a-analise-juridica-e-importante", "cobranca-indevida-gera-indenizacao"],
    },
]

# Autor padrão dos artigos (pode ser trocado por artigo com "author": "josue-ribeiro")
DEFAULT_AUTHOR = {"name": "Equipe Ribeiro & Flores", "url": "/socios/"}

CATEGORIES = {
    "trabalhista": {"label": "Direito Trabalhista", "cover": "trabalhista"},
    "previdenciario": {"label": "Direito Previdenciário", "cover": "previdenciario"},
    "consumidor": {"label": "Direito do Consumidor", "cover": "consumidor"},
    "civil": {"label": "Direito Civil", "cover": "civil"},
    "empresarial": {"label": "Direito Empresarial", "cover": "empresarial"},
    "orientacao": {"label": "Orientação Jurídica", "cover": "advocacia"},
}

for _a in ARTICLES:
    _c = CATEGORIES[_a["category"]]
    _a["category_label"] = _c["label"]
    _a["cover"] = _c["cover"]

for _ar in AREAS:
    _ar["wa"] = wa(f"Olá! Vim pela página de {_ar['name']} do site da Ribeiro & Flores e gostaria de uma análise do meu caso.")
