import random
import time

# Lista de palavras difíceis com 7 letras ou mais
palavras_dificeis = [
    "abstrato", "complexo", "fragmento", "labirinto", "esquisito",
    "psicopata", "gladiador", "tempestade", "misterioso", "paradoxo",
    "impensável", "furacão", "detalhado", "vigilante", "mistério",
    "fascinação", "esforço", "enigma", "vigor", "corte", "sombra",
    "sopro", "força", "fisíco", "ataque", "correr", "falar",
    "esquiva", "jab", "assistir", "fazer", "ouvir", "tanque", "guerra",
    "mundo", "planeta", "pão", "miojo", "macarrão", "pastel", "lacoste",
    "bangela", "banguela", "germes", "feminismo", "machismo", 
    "alface", "lápis", "caneta", "tijolo", "feijão", "linguiça", "caramelo"
]

# Faz uma cópia da lista pra ir removendo as usadas
palavras_disponiveis = palavras_dificeis.copy()

# Função que gera e testa a sequência de letras (palavra)
def desafio_de_reacao():
    global palavras_disponiveis

    # Se acabar as palavras, reinicia a lista
    if not palavras_disponiveis:
        palavras_disponiveis = palavras_dificeis.copy()

    palavra = random.choice(palavras_disponiveis)
    palavras_disponiveis.remove(palavra)

    print("\n⚠️ Prepare-se! Memorize a palavra difícil!")
    print(f"🧠 Palavra: {palavra.upper()}")
    time.sleep(2)
    
    print("\n" * 30)  # Limpa a tela simulando
    print("Agora digite a palavra: ")

    inicio = time.time()
    resposta = input("> ").lower().strip()
    fim = time.time()

    tempo_total = fim - inicio

    acertos = sum(1 for i in range(min(len(resposta), len(palavra))) if resposta[i] == palavra[i])

    print(f"\n⏱️ Tempo usado: {tempo_total:.1f} segundos")
    print(f"✅ Letras corretas na posição certa: {acertos} de {len(palavra)}")

    if tempo_total > 6:
        print("⏳ Passou do tempo!")
        return False, acertos

    if acertos >= len(palavra) - 2:
        return True, acertos
    else:
        print("😵 Errou demais! O ataque falhou!")
        return False, acertos
# Classe dos personagens
class Lutador:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def atacar(self, oponente):
        print(f"\n{self.nome} vai atacar {oponente.nome}!")

        sucesso, acertos = desafio_de_reacao()
        if not sucesso:
            print(f"{self.nome} perdeu a chance de atacar!")
            return

        # Escolhe ataque e calcula dano
        if self.nome == "Gorila":
            ataque = random.choice(["soco", "mordida"])
            if ataque == "soco":
                dano = oponente.vida * (0.1 * acertos)  # 10% por acerto
                print(f"💥 {self.nome} desce a PORRADA com um soco poderoso!")
            else:
                dano = 5 * acertos
                print(f"🦷 {self.nome} morde com fúria!")

        elif self.nome == "Urso Pardo":
            ataque = random.choice(["garra", "mordida"])
            if ataque == "garra":
                dano = oponente.vida * (0.1 * acertos)  # 10% por acerto
                print(f"🐾 {self.nome} ataca com suas garras afiadas!")
            else:
                dano = 3 * acertos
                print(f"🦷 {self.nome} dá uma mordida!")

        # Esquiva ainda vale
        chance_esquiva = 0.3 if oponente.nome == "Gorila" else 0.1
        if random.random() < chance_esquiva:
            print(f"💨 {oponente.nome} desviou do ataque!")
            return

        # Aplica dano
        oponente.vida -= dano
        oponente.vida = max(oponente.vida, 0)
        print(f"{self.nome} causou {dano:.1f} de dano em {oponente.nome}!")
        print(f"Vida de {oponente.nome}: {oponente.vida:.1f}")

# Escolha de personagem
def escolher_personagem(jogador):
    print(f"\n{jogador}, escolha seu personagem:")
    print("1. 🐻 Urso Pardo")
    print("2. 🦍 Gorila")

    while True:
        escolha = input("Digite 1 para Urso ou 2 para Gorila: ")
        if escolha == "1":
            return Lutador("Urso Pardo")
        elif escolha == "2":
            return Lutador("Gorila")
        else:
            print("Escolha inválida. Tente de novo.")

# Início do jogo
print("🔥 BATALHA: URSO PARDO vs GORILA 🔥")
p1 = escolher_personagem("Player 1")
p2 = Lutador("Gorila") if p1.nome == "Urso Pardo" else Lutador("Urso Pardo")

print(f"\nPlayer 1 escolheu: {p1.nome}")
print(f"Player 2 ficou com: {p2.nome}")

# Loop da luta
vez_do_p1 = True
while p1.vida > 0 and p2.vida > 0:
    time.sleep(1)
    if vez_do_p1:
        p1.atacar(p2)
    else:
        p2.atacar(p1)
    vez_do_p1 = not vez_do_p1

# Resultado final
print("\n💀 FIM DA LUTA! 💀")
if p1.vida <= 0:
    print(f"{p2.nome} venceu com {p2.vida:.1f} de vida restante!")
else:
    print(f"{p1.nome} venceu com {p1.vida:.1f} de vida restante!")
