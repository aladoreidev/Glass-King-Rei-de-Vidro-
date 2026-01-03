# # 1. LÓGICA DO JOGO (PYTHON)
# # -------------------------------------------------------------------------
# init python:
#     import random

#     class JogoMemoriaXadrez(object):
#         def __init__(self, dificuldade=3): 
#             self.elementos = ["peao", "tabuleiro", "relogio", "sumula"]
#             self.sequencia = [random.choice(self.elementos) for _ in range(dificuldade)]
#             self.cliques_jogador = []
#             self.decorando = True 
#             self.resultado = None 

#         def registrar_clique(self, item):
#             if self.decorando or self.resultado:
#                 return
#             self.cliques_jogador.append(item)
#             passo = len(self.cliques_jogador) - 1
#             if self.cliques_jogador[passo] != self.sequencia[passo]:
#                 self.resultado = "ERRO"
#             elif len(self.cliques_jogador) == len(self.sequencia):
#                 self.resultado = "VITORIA"

# # 2. INTERFACE (SCREEN) - SEM ERROS DE DYNAMIC IMAGE
# # -------------------------------------------------------------------------
# screen memoria_xadrez(jogo):
#     modal True
#     add Solid("#000e") 

#     # Feedback de Texto
#     if jogo.decorando:
#         timer 3.0 action SetField(jogo, "decorando", False)
#         text "MEMORIZE A SEQUÊNCIA..." align (0.5, 0.2) size 45 color "#d4af37"
#     elif jogo.resultado == "VITORIA":
#         text "{b}PARABÉNS! VOCÊ GANHOU!{/b}" align (0.5, 0.2) size 60 color "#0f0"
#     elif jogo.resultado == "ERRO":
#         text "{b}VOCÊ ERROU!{/b}" align (0.5, 0.2) size 60 color "#f00"
#     else:
#         text "RECONSTRUA A JOGADA!" align (0.5, 0.2) size 45 color "#ffffff"

#     # Peças no Centro
#     hbox:
#         align (0.5, 0.45)
#         spacing 25
#         for idx, item in enumerate(jogo.sequencia):
#             if jogo.decorando:
#                 add "mem_" + item zoom 0.6
#             else:
#                 if idx < len(jogo.cliques_jogador):
#                     add "mem_" + item zoom 0.6
#                 else:
#                     frame:
#                         xsize 120 ysize 120
#                         background Solid("#333")
#                         text "?" align (0.5, 0.5)

#     # Botões de Clique
#     if not jogo.decorando:
#         if jogo.resultado:
#             # BOTÃO DE SAÍDA QUE VOCÊ QUERIA
#             textbutton "CLIQUE PARA VOLTAR AO HUB":
#                 align (0.5, 0.85)
#                 text_size 40
#                 action Return(jogo.resultado)
#         else:
#             hbox:
#                 align (0.5, 0.8)
#                 spacing 50
#                 for b in jogo.elementos:
#                     # Forma mais simples de evitar o NameError
#                     $ img = "mem_" + b
#                     imagebutton:
#                         idle img
#                         action Function(jogo.registrar_clique, b)

# # 3. LABEL DA LUTA (MANDANDO PRO HUB)
# # -------------------------------------------------------------------------
# label boss_fight_xadrez:
#     $ jogo_boss = JogoMemoriaXadrez(dificuldade=3)
    
#     "Theo respira fundo. É agora ou nunca."

#     call screen memoria_xadrez(jogo_boss)
    
#     $ res = _return

#     if res == "VITORIA":
#         "Você acertou tudo!"
#     else:
#         "Você falhou na sequência."

#     # COMANDO PARA IR PARA O HUB
#     jump abrir_hub


# 1. LÓGICA DO JOGO (PYTHON)
# -------------------------------------------------------------------------
init python:
    import random

    class JogoMemoriaXadrez(object):
        def __init__(self, dificuldade=3, tempo_base=3.0, bonus_foco=0.0): 
            self.elementos = ["peao", "tabuleiro", "relogio", "sumula"]
            self.sequencia = [random.choice(self.elementos) for _ in range(dificuldade)]
            self.cliques_jogador = []
            self.decorando = True 
            self.resultado = None 
            
            # DICA: O tempo total é o tempo base + (foco do Theo / 20)
            # Ex: Se Theo tem 40 de foco, ganha +2 segundos.
            self.tempo_visualizacao = tempo_base + (bonus_foco / 20.0)

        def registrar_clique(self, item):
            if self.decorando or self.resultado:
                return
            self.cliques_jogador.append(item)
            passo = len(self.cliques_jogador) - 1
            if self.cliques_jogador[passo] != self.sequencia[passo]:
                self.resultado = "ERRO"
            elif len(self.cliques_jogador) == len(self.sequencia):
                self.resultado = "VITORIA"

# 2. INTERFACE (SCREEN)
# -------------------------------------------------------------------------
screen memoria_xadrez(jogo):
    modal True
    add Solid("#000e") 

    if jogo.decorando:
        # Usa o tempo calculado com base no Foco do Theo
        timer jogo.tempo_visualizacao action SetField(jogo, "decorando", False)
        
        vbox:
            align (0.5, 0.2)
            text "MEMORIZE A SEQUÊNCIA..." xalign 0.5 size 45 color "#d4af37"
            text "Bônus de Foco: + [jogo.tempo_visualizacao - 3.0:.1f]s" xalign 0.5 size 18 color "#0f0"
    
    elif jogo.resultado == "VITORIA":
        text "{b}RODADA CONCLUÍDA!{/b}" align (0.5, 0.2) size 60 color "#0f0"
    elif jogo.resultado == "ERRO":
        text "{b}VOCÊ ERROU ESTA RODADA!{/b}" align (0.5, 0.2) size 60 color "#f00"
    else:
        text "RECONSTRUA A JOGADA!" align (0.5, 0.2) size 45 color "#ffffff"

    # Peças
    hbox:
        align (0.5, 0.45)
        spacing 25
        for idx, item in enumerate(jogo.sequencia):
            if jogo.decorando:
                add "mem_" + item zoom 0.6
            else:
                if idx < len(jogo.cliques_jogador):
                    add "mem_" + item zoom 0.6
                else:
                    frame:
                        xsize 120 ysize 120
                        background Solid("#333")
                        text "?" align (0.5, 0.5)

#     if not jogo.decorando:
#         if jogo.resultado:
#             textbutton "PRÓXIMO PASSO":
#                 align (0.5, 0.85)
#                 text_size 40
#                 action Return(jogo.resultado)
#         else:
#             hbox:
#                 align (0.5, 0.8)
#                 spacing 50
#                 for b in jogo.elementos:
#                     $ img = "mem_" + b
#                     imagebutton:
#                         idle img
#                         action Function(jogo.registrar_clique, b)

# # 3. LABEL DA LUTA (SISTEMA DE 3 RODADAS)
# # -------------------------------------------------------------------------
# label boss_fight_xadrez:
#     $ vitorias_theo = 0
    
#     # RODADA 1
#     t "Primeiro movimento... Enzo está calado."
#     $ jogo_boss = JogoMemoriaXadrez(dificuldade=3, bonus_foco=theo_foco)
#     call screen memoria_xadrez(jogo_boss)
#     if _return == "VITORIA":
#         $ vitorias_theo += 1
#         "Você acertou a primeira!"
#     else:
#         "Você errou a primeira... Enzo sorri."

#     # RODADA 2
#     t "O jogo está ficando complexo. Preciso enxergar além."
#     $ jogo_boss = JogoMemoriaXadrez(dificuldade=4, bonus_foco=theo_foco)
#     call screen memoria_xadrez(jogo_boss)
#     if _return == "VITORIA":
#         $ vitorias_theo += 1
#         "Segunda rodada concluída com sucesso!"
#     else:
#         "Sua mente deu um nó. Erro na segunda rodada."

#     # RODADA 3
#     t "Final da partida. Agora é tudo ou nada."
#     $ jogo_boss = JogoMemoriaXadrez(dificuldade=5, bonus_foco=theo_foco)
#     call screen memoria_xadrez(jogo_boss)
#     if _return == "VITORIA":
#         $ vitorias_theo += 1
#         "Xeque-mate! Você dominou a sequência final."

#     # RESULTADO FINAL PARA O HUB
#     if vitorias_theo >= 2:
#         "Você venceu o duelo de mentes contra Enzo!"
#         $ theo_foco += 30
#     else:
#         "Enzo venceu esta partida. Você sai do ginásio humilhado."
#         $ theo_estabilidade -= 20

#     jump abrir_hub



# 1. LÓGICA DO JOGO (PYTHON)
# -------------------------------------------------------------------------
# init python:
#     import random

#     class JogoMemoriaXadrez(object):
#         def __init__(self, dificuldade=3, tempo_base=3.0, bonus_foco=0.0, estabilidade_atual=0): 
#             self.elementos = ["peao", "tabuleiro", "relogio", "sumula"]
#             self.sequencia = [random.choice(self.elementos) for _ in range(dificuldade)]
#             self.cliques_jogador = []
#             self.decorando = True 
#             self.resultado = None 
            
#             # CÁLCULO DO FOCO: Cada 20 pontos de foco dão +1 segundo
#             self.tempo_visualizacao = tempo_base + (bonus_foco / 20.0)
            
#             # CÁLCULO DA ESTABILIDADE: Se > 50, ganha 1 chance de errar
#             self.chances = 1 if estabilidade_atual > 50 else 0
#             self.mensagem_erro = ""

#         def registrar_clique(self, item):
#             if self.decorando or self.resultado:
#                 return

#             self.cliques_jogador.append(item)
#             passo = len(self.cliques_jogador) - 1
            
#             # Se o jogador errar o clique
#             if self.cliques_jogador[passo] != self.sequencia[passo]:
#                 if self.chances > 0:
#                     # Gasta a chance de Estabilidade
#                     self.chances -= 1
#                     self.cliques_jogador = [] # Reseta os cliques atuais
#                     self.mensagem_erro = "ESTABILIDADE: Você recuperou o foco! Tente a sequência de novo."
#                 else:
#                     self.resultado = "ERRO"
            
#             # Se acertar tudo
#             elif len(self.cliques_jogador) == len(self.sequencia):
#                 self.resultado = "VITORIA"

# # 2. INTERFACE (SCREEN)
# # -------------------------------------------------------------------------
# screen memoria_xadrez(jogo):
#     modal True
#     add Solid("#000e") 

#     # Parte Superior: Instruções e Bónus
#     vbox:
#         align (0.5, 0.15)
#         spacing 10
#         if jogo.decorando:
#             timer jogo.tempo_visualizacao action SetField(jogo, "decorando", False)
#             text "MEMORIZE A SEQUÊNCIA..." xalign 0.5 size 40 color "#d4af37"
#             text "Bônus de Foco: +[jogo.tempo_visualizacao - 3.0:.1f]s" xalign 0.5 size 18 color "#0f0"
#         elif jogo.resultado == "VITORIA":
#             text "RODADA CONCLUÍDA!" xalign 0.5 size 50 color "#0f0"
#         elif jogo.resultado == "ERRO":
#             text "VOCÊ FALHOU NESTA RODADA!" xalign 0.5 size 50 color "#f00"
#         else:
#             text "RECONSTRUA A JOGADA!" xalign 0.5 size 40 color "#fff"
#             if jogo.mensagem_erro:
#                 text "[jogo.mensagem_erro]" xalign 0.5 size 20 color "#3498db" italic True

#     # Peças no Centro
#     hbox:
#         align (0.5, 0.45)
#         spacing 25
#         for idx, item in enumerate(jogo.sequencia):
#             if jogo.decorando:
#                 add "mem_" + item zoom 0.6
#             else:
#                 if idx < len(jogo.cliques_jogador):
#                     add "mem_" + item zoom 0.6
#                 else:
#                     frame:
#                         xsize 120 ysize 120
#                         background Solid("#333")
#                         text "?" align (0.5, 0.5)

#     # Botões de baixo
#     if not jogo.decorando:
#         if jogo.resultado:
#             textbutton "CONTINUAR":
#                 align (0.5, 0.85)
#                 text_size 45
#                 action Return(jogo.resultado)
#         else:
#             hbox:
#                 align (0.5, 0.8)
#                 spacing 50
#                 for b in jogo.elementos:
#                     $ img = "mem_" + b
#                     imagebutton:
#                         idle img
#                         action Function(jogo.registrar_clique, b)

# # 3. LABEL DA LUTA (3 RODADAS) - CORRIGIDO
# # -------------------------------------------------------------------------
# label boss_fight_xadrez:
#     $ vitorias_theo = 0
    
#     # Rodada 1
#     "Enzo move o peão. A pressão começa."
#     $ jogo_boss = JogoMemoriaXadrez(dificuldade=3, bonus_foco=theo_foco, estabilidade_atual=theo_estabilidade)
#     call screen memoria_xadrez(jogo_boss)
    
#     if _return == "VITORIA": 
#         $ vitorias_theo += 1

#     # Rodada 2
#     "O tabuleiro parece maior. Enzo sorri com desdém."
#     $ jogo_boss = JogoMemoriaXadrez(dificuldade=4, bonus_foco=theo_foco, estabilidade_atual=theo_estabilidade)
#     call screen memoria_xadrez(jogo_boss)
    
#     if _return == "VITORIA": 
#         $ vitorias_theo += 1

#     # Rodada 3
#     "É o xeque-mate ou a derrota total."
#     $ jogo_boss = JogoMemoriaXadrez(dificuldade=5, bonus_foco=theo_foco, estabilidade_atual=theo_estabilidade)
#     call screen memoria_xadrez(jogo_boss)
    
#     if _return == "VITORIA": 
#         $ vitorias_theo += 1

#     # Resultado Final
#     if vitorias_theo >= 2:
#         "Vitória! Enzo não consegue acreditar que você manteve o ritmo."
#         $ theo_foco += 15
#     else:
#         "O Enzo dominou você. Sua mente cedeu sob a pressão."
#         $ theo_estabilidade -= 15

#     jump abrir_hub


# 1. LÓGICA DO JOGO (PYTHON)
# -------------------------------------------------------------------------
init python:
    import random

    class JogoMemoriaXadrez(object):
        def __init__(self, dificuldade=3, tempo_base=3.0, bonus_foco=0.0, estabilidade_atual=0): 
            self.elementos = ["relogio", "tabuleiro", "sumula", "livro", "pc", 
        "rei", "dama", "peao", "bispo", "torre", "cavalo","trofeu"]
            self.sequencia = [random.choice(self.elementos) for _ in range(dificuldade)]
            self.cliques_jogador = []
            self.decorando = True 
            self.resultado = None 
            
            # CÁLCULO DO FOCO: Cada 20 pontos dão +1 segundo
            self.tempo_visualizacao = tempo_base + (bonus_foco / 20.0)
            
            # TESTE: Segunda chance agora ativa com ESTABILIDADE acima de 40
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
                    self.cliques_jogador = [] # Reseta cliques
                    self.teve_misericordia = True # Ativa aviso na tela
                else:
                    self.resultado = "ERRO"
            
            elif len(self.cliques_jogador) == len(self.sequencia):
                self.resultado = "VITORIA"

# 2. INTERFACE (SCREEN) COM PLACAR
# -------------------------------------------------------------------------
# 2. INTERFACE (SCREEN) ATUALIZADA COM GRADE PARA 11 IMAGENS
# -------------------------------------------------------------------------
# 2. INTERFACE (SCREEN) - CORREÇÃO DEFINITIVA DO ZOOM
# -------------------------------------------------------------------------
screen memoria_xadrez(jogo, rodada_atual, v_theo, v_enzo):
    modal True
    add Solid("#000e") 

    # PLACAR NO TOPO
    hbox:
        align (0.5, 0.05)
        spacing 100
        text "THEO [v_theo]" color "#0f0" size 30
        text "RODADA [rodada_atual]/3" color "#fff" size 25
        text "ENZO [v_enzo]" color "#f00" size 30

    vbox:
        align (0.5, 0.2)
        spacing 10
        if jogo.decorando:
            timer jogo.tempo_visualizacao action SetField(jogo, "decorando", False)
            text "MEMORIZE A SEQUÊNCIA..." xalign 0.5 size 40 color "#d4af37"
            text "Bônus de Foco: +[jogo.tempo_visualizacao - 3.0:.1f]s" xalign 0.5 size 18 color "#0f0"
        elif jogo.resultado == "VITORIA":
            text "RODADA CONCLUÍDA!" xalign 0.5 size 50 color "#0f0"
        elif jogo.resultado == "ERRO":
            text "VOCÊ FALHOU NESTA RODADA!" xalign 0.5 size 50 color "#f00"
        else:
            text "RECONSTRUA A JOGADA!" xalign 0.5 size 40 color "#fff"
            if jogo.teve_misericordia:
                text "ESTABILIDADE: Você recuperou o foco! Tente de novo." xalign 0.5 size 20 color "#3498db" italic True

    # EXIBIÇÃO DAS PEÇAS (SEQUÊNCIA CENTRAL)
    hbox:
        align (0.5, 0.45)
        spacing 25
        for idx, item in enumerate(jogo.sequencia):
            if jogo.decorando:
                add "mem_" + item zoom 0.6
            else:
                if idx < len(jogo.cliques_jogador):
                    add "mem_" + item zoom 0.6
                else:
                    frame:
                        xsize 120 ysize 120
                        background Solid("#333")
                        text "?" align (0.5, 0.5)

    # BOTÕES DE RESPOSTA (GRADE PARA AS 11 IMAGENS)
    if not jogo.decorando:
        if jogo.resultado:
            textbutton "CONTINUAR":
                align (0.5, 0.85)
                text_size 45
                action Return(jogo.resultado)
        else:
            # Grade Perfeita: 6 colunas e 2 linhas para 12 imagens
            grid 6 2:
                xalign 0.5          # Centraliza o bloco todo na largura da tela
                yalign 0.9          # Posiciona o bloco na parte inferior
                spacing 15          # Espaço entre as peças (reduzi um pouco para caber melhor)
                
                for b in jogo.elementos:
                    imagebutton:
                        align (0.5, 0.5)
                        idle Transform("mem_" + b, zoom=0.42) # Zoom levemente menor para garantir o respiro
                        hover Transform("mem_" + b, zoom=0.42, matrixcolor=BrightnessMatrix(0.2))
                        action Function(jogo.registrar_clique, b)

# 3. LABEL DA LUTA (3 RODADAS COM PLACAR)
# -------------------------------------------------------------------------
label boss_fight_xadrez:
    $ v_theo = 0
    $ v_enzo = 0
    
    # RODADA 1
    $ jogo_boss = JogoMemoriaXadrez(dificuldade=3, bonus_foco=theo_foco, estabilidade_atual=theo_estabilidade)
    call screen memoria_xadrez(jogo_boss, 1, v_theo, v_enzo)
    if _return == "VITORIA":
        $ v_theo += 1
    else:
        $ v_enzo += 1

    # RODADA 2
    $ jogo_boss = JogoMemoriaXadrez(dificuldade=4, bonus_foco=theo_foco, estabilidade_atual=theo_estabilidade)
    call screen memoria_xadrez(jogo_boss, 2, v_theo, v_enzo)
    if _return == "VITORIA":
        $ v_theo += 1
    else:
        $ v_enzo += 1

    # RODADA 3
    $ jogo_boss = JogoMemoriaXadrez(dificuldade=5, bonus_foco=theo_foco, estabilidade_atual=theo_estabilidade)
    call screen memoria_xadrez(jogo_boss, 3, v_theo, v_enzo)
    if _return == "VITORIA":
        $ v_theo += 1
    else:
        $ v_enzo += 1

    # FIM DA LUTA
    if v_theo >= 2:
        "Placar Final: Theo [v_theo] x [v_enzo] Enzo. Você venceu o duelo!"
        $ theo_foco += 15
    else:
        "Placar Final: Theo [v_theo] x [v_enzo] Enzo. Você perdeu a partida."
        $ theo_estabilidade -= 15

    jump abrir_hub