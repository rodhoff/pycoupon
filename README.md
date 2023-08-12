# cupom_fiscal
Vamos às explicações do código. Vou explicar cada parte para quem quiser compreender melhor e vou destacar alguns pontos no final para que meu coração fique mais satisfeito.
Observação: É importante compreender que há uma diferença entre Cupom Fiscal e Nota Fiscal. São diferentes; em termos simplificados, "Cupom" geralmente está relacionado a supermercados e afins, enquanto "Nota" está associada a compras na Shein ou em lojas de móveis e eletrônicos no geral (não é regra, só uma explicação simplificada e fácil). Inclusive, vou inserir uma imagem ao final para ilustrar essa diferença, já que gosto de tudo bem explicado. 😄 Agora, vamos continuar, é sério.

# Importando algumas bibliotecas
 > from tkinter import *: Aqui, estamos importando todas as classes e funções da biblioteca tkinter, usada para criar interfaces gráficas em Python (GUI - Graphical User Interface). Com ela, você pode criar janelas, botões, caixas de texto, imagens e outros elementos interativos em seus programas.
 > from tkinter import ttk: Esta linha importa classes específicas da biblioteca tkinter que são usadas para criar widgets mais avançados, como guias, árvores e outros controles.
 > from tkinter import messagebox: Isso importa a funcionalidade de caixas de diálogo e mensagens do tkinter, que permite exibir mensagens ou caixas de alerta para interação com o usuário.
 > import pymysql: Aqui, estamos importando a biblioteca pymysql, que é uma interface para trabalhar com bancos de dados MySQL usando Python. Ela permite realizar operações de banco de dados em seu código.
 > from tkinter import Tk, Label: Estamos importando as classes Tk e Label do tkinter. A classe Tk é a janela principal da interface gráfica, e a classe Label é usada para exibir textos ou imagens na interface.
 > from PIL import Image, ImageTk: Aqui, estamos importando as classes Image e ImageTk da biblioteca PIL (Python Imaging Library). A classe Image é usada para carregar e manipular imagens, e a classe ImageTk é usada para exibir imagens em widgets do tkinter (Usei para colocar uma imagem no background).
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
> vamos lá, existe um software chamado XAMPP instale ele (do site oficial pls🙏 )

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/e5f3cdff-8701-4f9f-9057-60d875f9e999)

> bemm simples de usar, ele já vem com a interface muito fácil de entender, basta ativar os dois primeiros itens que aparece que é o Apache o MySQL(🤮).

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/d7ec08a7-3012-4f5e-8342-2fa1be6224d9)

> Apertou start eles vão iniciar e ficar verdes.

> ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/eb68c5e2-c7cc-45c5-8382-cd9bece5e468)

> ficou verde, ótimo, esta funcionando.
> clique em admin que você será redirecionado para o servidor localhost.
 
 ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/2720474a-a0ab-4185-bf46-56b17bff4cdd)
 
> agora vá em novo

 ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/fc9943e0-c5fe-48a8-8125-ccb439fae2bc)

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/557ed333-694f-43ab-91ce-c3a93a760d43)

> pode colocar quantas colunas quiser, só não abusa

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/28e60d67-f7e1-41cf-b630-46af5eda9443)

> e pronto, você pode colocar os nomes que vão ficar nas colunas, tipo de dado que será inserido e assim por diante. É importante marcar o tipo de entrada de dados para que não dê erro la na frente. Como da pra ver na imagem vai ter a interrogação que te encaminha para explicações sobre Mysql.
 
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/756c04a8-c2af-4491-a9bc-5f29faa008de)

> rola pra baixo e selicona guardar para gravar a tabela

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/580d4f32-e981-49cd-abf6-97c29203effb)

> pronto ta feito.

> ![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/c28dfd4d-4ca0-46f4-be1c-ead6d4592a93)

> vou deixar aqui a tabela do codigo, caso queira copiar. Repara que são três tabelas  dentro de outra tabela em cabeçudos.

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/9adf9b8c-24a0-4485-a3ab-328d329bc3b5)

> tabela de users ( aqui fica registrado os usuarios, como foi localhost e só para testar o codigo, a senha não é lá de importância, mas faça a sua como quiser)

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/4a1461aa-25a1-415f-a5e2-b53d87009dd0)

> a tabela de itens, todo item que for adicionado vai parar nela e sempre que for editado sera editado nela também automaticamente.

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/eb3e7768-eb7d-4a6d-a9d0-84fd3c6e5c29)

> a tabela de bill é onde toda compra sera armazenada, então quando você estiver acessando o historico vai ver o que esta nessa tabela

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


#    visualização dos detalhes de um item selecionado na treeview "updateTV" ao realizar um clique duplo sobre ele.

    def onDoubleClick(event):
       # Obtendo variáveis globais para a manipulação dos campos de entrada e seleção
       global  addItemNameVar
       global addItemRateVar
       global addItemTypeVar
       global addstoredVar
       global updateItemId
      
    # Obtendo o item selecionado na treeview "updateTV"
    item = updateTV.selection()
    
    # Capturando o ID do item selecionado e os detalhes associados a ele
    updateItemId = updateTV.item(item, "text")
    item_detail = updateTV.item(item, "values")
    
    # Obtendo o índice da opção de armazenamento na lista "storeOptions"
    item_index = storeOptions.index(item_detail[3])
    
    # Configurando os campos de entrada com os detalhes do item selecionado
    addItemTypeVar.set(item_detail[2])  # Defini a descrição do produto
    addItemRateVar.set(item_detail[1])  # Defini o preço do produto
    addItemNameVar.set(item_detail[0])  # Defini o nome do produto
    addstoredVar.set(storeOptions[item_index])  # Defini a opção de armazenamento do produto


# atualizando a exibição dos produtos selecionados na treeview "billsTV"
    
    def updateListView():
        # Remove registros anteriores da treeview "billsTV"
        records = billsTV.get_children()
        for element in records:
            billsTV.delete(element)
    
        # Insere novos registros na treeview "billsTV"
        for row in itemLists:
            # Insere uma nova linha na treeview exibindo o nome do produto, a taxa, a quantidade e o custo
            billsTV.insert('', 'end', text=row['name'], values=(row["rate"], row["quantity"], row["cost"]))


# obtendo os detalhes dos produtos do banco de dados para exibi-los na treeview "updateTV".

    def getItemLists():
        # Remove registros anteriores da treeview "updateTV"
        records = updateTV.get_children()
        for element in records:
            updateTV.delete(element)
 
     # Conecta-se ao banco de dados para obter os detalhes dos produtos
     conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
     cursor = conn.cursor(pymysql.cursors.DictCursor)
     query = "select * from itemlist"
     cursor.execute(query)
     data = cursor.fetchall()
 
     # Insere os detalhes dos produtos na treeview "updateTV"
     for row in data:
         # Insere uma nova linha na treeview exibindo o ID do produto, o nome, a taxa, o tipo e a classificação de estoque
         updateTV.insert('', 'end', text=row['nameid'], values=(row['name'], row['rate'], row['type'], row['storetpe']))
     
     # Associa a função "onDoubleClick" a eventos de clique duplo na treeview "updateTV"
     updateTV.bind("<Double-1>", onDoubleClick)
     
     # Fecha a conexão com o banco de dados
     conn.close()

# Formatação do Cupom 
essa aqui é dificil de entender em :v

    def print_bill():
        global itemLists
        global totalCost
    
    # Imprime o cabeçalho do cupom fiscal
    print("======================== Cupom Fiscal ======================")
    print("=========================== Nome_qualquer ==================")
    
    # Imprime o cabeçalho da tabela de itens (vou deixar aqui de novo que você pode mudar esses nomes assim como das funções, coloca o que jesus tocar no seu coração para seu codigo)
    print("{:<20} {:<10} {:<15} {:<10}".format("Nome","Valor Unit.","Quantidade","Valor Total"))
    print("============================================================")
    
    # Itera sobre os itens na lista e imprime os detalhes de cada item
    for item in itemLists:
        print("{:<20} {:<10} {:<15} {:<10}".format(item["name"], item["rate"], item["quantity"], item["cost"]))
    
    # Imprime o rodapé da tabela de itens e o total da compra
    print("============================================================")
    print("{:<20} {:<10} {:<15} {:<10}".format("Total = ", " ", " ",totalCost))
    
    # Reseta a lista de itens e o custo total, atualiza a exibição na treeview e redefine o valor da variável totalCostVar
    itemLists = []
    totalCost = 0.0
    updateListView()
    totalCostVar.set("Total = {}".format(totalCost))

> imagem aqui para ficar fácil vizualisar. E da para conectar o pc em uma impressora e desenvolver uma parte complementar para mandar direto para a impressora ou mandar/salvar como  pdf.

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/6c431864-d1fc-402a-93a5-44ce91b3e33c)

#   Encerra a aplicação fechando a janela principal (window).
Ativa o botão de sair, toda vez que apertar em "sair" a janela vai fechar.
    
    def iExit():
        window.destroy()

# Limpa todos os widgets da tela atual e move para a tela de atualização de itens (updateItemWindow()).  
 Quando mudar de tela não vai ficar "bugando" varias telas ao mesmo tempo.

    def moveToUpdate():
        remove_all_widgets()
        updateItemWindow()
        
# Limpa todos os widgets da tela atual e move para a tela de visualização de todos os cupons (ViewAllBills()).
historico :)

      def moveToBills():
          remove_all_widgets()
          ViewAllBills()
 
#  inicializando variaveis globais para armazenar informações sobre os itens. Em seguida, uma conexão com o banco de dados é estabelecida usando os parâmetros fornecidos (host, usuário, senha e nome do banco de dados). Um cursor é criado para executar consultas SQL no banco de dados usando o módulo pymysql   
    def readAllData():
        global options
        global rateDict
        global itemVariable
        global itemRate
        global rateVar
       
    # Inicializa as variáveis globais que serão usadas para armazenar informações sobre os itens.
    options = []     # Lista para armazenar os nomes dos itens.
    rateDict = {}    # Dicionário para armazenar as taxas dos itens.
    
    # Estabelece uma conexão com o banco de dados usando os parâmetros de conexão fornecidos.
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    
    # Cria um cursor que permite executar consultas SQL no banco de dados.
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    # O restante do código da função continuará a recuperar dados do banco de dados e popula as variáveis globais.

    
    # Recupera todos os itens da tabela itemlist do banco de dados e popula as listas options e rateDict.
    query = "select * from itemlist"
    cursor.execute(query)
    data = cursor.fetchall()
    count = 0
    for row in data:
        count += 1
        options.append(row['nameid'])
        rateDict[row['nameid']] = row['rate']
        itemVariable.set(options[0])
        itemRate = str(rateDict[options[0]])  # int
    
    conn.close()
    
    # Define a taxa do primeiro item como a taxa atual e verifica se há itens na lista.
    rateVar.set(itemRate)  # "%.2f"%
    if count == 0:
        remove_all_widgets()
        itemAddWindow()  # Se não houver itens, move para a tela de adição de itens.
    else:
        remove_all_widgets()
        mainwindow()  # Se houver itens, move para a tela principal (mainwindow()).

# Função para atualizar a taxa e variáveis relacionadas ao selecionar um item no menu de opções.
     def optionMenuListener(event):
         global itemVariable
         global rateDict
         global itemRate
         
     # Obtém o item selecionado no menu de opções.
    item = itemVariable.get()
    
    # Obtém a taxa do item selecionado a partir do dicionário de taxas.
    itemRate = float(rateDict[item])
    
    # Atualiza a variável de exibição da taxa com o valor formatado.
    rateVar.set("%.2f" % itemRate) 

# Função para remover todos os widgets presentes na janela.
def remove_all_widgets():
    global window
    
    # Remove cada widget (elemento gráfico) presente na janela.
    for widget in window.winfo_children():
        widget.grid_remove()

# Função para atualizar os dados da TreeView de contas.
 
    def updateBillsData():
        records = billsTV.get_children()
        
        # Remove todas as entradas presentes na TreeView de contas.
        for element in records:
            billsTV.delete(element)

    # Estabelece uma conexão com o banco de dados.
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    # Executa a consulta SQL para recuperar os dados das contas.
    query = "select * from bill"
    cursor.execute(query)
    data = cursor.fetchall()

    # Insere as informações das contas na TreeView.
    for row in data:
        billsTV.insert('', 'end', text=row['name'], values=(row["rate"], row["quantity"], row["cost"]))

    conn.close()    

# Função para realizar login de administrador.

    def adminLogin():
        global usernameVar
        global passwordVar
     
    # Obtém os valores inseridos nos campos de usuário e senha.
    username = usernameVar.get()
    password = passwordVar.get()
    
    # Estabelece uma conexão com o banco de dados.
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor()
    
    # Executa a consulta SQL para verificar as credenciais do administrador.
    query = "select * from users where username='{}' and password='{}'".format(username, password)
    cursor.execute(query)
    data = cursor.fetchall()
    
    admin = False
    for row in data:
        admin = True
        
    conn.close()
    
    # Se as credenciais estiverem corretas, exibe a próxima janela, caso contrário, mostra uma mensagem de erro.
    if admin:
        remove_all_widgets()
        itemAddWindow()
    else:
        messagebox.showerror("Usuário ou Senha Inválido", "Insira usuário e senha corretamente")    

 # Função para lidar com a ação de adicionar item.
 
    def addItemListener():
        # Remove todos os widgets presentes na janela atual.
        remove_all_widgets()
        # Abre a janela para adicionar item.
        itemAddWindow()

# Função para retornar à janela principal.
Botão voltar
    def goBack():
        # Remove todos os widgets presentes na janela atual.
        remove_all_widgets()
        # Retorna à janela principal.
        mainwindow()

# Função para adicionar um novo item ao banco de dados.
   
    def addItem():
        global addItemNameVar
        global addItemRateVar
        global addItemTypeVar
        global addstoredVar
    
    # Obtém os valores dos campos do novo item.
    name = addItemNameVar.get()
    rate = addItemRateVar.get()
    Type = addItemTypeVar.get()
    storetpe = addstoredVar.get()
    
    # Cria um ID único para o item substituindo espaços por underscores.
    nameId = name.replace(" ", "_")
    
    # Estabelece uma conexão com o banco de dados.
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor()
    
    # Executa a consulta SQL para inserir os dados do novo item no banco de dados.
    query = "insert into itemlist (name,nameid,rate,type,storetpe) value('{}','{}','{}','{}','{}')".format(name, nameId, rate, Type, storetpe)
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    # Limpa os campos após a adição do item.
    addItemNameVar.set("")
    addItemRateVar.set("")
    addItemTypeVar.set("")

# Função para atualizar um item no banco de dados.
def updateItem():

     global addItemNameVar
     global addItemRateVar
     global addItemTypeVar
     global addstoredVar
     global updateItemId
     
    # Obtém os valores dos campos do item a ser atualizado.
    name = addItemNameVar.get()
    rate = addItemRateVar.get()
    Type = addItemTypeVar.get()
    storetpe = addstoredVar.get()
    
    # Estabelece uma conexão com o banco de dados.
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor()
    
    # Executa a consulta SQL para atualizar os dados do item no banco de dados.
    query = "UPDATE itemlist SET name='{}', rate='{}', type='{}', storetpe='{}' WHERE nameid={}".format(name, rate, Type, storetpe, updateItemId)
    cursor.execute(query)
    conn.commit()
    conn.close()

    # Limpa os campos após a atualização do item.
    addItemNameVar.set("")
    addItemRateVar.set("")
    addItemTypeVar.set("")

    # Atualiza a lista de itens na TreeView.
    getItemLists()

 # Tela de login   

    def loginWindow():
        # Configura a geometria da janela com base nas dimensões da tela.
        window.geometry(f"{screen_width}x{screen_height}")
        # Define a aparência da janela em tela cheia (comentado para uso futuro).
        # window.attributes('-fullscreen', True)

    # Criação de um rótulo de título para a janela.
    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249', fg="white")
    titleLabel.grid(row=0, column=0, columnspan=4, padx=(130, 0), pady=(10, 0))

    # Criação de um rótulo para a seção de login.
    loginLabel = Label(window, text="Login", font="Arial 30", bg='#093249', fg="white")
    loginLabel.grid(row=1, column=1, padx=(0, 850), columnspan=2, pady=(170, 5))

    # Rótulo e entrada para o campo de nome de usuário.
    usernameLabel = Label(window, text="Usuario :", font=("bold", 15), bg='#093249', fg="white")
    usernameLabel.grid(row=2, column=1, padx=(30, 100), pady=5)
    usernameEntry = Entry(window, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=(0, 900), pady=5)

    # Rótulo e entrada para o campo de senha.
    passwordLabel = Label(window, text="Senha :", font=("bold", 15), bg='#093249', fg="white")
    passwordLabel.grid(row=3, column=1, padx=(30, 100), pady=5)
    passwordEntry = Entry(window, textvariable=passwordVar, show="*")
    passwordEntry.grid(row=3, column=2, padx=(0, 900), pady=5)

    # Botão de login que chama a função adminLogin() quando pressionado.
    loginButton = Button(window, text="Entrar", bg='#093249', fg="white", font=("arial", 17), width=15, height=2, command=lambda: adminLogin())
    loginButton.grid(row=4, column=1, columnspan=2, padx=(0, 850))

# Janela principal

    def mainwindow():
        # Configura a geometria da janela com base nas dimensões da tela.
        window.geometry(f"{screen_width}x{screen_height}")

    # Criação de um rótulo de título para a janela.
    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30),  bg='#093249', fg="white")
    titleLabel.grid(row=0, column=1, columnspan=4, pady=(10, 0))

    # Botões para adicionar e atualizar produtos, e mostrar histórico de contas.
    addNewItem = Button(window, text="Add Produto", font=("bold", 10), width=15, bg='#093249', fg="white", height=2, command=lambda: addItemListener())
    addNewItem.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))
    updateItem = Button(window, text="Atualizar", bg='#093249', font=("bold", 10), fg="white", width=15, height=2, command=lambda: moveToUpdate())
    updateItem.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))
    showallEntry = Button(window, text="Historico", width=15, height=2, font=("bold", 10), bg='#093249', fg="white", command=lambda: moveToBills())
    showallEntry.grid(row=1, column=2, padx=(10, 0), pady=(10, 0))

    # Rótulos e dropdown para selecionar um produto.
    itemLabel = Label(window, text="Selecionar Produto", bg='#093249',fg="white")
    itemLabel.grid(row=2, column=0, padx=(5, 0), pady=(10, 0))
    itemDropDown = OptionMenu(window, itemVariable, *options, command=optionMenuListener)
    itemDropDown.grid(row=2, column=1, padx=(10, 0), pady=(10, 0))

    # Rótulo e valor para exibir o preço do produto selecionado.
    rateLabel = Label(window, text="Preço",bg='#093249', fg="white")
    rateLabel.grid(row=2, column=2, padx=(10, 0), pady=(10, 0))
    rateValue = Label(window, bg="white", textvariable=rateVar)
    rateValue.grid(row=2, column=3, padx=(10, 0), pady=(10, 0))
    rateValue.config(width=10, height=1)

    # Rótulos, entrada e campos para quantidade e custo.
    quantityLabel = Label(window, bg='#093249', fg="white",text="Quantidade")
    quantityLabel.grid(row=3, column=0, padx=(5, 0), pady=(10, 0))
    quantityEntry = Entry(window, textvariable=quantityVar)
    quantityEntry.grid(row=3, column=1, padx=(5, 0), pady=(10, 0))
    costLabel = Label(window, bg='#093249', fg="white",text="Valor Total do Produto")
    costLabel.grid(row=3, column=2, padx=(10, 0), pady=(10, 0))
    costEntry = Entry(window, textvariable=costVar)
    costEntry.grid(row=3, column=3, padx=(10, 0), pady=(10, 0))

    # Botão para adicionar o item à lista.
    buttonBill = Button(window, text="Adicionar a lista", font=("bold", 10), width=15, bg='#093249', fg="white",command=lambda: generate_bill())
    buttonBill.grid(row=4, column=4, padx=(2, 0), pady=(20, 0))

    # Rótulo para a lista de produtos.
    billLabel = Label(window, text="Lista De Produtos", font="bold 25", bg='#093249', fg="white")
    billLabel.grid(row=4, column=2)

    # Tabela (Treeview) para exibir os produtos adicionados.
    billsTV.grid(row=5, column=0, columnspan=5, padx=(5))

    # Barra de rolagem vertical para a tabela.
    scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=5, column=3, padx=(300,0),sticky="NSE")
    billsTV.configure(yscrollcommand=scrollBar.set)

    # Configura os cabeçalhos da tabela.
    billsTV.heading('#0', text="Prod Nome")
    billsTV.heading('#1', text="Taxa")
    billsTV.heading('#2', text="Quantidade")
    billsTV.heading('#3', text="Custo")

    # Botão para gerar um cupom fiscal.
    generateBill = Button(window, text="Gerar Cupom Fiscal",font=("bold", 10), width=15, bg='#093249',fg="white", command=lambda:print_bill())
    generateBill.grid(row=1, column=4)

    # Rótulo para exibir o custo total.
    totalCostLabel = Label(window, textvariable=totalCostVar,bg='#093249',fg="white")
    totalCostLabel.grid(row=6, column=1)
    totalCostLabel.config(width=8, height=1)

    # Botão de logout.
    logoutBtn = Button(window, text="Sair", width=15, height=2, font=("bold", 10), bg='#093249', fg="white", command=lambda: iExit())
    logoutBtn.grid(row=6, column=4, pady=(10, 0))

    # Atualiza a visualização da lista de produtos.
    updateListView()


# Janela para adicionar itens 

    def itemAddWindow():
        # Configuração da geometria da janela com as dimensões especificadas
        window.geometry(f"{screen_width}x{screen_height}")

    # Título da janela
    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249', fg="white")
    titleLabel.grid(row=0, column=2, columnspan=3, pady=(10, 0))

    # Rótulo e campo de entrada para o nome do item
    itemNameLabel = Label(window, text="Nome", bg='#093249', fg="white")
    itemNameLabel.grid(row=1, column=1, pady=(10, 0))
    itemNameEntry = Entry(window, textvariable=addItemNameVar)
    itemNameEntry.grid(row=1, column=2, pady=(10, 0))

    # Rótulo e campo de entrada para o preço do item
    itemRateLabel = Label(window, text="Preço", bg='#093249', fg="white")
    itemRateLabel.grid(row=1, column=3, pady=(10, 0))
    itemRateEntry = Entry(window, textvariable=addItemRateVar)
    itemRateEntry.grid(row=1, column=4, pady=(10, 0))

    # Rótulo e campo de entrada para a descrição do item
    itemtypeLabel = Label(window, text="Descrição do Produto", bg='#093249', fg="white")
    itemtypeLabel.grid(row=2, column=1, pady=(10, 0))
    itemTypeEntry = Entry(window, textvariable=addItemTypeVar)
    itemTypeEntry.grid(row=2, column=2, pady=(10, 0))

    # Rótulo e campo de entrada para a classificação por tipagem do item
    storeTypeLabel = Label(window, text="Classificação por tipagem", bg='#093249', fg="white")
    storeTypeLabel.grid(row=2, column=3, pady=(10, 0))
    storeEntry = OptionMenu(window, addstoredVar, *storeOptions)
    storeEntry.grid(row=2, column=4, pady=(10, 0))

    # Botão para adicionar o item à lista
    AddItemButton = Button(window, text="Add Prod", bg='#093249', fg="white", width=20, height=2, command=lambda: addItem())
    AddItemButton.grid(row=3, column=3, pady=(10, 0))

    # Botão para voltar à visualização de todos os itens
    backButton = Button(window, text="Voltar", bg='#093249', fg="white", command=lambda: readAllData())
    backButton.grid(row=6, column=5)
    
# Janela para Atualizar os itens 

    def updateItemWindow():
        # Configuração da geometria da janela com as dimensões especificadas
        window.geometry(f"{screen_width}x{screen_height}")

    # Título da janela
    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249', fg="white")
    titleLabel.grid(row=0, column=2, columnspan=4, pady=(10, 0))

    # Rótulo e campo de entrada para o nome do item
    itemNameLabel = Label(window, text="Nome", bg='#093249', fg="white")
    itemNameLabel.grid(row=1, column=1, pady=(10, 0))
    itemNameEntry = Entry(window, textvariable=addItemNameVar)
    itemNameEntry.grid(row=1, column=2, pady=(10, 0))

    # Rótulo e campo de entrada para o preço do item
    itemRateLabel = Label(window, text="Preço", bg='#093249', fg="white")
    itemRateLabel.grid(row=1, column=3, pady=(10, 0))
    itemRateEntry = Entry(window, textvariable=addItemRateVar)
    itemRateEntry.grid(row=1, column=4, pady=(10, 0))

    # Rótulo e campo de entrada para a descrição do item
    itemtypeLabel = Label(window, text="Descrição do Produto", bg='#093249', fg="white")
    itemtypeLabel.grid(row=2, column=1, pady=(10, 0))
    itemTypeEntry = Entry(window, textvariable=addItemTypeVar)
    itemTypeEntry.grid(row=2, column=2, pady=(10, 0))

    # Rótulo e campo de entrada para a classificação por tipagem do item
    storeTypeLabel = Label(window, text="Classificação por tipagem", bg='#093249', fg="white")
    storeTypeLabel.grid(row=2, column=3, pady=(10, 0))
    storeEntry = OptionMenu(window, addstoredVar, *storeOptions)
    storeEntry.grid(row=2, column=4, pady=(10, 0))

    # Botão para atualizar as informações do item
    AddItemButton = Button(window, text="Atualizar Produto", bg='#093249', fg="white", width=20, height=2, command=lambda: updateItem())
    AddItemButton.grid(row=3, column=3, pady=(10, 0))

    # Configuração e exibição da Treeview para visualizar os itens
    updateTV.grid(row=5, column=0, columnspan=5, padx=(9))
    scrollBar = Scrollbar(window, orient="vertical", command=updateTV.yview)
    scrollBar.grid(row=5, column=4, sticky="NSE")
    updateTV.configure(yscrollcommand=scrollBar.set)

    # Configuração dos cabeçalhos da Treeview
    updateTV.heading('#0', text="Prod ID")
    updateTV.heading('#1', text="Prod Nome")
    updateTV.heading('#2', text="Preço")
    updateTV.heading('#3', text="Tipo")
    updateTV.heading('#4', text="Tipo Estoque")

    # Botão para voltar à visualização de todos os itens
    backButton = Button(window, text="Voltar", bg='#093249', fg="white", command=lambda: readAllData())
    backButton.grid(row=6, column=5)

    # Atualiza a lista de itens na Treeview
    getItemLists()
# Janela de historico para compras 

    def ViewAllBills():
        # Configuração da geometria da janela com as dimensões especificadas
        window.geometry(f"{screen_width}x{screen_height}")

    # Título da janela
    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249', fg="white")
    titleLabel.grid(row=1, column=0, columnspan=4, padx=30, pady=(10, 10))

    # Configuração e exibição da Treeview para visualizar todas as contas
    billsTV.grid(row=5, column=0, columnspan=5, padx=(5))
    scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=5, column=3, padx=(300, 0), sticky="NSE")
    billsTV.configure(yscrollcommand=scrollBar.set)

    # Configuração dos cabeçalhos da Treeview
    billsTV.heading('#0', text="Prod Nome")
    billsTV.heading('#1', text="Taxa")
    billsTV.heading('#2', text="Quantidade")
    billsTV.heading('#3', text="Custo")

    # Botão para voltar à visualização de todos os itens
    backButton = Button(window, text="Voltar", bg='#093249', fg="white", command=lambda: readAllData())
    backButton.grid(row=6, column=5)

    # Atualiza os dados da Treeview com informações sobre as contas
    updateBillsData()
# Chamando a função para criar a janela de login e configurar os elementos da interface
    loginWindow()

# Iniciando o loop principal da interface gráfica, permitindo interações do usuário e eventos
    window.mainloop()
    

CUPOM FISCAL x Nota Fiscal 

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/b593370e-675f-4190-b5f3-68ece937cd21)




Não pretendo deixar nenhum link de aula, tampouco dar IB. Não é difícil de encontrar, bastando pesquisar pelo nome no YouTube ou Google (veja os motivos).

1.1. Na minha opinião, o "professor" deixou a desejar. Acredito na beleza de abordar o ensino com humildade, e tenho um temperamento bastante enérgico. Quando me deparo com pessoas que, na minha percepção, agem de maneira um tanto ríspida, acabo desenvolvendo certa aversão. Não quero dizer que não sou grata pela aula, mas devido ao método de ensino que não me agradou muito, acabei buscando MUITA informação por conta própria, quase achei mais facil ter pego as bibliotecas e me virado nos 30 sozinha... Isso foi algo que me causou muito estresse e foi muito difícil, porém, como resultado, acabei aprendendo mais do que teria aprendido se ele tivesse explicado de forma mais clara ou explicado de fato.

1.2. Ao final das aulas, planejava deixar um comentário agradecendo e mencionando pontos que talvez pudessem ser melhorados. É claro que não tinha intenção de atacar, pois isso não é necessário, mas ele mesmo deixou claro que esse tipo de comentário é apagado. Logo, compreendi a razão pela qual não recebe muita visibilidade.

1.3. Na metade das aulas, estava começando a compreender o assunto e, de repente, foi informado que o código havia sido completamente alterado, sem qualquer explicação, nem mesmo uma indicação de onde, algo como "pegue lá no GitHub, porque se não estiver desse jeito, não vai funcionar". Gosto de seguir as aulas, porém sempre faço do meu jeito. Não sou fã de simplesmente copiar e colar. No entanto, sem conhecer a alteração, fica complicado entender por que algo não funcionaria e pensar em alguma alternativa, como foi feito em alguns pontos.

1.4. Desmotivar os iniciantes durante as aulas é algo terrível, pois isso afeta muitas pessoas. Se você não é afetado, ótimo. Mas, por exemplo, se estou passando por um momento difícil na vida, me esforçando, e ouço um "professor" desmotivador, é bastante frustrante.

1.5. Além de desmotivar os alunos, também fica evidente que o próprio professor também demonstra certa preguiça, acho hipocrisia desanimar quem está apenas querendo aprender sendo que ele é igual.

Lembrando que essa é a minha opinião e meu ponto de vista. Não gostei e também não busquei ficar reclamando disso no email, comentarios ou qualquer outra forma de contato. Se ele não gosta de ouvir coisas que podem ser interpretadas como críticas, tudo bem. Agradeço pelas aulas, o estresse e os dias que poderiam ter sido mais tranquilos foram, na verdade, de muito aprendizado.

Cada pessoa tem a sua própria forma de ver, entender, absorver e transmitir. Para quem gosta, tudo bem, aproveite e seja feliz. Infelizmente, eu não recomendo e não pretendo fazer mais nenhum curso com esse "professor", pois isso não se alinha às minhas necessidades. É isso. Se você leu tudo isso ( eu mesma talvez não teria lido😅 ) e quiser me falar algo devido à ausência do IB, aqui está um esboço de explicação, não que eu deva alguma ahahahah xD  um xero.
