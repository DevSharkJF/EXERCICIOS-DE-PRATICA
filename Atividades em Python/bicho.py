import os # Limpa Tela
import time # Tempo de Tela

# ------ BACKEND DO CÓDIGO ------
# Def's de alteração:
class BichoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 10
        self.saude = 50
        self.idade = 1
        self.banho = 0.5
        self.banheiro = 1

    def AlterarNome(self, novo_nome):
        self.nome = novo_nome

    def AlterarFome(self, valor_fome):
        self.fome += valor_fome
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0

    def AlterarSaude(self, valor_saude):
        self.saude += valor_saude
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0

    def AlterarBanho(self, valor_banho):
        self.banho += valor_banho
        if self.banho > 5:
            self.banho = 5
        elif self.banho < 0:
            self.banho = 0

    def AlterarBanheiro(self, valor_banheiro):
        self.banheiro += valor_banheiro
        if self.banheiro > 10:
            self.banheiro = 10
        elif self.banheiro < 0:
            self.banheiro = 0

    def AlterarIdade(self):
        self.idade += 1

# Def's de Alteração:
    def RetornarNome(self):
        return self.nome

    def RetornarFome(self):
        return self.fome

    def RetornarSaude(self):
        return self.saude

    def RetornarIdade(self):
        return self.idade

    def RetornarHumor(self):
        humor = self.saude + self.fome
        if humor <= 25:
            return "Triste"
        elif 26 <= humor <= 70:
            return "Normal"
        else:
            return "Alegre"
        
    def RetornarBanho(self):
        banho_2 = self.banho
        if banho_2 >= 4:
            return "Está Sujo"
        elif banho_2 <=3:
            return "Está limpo"
        
    def RetornarBanheiro(self):
        banheiro_2 = self.banheiro
        if banheiro_2 >= 7:
            return "Estou Muito Apertado"
        elif banheiro_2 <= 6:
            return "Não estou com vontade de ir ao banheiro"

os.system('cls')

# ------ FRONTEND DO CÓDIGO ------
print(f"""\n👋 SEJA BEM VINDO AO TAMAGOTCHI-SHARK 🦈""")

nome_bicho = input(
    f"""\nQual nome deseja colocar no seu Tamagotchi? """)
os.system('cls')
bicho = BichoVirtual(nome = nome_bicho)

while (bicho.saude > 0) and (bicho.fome < 100):
    bicho.AlterarFome(+3)
    bicho.AlterarSaude(-3)
    bicho.AlterarIdade()
    resposta = input(
        f"""\n
    /  \.-" "-./  \ 
    \    -   -    /
     |   ●   ●   |
     \  .-'''-.  /
      '-\_ ω _/-'
         `---`
   /———/       \———\ 
  /   /         \   \    
 /   /           \   \   
人  |             |  人 
    |             | 
     \           /
      \_________/     
     \nOlá, meu nome é {bicho.nome}.\n\nEscolha uma Ação:\n
        1- 🍯 Alimentar (-10 de fome)\n
        2- 💤 Dormir (+10 de saúde)\n
        3- 🐻 Alterar nome\n
        4- 💢 Visualizar humor\n
        5- 🕒 Visualizar idade\n
        6- 🍴 Visualizar fome\n
        7- 🫀  Visualizar saúde\n
        8- 🚿  Dar banho\n   
        9- 🚽 Ir ao banheiro\n
        0 - ❌ Sair\n
        ➡️  RESPOSTA: """)
    os.system('cls')
    
    if resposta == '1':
        bicho.AlterarFome(-10)
        bicho.AlterarBanho(+0.5)
        bicho.AlterarBanheiro(+1)
        print("✅ AÇÃO:")
        print('-10 de fome! Obrigado')
        print("Necessidades: ", bicho.RetornarBanheiro())
        time.sleep(2)
        print("__________________________")

    elif resposta == '2':
        bicho.AlterarSaude(+10)
        bicho.AlterarBanho(+0.5)
        print("✅ AÇÃO:")
        print("+10 de saúde! Obrigado!")
        time.sleep(2)
        print("__________________________")

    elif resposta == '3':
        nome2 = input('Qual nome deseja colocar?')
        bicho.AlterarNome(nome2)
        os.system('cls')

    elif resposta == '4':
        print("✅ AÇÃO:")
        print("Humor: ", bicho.RetornarHumor())
        time.sleep(2)
        print("__________________________")

    elif resposta == '5':
        print("✅ AÇÃO:")
        print("Idade: ", bicho.RetornarIdade())
        time.sleep(2)
        print("__________________________")

    elif resposta == '6':
        print("✅ AÇÃO:")
        print("Fome: ", bicho.RetornarFome())
        time.sleep(2)
        print("__________________________")

    elif resposta == '7':
        print("✅ AÇÃO:")
        print("Saúde: ", bicho.RetornarSaude())
        time.sleep(2)
        print("__________________________")

    elif resposta == '8':
        bicho.AlterarBanho(-1)
        print("✅ AÇÃO:")
        print("-1 de sujeira! Obrigado!")
        print("Higiene: ", bicho.RetornarBanho())
        time.sleep(2)
        print("__________________________")

    elif resposta == '9':
        bicho.AlterarBanheiro(-4)
        print("✅ AÇÃO:")
        print("Aliviado, Obrigado!")
        time.sleep(2)
        print("__________________________")

    elif resposta == '0':
        print("\n❗VOCÊ SAIU DO JOGO 🔚")
        break 

    else:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')

else:
    print(f"""\n
    /  \.-" "-./  \ 
    \    -   -    /
     |   X   X   |
     \  .-'''-.  /
      '-\_ ω _/-'
         `---`
   /———/       \———\ 
  /   /         \   \    
 /   /           \   \   
人  |             |  人 
    |             | 
     \           /
      \_________/     
      
          \n🚨VOCÊ ME DEIXOU MORRER🚨\n""")
