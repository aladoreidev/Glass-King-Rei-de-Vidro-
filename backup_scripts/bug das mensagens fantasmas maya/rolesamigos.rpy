# 1. INICIALIZAÇÃO (Fora das labels)
# Garante que as variáveis existam mesmo se começarmos o jogo por aqui
default persistent.maya_chamada_hoje = False

# 2. SISTEMA DE CONVITE (Lógica de decisão)
label convidar_maya_para_role:
    # Verifica se já gastou as ações do dia (opcional, mas recomendado)
    if acoes_hoje >= 3:
        "Você está exausto demais para sair agora. Melhor descansar."
        jump abrir_hub

    if persistent.maya_chamada_hoje:
        "Você já mandou mensagem para Maya hoje. Melhor não parecer desesperado."
        jump abrir_hub

    $ persistent.maya_chamada_hoje = True
    $ acoes_hoje += 1 

    # Início da cena de ligação
    "Você pega o celular e liga para a Maya."
    
    # Se você tiver um fundo de 'quarto' ou 'rua', use aqui
    # scene bg_quarto with fade 

    ma "Alô? Theo? Aconteceu alguma coisa no clube?"
    t "Não, não. Só queria saber se você topa fazer algo... relaxar um pouco."

    # TESTE DE STATUS: Ela só sai se você tiver o mínimo de Estabilidade
    if theo_estabilidade >= 60:
        ma "Um rolê? Claro! Eu adoraria sair da frente desses livros. Onde nos encontramos?"
        t "Pode ser naquele café perto da praça?"
        ma "Combinado! Chego em 10 minutos."
        
        # O 'call' faz o jogo ir para a cena e VOLTAR para cá quando terminar
        call cena_role_maya 
    else:
        ma "Ah, Theo... Hoje eu realmente preciso terminar esse relatório. Quem sabe no final de semana?"
        t "Entendo. Sem problemas, a gente se fala depois."
        "Você sente que precisava de um pouco mais de presença para convencê-la."

    jump abrir_hub

# 3. A CENA DO ROLÊ (Diálogos e Recompensas)
label cena_role_maya:
    # Mudança de cenário
    scene clube_xadrez_exterior 
    with fade 

    show maya sorrindo at left
    show theo padrao at right

    "O ambiente do café é relaxante, bem diferente da tensão silenciosa do clube de xadrez."
    
    ma "Estou tão feliz que você me chamou! Às vezes você fica tão focado no xadrez que esquece que existe sol lá fora."
    t "Eu sei... às vezes eu me perco um pouco nos cálculos."

    menu:
        "Fazer um elogio sincero":
            t "Você é uma ótima amiga, Maya. Sua companhia sempre me ajuda a colocar os pés no chão."
            show maya envergonhada # Se tiver esse sprite
            ma "Aw, Theo... assim você me deixa sem jeito. Mas obrigada, eu sinto o mesmo."
            $ theo_estabilidade += 5
            "Sua Estabilidade aumentou significativamente!"

        "Falar sobre a última partida":
            t "Ainda estou pensando no que o Enzo fez. Aquela estrutura de peões foi bizarra."
            show maya seria
            ma "Theo! Regra número um do nosso rolê: nada de falar de peões, bispos ou cavalos por uma hora!"
            t "Desculpa, força do hábito."
            $ theo_estabilidade += 1
            "Você relaxou um pouco, mas sua mente ainda está no tabuleiro."

    ma "Foi ótimo passar esse tempo com você, Theo. Me sinto renovada!"
    t "Eu também, Maya. Obrigado por vir."

    hide maya
    hide theo
    with dissolve
    
    # IMPORTANTE: O return faz o jogo voltar para a label 'convidar_maya_para_role'
    # que por sua vez dará o jump para o hub.
    return 

# 4. ROTA ALTERNATIVA (Caso você queira ir direto para a praça sem ligar)
label role_com_maya_direto:
    $ acoes_hoje += 1 
    scene bg_pr