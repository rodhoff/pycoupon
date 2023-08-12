# cupom_fiscal
Vamos às explicações do código. Vou explicar cada parte para quem quiser compreender melhor e vou destacar alguns pontos no final para que meu coração fique mais satisfeito.
Observação: É importante compreender que há uma diferença entre Cupom Fiscal e Nota Fiscal. São diferentes; em termos simplificados, "Cupom" geralmente está relacionado a supermercados e situações semelhantes, enquanto "Nota" está associada a compras na Shein ou em lojas de móveis e eletrônicos(não é regra, só uma explicação simplificada e fácil). Inclusive, vou inserir uma imagem ao final para ilustrar essa diferença, já que gosto de tudo bem explicado. 😄 Agora, vamos continuar, é sério.

# Importando algumas bibliotecas
 > from tkinter import *: Aqui, estamos importando tudo (todas as classes e funções) da biblioteca tkinter, que é usada para criar interfaces gráficas em Python. (GUI - Graphical User Interface). Com ele, você pode criar janelas, botões, caixas de texto, imagens e outros elementos interativos em seus programas.
 > from tkinter import ttk: Esta linha importa classes específicas da biblioteca tkinter que são usadas para criar widgets mais avançados, como guias, árvores e outros controles.
 > from tkinter import messagebox: Isso importa a funcionalidade de caixas de diálogo e mensagens do tkinter, que permite exibir mensagens ou caixas de alerta para interação com o usuário.
 > import pymysql: Aqui, estamos importando a biblioteca pymysql, que é uma interface para trabalhar com bancos de dados MySQL usando Python. Ela permite realizar operações de banco de dados em seu código.
  > from tkinter import Tk, Label: Estamos importando as classes Tk e Label do tkinter. A classe Tk é a janela principal da interface gráfica, e a classe Label é usada para exibir textos ou imagens na interface.
   > from PIL import Image, ImageTk: Aqui, estamos importando as classes Image e ImageTk da biblioteca PIL (Python Imaging Library). A classe Image é usada para carregar e manipular imagens, e a classe ImageTk é usada para exibir imagens em widgets do tkinter.(Usei para colocar uma imagem no background)
Resumindo, essas importações estão trazendo funcionalidades e recursos de diferentes bibliotecas para serem usados no código, como criar interfaces gráficas, exibir mensagens, trabalhar com bancos de dados MySQL e manipular imagens.
   
    from tkinter import *
    from tkinter import Tk, Label, ttk, messagebox
    from PIL import Image, ImageTk
    import pymysql

# Criando uma janela (interface gráfica) usando a classe Tk do módulo tkinter. 
 > window = Tk(): Isso cria uma nova janela principal usando a classe Tk. Esta é a janela principal da sua interface gráfica, onde todos os widgets e elementos serão colocados.
 > window.geometry("900x600"): Isso define as dimensões da janela em pixels. Nesse caso, a janela terá uma largura de 900 pixels e uma altura de 600 pixels.(Tentei varios metodos para deixar fullscreen e sinceramente não fiquei feliz com o resultado. A janela é iterativa entao pode so maximizar normalmente, ou deixar com a configuração:
    > window.geometry(f"{screen_width}x{screen_height}") que vai deixar quase janela cheia, vai ficar com um pouquinho so menor,
    > window.attributes('-fullscreen', True)) esse vai funcionar como um F11, deixa literalmente a tela toda preenchida, fique a vontade 
      para testar ou achar uma solução.
 > window.title("Faturamentos em Python | padilhajordane@gmail.com"): Aqui,  está definindo o título da janela. Ele aparecerá na barra de título da janela.
 > window.configure(bg='#093249'): Isso define a cor de fundo da janela. O código hexadecimal #093249 representa uma cor específica. A cor de fundo da janela(background) será definida para essa cor.
 > screen_width = window.winfo_screenwidth(): Nesta linha, está  o método winfo_screenwidth() do objeto window para obter a largura da tela em pixels. Isso é útil quando você quer ajustar ou dimensionar a sua interface gráfica com base nas dimensões da tela atual.
 > screen_height = window.winfo_screenheight(): Aqui, está  o método winfo_screenheight() do objeto window para obter a altura da tela em pixels.

      window = Tk()
      window.geometry("900x600")
      window.title("Faturamentos em Python | padilhajordane@gmail.com")
      window.configure(bg='#093249')
      
      screen_width = window.winfo_screenwidth()
      screen_height = window.winfo_screenheight()
      
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/2a00d929-0ffc-4cce-a941-9e4b5ae00762)


  #  imagem de plano de fundo na janela da interface gráfica (Metodo alternatio caso não queira usar cor como background ).

  > image_path = "caminho\da\sua\imagem": Nesta linha, você deveria definir o caminho completo para a imagem que deseja usar como plano de fundo. Essa imagem será carregada da localização especificada.
  > image = Image.open(image_path): Aqui, você estaria abrindo a imagem especificada usando a biblioteca PIL (Python Imaging Library), que é usada para manipular imagens em Python.
  > background_Label = Label(window): Isso cria um widget do tipo Label que será usado para exibir a imagem de plano de fundo. Você o vincula à janela principal (window).
  > background_Label.place(x=0, y=0, relwidth=1, relheight=1): Essa linha define a posição e o tamanho do Label. Neste caso, a imagem do Label ocuparia toda a janela, uma vez que relwidth (largura relativa) e relheight (altura relativa) estão definidos como 1.
  > photo = ImageTk.PhotoImage(image): Aqui, você está criando um objeto PhotoImage do tkinter usando a imagem carregada anteriormente. Isso é necessário para exibir a imagem dentro do widget Label.
  > background_Label.configure(image=photo): Por fim, você está configurando o Label para exibir a imagem carregada por meio do objeto PhotoImage.
  > screen_width = window.winfo_screenwidth(): Nesta linha, está  o método winfo_screenwidth() do objeto window para obter a largura da tela em pixels. Isso é útil quando você quer ajustar ou dimensionar a sua interface gráfica com base nas dimensões da tela atual.
 > screen_height = window.winfo_screenheight(): Aqui, está  o método winfo_screenheight() do objeto window para obter a altura da tela em pixels.
  OBS.: Nas minhas pesquisas achei alumas video aulas ensinando modos mais simples, porem esse foi o unico que funcionou para mim.
 
     image_path = "caminho\da\sua\imagem"
     image = Image.open(image_path)
     background_Label = Label(window)
     background_Label.place(x=0, y=0, relwidth=1, relheight=1)
     photo = ImageTk.PhotoImage(image)
     background_Label.configure(image=photo)
     
     screen_width = window.winfo_screenwidth()
     screen_height = window.winfo_screenheight()

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/434ff9a2-a369-4a85-92b5-3432cf31860e)

 # defnindo uma função quantityFieldListener
 
> é uma função que monitora as alterações feitas em um campo de entrada relacionado à quantidade de um item. Essa função é ativada automaticamente sempre que o valor no campo de quantidade é modificado pelo usuário. Vou deixar os comentarios explicando.

    #defnindo uma função quantityFieldListener
    def quantityFieldListener(a, b, c):
    
       # Obtém as variáveis globais necessárias
       global quantityVar
       global costVar
       global itemRate 
       
     # Obtém o valor da quantidade do campo de entrada
    quantity = quantityVar.get()
    
    # Verifica se a quantidade não está vazia
    if quantity != "":
        try:
            # Tenta converter a quantidade em um número de ponto flutuante
            quantity = float(quantity)
            
            # Calcula o custo com base na taxa do item
            cost = quantity * itemRate
            
            # Define a quantidade formatada com duas casas decimais
            quantityVar.set("%.2f" % quantity)
            
            # Define o custo formatado com duas casas decimais
            costVar.set("%.2f" % cost)
        except ValueError:
            # Se a conversão falhar, remove o último caractere da quantidade
            quantity = quantity[:-1]
            quantityVar.set(quantity)
    else:
        # Se a quantidade estiver vazia, define-a como zero
        quantity = 0
        quantityVar.set("%.2f" % quantity)



# Função para atualizar o campo de custo com base no valor inserido e na taxa do item
> é  utilizada para monitorar alterações em um campo de entrada  que representa o custo de um item. Sempre que ocorrerem alterações nesse campo, a função costFieldListener será chamada automaticamente e executará o código contido nela para atualizar outros campos relacionados, como a quantidade do item. O objetivo principal dessa função é manter a consistência entre o campo de custo e o campo de quantidade, garantindo que os valores sejam coerentes de acordo com a taxa do item.

   
    def costFieldListener(a, b, c):
      # Importando as variáveis globais necessárias
      global quantityVar  # Variável que armazena a quantidade do item
      global costVar      # Variável que armazena o custo total do item
      global itemRate     # Taxa do item

    # Obtendo o valor atual do custo da variável costVar
    cost = costVar.get()

    # Verificando se o campo de custo não está vazio
    if cost != "":
        try:
            # Tentando converter o custo para um número de ponto flutuante
            cost = float(cost)

            # Calculando a quantidade com base no custo e na taxa do item
            quantity = cost / itemRate

            # Atualizando a variável de quantidadeVar com a quantidade calculada
            quantityVar.set("%.2f" % quantity)

            # Atualizando a variável de custoVar com o custo inserido
            costVar.set("%.2f" % cost)
        except ValueError:
        
            # Se ocorrer um erro de conversão (ValorError), remova o último caractere do custo
            cost = cost[:-1]

            # Atualizando a variável de custoVar com o valor corrigido
            costVar.set(cost)
    else:
        # Se o campo de custo estiver vazio, defina o custo como 0
        cost = 0

        # Atualizando a variável de custoVar com o valor 0
        costVar.set(cost)


# Definindo variaveis 

    # Variáveis para armazenar informações do usuário
    usernameVar = StringVar()  # Variável para armazenar o nome de usuário
    passwordVar = StringVar()  # Variável para armazenar a senha do usuário
    
    # Lista de opções de itens e dicionário vazio para taxa dos itens
    options = ["Item1", "Item2", "Item3"]
    rateDict = {}
    
    # Variável para controlar a opção selecionada de item
    itemVariable = StringVar()
    itemVariable.set(options[0])  # Definir a primeira opção como a selecionada
    
    # Variável para armazenar a quantidade de itens
    quantityVar = StringVar()
    
    # Vincular a função 'quantityFieldListener' às mudanças na variável de quantidade
    quantityVar.trace('w', quantityFieldListener)
    
    # Taxa padrão do item (coloca a taxa que quiser aq )
    itemRate = 2
    
    # Variável para exibir a taxa do item em um formato específico
    rateVar = StringVar()
    rateVar.set("%.2f" % itemRate)
    
    # Variável para armazenar o custo do item
    costVar = StringVar()
    
    # Vincular a função 'costFieldListener' às mudanças na variável de custo
    costVar.trace('w', costFieldListener)
    
    # Widget Treeview para exibir informações sobre os itens na interface
    billsTV = ttk.Treeview(height=15, columns=('Rate', 'Quantity', 'Cost'))
    
    # Widget Treeview para atualização de informações na interface
    updateTV = ttk.Treeview(height=15, columns=('name', 'rate', 'type','storetpe'))
    
    # Opções de classificação por tipagem (da para por quantas quiser)
    storeOptions = ['Opção1', 'Opção2']
    
    # Variáveis para adicionar novo item
    addItemNameVar = StringVar()
    addItemRateVar = StringVar()
    addItemTypeVar = StringVar()
    addstoredVar = StringVar()
    addstoredVar.set(storeOptions[0])  # Definir a primeira opção como selecionada
    
    # Lista vazia para armazenar informações sobre os itens
    itemLists = list()
    
    # Variáveis para cálculos e exibição do custo total
    totalCost = 0.0
    totalCostVar = StringVar()
    totalCostVar.set("Total = {}".format(totalCost))
    
    # Variável para identificação de item a ser atualizado
    updateItemId = ""


# registrando as compras realizadas no banco de dados, atualizando a lista de itens exibida e calculando o custo total das compras feitas até o momento.
  > Se for so copiar o codigo com certeza não vai funcionar, ele precisa de um banco de dados para ser executado. Eu utilizo  localhost para criar minhas tabelas e fazer meus testes.
> vamos lá, existe um software chamado XAMPP instale ele (do site oficial pls)
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/e5f3cdff-8701-4f9f-9057-60d875f9e999)
> bemm simples de usar, ele já vem com a interface muito fácil de entender, basta ativar os dois primeiros itens que aparece que é o Apache o MySQL(🤮).
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/d7ec08a7-3012-4f5e-8342-2fa1be6224d9)
> Apertou start eles vão iniciar e ficar verdes.
> ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/eb68c5e2-c7cc-45c5-8382-cd9bece5e468)
> ficou verde, ótimo, esta funcionando.
> clique em admin que você será redirecionado para o servidor localhost. ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/2720474a-a0ab-4185-bf46-56b17bff4cdd)
> agora vá em novo
 ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/fc9943e0-c5fe-48a8-8125-ccb439fae2bc)

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/557ed333-694f-43ab-91ce-c3a93a760d43)
> pode colocar quantas colunas quiser em
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/28e60d67-f7e1-41cf-b630-46af5eda9443)
e pronto, voce pode colocar os nomes que vao ficar nas colunas, tipo de dado que será inserido e assim por diante. É importante marcar o tipo de entrada de dados para que não dê erro la na frente. Como da pra ver na imagem vai ter a interrogação que explica melhor sobre sql. 
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/756c04a8-c2af-4491-a9bc-5f29faa008de)
> rola pra baixo e selicona guardar para gravar a tabela
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/580d4f32-e981-49cd-abf6-97c29203effb)
> pronto ta feito.
> ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/c28dfd4d-4ca0-46f4-be1c-ead6d4592a93)
> vou deixar aqui a tabela do codigo, caso queira copiar.
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/9adf9b8c-24a0-4485-a3ab-328d329bc3b5)
> tabela de users ( aqui fica registrado o susuarios, como foi localhost e só para testar o codigo a senha não é lá de importância) 
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/4a1461aa-25a1-415f-a5e2-b53d87009dd0)
> a tabela de itens, todo item que for adicionado vai parar nela e sempre que for ediatodo sera editado nela tambem automaticamente.
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/eb3e7768-eb7d-4a6d-a9d0-84fd3c6e5c29)
> a tabela de bill é onde toda compra sera armazenada, então quando você estiver acessando o historico esta vendo o que esta nessa tabela
 ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/c9c1aafa-2be3-47dd-8335-9f59b6bb990a)


    def generate_bill():
        global itemVariable
        global quantityVar
        global itemRate
        global costVar
        global itemLists
        global totalCost
        global totalCostVar

    # Obter o nome do item selecionado, quantidade e custo dos campos de entrada
    itemName = itemVariable.get()
    quantity = quantityVar.get()
    cost = costVar.get()

    # Conecta ao banco de dados
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor()

    # Monta a consulta SQL para inserir os detalhes da compra na tabela (coloca o nome que quiser na sua tabela ou esse mesmo, se tiver ela o codigo funciona kk, como é banco de dados e eu particularmente detesto, vou deixar tudo certinho de como fazer essa tabela)
    query = "insert into bill (name,quantity,rate,cost) value('{}','{}','{}','{}')".format(itemName, quantity, itemRate, cost)
    
    # Executa a consulta SQL
    cursor.execute(query)
    conn.commit()
    conn.close()

    # Cria um dicionário com detalhes do item e adiciona à lista 'itemLists'
    listDict = {"name": itemName, "rate": itemRate, "quantity": quantity, "cost": cost}
    itemLists.append(listDict)

    # Atualiza o custo total e os campos de entrada de quantidade e custo
    totalCost = float(cost)
    quantityVar.set("0")
    costVar.set("0")

    # Atualiza a exibição da lista de itens e o custo total exibido
    updateListView()
    totalCostVar.set("Total = {}".format(totalCost))


#    





Não pretendo deixar nenhum link, tampouco dar IB. Não é difícil de encontrar, bastando pesquisar pelo nome no YouTube ou Google (veja os motivos).

1.1. Na minha opinião, o "professor" deixou a desejar. Acredito na beleza de abordar o ensino com humildade, e tenho um temperamento bastante enérgico. Quando me deparo com pessoas que, na minha percepção, agem de maneira um tanto ríspida, acabo desenvolvendo certa aversão. Não quero dizer que não sou grata pela aula, mas devido ao método de ensino que não me agradou muito, acabei buscando MUITA informação por conta própria, quase achei mais facil ter pego as bibliotecas e me virado nos 30 sozinha... Isso foi algo que me causou muito estresse e foi muito difícil, porém, como resultado, acabei aprendendo mais do que teria aprendido se ele tivesse explicado de forma mais clara ou explicado de fato.

1.2. Ao final das aulas, planejava deixar um comentário agradecendo e mencionando pontos que talvez pudessem ser melhorados. É claro que não tinha intenção de atacar, pois isso não é necessário, mas ele mesmo deixou claro que esse tipo de comentário é apagado. Logo, compreendi a razão pela qual não recebe muita visibilidade.

1.3. Na metade das aulas, estava começando a compreender o assunto e, de repente, foi informado que o código havia sido completamente alterado, sem qualquer explicação, nem mesmo uma indicação de onde, algo como "pegue lá no GitHub, porque se não estiver desse jeito, não vai funcionar". Gosto de seguir as aulas, porém sempre faço do meu jeito. Não sou fã de simplesmente copiar e colar. No entanto, sem conhecer a alteração, fica complicado entender por que algo não funcionaria e pensar em alguma alternativa como foi feito em alguns pontos.

1.4. Desmotivar os iniciantes durante as aulas é algo terrível, pois isso afeta muitas pessoas. Se você não é afetado, ótimo. Mas, por exemplo, se estou passando por um momento difícil na vida, me esforçando, e ouço um "professor" desmotivador, é bastante frustrante.

1.5. Além de desmotivar os alunos, também fica evidente que o próprio professor também demonstra certa preguiça, tornando difícil acompanhar as aulas.

Lembrando que essa é a minha opinião e meu ponto de vista. Não gostei e também não busquei ficar reclamando disso no email, comentarios ou qualquer outra forma de contato. Se ele não gosta de ouvir coisas que podem ser interpretadas como críticas, tudo bem. Agradeço pelas aulas, o estresse e os dias que poderiam ter sido mais tranquilos foram, na verdade, de muito aprendizado.

Cada pessoa tem a sua própria forma de ver, entender, absorver e transmitir. Para quem gosta, tudo bem, aproveite e seja feliz. Infelizmente, eu não recomendo e não pretendo fazer mais nenhum curso com esse "professor", pois isso não se alinha às minhas necessidades. É isso. Se você leu tudo isso , eu mesma talvez não tivesse lido,  quiser me falar algo devido à ausência do IB, aqui está um esboço de explicação, não que eu deva alguma ahahahah xD  um xero.
