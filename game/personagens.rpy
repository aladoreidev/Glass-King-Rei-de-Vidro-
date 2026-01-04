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

# Transforms (O Ren'Py precisa ler isso antes de usar)
transform modo_full:
    yalign 1.0
    zoom 1.0
    yoffset 0

transform modo_busto:
    yalign 1.0
    zoom 1.6
    yoffset 550

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
