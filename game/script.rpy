# --- Status do Jogador ---
default theo_rating = 1200      # Necessário p/ torneios (Ex: 1500 p/ o Regional, 2200 p/ Nacional)
default theo_foco = 50         # Influencia a chance de ignorar distrações (como a xícara)
default theo_estabilidade = 50  # Menor variação de performance sob pressão
default theo_ousadia = 50       # Libera jogadas arriscadas ou táticas agressivas
default acoes_hoje = 0

# --- Relacionamentos (Pontos de Afeto) ---
default afeto_leo = 0           # Amizade com o melhor amigo/rival
default afeto_maya = 0       # Substitua pelo nome da personagem
default afeto_luisa = 0       # Substitua pelo nome da personagem

# Coloque isso no topo do seu script.rpy, fora de qualquer label
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

#Hh para Boss Figth
default theo_hp = 200
default theo_max = 200
default luisa_hp = 200
default luisa_max = 200
default enzo_max = 300
default dano_recebido = 0  
default round_atual = 1

# Placar da Boss Fight atual
default v_theo = 0
default v_rival = 0

# Mensagens 
default nova_msg_maya = False
default nova_msg_leo = False
default nova_msg_luisa = False

# Para garantir que eles não mandem a mesma mensagem várias vezes
default msg_luisa_derrotada_lida = False
default msg_enzo_derrotado_lida = False # Caso queira usar essa trava específica

# Declaração das variáveis persistentes (para não dar erro de 'not defaulted')
default persistent.enzo_vencido = False
default persistent.luisa_vencida = False
default persistent.copa_local_vencida = False
default persistent.regional_vencido = False
default persistent.aberto_cidade_vencido = False
default persistent.estadual_vencido = False
default persistent.memorial_vencido = False
default persistent.nacional_vencido = False
default persistent.seletiva_vencido = False
default persistent.candidatos_vencido = False
default persistent.mundial_vencido = False

# --- VARIÁVEIS DE PROGRESSO NA HISTÓRIA (CHAVES) ---
default hist_magnum = False
default hist_luisa = False
default hist_ala_rei = False
default hist_regional = False
default hist_aberto = False
default hist_estadual = False
default hist_memorial = False
default hist_nacional = False
default hist_seletiva = False
default hist_candidatos = False
default hist_mundial = False

# --- VARIÁVEIS DE VITÓRIA ---
default enzo_vencido = False
default luisa_vencida = False
default copa_local_vencida = False
default regional_vencido = False
default aberto_cidade_vencido = False
default estadual_vencido = False
default memorial_vencido = False
default nacional_vencido = False
default seletiva_vencido = False
default candidatos_vencido = False
default mundial_vencido = False

# Status de Jogo
default theo_ansiedade = 0
default limite_ansiedade = 6  # Valor padrão que mudará conforme a dificuldade
default dificuldade_nome = "MF" # Valor padrão (Mestre Fide)




label start:
    #show screen status_personagem
    
    # 1. Primeiro define a dificuldade (Obrigatório)
    call escolher_dificuldade
    
    # 2. Agora o salto para o início da história
    # (Descomente apenas o que for testar)
    #jump cena_derrota_clube
    #jump boss_fight_enzo
    #jump abrir_hub
    #jump teste_de_expressoes
    #jump cena_exemplo_dimensoes_personagens
    #jump encontro_amigos_pos_derrota
    #jump cena_escola_rival
    #jump flashback_infancia
    jump cena_jantar_pais
    show screen status_hud
    #jump cena_pos_vitoria_enzo

label escolher_dificuldade:
    menu:
        "Escolha sua Titulação Alvo.\n{size=-5}Isso define quantas derrotas sua mente suporta antes de desistir do xadrez.{/size}"
        
        "Candidato a Mestre (CM)":
            $ limite_ansiedade = 99
            $ dificuldade_nome = "CM"
            "{i}(Modo História: Ideal para quem quer curtir a jornada do Theo sem risco de Game Over.){/i}"

        "Mestre Fide (MF)":
            $ limite_ansiedade = 6
            $ dificuldade_nome = "MF"
            "{i}(Modo Equilibrado: O desafio padrão. Permite alguns erros nos momentos críticos.){/i}"

        "Mestre Internacional (MI)":
            $ limite_ansiedade = 4
            $ dificuldade_nome = "MI"
            "{i}(Modo Desafiador: A pressão aumenta. Cada derrota aproxima o Theo do colapso.){/i}"

        "Grande Mestre (GM)":
            $ limite_ansiedade = 2
            $ dificuldade_nome = "GM"
            "{i}(Modo Profissional: Apenas uma segunda chance. Um erro pode ser fatal para sua carreira.){/i}"

        "Super GM (SGM)":
            $ limite_ansiedade = 1
            $ dificuldade_nome = "SGM"
            "{i}(Modo Insano: Morte Súbita. Uma única derrota em Boss Fight encerra o jogo.){/i}"
            
    "Você escolheu o caminho de [dificuldade_nome]. Boa sorte, Theo."
    return

















