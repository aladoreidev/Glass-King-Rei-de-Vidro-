label cena_pesadelo_derrota:
    scene black with Dissolve(1.5)
    play sound "audio/heartbeat.ogg" # Se tiveres um som de batida de coração
    
    $ theo_ansiedade += 1
    
    "A voz do Enzo ecoa na escuridão..."
    enz "{i}Amador... Vidro... Fraco...{/i}"
    
    window hide
    with hpunch # A tela treme para simular o susto
    
    # --- CHECK DE MORTE SÚBITA (Modo SGM) ---
    if dificuldade_nome == "SGM":
        t "Eu perdi... Não foi um sonho. O vidro quebrou de vez."
        jump game_over_definitivo

    # --- CHECK DE LIMITE (Outros Modos) ---
    if theo_ansiedade >= limite_ansiedade:
        "O peso da derrota é insuportável. Minha mente atingiu o limite."
        jump game_over_definitivo

    # --- FLUXO NORMAL: ACORDAR NO QUARTO ---
    scene quartonoite with dissolve
    t "Argh! {i}(Ofegante){/i} Foi... foi só um sonho."
    t "Mas pareceu tão real. Se eu não treinar e subir o meu Rating, vou acabar derrotado no ginásio."
    
    if dificuldade_nome != "CM": # Não mostra o contador no modo fácil
        "Ansiedade acumulada: [theo_ansiedade] de [limite_ansiedade]."
    
    jump abrir_hub


    label game_over_definitivo:
        scene black with Dissolve(4.0)
        show text "{size=50}Theo desistiu do torneio e abandonou o xadrez para sempre.{/size}" at truecenter with dissolve
        pause 4.0
        return # Volta para o Menu Principal