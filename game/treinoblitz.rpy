label hub_laptop_blitz:
    # Verificação de limite de atividades (2 por dia)
    if acoes_hoje >= 2:
        window show
        t "Minha visão está até meio embaçada de tanto olhar para esse tabuleiro..."
        t "Se eu tentar jogar um Blitz agora, vou perder rating por puro cansaço. Melhor fechar o laptop."
        window hide
        jump abrir_hub

    # Verificação de Foco (Blitz geralmente cansa bastante)
    if theo_foco < 30:
        window show
        t "Não tenho foco suficiente para uma partida rápida. Vou acabar pendurando uma peça."
        window hide
        jump abrir_hub

    # --- LÓGICA DA PARTIDA BLITZ COMEÇA AQUI ---
    t "Vou abrir o site e jogar uma partida rápida para treinar meus reflexos."
    
    # (Espaço para sua futura implementação de Blitz)
    
    # Finalização da Atividade
    $ acoes_hoje += 1
    $ theo_foco -= 25
    t "Partida finalizada. Isso realmente consome muita energia mental."
    
    jump abrir_hub