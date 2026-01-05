init:
    python:
        import math

        def shake_dist(trans, st, at, dist=10):
            trans.xoffset = int(math.sin(st * 30) * dist)
            trans.yoffset = int(math.cos(st * 30) * dist)
            if st < 0.2: # Duração do tremor
                return 0
            else:
                trans.xoffset = 0
                trans.yoffset = 0
                return None

    transform shake:
        function renpy.curry(shake_dist)(dist=10)

# =========================================================
# 1. DEFINIÇÕES (Sempre no topo, fora de labels)
# =========================================================

# Personagens
# Personagens com vínculo de imagem
define t = Character("Theo", color="#3b0fea", image="theo")
define l = Character("Léo", color="#12ef6e", image="leo")   
define ma = Character("Maya", color="#e91e63", image="maya") 
define lu = Character("Luisa", color="#e4e126", image="luisa") 
define m = Character("Macedo", color="#7f8c8d", image="macedo") 
define ph = Character("Dr Henrique", color="#7f8c8d", image="dr_henrique") 
define enz = Character("Enzo", color="#e74c3c", image="enzo")
define mae = Character("Dra karolina", color="#ed2913", image="dra_karolina")
define v = Character("Vico", color="#043d23", image="vico")



# Para sprites de 2400x3600px


transform modo_full:
    yalign 1.0
    zoom 0.5
    yoffset 0

transform modo_busto:
    yalign 1.0     # Alinha a base da imagem no fundo da tela
    zoom 0.75   # Diminuí bastante o zoom para o rosto entrar na tela
    yoffset 0      # Resetamos o offset para ver onde a cabeça para


transform side_look:
    # 1. Ajuste do tamanho
    zoom 0.35       # Aumentamos de 0.12 para 0.35 (quase o triplo do tamanho anterior)
    
    # 2. Ajuste do enquadramento (pegar a cabeça)
    # Como a imagem original tem 3600px, o rosto está lá no topo.
    yanchor 0.1     # Fixa o "ponto de ancoragem" perto do topo da imagem
    ypos 0.1        # Posiciona esse ponto no topo da área da side image
    
    # 3. Ajuste de posição na tela
    xalign 0.0      # Gruda na esquerda
    yalign 1.0      # Gruda no fundo (alinhado com a caixa de texto)
    
    # 4. Ajuste fino (se precisar afastar ou subir)
    xoffset 10      # Empurra um pouquinho para a direita para não cortar no canto
    yoffset 60    # Sobe um pouquinho se estiver atrás do texto


transform side_look_small:
    zoom 0.25        # Ajusta o 600px para caber no canto
    xalign 0.0        # Fixa na esquerda
    yalign 1.0        # Fixa na base
    xoffset 20        # Afasta um pouco da borda
    yoffset 0











# 2. Declare as Side Images usando 'At' em vez de LayeredImageProxy
# O modelo é: image side [tag] [expressão] = At("nome_do_arquivo", side_look)





image theo = "theo normal"
image leo = "leo normal"
image maya = "maya normal"
image luisa = "luisa normal"
image enzo = "enzo normal"



# =========================================================
# SIDE IMAGES - SKINS ESCOLARES
# =========================================================


# Dr. Henrique (Usando o transform para imagens menores)
image side dr_henrique arrogante = At("dr_henrique arrogante", side_look_small)
image side dr_henrique pensativo = At("dr_henrique pensativo", side_look_small)
image side dr_henrique triste = At("dr_henrique triste", side_look_small)
image side dr_henrique raiva = At("dr_henrique raiva", side_look_small)

# Side Images da Dra. Karolina
image side dra_karolina normal = At("dra_karolina normal", side_look_small)
image side dra_karolina feliz = At("dra_karolina feliz", side_look_small)
image side dra_karolina triste = At("dra_karolina triste", side_look_small)
image side dra_karolina raiva = At("dra_karolina raiva", side_look_small)

# --- THEO ---
image side theo normal = At("theo normal", side_look)
image side theo triste = At("theo triste", side_look)
image side theo raiva = At("theo raiva", side_look)
# Versões Escolares
image side theo escolar normal = At("theo escolar normal", side_look)
image side theo escolar triste = At("theo escolar triste", side_look)
image side theo escolar raiva = At("theo escolar raiva", side_look)

# --- LÉO ---
image side leo normal = At("leo normal", side_look)
image side leo triste = At("leo triste", side_look)
image side leo raiva = At("leo raiva", side_look)
# Versões Escolares
image side leo escolar normal = At("leo escolar normal", side_look)
image side leo escolar triste = At("leo escolar triste", side_look)
image side leo escolar raiva = At("leo escolar raiva", side_look)

# --- LUÍSA ---
image side luisa normal = At("luisa normal", side_look)
image side luisa triste = At("luisa triste", side_look)
image side luisa raiva = At("luisa raiva", side_look)
# Versões Escolares
image side luisa escolar normal = At("luisa escolar normal", side_look)
image side luisa escolar triste = At("luisa escolar triste", side_look)
image side luisa escolar raiva = At("luisa escolar raiva", side_look)

# --- MAYA ---
image side maya normal = At("maya normal", side_look)
image side maya triste = At("maya triste", side_look)
image side maya raiva = At("maya raiva", side_look)
# Versões Escolares (Se ela tiver)
image side maya escolar normal = At("maya escolar normal", side_look)



# enzo
image side enzo normal = At("enzo normal", side_look)
image side enzo feliz = At("enzo feliz", side_look)
image side enzo arrogante = At("enzo arrogante", side_look)
image side enzo raiva = At("enzo raiva", side_look)
image side enzo esnobe = At("enzo esnobe", side_look)



# THEO
image side theo = At(SideImage(), side_look)

# LÉO
image side leo = At(SideImage(), side_look)

# MAYA
image side maya = At(SideImage(), side_look)

# LUÍSA
image side luisa = At(SideImage(), side_look)

# ENZO
image side enzo = At(SideImage(), side_look)











# =========================================================
# 2. LABEL DE TESTE (Vem depois das definições)
# =========================================================

label cena_exemplo_dimensoes_personagens:
    scene black
    
    "--- TESTE 1: BUSTO (1.6) E EXPRESSÕES ---"

    # Posição Normal
    show leo normal at modo_busto:
        xalign 0.0
    show theo normal at modo_busto:
        xalign 0.25
    show enzo normal at modo_busto:
        xalign 0.5
    show maya normal at modo_busto:
        xalign 0.75
    show luisa normal at modo_busto:
        xalign 1.0

    "Todos em posição 'Normal'. Veja se o Enzo está alinhado."

    # Teste de Expressão: Feliz / Esnobe
    show leo feliz at modo_busto
    show theo feliz at modo_busto
    show enzo esnobe at modo_busto
    show maya feliz at modo_busto
    show luisa feliz at modo_busto
    
    enz "Hmph... nada mal para amadores."

    # Teste de Expressão: Raiva / Arrogante
    show leo raiva at modo_busto
    show theo raiva at modo_busto
    show enzo arrogante at modo_busto
    show maya raiva at modo_busto
    show luisa raiva at modo_busto

    enz "Mas ainda estão anos-luz de me vencer."

    # Teste de Expressão: Triste / Raiva (Enzo)
    show leo triste at modo_busto
    show theo triste at modo_busto
    show enzo raiva at modo_busto
    show maya triste at modo_busto
    show luisa triste at modo_busto

    "Fim do teste de busto."
    
    pause
    return



