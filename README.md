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

      window = Tk()
      window.geometry("900x600")
      window.title("Faturamentos em Python | padilhajordane@gmail.com")
      window.configure(bg='#093249')
      
![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/2a00d929-0ffc-4cce-a941-9e4b5ae00762)


  #  imagem de plano de fundo na janela da interface gráfica (Metodo alternatio caso não queira usar cor como background ).

  > image_path = "caminho\da\sua\imagem": Nesta linha, você deveria definir o caminho completo para a imagem que deseja usar como plano de fundo. Essa imagem será carregada da localização especificada.
  > image = Image.open(image_path): Aqui, você estaria abrindo a imagem especificada usando a biblioteca PIL (Python Imaging Library), que é usada para manipular imagens em Python.
  > background_Label = Label(window): Isso cria um widget do tipo Label que será usado para exibir a imagem de plano de fundo. Você o vincula à janela principal (window).
  > background_Label.place(x=0, y=0, relwidth=1, relheight=1): Essa linha define a posição e o tamanho do Label. Neste caso, a imagem do Label ocuparia toda a janela, uma vez que relwidth (largura relativa) e relheight (altura relativa) estão definidos como 1.
  > photo = ImageTk.PhotoImage(image): Aqui, você está criando um objeto PhotoImage do tkinter usando a imagem carregada anteriormente. Isso é necessário para exibir a imagem dentro do widget Label.
  > background_Label.configure(image=photo): Por fim, você está configurando o Label para exibir a imagem carregada por meio do objeto PhotoImage.
  OBS.: Nas minhas pesquisas achei alumas video aulas ensinando modos mais simples, porem esse foi o unico que funcionou para mim.
 
     image_path = "caminho\da\sua\imagem"
     image = Image.open(image_path)
     background_Label = Label(window)
     background_Label.place(x=0, y=0, relwidth=1, relheight=1)
     photo = ImageTk.PhotoImage(image)
     background_Label.configure(image=photo)

![image](https://github.com/SraPadilha/cupom_fiscal/assets/110247189/434ff9a2-a369-4a85-92b5-3432cf31860e)



Não pretendo deixar nenhum link, tampouco dar IB. Não é difícil de encontrar, bastando pesquisar pelo nome no YouTube ou Google (veja os motivos).

1.1. Na minha opinião, o "professor" deixou a desejar. Acredito na beleza de abordar o ensino com humildade, e tenho um temperamento bastante enérgico. Quando me deparo com pessoas que, na minha percepção, agem de maneira um tanto ríspida, acabo desenvolvendo certa aversão. Não quero dizer que não sou grata pela aula, mas devido ao método de ensino que não me agradou muito, acabei buscando MUITA informação por conta própria, quase achei mais facil ter pego as bibliotecas e me virado nos 30 sozinha... Isso foi algo que me causou muito estresse e foi muito difícil, porém, como resultado, acabei aprendendo mais do que teria aprendido se ele tivesse explicado de forma mais clara ou explicado de fato.

1.2. Ao final das aulas, planejava deixar um comentário agradecendo e mencionando pontos que talvez pudessem ser melhorados. É claro que não tinha intenção de atacar, pois isso não é necessário, mas ele mesmo deixou claro que esse tipo de comentário é apagado. Logo, compreendi a razão pela qual não recebe muita visibilidade.

1.3. Na metade das aulas, estava começando a compreender o assunto e, de repente, foi informado que o código havia sido completamente alterado, sem qualquer explicação, nem mesmo uma indicação de onde, algo como "pegue lá no GitHub, porque se não estiver desse jeito, não vai funcionar". Gosto de seguir as aulas, porém sempre faço do meu jeito. Não sou fã de simplesmente copiar e colar. No entanto, sem conhecer a alteração, fica complicado entender por que algo não funcionaria e pensar em alguma alternativa como foi feito em alguns pontos.

1.4. Desmotivar os iniciantes durante as aulas é algo terrível, pois isso afeta muitas pessoas. Se você não é afetado, ótimo. Mas, por exemplo, se estou passando por um momento difícil na vida, me esforçando, e ouço um "professor" desmotivador, é bastante frustrante.

1.5. Além de desmotivar os alunos, também fica evidente que o próprio professor também demonstra certa preguiça, tornando difícil acompanhar as aulas.

Lembrando que essa é a minha opinião e meu ponto de vista. Não gostei e também não busquei ficar reclamando disso no email, comentarios ou qualquer outra forma de contato. Se ele não gosta de ouvir coisas que podem ser interpretadas como críticas, tudo bem. Agradeço pelas aulas, o estresse e os dias que poderiam ter sido mais tranquilos foram, na verdade, de muito aprendizado.

Cada pessoa tem a sua própria forma de ver, entender, absorver e transmitir. Para quem gosta, tudo bem, aproveite e seja feliz. Infelizmente, eu não recomendo e não pretendo fazer mais nenhum curso com esse "professor", pois isso não se alinha às minhas necessidades. É isso. Se você leu tudo isso , eu mesma talvez não tivesse lido,  quiser me falar algo devido à ausência do IB, aqui está um esboço de explicação, não que eu deva alguma ahahahah xD  um xero.
