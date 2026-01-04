# -------------------------------------------------------------------------
# 1. LÓGICA DO JOGO EM PYTHON
# -------------------------------------------------------------------------
init python:
    import random

    class JogoMemoriaXadrez(object):
        def __init__(self, dificuldade=3, tempo_base=3.0, bonus_foco=0.0, estabilidade_atual=0): 
            self.elementos = [
                "relogio", "tabuleiro", "sumula", "livro", "pc", 
                "rei", "dama", "peao", "bispo", "torre", "cavalo", "trofeu"
            ]
            self.sequencia = [random.choice(self.elementos) for _ in range(dificuldade)]
            self.cliques_jogador = []
            self.decorando = True 
            self.resultado = None 
            # O tempo de visualização e reflexão escala com o Foco do Theo
            self.tempo_visualizacao = tempo_base + (bonus_foco / 20.0)
            self.tempo_reflexao_max = 20.0 + (bonus_foco / 20.0)
            self.tempo_reflexao = self.tempo_reflexao_max
            # Se a estabilidade for alta, o jogador tem 1 chance de errar
            self.chances = 1 if estabilidade_atual > 40 else 0
            self.teve_misericordia = False 

        def registrar_clique(self, item):
            if self.decorando or self.resultado:
                return
            self.cliques_jogador.append(item)
            passo = len(self.cliques_jogador) - 1
            
            if self.cliques_jogador[passo] != self.sequencia[passo]:
                if self.chances > 0:
                    self.chances -= 1
                    self.cliques_jogador = [] 
                    self.teve_misericordia = True
                else:
                    self.resultado = "ERRO"
            elif len(self.cliques_jogador) == len(self.sequencia):
                self.resultado = "VITORIA"

# -------------------------------------------------------------------------
# 2. INTERFACE (SCREEN)
# -------------------------------------------------------------------------
screen memoria_xadrez(jogo, rodada_atual, p_theo, p_macedo):
    modal True
    add "clubexadrez" at truecenter 
    add Solid("#3d230388") 

    frame:
        align (0.5, 0.5)
        xsize 1300 ysize 940 
        background Solid("#000c") 

    # PLACAR DO DUELO
    hbox:
        align (0.5, 0.05)
        spacing 100
        text "THEO [p_theo]" color "#0f0" size 30 outlines [(2, "#000")]
        text "RODADA [rodada_atual]/5" color "#fff" size 25 outlines [(1, "#000")]
        text "MACEDO [p_macedo]" color "#f00" size 30 outlines [(2, "#000")]

    vbox:
        align (0.5, 0.2)
        spacing 10 
        
        if jogo.decorando:
            timer 0.05 repeat True action If(jogo.tempo_visualizacao > 0, SetField(jogo, "tempo_visualizacao", jogo.tempo_visualizacao - 0.05), SetField(jogo, "decorando", False))
            text "MEMORIZE A SEQUÊNCIA..." xalign 0.5 size 40 color "#d4af37"
            bar value jogo.tempo_visualizacao range (3.0 + (theo_foco / 20.0)):
                xalign 0.5 xsize 500 ysize 15
        
        elif jogo.resultado == "VITORIA":
            text "RODADA CONCLUÍDA!" xalign 0.5 size 50 color "#0f0"
        elif jogo.resultado == "ERRO":
            text "VOCÊ FALHOU NESTA RODADA!" xalign 0.5 size 50 color "#f00"
        else:
            timer 0.1 repeat True action If(jogo.tempo_reflexao > 0, SetField(jogo, "tempo_reflexao", jogo.tempo_reflexao - 0.1), Return("ERRO"))
            text "RECONSTRUA A JOGADA!" xalign 0.5 size 40 color "#fff"
            bar value jogo.tempo_reflexao range jogo.tempo_reflexao_max:
                xalign 0.5 xsize 500 ysize 15

    # EXIBIÇÃO DAS PEÇAS (SEQUÊNCIA)
    hbox:
        align (0.5, 0.45)
        spacing 25
        for idx, item in enumerate(jogo.sequencia):
            if jogo.decorando or idx < len(jogo.cliques_jogador):
                add "mem_" + item zoom 0.6
            else:
                frame:
                    xsize 120 ysize 120
                    background Solid("#333")
                    text "?" align (0.5, 0.5)

    # BOTÕES DE RESPOSTA
    if not jogo.decorando:
        if jogo.resultado:
            textbutton "CONTINUAR":
                align (0.5, 0.88)
                text_size 45
                action Return(jogo.resultado)
        else:
            grid 6 2:
                align (0.5, 0.92) # <--- Aqui estava o xalign errado, agora é align
                spacing 20
                for b in jogo.elementos:
                    imagebutton:
                        idle Transform("mem_" + b, zoom=0.42)
                        hover Transform("mem_" + b + "_hover", zoom=0.42)
                        action Function(jogo.registrar_clique, b)

# -------------------------------------------------------------------------
# 3. CENA DE DIÁLOGO E INTRODUÇÃO
# -------------------------------------------------------------------------
label cena_torneio_ala_do_rei:
    scene clubexadrez with fade
    play music "audio/tensao_torneio.mp3" fadein 2.0

    "O ar no Clube Ala do Rei estava pesado. O som de relógios sendo batidos e o sussurro dos espectadores preenchiam o salão."
    "Este não era um jogo qualquer. Era o Torneio Anual, e o destino me colocou frente a frente com o meu rival."

    show macedo_serio at right with moveinright
    m "Olha só quem resolveu aparecer... O garoto que nem sabia proteger o Rei na abertura."
    
    show theo_focado at left with moveinleft
    t "As coisas mudaram, Macedo. Eu não sou mais aquele iniciante de meses atrás."

    m "Palavras bonitas. Mas xadrez se joga com a mente, não com a boca. Vamos ver se sua Estabilidade aguenta a pressão."

    if theo_foco > 50:
        "Sinto minha mente afiada. O treinamento intenso está valendo a pena."
    else:
        "Meu coração está acelerado... Preciso manter a calma."

    window hide
    pause 1.0
    jump boss_fight_macedo

# -------------------------------------------------------------------------
# 4. LÓGICA DO DUELO (MELHOR DE 5)
# -------------------------------------------------------------------------
label boss_fight_macedo:
    $ v_theo = 0
    $ v_macedo = 0
    
    # Executa as 5 rodadas chamando o "operário" abaixo
    call rodada_xadrez(3, 1)
    call rodada_xadrez(4, 2)
    call rodada_xadrez(4, 3)
    call rodada_xadrez(5, 4)
    call rodada_xadrez(6, 5)

    # Cálculo dos resultados e recompensas
    if v_theo >= 3:
        "FINAL: Theo [v_theo] x [v_macedo] Macedo. Você venceu!"
        
        if v_theo == 5:
            "{color=#d4af37}{b}PERFORMANCE PERFEITA!{/b}{/color}"
            "Macedo está em choque. Você não cometeu um único erro!"
            $ theo_rating += 250
            $ theo_foco += 30
            "Recompensa: +250 Rating / +30 Foco."
        else:
            $ theo_rating += 150
            $ theo_foco += 20
            "Recompensa: +150 Rating / +20 Foco."
            
        $ persistent.copa_local_vencida = True
    else:
        "FINAL: Theo [v_theo] x [v_macedo] Macedo. Você perdeu."
        $ theo_rating -= 50
        $ theo_estabilidade -= 20
        "Penalidade: -50 Rating / -20 Estabilidade."

    "Status Atual: Rating [theo_rating] | Foco [theo_foco] | Estabilidade [theo_estabilidade]"
    
    jump abrir_hub

# -------------------------------------------------------------------------
# 5. LABEL DE SUPORTE (RODADA INDIVIDUAL)
# -------------------------------------------------------------------------
label rodada_xadrez(diff, num):
    # Isso impede o jogador de usar a roda do mouse/tecla de voltar
    $ renpy.block_rollback() 

    $ jogo_boss = JogoMemoriaXadrez(dificuldade=diff, bonus_foco=theo_foco, estabilidade_atual=theo_estabilidade)
    call screen memoria_xadrez(jogo_boss, num, v_theo, v_macedo)
    
    if _return == "VITORIA":
        $ v_theo += 1
    else:
        $ v_macedo += 1
    
    # Bloqueia novamente para garantir que ele não volte após ver o resultado
    $ renpy.block_rollback() 
    return