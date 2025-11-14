import flet as ft
from datetime import datetime
import pymongo
from pymongo import MongoClient

class Fabidoces:
    def __init__(self, page: ft.Page ):
        self.page = page
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.bgcolor = ft.Colors.PINK_50
        self.page.window.width = 350
        self.page.window.height = 600
        self.page.window.resizable = True
        self.page.window.always_on_top = True
        self.page.title = 'Fabidoces'
        self.pedido = []
        self.check_ano()
        self.main_page()

    def check_ano(self):
        
            client = MongoClient("mongodb+srv://admin:jaGGlBYiaMNYv1If@fabidocesdb.yrklu8c.mongodb.net/?appName=fabidocesdb")
            db = client['fabidoces']
            colecao = db['ped_numeracao']
            ano_actual = datetime.now().year
            cursor = colecao.find()
            for item in cursor:
                if item['ano_atual'] != ano_actual:
                    colecao.update_one({'ano_atual':item['ano_atual']},{"$set":{'ano_atual':ano_actual,'ped_numero':0}})
            client.close()
    
    def main_page(self):
        
        #******************    Variaveis - Inicio      *************************************
        
        CONNECTION_STRING = "mongodb+srv://admin:jaGGlBYiaMNYv1If@fabidocesdb.yrklu8c.mongodb.net/?appName=fabidocesdb"
        recheio_bd = []
        salgados = []
        doce_doe = []
        doce_dot = []
        pesq_param = []
        
        data_agenda = datetime.now().strftime('%d/%m/%Y')
        
        quant_bd = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_topo_bd = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_bv = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_td = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_tdd = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_topo_tdd = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_ts = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_cup = ft.Text(value="1", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD,width=45)
        quant_dot = ft.Text(value="25", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD, width=60)
        quant_doe = ft.Text(value="25", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD, width=60)
        quant_salg = ft.Text(value="25", text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD, width=60)
        
        valor_topo_bd = ft.TextField(value='',label='R$',width=120,text_align='right',
                                    on_change=lambda e:valor_parcial_item(e,'topo_bd'))
        valor_topo_tdd = ft.TextField(value='',label='R$',width=120,text_align='right',
                                    on_change=lambda e:valor_parcial_item(e,'topo_tdd'))
        valor_un_bd = ft.TextField(value='',label='R$',width=120,text_align='right',
                                on_change=lambda e:valor_parcial_item(e,'Bolo Decorado'))
        valor_un_bv = ft.TextField(value='',label='R$',width=120,text_align='right',
                                on_change=lambda e:valor_parcial_item(e,'Bolo Vulcão'))
        valor_un_td = ft.TextField(value='',label='R$',width=120,text_align='right',
                                on_change=lambda e:valor_parcial_item(e,'Torta'))
        valor_un_tdd = ft.TextField(value='',label='R$',width=120,text_align='right',
                                on_change=lambda e:valor_parcial_item(e,'Torta Decorada'))
        valor_un_ts = ft.TextField(value='',label='R$',width=120,text_align='right',
                                on_change=lambda e:valor_parcial_item(e,'Torta Salgada'))
        valor_un_cup = ft.TextField(label='R$',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Cupcake'))
        valor_cent_doe = ft.TextField(label='R$',width=120,
                            on_change=lambda e:valor_parcial_item(e,'Docesp'))
        valor_cent_dot = ft.TextField(label='R$',width=120,
                            on_change=lambda e:valor_parcial_item(e,'Docest'))
        valor_cent_salg = ft.TextField(label='R$',width=120,
                            on_change=lambda e:valor_parcial_item(e,'Salgados'))
        
        total_bd = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_bv = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_td = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_tdd = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_ts = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_cup = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_dot = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_doe = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_salg = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_arroz_gal = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_arroz_para = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_bem_cas = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_empadao = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_sobremesa = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_pudim = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_taca = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_ts_esp = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        total_diversos = ft.Text(size=20, color=(ft.Colors.RED_900),text_align=(ft.TextAlign.CENTER),weight=ft.FontWeight.BOLD)
        
        tam_bd = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='10 cm',label='10 cm'),
                ft.Radio(value='12 cm',label='12 cm'),
                ft.Radio(value='15 cm',label='15 cm'),
                ft.Radio(value='20 cm',label='20 cm'),
                ft.Radio(value='25 cm',label='25 cm'),
                ft.Radio(value='30 cm',label='30 cm'),
                ft.Radio(value='35 cm',label='35 cm'),
                ft.Radio(value='40 cm',label='40 cm'),
                ft.Radio(value='Outro',label='Outro'),
            ],wrap=True,height=180)
        )
        niveis_bd = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='1 andar',label='1 andar'),
                ft.Radio(value='2 andares',label='2 andares'),
                ft.Radio(value='3 andares',label='3 andares'),
                ft.Radio(value='+ de 3',label='+ de 3'),
                
            ],wrap=True,height=180)
        )
        tam_bv= ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='Pequeno',label='Pequeno'),
                ft.Radio(value='Médio',label='Médio'),
                ft.Radio(value='Grande',label='Grande'),
            ])
        )
        tam_td = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                height=180,
                controls=[
                    ft.Radio(value='10 cm',label='10 cm'),
                    ft.Radio(value='12 cm',label='12 cm'),
                    ft.Radio(value='15 cm',label='15 cm'),
                    ft.Radio(value='20 cm',label='20 cm'),
                    ft.Radio(value='25 cm',label='25 cm'),
                    ft.Radio(value='30 cm',label='30 cm'),
                    ft.Radio(value='35 cm',label='35 cm'),
                    ft.Radio(value='40 cm',label='40 cm'),
                    ft.Radio(value='Outro',label='Outro'),
                ]
            )
        )
        tam_tdd = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                height=180,
                controls=[
                    ft.Radio(value='10 cm',label='10 cm'),
                    ft.Radio(value='12 cm',label='12 cm'),
                    ft.Radio(value='15 cm',label='15 cm'),
                    ft.Radio(value='20 cm',label='20 cm'),
                    ft.Radio(value='25 cm',label='25 cm'),
                    ft.Radio(value='30 cm',label='30 cm'),
                    ft.Radio(value='35 cm',label='35 cm'),
                    ft.Radio(value='40 cm',label='40 cm'),
                    ft.Radio(value='Outro',label='Outro'),
                ]
            )
        )
        tam_ts = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='1 Pão',label='1 Pão'),
                ft.Radio(value='2 Pães',label='2 Pães'),
                ft.Radio(value='3 Pães',label='3 Pães'),
            ])
        )
        
        massa_bd = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                height=120,
                controls=[
                    ft.Radio(value='Branca',label='Branca'),
                    ft.Radio(value='Black',label='Black'),
                    ft.Radio(value='Chocolate',label='Chocolate'),
                    ft.Radio(value='Mista',label='Mista'),
                    ft.Radio(value='Red Velvet',label='Red Velvet'),
                    ft.Radio(value='Outra',label='Outra'),
                ])
        )
        massa_td = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                height=120,
                controls=[
                    ft.Radio(value='Branca',label='Branca'),
                    ft.Radio(value='Black',label='Black'),
                    ft.Radio(value='Chocolate',label='Chocolate'),
                    ft.Radio(value='Mista',label='Mista'),
                    ft.Radio(value='Red Velvet',label='Red Velvet'),
                    ft.Radio(value='Outra',label='Outra'),
                ])
        )
        massa_tdd = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                height=120,
                controls=[
                    ft.Radio(value='Branca',label='Branca'),
                    ft.Radio(value='Black',label='Black'),
                    ft.Radio(value='Chocolate',label='Chocolate'),
                    ft.Radio(value='Mista',label='Mista'),
                    ft.Radio(value='Red Velvet',label='Red Velvet'),
                    ft.Radio(value='Outra',label='Outra'),
                ])
        )
        
        acab_bd = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value='Chantilly',label='Chantilly'),
                ft.Radio(value='Ganache',label='Ganache'),
                ft.Radio(value='Outro',label='Outro'),
            ])
        )
        acab_tdd = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value='Chantilly',label='Chantilly'),
                ft.Radio(value='Ganache',label='Ganache'),
                ft.Radio(value='Outro',label='Outro'),
            ])
        )
        
        tema_bd = ft.TextField(label='Tema:',width=350,capitalization=(ft.TextCapitalization.WORDS))
        tema_tdd = ft.TextField(label='Tema:',width=350,capitalization=(ft.TextCapitalization.WORDS))
        
        topo_bd = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                height=350,
                controls=[
                    ft.Radio(value='Chantilly',label='Chantilly',toggleable=True),
                    ft.Radio(value='Flores Artificiais',label='Flores Artificiais',toggleable=True),
                    ft.Radio(value='Flores Naturais',label='Flores Naturais',toggleable=True),
                    ft.Radio(value='Flores em Papelaria',label='Flores em Papelaria',toggleable=True),
                    ft.Radio(value='Glitter',label='Glitter',toggleable=True),
                    ft.Radio(value='Topo 3D',label='Topo 3D',toggleable=True),
                    ft.Radio(value='Topo em Camada',label='Topo em Camada',toggleable=True),
                    ft.Radio(value='Topo Simples',label='Topo Simples',toggleable=True),
                ])
        )
        topo_tdd = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                height=350,
                controls=[
                    ft.Radio(value='Chantilly',label='Chantilly',toggleable=True),
                    ft.Radio(value='Flores Artificiais',label='Flores Artificiais',toggleable=True),
                    ft.Radio(value='Flores Naturais',label='Flores Naturais',toggleable=True),
                    ft.Radio(value='Flores em Papelaria',label='Flores em Papelaria',toggleable=True),
                    ft.Radio(value='Glitter',label='Glitter',toggleable=True),
                    ft.Radio(value='Topo 3D',label='Topo 3D',toggleable=True),
                    ft.Radio(value='Topo em Camada',label='Topo em Camada',toggleable=True),
                    ft.Radio(value='Topo Simples',label='Topo Simples',toggleable=True),
                ])
        )
        
        sabor_td = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='Abacaxi',label='Abacaxi'),
                ft.Radio(value='Chocolate',label='Chocolate'),
                ft.Radio(value='Cupuaçu',label='Cupuaçu'),
                ft.Radio(value='Maracuja',label='Maracuja'),
                ft.Radio(value='Morango',label='Morango'),
            ])
        )
        sabor_tdd = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='Abacaxi',label='Abacaxi'),
                ft.Radio(value='Bacuri - Mª Isabel',label='Bacuri - Mª Isabel'),
                ft.Radio(value='Chocolate',label='Chocolate'),
                ft.Radio(value='Cupuaçu',label='Cupuaçu'),
                ft.Radio(value='Cupuaçu - Mª Isabel',label='Cupuaçu - Mª Isabel'),
                ft.Radio(value='Maracuja',label='Maracuja'),
                ft.Radio(value='Morango',label='Morango'),
            ])
        )
        
        forma_cor_cup = ft.TextField(label='Cor da forma:',width=350,capitalization=(ft.TextCapitalization.WORDS))
        
        gram_docesp = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                #height=100,
                controls=[
                ft.Radio(value='12 Gramas',label='12 Gramas'),
                ft.Radio(value='14 Gramas',label='14 Gramas'),
                ft.Radio(value='Outra',label='Outra'),
            ])
        )
        
        tipo_caixa_docesp = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                #height=100,
                controls=[
                ft.Radio(value='Caixa Normal',label='Caixa Normal'),
                ft.Radio(value='Caixa 4 Pontas',label='Caixa 4 Pontas'),
                ft.Radio(value='Margarida',label='Margarida'),
                ft.Radio(value='Outra',label='Outra'),
            ])
        )
        
        cor_caixa_docesp = ft.TextField(label='Cor da caixa:',width=310,capitalization=(ft.TextCapitalization.WORDS))
        
        cor_tap_docesp = ft.TextField(label='Cor do tapetinho:',width=310,capitalization=(ft.TextCapitalization.WORDS))
        
        gram_docest = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                #height=100,
                controls=[
                ft.Radio(value='12 Gramas',label='12 Gramas'),
                ft.Radio(value='14 Gramas',label='14 Gramas'),
                ft.Radio(value='Outra',label='Outra'),
            ])
        )
        
        tipo_caixa_docest = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                #height=100,
                controls=[
                    ft.Radio(value='Caixa Normal',label='Caixa Normal'),
                    ft.Radio(value='Caixa 4 Pontas',label='Caixa 4 Pontas'),
                    ft.Radio(value='Margarida',label='Margarida'),
                    ft.Radio(value='Outra',label='Outra'),
            ])
        )
        
        cor_caixa_docest = ft.TextField(label='Cor da caixa:',width=310,capitalization=(ft.TextCapitalization.WORDS))
        
        cor_tap_docest = ft.TextField(label='Cor do tapetinho:',width=310,capitalization=(ft.TextCapitalization.WORDS))
        
        valor_arroz_gal = ft.TextField(label='R$',width=120,on_change=lambda e:valor_parcial_item(e,'Arroz_gal'))
        quant_arroz_gal = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                #height=100,
                controls=[
                ft.Radio(value='2 litros',label='2 litros'),
                ft.Radio(value='3 litros',label='3 litros'),
                ft.Radio(value='4 litros',label='4 litros'),
                ft.Radio(value='5 litros',label='5 litros'),
                ft.Radio(value='6 litros',label='6 litros'),
            ])
        )
        
        valor_arroz_para = ft.TextField(label='R$',width=120,on_change=lambda e:valor_parcial_item(e,'Arroz_para'))
        quant_arroz_para = ft.RadioGroup(
            content=ft.Column(
                wrap=True,
                #height=100,
                controls=[
                ft.Radio(value='2 litros',label='2 litros'),
                ft.Radio(value='3 litros',label='3 litros'),
                ft.Radio(value='4 litros',label='4 litros'),
                ft.Radio(value='5 litros',label='5 litros'),
                ft.Radio(value='6 litros',label='6 litros'),
            ])
        )
        
        valor_un_bem_cas = ft.TextField(value='',label='R$',text_align='right',width=120,
                                        on_change=lambda e:valor_parcial_item(e,'Bem Casados'))
        quant_bem_cas = ft.TextField(value='1',label='Unidades',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Bem Casados'))
        
        valor_empadao = ft.TextField(value='',label='R$',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Empadão'))
        tam_empadao = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='20 cm',label='20 cm'),
                ft.Radio(value='25 cm',label='25 cm'),
            ])
        )
        
        valor_pudim = ft.TextField(value='',label='R$',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Pudim'))
        tam_pudim = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='1 Kg',label='1 Kg'),
                ft.Radio(value='2 Kg',label='2 Kg'),
            ])
        )
        
        sabor_sobremesa = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='Bombom de Uva',label='Bombom de Uva'),
                ft.Radio(value='Delicia de Abacaxi',label='Delicia de Abacaxi'),
                ft.Radio(value='Mousse de Maracujá',label='Mousse de Maracujá'),
                ft.Radio(value='Pavê de Bacuri',label='Pavê de Bacuri'),
                ft.Radio(value='Pavê de Cupuaçu',label='Pavê de Cupuaçu'),
            ])
        )
        
        quant_sobremesa = ft.TextField(value='1',label='Unidades',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Sobremesa'))
        valor_un_sobremesa = ft.TextField(value='',label='R$',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Sobremesa'))
        
        tam_vol_taca = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='2,5 litros',label='2,5 litros'),
                ft.Radio(value='5 litros',label='5 litros'),
            ])
        )
        
        valor_taca = ft.TextField(value='',label='R$',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Taça da Felicidade'))
        
        sabor_ts_esp = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='Atum',label='Atum'),
                ft.Radio(value='Camarão',label='Camarão'),
                ft.Radio(value='Legumes',label='Legumes'),
            ])
        )
        
        tam_ts_esp = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='1 Pão',label='1 Pão'),
                ft.Radio(value='2 Pães',label='2 Pães'),
                ft.Radio(value='3 Pães',label='3 Pães'),
            ])
        )
        
        quant_ts_esp = ft.TextField(value='1',label='Unidades',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Torta Salg Esp'))
        valor_ts_esp = ft.TextField(value='',label='R$',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Torta Salg Esp'))
        
        descricao_diversos = ft.TextField(value='',label='Descrição',text_align='left',width=350)
        
        valor_diversos = ft.TextField(value='',label='R$',text_align='right',width=120,
                                    on_change=lambda e:valor_parcial_item(e,'Diversos'))
        
        pesquisa_data_c = ft.TextField(label='Data de Entrega:',expand=True)
        
        pesquisa_nome = ft.TextField(label='Nome do cliente:',capitalization=(ft.TextCapitalization.WORDS),
                                    expand=True)
        pesquisa_servico = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value='Retirada',label='Retirada'),
                ft.Radio(value='Delivery',label='Delivery'),
            ])
        )
        
        pesquisa_tema = ft.TextField(label='Tema:',capitalization=(ft.TextCapitalization.WORDS),
                                    expand=True)
        
        pesquisa_num_pedido = ft.TextField(label='Nº do Pedido: ex:numero/aaaa',
                                    expand=True)
        
        total_pedido = ft.Text(size=20, color=(ft.Colors.RED),text_align=(ft.TextAlign.CENTER),
                            weight=ft.FontWeight.BOLD)

        #******************    Variaveis - Fim      ******************************************
        
        #****************** Componentes - Inicio *********************************************
        class icon_btn_rem(ft.IconButton):            
            def __init__(self,on_click):
                super().__init__()
                self.icon = ft.Icons.REMOVE
                self.bgcolor = ft.Colors.RED_300
                self.icon_color = ft.Colors.BLACK
                self.on_click = on_click
        
        class icon_btn_add(ft.IconButton):            
            def __init__(self,on_click):
                super().__init__()
                self.icon = ft.Icons.ADD
                self.bgcolor = ft.Colors.GREEN_300
                self.icon_color = ft.Colors.BLACK
                self.on_click = on_click
        
        class btn_cancel(ft.ElevatedButton):
            def __init__(self,text,on_click):
                super().__init__()
                self.text = text
                self.on_click = on_click
                self.icon = ft.Icons.CANCEL
                self.bgcolor = ft.Colors.RED_900
                self.icon_color = ft.Colors.WHITE
                self.color=ft.Colors.WHITE
        
        class btn_confirm(ft.ElevatedButton):
            def __init__(self,text,on_click):
                super().__init__()
                self.text = text
                self.on_click = on_click
                self.icon = ft.Icons.ADD_CIRCLE
                self.bgcolor = ft.Colors.GREEN_900
                self.icon_color = ft.Colors.WHITE
                self.color=ft.Colors.WHITE
        
        class btn_pesquisa_un(ft.IconButton):
            def __init__(self,on_click):
                super().__init__()
                self.icon = ft.Icons.SEARCH
                self.bgcolor = ft.Colors.GREEN_300
                self.icon_color = ft.Colors.BLACK
                self.on_click = on_click

        class btn_imprime_pedido(ft.ElevatedButton):
            def __init__(self,text,on_click):
                super().__init__()
                self.text = text
                self.on_click = on_click
                self.icon = ft.Icons.PRINT
                self.bgcolor = ft.Colors.BLUE
                self.icon_color = ft.Colors.WHITE
                self.color=ft.Colors.WHITE
        
        class btn_imprime_controle(ft.ElevatedButton):
            def __init__(self,text,on_click):
                super().__init__()
                self.text = text
                self.on_click = on_click
                self.icon = ft.Icons.PRINT
                self.bgcolor = ft.Colors.BLUE
                self.icon_color = ft.Colors.WHITE
                self.color=ft.Colors.WHITE
        
        class btn_imprime_tag(ft.ElevatedButton):
            def __init__(self,text,on_click):
                super().__init__()
                self.text = text
                self.on_click = on_click
                self.icon = ft.Icons.PRINT
                self.bgcolor = ft.Colors.BLUE
                self.icon_color = ft.Colors.WHITE
                self.color=ft.Colors.WHITE
        
        btn_return_item = ft.ElevatedButton(
            'Add Itens ao Pedido',
            icon = ft.Icons.ADD_SHOPPING_CART,
            bgcolor = ft.Colors.ORANGE_900,
            icon_color = ft.Colors.WHITE,
            color=ft.Colors.WHITE,
            visible=False,
            on_click = lambda e:pag_sec(e)
        )
        
        tabela_pedido = ft.DataTable(
                        data_row_max_height=float('inf'),
                        border=ft.border.all(1,color=ft.Colors.PINK_200),
                        border_radius=5,
                        width=350,
                        heading_row_color=ft.Colors.PINK_100,
                        column_spacing=5,
                        vertical_lines=ft.border.BorderSide(1,ft.Colors.PINK_200),
                        columns=[
                            ft.DataColumn(ft.Text('Item',weight=ft.FontWeight.BOLD),heading_row_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text('Descrição',weight=ft.FontWeight.BOLD),heading_row_alignment=ft.MainAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text('Valor',weight=ft.FontWeight.BOLD),numeric=True,heading_row_alignment=ft.CrossAxisAlignment.CENTER),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text('')),
                                    ft.DataCell(ft.Text('')),
                                    ft.DataCell(ft.Text('')),
                                ]
                            )
                        ],
                    )
        
        tabela_cliente = ft.DataTable(
            data_row_max_height=float('inf'),
            border=ft.border.all(1,color=ft.Colors.PINK_200),
            border_radius=5,
            width=350,
            heading_row_color=ft.Colors.PINK_100,
            column_spacing=5,
            vertical_lines=ft.border.BorderSide(2,ft.Colors.PINK_200),
            columns=[
                ft.DataColumn(ft.Text('Resumo do Pedido',size=16,weight=ft.FontWeight.BOLD),
                            heading_row_alignment=ft.MainAxisAlignment.CENTER)
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(''))
                    ]
                )
            ]
        )
        
        navigation = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.ADD,label="Pedido"),
                ft.NavigationBarDestination(icon=ft.Icons.SCHEDULE,label="Agenda"),
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH,label="Pesquisa"),
                ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART,label="Carrinho"),
                #ft.NavigationBarDestination(icon=ft.Icons.REPORT,label="Recursos"),
            ],
            on_change=lambda e:navegacao(e),
        )        
        
        header = ft.ListTile(
            #leading=ft.Image(src="/icons/icon-192.png", fit="contain"),
            title=ft.Text("FABIDOCES\n - Qualidade na confeitaria -",
                            text_align='center'),
        )
        
        cabecalho = ft.Container(
            bgcolor=ft.Colors.PINK_100,
            border_radius = 16,
            border=ft.border.all(3,color=ft.Colors.PINK_200),
            content=ft.Column([
                header
            ])
        )
        
        item_pedido = ft.Dropdown(
            options=[
                ft.DropdownOption(key='Bolo',
                                leading_icon=ft.Image(src=f"app/src/assets/icone_bolo.png",width=25,height=25)),
                ft.DropdownOption(key='Torta',
                                leading_icon=ft.Image(src=f"app/src/assets/icone_torta.jpg",width=25,height=25)),
                ft.DropdownOption(key='Cupcake',
                                leading_icon=ft.Image(src=f"app/src/assets/icone_cup.jpg",width=25,height=25)),
                ft.DropdownOption(key='Doces',
                                leading_icon=ft.Image(src=f"app/src/assets/icone_doce.jpg",width=25,height=25)),
                ft.DropdownOption(key='Salgados',
                                leading_icon=ft.Image(src=f"app/src/assets/icone_salgado.jpg",width=25,height=25)),
                ft.DropdownOption(key='Outros',
                                leading_icon=ft.Image(src=f"app/src/assets/icone_conf.jpg",width=25,height=25)),
            ],
            text_align='center',
            text_size=20,
            width=350,
            border_width=3,
            border_radius=16,
            border_color=ft.Colors.PINK_200,
            on_change=lambda e:navegacao(e),
            bgcolor=ft.Colors.WHITE,
            label=ft.Text('Escolher itens do pedido'),
            visible=True,
            #disabled=True,
        )
        
        outros_itens = ft.Dropdown(
            options=[
                ft.DropdownOption(key='Arroz c/ Galinha'),
                ft.DropdownOption(key='Arroz Paraense'),
                ft.DropdownOption(key='Bem Casados'),
                ft.DropdownOption(key='Empadão'),
                ft.DropdownOption(key='Sobremesa'),
                ft.DropdownOption(key='Pudim'),
                ft.DropdownOption(key='Taça da Felicidade'),
                ft.DropdownOption(key='Torta Salg Esp'),
                ft.DropdownOption(key='Diversos'),
            ],
            text_align='center',
            width=300,
            text_size=20,
            border_width=3,
            border_radius=16,
            border_color=ft.Colors.BLUE_800,
            bgcolor=ft.Colors.BLUE_100,
            label=ft.Text('Itens Disponiveis'),
            on_change=lambda e:outros_especificar(e),
        )
        
        form_bd = ft.Column(
            controls=[
                ft.Text('Níveis:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                niveis_bd,
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Tamanho:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                tam_bd,
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Massa:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                ft.Column(
                    controls=[
                    massa_bd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Recheio:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),                                      
                ft.Column(
                    wrap=True,
                    height=180,
                    controls=[
                        rech_bd_leiten := ft.Checkbox(label='Leite Ninho',on_change=lambda _:add_rem_rech('Leite Ninho')),
                        rech_bd_choc := ft.Checkbox(label='Chocolate',on_change=lambda _:add_rem_rech('Chocolate')),
                        rech_bd_docel := ft.Checkbox(label='Doce de Leite',on_change=lambda _:add_rem_rech('Doce de Leite')),
                        rech_bd_casta := ft.Checkbox(label='Castanha',on_change=lambda _:add_rem_rech('Castanha')),
                        rech_bd_cupu := ft.Checkbox(label='Cupuaçu',on_change=lambda _:add_rem_rech('Cupuaçu')),
                    ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Acabamento:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                ft.Column(
                    wrap=True,
                    height=60,
                    controls=[
                        acab_bd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Ornamentação:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                ft.Column([
                    tema_bd,
                    ft.Text('Topo:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                    topo_bd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Column([
                        ft.Text('Valores:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                        ft.Text('Topo/Ornamentação:',size=12,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_topo_bd,
                        ft.Text('Bolo:',size=12,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_un_bd,
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column([
                        ft.Text('Quantidades:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'topo_bd','remove')),
                            quant_topo_bd,
                            icon_btn_add(on_click=lambda e:quantidades(e,'topo_bd','adiciona')),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Bolo Decorado','remove')),
                            quant_bd,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Bolo Decorado','adiciona')),
                        ])
                        
                    ]),
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,weight=ft.FontWeight.BOLD),
                    total_bd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Bolo Decorado')),
                ],alignment=ft.MainAxisAlignment.END,),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                
            ]
        )
        
        form_bv = ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                    ft.Column([
                        tam_bv,
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column(
                        controls=[
                        ft.Text('Quantidade:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Bolo Vulcão','remove')),
                            quant_bv,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Bolo Vulcão','adiciona'))
                        ])
                        
                    ]),
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Column([
                        ft.Text('Valor Unitário:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_un_bv
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column([
                        ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,weight=ft.FontWeight.BOLD),
                        total_bv
                    ])
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Bolo Vulcão')),
                ],alignment=ft.MainAxisAlignment.END),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ]
        )
        
        form_td = ft.Column(
            controls=[
                ft.Text('Tamanho:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                tam_td,
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Sabor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                ft.Column([
                    sabor_td := ft.RadioGroup(
                    content=ft.Column([
                        ft.Radio(value='Abacaxi',label='Abacaxi'),
                        ft.Radio(value='Bacuri - Mª Isabel',label='Bacuri - Mª Isabel'),
                        ft.Radio(value='Chocolate',label='Chocolate'),
                        ft.Radio(value='Cupuaçu',label='Cupuaçu'),
                        ft.Radio(value='Cupuaçu - Mª Isabel',label='Cupuaçu - Mª Isabel'),
                        ft.Radio(value='Maracuja',label='Maracuja'),
                        ft.Radio(value='Morango',label='Morango'),
                    ])
                )
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Massa:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                ft.Column(
                    controls=[
                    massa_td,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Column([
                        ft.Text('Valores:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                        ft.Text('Torta:',size=12,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_un_td,
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column([
                        ft.Text('Quantidades:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Torta','remove')),
                            quant_td,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Torta','adiciona')),
                        ])
                        
                    ]),
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,weight=ft.FontWeight.BOLD),
                    total_td
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Torta'))
                ],alignment=ft.MainAxisAlignment.END,),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ]
        )
        
        form_tdd = ft.Column(
            controls=[
                ft.Text('Tamanho:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                tam_tdd,
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Massa:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                ft.Column(
                    controls=[
                    massa_tdd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Sabor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                ft.Column([
                    sabor_tdd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Acabamento:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                ft.Column(
                    wrap=True,
                    height=60,
                    controls=[
                        acab_tdd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Text('Ornamentação:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                ft.Column([
                    tema_tdd,
                    ft.Text('Topo:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                    topo_tdd,
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Column([
                        ft.Text('Valores:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                        ft.Text('Topo/Ornamentação:',size=12,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_topo_tdd,
                        ft.Text('Torta:',size=12,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_un_tdd,
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column([
                        ft.Text('Quantidades:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'topo_tdd','remove')),
                            quant_topo_tdd,
                            icon_btn_add(on_click=lambda e:quantidades(e,'topo_tdd','adiciona')),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Torta Decorada','remove')),
                            quant_tdd,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Torta Decorada','adiciona')),
                        ])
                        
                    ]),
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,weight=ft.FontWeight.BOLD),
                    total_tdd
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Torta Decorada'))
                ],alignment=ft.MainAxisAlignment.END,),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ]
        )
        
        form_ts = ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                    ft.Column([
                        ft.Text('Tamanho:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        tam_ts,
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column(
                        controls=[
                        ft.Text('Quantidade:',size=17, color=(ft.Colors.GREEN_900),weight=ft.FontWeight.BOLD),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Torta Salgada','remove')),
                            quant_ts,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Torta Salgada','adiciona'))
                        ])
                        
                    ]),
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Column([
                        ft.Text('Valor Unitário:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_un_ts
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column([
                        ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,weight=ft.FontWeight.BOLD),
                        total_ts
                    ])
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Torta Salgada')),
                ],alignment=ft.MainAxisAlignment.END),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ]
        )
        
        form_cup = ft.Column(
            controls=[
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                forma_cor_cup,
                ft.Row([
                    ft.Column([
                        ft.Text('Valor Unitário:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        valor_un_cup
                    ]),
                    ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Column([
                        ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Cupcake','remove')),
                            quant_cup,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Cupcake','adiciona'))
                        ])
                    ])
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,weight=ft.FontWeight.BOLD),
                    total_cup
                ]),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ft.Row([
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Cupcake')),
                ],alignment=ft.MainAxisAlignment.END),
                ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ]
        )
        
        form_docesp = ft.Column([
            ft.Text('Gramatura:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
            gram_docesp,
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Text('Sabores:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
            ft.Column(
                wrap=True,
                height=200,
                controls=[
                    doe_brig_amen := ft.Checkbox(label='Brig c/ Amendoim',on_change=lambda _:add_rem_doces('doe','Brig c/ Amendoim')),
                    doe_casad := ft.Checkbox(label='Casadinho',on_change=lambda _:add_rem_doces('doe','Casadinho')),
                    doe_chu := ft.Checkbox(label='Churros',on_change=lambda _:add_rem_doces('doe','Churros')),
                    doe_coco_q := ft.Checkbox(label='Côco Queimado',on_change=lambda _:add_rem_doces('doe','Côco Queimado')),
                    doe_limao := ft.Checkbox(label='Limão',on_change=lambda _:add_rem_doces('doe','Limão')),
                    doe_marac := ft.Checkbox(label='Maracujá',on_change=lambda _:add_rem_doces('doe','Maracujá')),
                    doe_nin_nut := ft.Checkbox(label='Ninho c/ Nutella',on_change=lambda _:add_rem_doces('doe','Ninho c/ Nutella')),
                    doe_pacoca := ft.Checkbox(label='Paçoca',on_change=lambda _:add_rem_doces('doe','Paçoca')),
                    doe_r_e_j := ft.Checkbox(label='Romeu e Julieta',on_change=lambda _:add_rem_doces('doe','Romeu e Julieta')),
                    doe_uvinha := ft.Checkbox(label='Uvinha',on_change=lambda _:add_rem_doces('doe','Uvinha')),
                ]
            ),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text('Embalagem:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                            tipo_caixa_docesp,
                            cor_caixa_docesp,
                            cor_tap_docesp,
                        ]
                    ),
                ]
            ),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row([
                ft.Column(
                    controls=[
                    ft.Text('Valor/Cento:',size=17,color=ft.Colors.GREEN_900,
                            weight=ft.FontWeight.BOLD),
                    valor_cent_doe
                    ]
                ),
                ft.VerticalDivider(width=9,thickness=3,color=ft.Colors.PINK_200),
                ft.Column(
                    controls=[
                    ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Docesp','remove')),
                            quant_doe,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Docesp','adiciona'))
                            ]
                        )
                    ]
                )
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row([
                ft.Column(
                    controls=[
                        ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,
                            weight=ft.FontWeight.BOLD),
                    ]
                ),
                ft.Column([
                    total_doe
                ])
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Docesp')),
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200)
        ])
        
        form_docest = ft.Column([
            ft.Text('Gramatura:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
            gram_docest,
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Text('Sabores:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
            ft.Column(
                wrap=True,
                height=120,
                controls=[
                    dot_amend := ft.Checkbox(label='Amendoim',on_change=lambda _:add_rem_doces('dot','Amendoim')),
                    dot_brig := ft.Checkbox(label='Brigadeiro',on_change=lambda _:add_rem_doces('dot','Brigadeiro')),
                    dot_brigb := ft.Checkbox(label='Brigadeiro Branco',on_change=lambda _:add_rem_doces('dot','Brigadeiro Branco')),
                    dot_coco := ft.Checkbox(label='Côco',on_change=lambda _:add_rem_doces('dot','Côco')),
                    dot_queijo := ft.Checkbox(label='Queijo',on_change=lambda _:add_rem_doces('dot','Queijo')),
                    dot_rosa := ft.Checkbox(label='Rosinha',on_change=lambda _:add_rem_doces('dot','Rosinha')),
                ]
            ),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row(
                controls=[
                    ft.Column(
                        #wrap=True,
                        #height=250,
                        controls=[
                            ft.Text('Embalagem:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                            tipo_caixa_docest,
                            cor_caixa_docest,
                            cor_tap_docest
                            
                        ]
                    ),
                ]
            ),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row(
                controls=[
                ft.Column(
                    controls=[
                    ft.Text('Valor/Cento:',size=17,color=ft.Colors.GREEN_900,
                            weight=ft.FontWeight.BOLD),
                        valor_cent_dot
                    ]
                ),
                ft.VerticalDivider(width=9,thickness=3,color=ft.Colors.PINK_200),
                ft.Column(
                    controls=[
                    ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                        ft.Row([
                            icon_btn_rem(on_click=lambda e:quantidades(e,'Docest','remove')),
                            quant_dot,
                            icon_btn_add(on_click=lambda e:quantidades(e,'Docest','adiciona'))
                            ]
                        )
                    ]
                ),
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row([
                ft.Column(
                    controls=[
                        ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,
                            weight=ft.FontWeight.BOLD),
                    ]
                ),
                ft.Column([
                    total_dot
                ])
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Docest')),
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200)
        ])
        
        form_salgados = ft.Column([
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ft.Text('Sabores:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
            ft.Column(
                wrap=True,
                height=300,
                controls=[
                    salg_bol := ft.Checkbox(label='Bol. de Queijo', on_change=lambda _:add_rem_salg('Bol. de Queijo')),
                    salg_can := ft.Checkbox(label='Canudinho', on_change=lambda _:add_rem_salg('Canudinho')),
                    salg_cox := ft.Checkbox(label='Coxinha', on_change=lambda _:add_rem_salg('Coxinha')),
                    salg_cro := ft.Checkbox(label='Croquete', on_change=lambda _:add_rem_salg('Croquete')),
                    salg_emp := ft.Checkbox(label='Empada', on_change=lambda _:add_rem_salg('Empada')),
                    salg_enr := ft.Checkbox(label='Enrol. de Salsicha', on_change=lambda _:add_rem_salg('Enrol. de Salsicha')),
                    salg_pas := ft.Checkbox(label='Pastel', on_change=lambda _:add_rem_salg('Pastel')),
                    salg_qui := ft.Checkbox(label='Quibe', on_change=lambda _:add_rem_salg('Quibe')),
                    salg_rca := ft.Checkbox(label='Ris. de Carne', on_change=lambda _:add_rem_salg('Ris. de Carne')),
                    salg_rpq := ft.Checkbox(label='Ris. de Pres e Queijo', on_change=lambda _:add_rem_salg('Ris. de Pres e Queijo')),
                ]
            ),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row([
                ft.Column([
                    ft.Text('Valor/Cento:',size=17,color=ft.Colors.GREEN_900,
                            weight=ft.FontWeight.BOLD),
                    valor_cent_salg
                ]),
                ft.VerticalDivider(width=9,thickness=3,color=ft.Colors.PINK_200),
                ft.Column([
                    ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                    ft.Row([
                        icon_btn_rem(on_click=lambda e:quantidades(e,'Salgados','remove')),
                        quant_salg,
                        icon_btn_add(on_click=lambda e:quantidades(e,'Salgados','adiciona'))
                    ])
                    
                ])
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row([
                ft.Text('Total Parcial:',size=19,color=ft.Colors.RED_900,weight=ft.FontWeight.BOLD),
                total_salg
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,'Salgados')),
            ]),
            ft.Divider(height=9,thickness=3,color=ft.Colors.PINK_200)
        ])
        
        form_outros = ft.Column([
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            outros_itens,
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
        ])
        
        pedido_painel = ft.ExpansionPanelList(
            expand_icon_color=ft.Colors.BLACK,
            elevation=8,
            divider_color=ft.Colors.PINK_200,
            controls=[
                ft.ExpansionPanel(
                    content=ft.Text('Pedidos',size=16,weight=ft.FontWeight.BOLD),
                    header=ft.Text(f"Agenda do Dia: {data_agenda}",size=1,weight=ft.FontWeight.BOLD),
                    bgcolor=ft.Colors.PINK_100,
                    expanded=True,
                )
            ],
        )
        
        pesquisa_painel = ft.ExpansionPanelList(
            expand_icon_color=ft.Colors.BLACK,
            elevation=8,
            divider_color=ft.Colors.PINK_200,
            controls=[
                ft.ExpansionPanel(
                    content=ft.Text('Resultados',size=16,weight=ft.FontWeight.BOLD),
                    header=ft.Text(f"Encontrados",size=16,weight=ft.FontWeight.BOLD),
                    bgcolor=ft.Colors.PINK_100,
                    expanded=True,
                )
            ],
        )
        
        #****************** Componentes - Fim ************************************************
        #****************** Funções - Inicio *************************************************
        def show(e,info):
            print('e:',e)
            #print(e.control.cells[0].content.value)
            #print('Info:',info)
            #print('***',e.control.parent)
            print('Info:',info)
            
        '''
        def imprime_pedido():
            print('************* Pedido - Inicio **************')
            print('--------------------------------------------')
            for dic in self.pedido:
                for k,v in dic.items():
                    if v !='' and v != None:
                        print(k,v)
                print('----------------------------------------')
            print('*************** Pedido - Fim ***************')
            
        '''
        def sucesso(msg):
            self.page.open(
                ft.SnackBar(ft.Text(msg,text_align='center'),duration=2000)
            )
        def erro(msg):
            self.page.open(
                ft.SnackBar(ft.Text(msg,text_align='center'),duration=2000)
            )

        def conecta_bd(tipo):
            if tipo == 'numpedido':
                client = MongoClient(CONNECTION_STRING)
                db = client['fabidoces']
                colecao = db['ped_numeracao']
                return db,colecao
            elif tipo == 'agenda':
                client = MongoClient(CONNECTION_STRING)
                db = client['fabidoces']
                colecao = db['pedidos']
                cursor = colecao.find({'Pedido:.Data da Entrega:':data_agenda})
                return cursor
            elif tipo == 'salvar':
                client = MongoClient(CONNECTION_STRING)
                db = client['fabidoces']
                colecao = db['pedidos']
                return db,colecao
            elif tipo == 'pesquisa':
                client = MongoClient(CONNECTION_STRING)
                db = client['fabidoces']
                colecao = db['pedidos']
                return colecao
            client.close()
        def navegacao(e):
            if e.data == '0':
                self.page.controls.clear()
                self.page.update()
                self.page.controls.append(pag_principal)
                self.page.controls.append(navigation)
            elif e.data == '1':
                self.page.controls.clear()
                self.page.update()
                self.page.controls.append(pag_pedidos)
                self.page.controls.append(navigation)
            elif e.data == '2':
                pedido_painel.controls.clear()
                self.page.controls.clear()
                self.page.controls.append(pag_agenda)
                self.page.controls.append(navigation)
                pedido_agenda()
                self.page.update()
            elif e.data == '3':
                self.page.controls.clear()
                self.page.update()
                self.page.controls.append(pag_pesquisa)
                self.page.controls.append(navigation)
            elif e.data == '4':
                self.page.controls.clear()
                self.page.controls.append(pag_carrinho)
                self.page.controls.append(navigation)
            elif e.data == '5':
                self.page.controls.clear()
                self.page.update()
                self.page.controls.append(pag_relatorios)
                self.page.controls.append(navigation)
            elif e.data == 'Bolo':
                self.page.controls.clear()
                self.page.controls.append(aba_bolo)
                self.page.controls.append(navigation)
            elif e.data == 'Torta':
                self.page.controls.clear()
                self.page.controls.append(aba_torta)
                self.page.controls.append(navigation)
            elif e.data == 'Cupcake':
                self.page.controls.clear()
                self.page.controls.append(aba_cupcake)
                self.page.controls.append(navigation)
            elif e.data == 'Doces':
                self.page.controls.clear()
                self.page.update()
                self.page.controls.append(aba_doces)
                self.page.controls.append(navigation)
            elif e.data == 'Salgados':
                self.page.controls.clear()
                self.page.update()
                self.page.controls.append(aba_salgados)
                self.page.controls.append(navigation)
            elif e.data == 'Outros':
                self.page.controls.clear()
                self.page.update()
                self.page.controls.append(aba_outros)
                self.page.controls.append(navigation)
            self.page.update()
            
        def pag_sec(e):
            self.page.controls.clear()
            self.page.controls.append(pag_item_pedido)
            self.page.controls.append(navigation)
            self.page.update()

        def set_datas(e,data):
            if data == 'p':
                data_p.value = f"{e.control.value.strftime('%d/%m/%Y')}"
            elif data == 'c':
                data_c.value = f"{e.control.value.strftime('%d/%m/%Y')}"
            elif data == 'pesq_data_c':
                pesquisa_data_c.value = f"{e.control.value.strftime('%d/%m/%Y')}"
            self.page.update()

        def set_hora(e):
            hora_c.value = f"{e.control.value.strftime('%H:%M')}"
            self.page.update()
        
        def add_cliente(e):
            if nome.value and data_c.value and servico.value:
                cliente_id = {'Tipo:':'Cliente', 'Nome:':nome.value, 'Endereço:':endereco.value, 'Contato:':contato.value,
                        'Data do Pedido:':data_p.value, 'Data da Entrega:':data_c.value,'Hora da Entrega:':hora_c.value,
                        'Serviço:':servico.value}
                if len(self.pedido)==0:
                    self.pedido.insert(0,cliente_id)
                    #item_pedido.visible = True
                    sucesso('Cliente confirmado!')
                    nome.value = ''
                    endereco.value = ''
                    contato.value = ''
                    data_p.value = ''
                    data_c.value = ''
                    hora_c.value = ''
                    servico.value = ''
                    pag_sec(e)
                else:
                    self.pedido[0] = cliente_id
                    sucesso('Cliente atualizado!')
                    nome.value = ''
                    endereco.value = ''
                    contato.value = ''
                    data_p.value = ''
                    data_c.value = ''
                    hora_c.value = ''
                    servico.value = ''
                    pag_sec(e)
                btn_return_item.visible=True
                #btn_float.visible=True
                carrinho()
                self.page.update()
            else:
                erro('Os campos "Nome", "Data p/ Conclusão" e "Serviço" devem ser preenchidos! ')
        
        def adic_item_ped(e,tipo):
            if tipo == 'Bolo Decorado':
                if valor_un_bd.value == '' or valor_un_bd.value == '0':
                    erro('O valor do item deve ser informado!')
                else:
                    if valor_topo_bd.value == '':
                        recheio = ''
                        for i in range(len(recheio_bd)):
                            if i+1 < len(recheio_bd):
                                recheio += recheio_bd[i] + ' '+'-'+' '
                            else:
                                recheio += recheio_bd[i]
                        item = {'Tipo:':'Bolo Decorado','Níveis:':niveis_bd.value,'Tamanho:':tam_bd.value,'Massa:':massa_bd.value,
                                'Recheio:':recheio,'Acabamento:':acab_bd.value,'Tema:':tema_bd.value,'Valor do Topo:':topo_bd.value,
                                'Quantidade:':quant_bd.value,'Valor Unitário:':valor_un_bd.value, 'Quantidade Topo':'0',
                                'Valor do Topo:':'0','Valor Final:':total_bd.value}
                        self.pedido.append(item)
                        restart_var(e,tipo)
                        sucesso('Item adicionado ao pedido!')
                    else:
                        recheio = ''
                        for i in range(len(recheio_bd)):
                            if i+1 < len(recheio_bd):
                                recheio += recheio_bd[i] + ' '+'-'+' '
                            else:
                                recheio += recheio_bd[i]
                        item = {'Tipo:':'Bolo Decorado','Níveis:':niveis_bd.value,'Tamanho:':tam_bd.value,'Massa:':massa_bd.value,
                                'Recheio:':recheio,'Acabamento:':acab_bd.value,'Tema:':tema_bd.value,'Topo:':topo_bd.value,
                                'Quantidade:':quant_bd.value,'Valor Unitário:':valor_un_bd.value,'Quantidade Topo:':quant_topo_bd.value,
                                'Valor do Topo:':valor_topo_bd.value,'Valor Final:':total_bd.value}
                        self.pedido.append(item)
                        restart_var(e,tipo)
                        sucesso('Item adicionado ao pedido!')
            elif tipo =='Bolo Vulcão':
                if valor_un_bv.value == '' or valor_un_bv.value == '0':
                    erro('Informe o valor do Item!')
                else:
                    item = {'Tipo:':'Bolo Vulcão','Tamanho:':tam_bv.value,'Quantidade:':quant_bv.value,
                            'Valor Unitário:':valor_un_bv.value,
                            'Valor Final:':total_bv.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
            elif tipo =='Torta':
                item = {'Tipo:':'Torta', 'Tamanho:':tam_td.value, 'Massa:':massa_td.value,
                            'Sabor':sabor_td.value, 'Quantidade:':quant_td.value,'Valor Unitário:':valor_un_td.value,
                            'Valor Final:':total_td.value}
                self.pedido.append(item)
                restart_var(e,tipo)
                sucesso('Item adicionado ao pedido!')
            elif tipo =='Torta Decorada':
                if valor_un_tdd.value == '' or valor_un_tdd.value == '0':
                    erro('O valor do bolo deve ser informado!')
                else:
                    if valor_topo_tdd.value == '':
                        item = {'Tipo:':'Torta Decorada', 'Tamanho:':tam_tdd.value, 'Massa:':massa_tdd.value,
                            'Sabor:':sabor_tdd.value,'Acabamento:':acab_tdd.value, 'Tema:':tema_tdd.value, 'Quantidade:':quant_tdd.value, 'Topo:':topo_tdd.value,
                            'Valor do Topo:':'0','Quantidade Topo':quant_topo_tdd,'Valor Unitário:':valor_un_tdd.value,'Valor Final:':total_tdd.value}
                        self.pedido.append(item)
                        restart_var(e,tipo)
                        sucesso('Item adicionado ao pedido!')
                    else:
                        indice = len(self.pedido) + 1
                        item = {'Tipo:':'Torta Decorada', 'Tamanho:':tam_tdd.value, 'Massa:':massa_tdd.value,
                                'Sabor:':sabor_tdd.value, 'Acabamento:':acab_tdd.value, 'Tema:':tema_tdd.value, 'Quantidade:':quant_tdd.value, 'Topo:':topo_tdd.value,
                                'Valor do Topo:':valor_topo_tdd.value,'Valor Unitário:':valor_un_tdd.value,'Valor Final:':total_tdd.value}
                        self.pedido.insert(indice,item)
                        restart_var(e,tipo)
                        sucesso('Item adicionado ao pedido!')
            elif tipo =='Torta Salgada':
                if valor_un_ts.value == '0' or valor_un_ts.value == '':
                    erro('Informar valor do item!')
                else:
                    item = {'Tipo:':'Torta Salgada','Tamanho:':tam_ts.value,'Quantidade:':quant_ts.value,
                            'Valor Unitário:':valor_un_ts.value,'Valor Final:':total_ts.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
            elif tipo =='Cupcake':
                if valor_un_cup.value == '0' or valor_un_cup.value == '':
                    erro('Informe o valor unitário do item!')
                else:
                    item ={'Tipo:':'Cupcake','Cor da Forma:':forma_cor_cup.value,'Quantidade:':quant_cup.value,
                            'Valor por Unidade:':valor_un_cup.value,'Valor Final:':total_cup.value}
                    self.pedido.append(item)
                    restart_var(e,tipo) 
                    sucesso('Item adicionado ao pedido!')
            elif tipo =='Docesp':
                if valor_cent_doe.value == '' or valor_cent_doe.value == '0':
                    erro("Informar valor do item!")
                else:
                    sabores = ''
                    for i in range(len(doce_doe)):
                        if i+1 < len(doce_doe):
                            sabores += doce_doe[i] + ' '+'-'+' '
                        else:
                            sabores += doce_doe[i]
                    item = {'Tipo:':'Doces Especiais','Gramatura:':gram_docesp.value,'Sabores:':sabores,'Quantidade:':quant_doe.value,
                            'Valor do Cento:':valor_cent_doe.value,'Valor Final:':total_doe.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    valor_parcial_item(e,tipo)
                    sucesso('Item adicionado ao pedido!')
            elif tipo =='Docest':
                if valor_cent_dot.value == '' or valor_cent_dot.value == '0':
                    erro("Informar valor do item!")
                else:
                    sabores = ''
                    for i in range(len(doce_dot)):
                        if i+1 < len(doce_dot):
                            sabores += doce_dot[i] + ' '+'-'+' '
                        else:
                            sabores += doce_dot[i]
                    item = {'Tipo:':'Doces Tradicionais','Gramatura:':gram_docest.value,'Sabores:':sabores,'Quantidade:':quant_dot.value,
                            'Valor do Cento:':valor_cent_dot.value,'Valor Final:':total_dot.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    valor_parcial_item(e,tipo)
                    sucesso('Item adicionado ao pedido!')
            elif tipo =='Salgados':
                if valor_cent_salg.value == '' or valor_cent_salg.value == '0':
                    erro('Informar valor do item!')
                else:
                    sabores = ''
                    for i in range (len(salgados)):
                        if i+1 < len(salgados):
                            sabores += salgados[i] + ' '+'-'+' '
                        else:
                            sabores += salgados[i]
                    item = {'Tipo:':'Salgados','Sabores:':sabores,'Quantidade:':quant_salg.value,
                            'Valor do Cento:':valor_cent_salg.value,'Valor Final:':total_salg.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    valor_parcial_item(e,tipo)
                    sucesso('Item adicionado ao pedido!')
            elif tipo =='Arroz c/ Galinha':
                if valor_arroz_gal.value != '0' and valor_arroz_gal.value != '' and quant_arroz_gal.value !='':
                    item ={'Tipo:':'Arroz c/ Galinha','Quantidade:':quant_arroz_gal.value,'Valor Final:':valor_arroz_gal.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor e/ou quantidade!')
            elif tipo =='Arroz Paraense':
                if valor_arroz_para.value != '0' and valor_arroz_para.value != '' and quant_arroz_para.value !='':
                    item ={'Tipo:':'Arroz Paraense','Quantidade:':quant_arroz_para.value,'Valor Final:':valor_arroz_para.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor e/ou quantidade!')
            elif tipo =='Bem Casados':
                if valor_un_bem_cas.value != '0' and valor_un_bem_cas.value != '' and quant_bem_cas.value != '0' and quant_bem_cas.value != '':
                    item ={'Tipo:':'Bem Casados','Quantidade:':quant_bem_cas.value,'Valor Unitario:':valor_un_bem_cas.value,
                        'Valor Final:':total_bem_cas.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor e/ou quantidade!')
            elif tipo =='Empadão':
                if valor_empadao.value !='0' and valor_empadao.value !='' and tam_empadao.value !='':
                    item ={'Tipo:':'Empadão','Tamanho:':tam_empadao.value,'Valor Final:':total_empadao.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor e/ou quantidade!')
            elif tipo =='Sobremesa':
                if quant_sobremesa.value > '0' and valor_un_sobremesa.value > '0' and valor_un_sobremesa !='':
                    item ={'Tipo:':'Sobremesa','Sabor:':sabor_sobremesa.value,'Quantidade:':quant_sobremesa.value,
                            'Valor Unitario:':valor_un_sobremesa.value,'Valor Final:':total_sobremesa.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Todos o campos devem ser preenchidos!')
            elif tipo =='Pudim':
                if valor_pudim.value !='0' and valor_pudim.value !='' and tam_pudim.value !='':
                    item ={'Tipo:':'Pudim','Tamanho:':tam_pudim.value,'Valor Final:':total_pudim.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor e/ou quantidade!')
            elif tipo =='Taça da Felicidade':
                if valor_taca.value !='0' and valor_taca.value !='':
                    item ={'Tipo:':'Taça da Felicidade','Tamanho:':tam_vol_taca.value,'Valor Final:':total_taca.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor!')
            elif tipo =='Torta Salg Esp':
                if valor_ts_esp.value != '0' and valor_ts_esp.value !='' and int(quant_ts_esp.value)>0:
                    item ={'Tipo:':'Torta Salg Esp','Sabor:':sabor_ts_esp.value,'Tamanho:':tam_ts_esp.value,
                            'Quantidade:':quant_ts_esp.value,'Valor Unitario:':valor_ts_esp.value,'Valor Final:':total_ts_esp.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor e/ou quantidade!')
            elif tipo =='Diversos':
                if valor_diversos.value !='0' and valor_diversos.value !='' and descricao_diversos.value !='':
                    item = {'Tipo:':'Diversos','Descrição:':descricao_diversos.value,'Valor Nominal:':valor_diversos.value,
                            'Valor Final:':total_diversos.value}
                    self.pedido.append(item)
                    restart_var(e,tipo)
                    sucesso('Item adicionado ao pedido!')
                else:
                    erro('Informe o valor e/ou descrição!')
            valor_total()
            carrinho()
            item_pedido.value = None
            self.page.update()
            
        def restart_var(e,tipo):
            if tipo == 'Bolo Decorado':
                recheio_bd.clear()
                niveis_bd.value = False
                tam_bd.value = False
                massa_bd.value = False
                rech_bd_casta.value = False
                rech_bd_choc.value = False
                rech_bd_cupu.value = False
                rech_bd_docel.value = False
                rech_bd_leiten.value = False
                acab_bd.value = False
                tema_bd.value = ''
                topo_bd.value = False
                quant_bd.value = '1'
                valor_topo_bd.value = ''
                valor_un_bd.value = ''
                total_bd.value = ''
            elif tipo =='Bolo Vulcão':
                tam_bv.value = False
                quant_bv.value = '1'
                valor_un_bv.value = ''
                total_bv.value = ''
            elif tipo =='Torta':
                tam_td.value = False
                massa_td.value = False
                sabor_td.value = False
                quant_td.value = '1'
                valor_un_td.value = ''
                total_td.value = ''
            elif tipo =='Torta Decorada':
                tam_tdd.value = False
                massa_tdd.value = False
                sabor_tdd.value = False
                acab_tdd.value = False
                tema_tdd.value = ''
                quant_tdd.value = '1'
                topo_tdd.value = False
                valor_topo_tdd.value = ''
                valor_un_tdd.value = ''
                total_tdd.value = ''
            elif tipo =='Torta Salgada':
                tam_ts.value = False
                quant_ts.value = '1'
                valor_un_ts.value = ''
                total_ts.value = ''
            elif tipo =='Cupcake':
                forma_cor_cup.value = ''
                quant_cup.value = '1'
                valor_un_cup.value = ''
                total_cup.value = ''
            elif tipo =='Docesp':
                doce_doe.clear()
                doe_brig_amen.value = False
                doe_casad.value = False
                doe_chu.value = False
                doe_coco_q.value = False
                doe_limao.value = False 
                doe_marac.value = False
                doe_nin_nut.value = False
                doe_pacoca.value = False
                doe_r_e_j.value = False
                doe_uvinha.value = False
                tipo_caixa_docesp.value = ''
                cor_caixa_docesp.value = ''
                cor_tap_docesp.value = ''
                gram_docesp.value = False
                quant_doe.value = '25'
                valor_cent_doe.value = ''
                total_doe.value = ''
            elif tipo =='Docest':
                doce_dot.clear()
                dot_brig.value = False
                dot_amend.value = False
                dot_brigb.value = False
                dot_coco.value = False
                dot_queijo.value = False
                dot_rosa.value = False
                tipo_caixa_docest.value = ''
                cor_caixa_docest.value = ''
                cor_tap_docest.value = ''
                gram_docest.value = False
                quant_dot.value = '25'
                valor_cent_dot.value = ''
                total_dot.value = ''
            elif tipo =='Salgados':
                salgados.clear()
                salg_bol.value = False
                salg_can.value = False
                salg_cox.value = False
                salg_cro.value = False
                salg_emp.value = False
                salg_enr.value = False
                salg_pas.value = False
                salg_qui.value = False
                salg_rca.value = False
                salg_rpq.value = False
                quant_salg.value = '25'
                valor_cent_salg.value = ''
                total_salg.value = ''
            elif tipo =='Arroz c/ Galinha':
                quant_arroz_gal.value = ''
                valor_arroz_gal.value = ''
                total_arroz_gal.value = ''
            elif tipo =='Arroz Paraense':
                quant_arroz_para.value = ''
                valor_arroz_para.value = ''
                total_arroz_para.value = ''
            elif tipo =='Bem Casados':
                quant_bem_cas.value = '1'
                valor_un_bem_cas.value = ''
                total_bem_cas.value = ''
            elif tipo =='Empadão':
                tam_empadao.value = ''
                valor_empadao.value = ''
                total_empadao.value = ''
            elif tipo =='Sobremesa':
                sabor_sobremesa.value = ''
                quant_sobremesa.value = '1'
                valor_un_sobremesa.value = ''
                total_sobremesa.value = ''
            elif tipo =='Pudim':
                tam_pudim.value = ''
                valor_pudim.value = ''
                total_pudim.value = ''
            elif tipo =='Taça da Felicidade':
                tam_vol_taca.value = ''
                valor_taca.value = ''
                total_taca.value = ''
            elif tipo =='Torta Salg Esp':
                sabor_ts_esp.value = ''
                tam_ts_esp.value = ''
                quant_ts_esp.value = '1'
                valor_ts_esp.value = ''
                total_ts_esp.value = ''
            elif tipo =='Diversos':
                valor_diversos.value = ''
                descricao_diversos.value = ''
                total_diversos.value = ''
            elif tipo == 'Salvar':
                self.pedido.clear()
                tabela_cliente.rows.clear()
                total_pedido.value = ''
                carrinho()
                e.data = '1'
                navegacao(e)
            item_pedido.value = None
            self.page.update()
        
        def quantidades(e,tipo,action):
            if tipo == 'Bolo Decorado':
                if action == 'remove':
                    if int(quant_bd.value) > 1:
                        quant_bd.value = str(int(quant_bd.value) - 1)
                        quant_bd.value = int(quant_bd.value)
                elif action == 'adiciona':
                    quant_bd.value = str(int(quant_bd.value) + 1)
                    quant_bd.value = int(quant_bd.value)
            elif tipo == 'topo_bd':
                if action == 'remove':
                    if int(quant_topo_bd.value) > 1:
                        quant_topo_bd.value = str(int(quant_topo_bd.value) - 1)
                        quant_topo_bd.value = int(quant_topo_bd.value)
                elif action == 'adiciona':
                    quant_topo_bd.value = str(int(quant_topo_bd.value) + 1)
                    quant_topo_bd.value = int(quant_topo_bd.value)
            elif tipo =='Bolo Vulcão':
                if action == 'remove':
                    if int(quant_bv.value) > 1:
                        quant_bv.value = str(int(quant_bv.value) - 1)
                        quant_bv.value = int(quant_bv.value)
                elif action == 'adiciona':
                    quant_bv.value = str(int(quant_bv.value) + 1)
                    quant_bv.value = int(quant_bv.value)
            elif tipo =='Torta':
                if action == 'remove':
                    if int(quant_td.value) > 1:
                        quant_td.value = str(int(quant_td.value) - 1)
                        quant_td.value = int(quant_td.value)
                        valor_parcial_item(e,tipo)
                elif action == 'adiciona':
                    quant_td.value = str(int(quant_td.value) + 1)
                    quant_td.value = int(quant_td.value)
                    valor_parcial_item(e,tipo)
            elif tipo =='Torta Decorada':
                if action == 'remove':
                    if int(quant_tdd.value) > 1:
                        quant_tdd.value = str(int(quant_tdd.value) - 1)
                        quant_tdd.value = int(quant_tdd.value)
                elif action == 'adiciona':
                    quant_tdd.value = str(int(quant_tdd.value) + 1)
                    quant_tdd.value = int(quant_tdd.value)
            elif tipo == 'topo_tdd':
                if action == 'remove':
                    if int(quant_topo_tdd.value) > 1:
                        quant_topo_tdd.value = str(int(quant_topo_tdd.value) - 1)
                        quant_topo_tdd.value = int(quant_topo_tdd.value)
                elif action == 'adiciona':
                    quant_topo_tdd.value = str(int(quant_topo_tdd.value) + 1)
                    quant_topo_tdd.value = int(quant_topo_tdd.value)
            elif tipo =='Torta Salgada':
                if action == 'remove':
                    if int(quant_ts.value) > 1:
                        quant_ts.value = str(int(quant_ts.value) - 1)
                        quant_ts.value = int(quant_ts.value)
                elif action == 'adiciona':
                    quant_ts.value = str(int(quant_ts.value) + 1)
                    quant_ts.value = int(quant_ts.value)
            elif tipo =='Cupcake':
                if action == 'remove':
                    if int(quant_cup.value) > 1:
                        quant_cup.value = str(int(quant_cup.value) - 1)
                        quant_cup.value = int(quant_cup.value)
                elif action == 'adiciona':
                    quant_cup.value = str(int(quant_cup.value) + 1)
                    quant_cup.value = int(quant_cup.value)
            elif tipo =='Docesp':
                if action == 'remove':
                    if int(quant_doe.value) > 25:
                        quant_doe.value = str(int(quant_doe.value) - 25)
                        quant_doe.value = int(quant_doe.value)
                elif action == 'adiciona':
                    quant_doe.value = str(int(quant_doe.value) + 25)
                    quant_doe.value = int(quant_doe.value)
            elif tipo =='Docest':
                if action == 'remove':
                    if int(quant_dot.value) > 25:
                        quant_dot.value = str(int(quant_dot.value) - 25)
                        quant_dot.value = int(quant_dot.value)
                elif action == 'adiciona':
                    quant_dot.value = str(int(quant_dot.value) + 25)
                    quant_dot.value = int(quant_dot.value)
            elif tipo =='Salgados':
                if action == 'remove':
                    if int(quant_salg.value) > 1:
                        quant_salg.value = str(int(quant_salg.value) - 25)
                        quant_salg.value = int(quant_salg.value)
                elif action == 'adiciona':
                    quant_salg.value = str(int(quant_salg.value) + 25)
                    quant_salg.value = int(quant_salg.value)

            elif tipo =='Arroz c/ Galinha':
                if action == 'remove':
                    pass
                elif action == 'adiciona':
                    pass
            elif tipo =='Bem Casados':
                print('Tipo:',tipo)
            elif tipo =='Empadão':
                print('Tipo:',tipo)
            elif tipo =='Delícia de':
                print('Tipo:',tipo)
            elif tipo =='Pudim':
                print('Tipo:',tipo)
            elif tipo =='Taça da Felicidade':
                print('Tipo:',tipo)
            elif tipo =='Torta Salgada Especial':
                print('Tipo:',tipo)
            elif tipo =='Outro':
                print('Tipo:',tipo)
            valor_parcial_item(e,tipo)
            self.page.update()
        
        def valor_parcial_item(e,tipo):
            if tipo == 'Bolo Decorado':
                if valor_un_bd.value != '' and valor_topo_bd.value != '':
                    total_bd.value = str(float(quant_bd.value)*(float(valor_un_bd.value)) + (float(quant_topo_bd.value) * float(valor_topo_bd.value)))
                elif valor_un_bd.value != '' and valor_topo_bd.value == '':
                    total_bd.value = str(float(quant_bd.value)*(float(valor_un_bd.value)))
                elif valor_un_bd.value == '' and valor_topo_bd.value != '':
                    total_bd.value =str(float(valor_topo_bd.value) * float(quant_topo_bd.value))
            elif tipo =='topo_bd':
                if valor_un_bd.value != '' and valor_topo_bd.value != '':
                    total_bd.value = str(float(quant_bd.value)*(float(valor_un_bd.value)) + (float(quant_topo_bd.value) * float(valor_topo_bd.value)))
                elif valor_un_bd.value != '' and valor_topo_bd.value == '':
                    total_bd.value = str(float(quant_bd.value)*(float(valor_un_bd.value)))
                elif valor_un_bd.value == '' and valor_topo_bd.value != '':
                    total_bd.value = str(float(valor_topo_bd.value) * float(quant_topo_bd.value))
            elif tipo =='Bolo Vulcão':
                if valor_un_bv.value != '':
                    total_bv.value = str(float(quant_bv.value)*float(valor_un_bv.value))
            elif tipo =='Torta':
                if valor_un_td.value != '':
                    total_td.value = str(int(quant_td.value)*float(valor_un_td.value))
            elif tipo =='Torta Decorada':
                if valor_un_tdd.value != '' and valor_topo_tdd.value != '':
                    total_tdd.value = str(int(quant_tdd.value)*(float(valor_un_tdd.value)) + (float(valor_topo_tdd.value) * float(quant_topo_tdd.value)))
                elif valor_un_tdd.value != '' and valor_topo_tdd.value == '':
                    total_tdd.value = str(int(quant_tdd.value)*(float(valor_un_tdd.value)))
                elif valor_un_tdd.value == '' and valor_topo_tdd.value != '':
                    total_tdd.value = str(float(valor_topo_tdd.value) * float(quant_topo_tdd.value))
            elif tipo =='topo_tdd':
                if valor_un_tdd.value != '' and valor_topo_tdd.value != '':
                    total_tdd.value = str(float(quant_tdd.value)*(float(valor_un_tdd.value)) + (float(quant_topo_tdd.value) * float(valor_topo_tdd.value)))
                elif valor_un_tdd.value != '' and valor_topo_tdd.value == '':
                    total_tdd.value = str(float(quant_tdd.value)*(float(valor_un_tdd.value)))
                elif valor_un_tdd.value == '' and valor_topo_tdd.value != '':
                    total_tdd.value = str(float(valor_topo_tdd.value) * float(quant_topo_tdd.value))
            elif tipo =='Torta Salgada':
                if valor_un_ts.value != '':
                    total_ts.value = str(int(quant_ts.value)*float(valor_un_ts.value))
            elif tipo =='Cupcake':
                if valor_un_cup.value != '':
                    total_cup.value = str(int(quant_cup.value)*float(valor_un_cup.value))
                    self.page.update()
            elif tipo =='Docesp':
                if valor_cent_doe.value != '':
                    total_doe.value = str(int(quant_doe.value)*int(valor_cent_doe.value)/100)
                    self.page.update()
            elif tipo =='Docest':
                if valor_cent_dot.value != '':
                    total_dot.value = str(int(quant_dot.value)*int(valor_cent_dot.value)/100)
                    self.page.update()
            elif tipo =='Salgados':
                if valor_cent_salg.value != '':
                    total_salg.value = str(int(quant_salg.value)*float(valor_cent_salg.value)/100)
            elif tipo =='Arroz_gal':
                if  valor_arroz_gal.value != '':
                    total_arroz_gal.value = str(int(valor_arroz_gal.value))
            elif tipo =='Arroz_para':
                if  valor_arroz_para.value != '':
                    total_arroz_para.value = str(int(valor_arroz_para.value))
            elif tipo =='Bem Casados':
                if valor_un_bem_cas.value != '':
                    total_bem_cas.value = str(int(valor_un_bem_cas.value)*int(quant_bem_cas.value))
            elif tipo =='Empadão':
                if valor_empadao.value !='':
                    total_empadao.value = str(int(valor_empadao.value))
            elif tipo =='Sobremesa':
                if valor_un_sobremesa.value !='':
                    total_sobremesa.value = str(int(valor_un_sobremesa.value)*int(quant_sobremesa.value))
            elif tipo =='Pudim':
                if valor_pudim.value !='':
                    total_pudim.value = str(int(valor_pudim.value))
            elif tipo =='Taça da Felicidade':
                if valor_taca.value != '0' and valor_taca.value !='' and tam_vol_taca.value !='':
                    total_taca.value = str(int(valor_taca.value))
            elif tipo =='Torta Salg Esp':
                if valor_ts_esp.value !='0' and valor_ts_esp.value !='' and int(quant_ts_esp.value) > 0:
                    total_ts_esp.value = str(int(valor_ts_esp.value)*int(quant_ts_esp.value))
            elif tipo == 'Diversos':
                if valor_diversos.value !='0' and valor_diversos.value !='' and descricao_diversos.value !='':
                    total_diversos.value = str(int(valor_diversos.value))
            self.page.update()
        
        def add_rem_rech(rech):
            check = rech in recheio_bd
            if check == True:
                recheio_bd.remove(rech)
            else:
                recheio_bd.append(rech)
                
        def add_rem_doces(tipo,sabor):
            if tipo == 'dot':
                check = sabor in doce_dot
                if check == True:
                    doce_dot.remove(sabor)
                else:
                    doce_dot.append(sabor)
                    doce_dot.sort()
            if tipo == 'doe':
                check = sabor in doce_doe
                if check == True:
                    doce_doe.remove(sabor)
                else:
                    doce_doe.append(sabor)
                    doce_doe.sort()
        
        def add_rem_salg(salg):
            check = salg in salgados
            if check == True:
                salgados.remove(salg)
            else:
                salgados.append(salg)
                salgados.sort()
        
        def form_itens(e):
            if e.data == 'bd':
                conteudo_bolos.content.controls.clear()
                conteudo_bolos.content.controls.append(form_bd)
            elif e.data == 'bv':
                conteudo_bolos.content.controls.clear()
                conteudo_bolos.content.controls.append(form_bv)
            elif e.data == 'td':
                conteudo_tortas.content.controls.clear()
                conteudo_tortas.content.controls.append(form_td)
            elif e.data == 'tdd':
                conteudo_tortas.content.controls.clear()
                conteudo_tortas.content.controls.append(form_tdd)
            elif e.data == 'ts':
                conteudo_tortas.content.controls.clear()
                conteudo_tortas.content.controls.append(form_ts)
            elif e.data == 'docesp':
                conteudo_doces.content.controls.clear()
                conteudo_doces.content.controls.append(form_docesp)
            elif e.data == 'docest':
                conteudo_doces.content.controls.clear()
                conteudo_doces.content.controls.append(form_docest)
            elif e.data == 'salgados':
                conteudo_tortas.content.controls.clear()
                conteudo_tortas.content.controls.append(form_salgados)
            elif e.data == 'outros':
                conteudo_outros.content.controls.clear()
                conteudo_outros.content.controls.append(form_outros)
                
            self.page.update()
        
        def valor_total():
            full_var = 0
            for dict in self.pedido:
                if dict['Tipo:'] != 'Cliente':
                    full_var = full_var + float(dict['Valor Final:'])
            total_pedido.value = str(full_var)
        
        def excluir_item(ind,page):
            self.page.close(page)
            indice = ind
            del self.pedido[indice]
            sucesso('Item excluido!')
            carrinho()
            valor_total()
            self.page.update()
        
        def detalha_pedido(e,indice):
            item_detalhado = ''
            for k,v in self.pedido[indice].items():
                if v !='' and v != None:
                    if k == 'Cliente':
                        if k == 'Tipo:' or k == 'Nome:':
                            item_detalhado += f"{v}\n"
                        else:
                            item_detalhado += f"{k} {v}\n"
                    elif k == 'Tipo:':
                        item_detalhado += f"{v}\n"
                    else:
                        item_detalhado += f"{k} {v}\n"
            detalhamento = ft.AlertDialog(
                modal = True,
                title = ft.Text('Detalhamento'),
                #content=(ft.Text(f"{self.pedido[indice]['Tipo:']}")),
                content=(ft.Text(item_detalhado)),
                actions=[
                    ft.TextButton('Fechar', on_click=lambda e:self.page.close(detalhamento)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            self.page.open(detalhamento)
        
        def gera_num_ped():
            db,colecao = conecta_bd('numpedido')
            cursor = colecao.find()
            for item in cursor:
                ano = item['ano_atual']
                np = item['ped_numero']
            colecao.update_one({'ano_atual':ano},{"$set":{'ped_numero':np+1}})
            novo_num = str(np)+"/"+str(ano)
            return(novo_num)
        
        def salvar_pedido(e):
            num_ctrl = gera_num_ped()
            db,colecao = conecta_bd('salvar')
            documento = {'Numero:':num_ctrl,'Pedido:':self.pedido,'Valor do Pedido:':total_pedido.value,'Status:':'Aberto'}
            colecao.insert_one(documento)
            restart_var(e,'Salvar')
            btn_return_item.visible=False
            sucesso(f"Pedido agendado!")
        
        def cancelar_pedido(e):
            self.pedido.clear()
            tabela_cliente.rows.clear()
            total_pedido.value = ''
            btn_return_item.visible=False
            #item_pedido.visible = False
            carrinho()
            e.data = '1'
            navegacao(e)
            self.page.update()
        
        def confirma_exclusao(e):
            indice = int(e.control.cells[0].content.value)
            aviso = ft.AlertDialog(
                modal = True,
                title = ft.Text('ATENÇÃO!'),
                content = ft.Text('Confirma EXCLUSÃO do item?'),
                actions=[
                    ft.TextButton('Cancela', on_click=lambda e:self.page.close(aviso)),
                    ft.TextButton('Confirma', on_click=lambda e:excluir_item(indice,aviso)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            self.page.open(aviso)
        
        def outros_especificar(e):
            info = e.data
            conteudo_outros.content.controls.clear()
            conteudo_outros.content.controls.append(ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200))
            if e.data == 'Arroz c/ Galinha':
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Row([
                            ft.Column([
                                ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                quant_arroz_gal,
                            ],width=175),
                            ft.Column([
                                ft.Text('Valor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_arroz_gal,
                            ]),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Column([
                                ft.Row([
                                    ft.Text('Total do Item:',size=19,color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
                                    total_arroz_gal
                                ]),
                            ]),
                        ]),
                    ])
                )
            elif e.data == 'Arroz Paraense':
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Row([
                            ft.Column([
                                ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                quant_arroz_para,
                            ],width=175),
                            ft.Column([
                                ft.Text('Valor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_arroz_para,
                            ]),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Text('Total do Item:',size=19,color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
                            total_arroz_para
                        ]),
                    ])
                )
            elif e.data == 'Bem Casados':
                conteudo_outros.content.controls.append(
                    ft.Column([
                            ft.Row([
                            ft.Column([
                                ft.Text('Valor Unitário:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_un_bem_cas,
                            ],width=150),
                            ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                            ft.Column([
                                ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                quant_bem_cas,
                            ],horizontal_alignment=ft.CrossAxisAlignment.START),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Text('Total do Item:',size=19,color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
                            total_bem_cas
                        ]),
                    ])
                )
            elif e.data == 'Empadão':
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Row([
                            ft.Column(
                                width=175,
                                controls=[
                                ft.Text('Tamanho:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                tam_empadao
                            ]),
                            #ft.VerticalDivider(width=9, thickness=3,color=ft.Colors.PINK_200),
                            ft.Column([
                                ft.Text('Valor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_empadao
                            ]),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                                ft.Text('Total do Item:',size=19,color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
                                total_empadao
                        ]),
                    ])
                )
            elif e.data == 'Sobremesa':
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Column([
                                ft.Text('Sabores:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                sabor_sobremesa
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Column([
                                ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                quant_sobremesa
                            ],width=150),
                            ft.Column([
                                ft.Text('Valor Unitário:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_un_sobremesa
                            ]),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Column([
                                ft.Row([
                                    ft.Text('Total do Item:',size=19,color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
                                    total_sobremesa
                                ]),
                            ]),
                        ]),
                    ])
                )
            elif e.data == 'Pudim':
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Row(
                            controls=[
                            ft.Column(
                                width=175,
                                controls=[
                                ft.Text('Tamanho:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                tam_pudim
                            ]),
                            ft.Column(
                                #horizontal_alignment=ft.CrossAxisAlignment.END,
                                controls=[
                                ft.Text('Valor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_pudim,
                            ])
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Text('Total do Item:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                            total_pudim
                        ])
                    ])
                )
            elif e.data == 'Taça da Felicidade':
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Row([
                            ft.Column([
                                ft.Text('Tam/Volume:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                tam_vol_taca
                            ],width=175),
                            ft.Column([
                                ft.Text('Valor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_taca
                            ]),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Text('Total do Item:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                            total_taca
                        ])
                    ])
                )
            elif e.data == 'Torta Salg Esp':
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Row([
                            ft.Column([
                                ft.Text('Sabor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                sabor_ts_esp
                            ],width=175),
                            ft.Column([
                                ft.Text('Tamanho:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                tam_ts_esp
                            ]),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Column([
                                ft.Text('Quantidade:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                quant_ts_esp
                            ],width=175),
                            ft.Column([
                                ft.Text('Valor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                                valor_ts_esp
                            ]),
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Text('Total do Item:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                            total_ts_esp
                        ])
                    ])
                )
            elif e.data == 'Diversos':
                dica = 'Especificar no campo abaixo o maior número de informações sobre o item'
                conteudo_outros.content.controls.append(
                    ft.Column([
                        ft.Column([
                        ft.Text(dica,size=15,weight=ft.FontWeight.BOLD),
                        descricao_diversos
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Text('Valor:',size=17,color=ft.Colors.GREEN_900,weight=ft.FontWeight.BOLD),
                            valor_diversos
                        ]),
                        ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                        ft.Row([
                            ft.Text('Total do Item:',size=17,color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
                            total_diversos
                        ])
                    ])
                )
            conteudo_outros.content.controls.append(ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200))
            conteudo_outros.content.controls.append(
                ft.Row([
                    #btn_cancel('Cancela',on_click=lambda e:cancelar(e)),
                    btn_confirm('Add ao Pedido',on_click=lambda e:adic_item_ped(e,info)),
                    #btn_imprime_tag('Imprimir Tag',on_click=lambda _:imprime_pedido())
                    
                ],alignment=ft.MainAxisAlignment.END)
            )
            conteudo_outros.content.controls.append(ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200))
            self.page.update()
        
        def carrinho():
            tabela_pedido.rows.clear()
            for indice, item in enumerate(self.pedido):
                if item['Tipo:'] == 'Cliente':
                    tabela_cliente.rows.clear()
                    tabela_cliente.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(
                                    ft.Row([
                                        ft.Text('Cliente ',weight=ft.FontWeight.BOLD),
                                        ft.Text(f"{item['Nome:']}"),
                                    ]),on_double_tap=lambda e:detalha_pedido(e,0)
                                )
                            ]
                        )
                    )
                    tabela_cliente.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(
                                    ft.Row([
                                        ft.Text('Serviço:',weight=ft.FontWeight.BOLD),
                                        ft.Text(f"{item['Serviço:']}"),
                                    ])
                                ),
                            ]
                        )
                    )
                elif item['Tipo:'] == 'Bolo Decorado' or item['Tipo:'] == 'Bolo Vulcão' or item['Tipo:'] == 'Torta' or \
                item['Tipo:'] == 'Torta Decorada' or item['Tipo:'] == 'Torta Salgada':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']} - {item['Tamanho:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] == 'Cupcake':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']} - Quant: {item['Quantidade:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] == 'Doces Especiais'or item['Tipo:'] == 'Doces Tradicionais' or item['Tipo:'] == 'Salgados':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}\nQuant: {item['Quantidade:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] == 'Arroz c/ Galinha':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] == 'Arroz Paraense':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] =='Bem Casados':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] =='Empadão':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] =='Sobremesa':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] =='Pudim':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] =='Taça da Felicidade':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] =='Torta Salg Esp':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Tipo:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )
                elif item['Tipo:'] == 'Diversos':
                    tabela_pedido.rows.append(
                        ft.DataRow(
                            on_long_press=lambda e:confirma_exclusao(e),
                            cells=[
                                ft.DataCell(ft.Text(indice)),
                                ft.DataCell(ft.Text(f"{item['Descrição:']}"),
                                            on_double_tap=lambda e:detalha_pedido(e,e.control.parent.cells[0].content.value)),
                                ft.DataCell(ft.Text(item['Valor Final:'])),
                            ]
                        )
                    )                
                self.page.update()
        
        def pedido_agenda():
            cursor = conecta_bd('agenda')
            for index,item in enumerate(cursor):
                exp = ft.ExpansionPanel(
                    header=ft.ListTile(title=ft.Text(f"Pedido nº  {item['Numero:']}")),
                )
                cont_pedido = ''
                for ordem in item['Pedido:']:
                    for k,v in ordem.items():
                        if v !='' and v != None:
                            if k == 'Cliente':
                                if k == 'Tipo:' or k == 'Nome:':
                                    cont_pedido += f"{v}\n"
                                else:
                                    cont_pedido += f"{k} {v}\n"
                            elif k == 'Tipo:':
                                cont_pedido += f"{v}\n"
                            else:
                                cont_pedido += f"{k} {v}\n"
                    cont_pedido+=('--------------------------------\n')
                cont_pedido+=f"Valor do Pedido: {item['Valor do Pedido:']}"
                exp.content = ft.ListTile(
                    title=ft.Text(cont_pedido),
                    #title=ft.Text(f"Descrição: {cont_pedido}"),
                    #subtitle=ft.Text(f"Press the icon to delete panel {i}"),
                    #trailing=ft.IconButton(ft.Icons.DELETE, on_click=handle_delete, data=exp),
                    trailing=ft.IconButton(ft.Icons.PRINT,data=exp),
                )
                pedido_painel.controls.append(exp)
            self.page.update()
            
        def pesquisa_unitaria(parametro):
            if parametro == 'pesq_data_c':
                colecao = conecta_bd('pesquisa')
                cursor = colecao.find({'Pedido:.Data da Entrega:':pesquisa_data_c.value})
            elif parametro =='pesq_nome':
                colecao = conecta_bd('pesquisa')
                cursor = colecao.find({'Pedido:.Nome:':pesquisa_nome.value})
            elif parametro == 'pesq_serviço':
                colecao = conecta_bd('pesquisa')
                cursor = colecao.find({'Pedido:.Serviço:':pesquisa_servico.value})
            elif parametro == 'pesq_tema':
                colecao = conecta_bd('pesquisa')
                cursor = colecao.find({'Pedido:.Tema:':pesquisa_tema.value})
            elif parametro == 'pesq_numped':
                colecao = conecta_bd('pesquisa')
                cursor = colecao.find({'Numero:':pesquisa_num_pedido.value})
                    
            pesquisa_resultado(cursor)
                    
        def pesquisa_resultado(consulta):
            pesquisa_painel.controls.clear()
            resultado = list(consulta)
            if len(resultado) != 0:
                for index,item in enumerate(resultado):
                    exp = ft.ExpansionPanel(
                        header=ft.ListTile(title=ft.Text(f"{index+1} - Pedido nº  {item['Numero:']}")),
                    )
                    cont_pesquisa = ''
                    for ordem in item['Pedido:']:
                        for k,v in ordem.items():
                            if v !='' and v != None:
                                if k == 'Cliente':
                                    if k == 'Tipo:' or k == 'Nome:':
                                        cont_pesquisa += f"{v}\n"
                                    else:
                                        cont_pesquisa += f"{k} {v}\n"
                                elif k == 'Tipo:':
                                    cont_pesquisa += f"{v}\n"
                                else:
                                    cont_pesquisa += f"{k} {v}\n"
                        cont_pesquisa+=('--------------------------------\n')
                    cont_pesquisa+=f"Valor do Pedido: {item['Valor do Pedido:']}"
                    exp.content = ft.ListTile(
                    title=ft.Text(cont_pesquisa),
                    trailing=ft.IconButton(ft.Icons.PRINT,data=exp),
                )
                    pesquisa_painel.controls.append(exp)
                    sucesso(f"Pesquisa concluída! {len(resultado)} resultado(s) encontrado(s).")  
                self.page.update()
            else:
                erro('Nenhum resultado encontrado!')
                self.page.update()
            resultado.clear()
                
        #****************** Funções - Fim *************************************************
        aba_bolo = ft.Column([
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                border_radius = 16,
                border=ft.border.all(3,color=ft.Colors.PINK_200),
                content=ft.Column([
                    header,
                ])
            ),
            ft.VerticalDivider(width=6),
            item_pedido,
            ft.RadioGroup(
                content=ft.Row([
                    ft.Radio(value='bd',label="Bolo Decorado"),
                    ft.Radio(value='bv',label="Bolo Vulcão"),
                ]),
                on_change=lambda e:form_itens(e)
            ),
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            conteudo_bolos := ft.Container(
                bgcolor=ft.Colors.PINK_100,
                content=ft.Column(
                    alignment=ft.CrossAxisAlignment.START,
                    controls=[
                                                
                    ],
                )
            ),
        ])

        aba_torta = ft.Column([
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                border_radius = 16,
                border=ft.border.all(3,color=ft.Colors.PINK_200),
                content=ft.Column([
                    header,
                ])
            ),
            
            item_pedido,
            ft.RadioGroup(
                content=ft.Row([
                    ft.Radio(value='td',label="Torta"),
                    ft.Radio(value='tdd',label="Torta Decorada"),
                    ft.Radio(value='ts',label="Torta Salgada"),
            ],wrap=True,),
                on_change=lambda e:form_itens(e)
            ),
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            conteudo_tortas := ft.Container(
                bgcolor=ft.Colors.PINK_100,
                content=ft.Column(
                    alignment=ft.CrossAxisAlignment.START,
                    controls=[
                                                
                    ],
                )
            ),
            ft.Tabs(
                animation_duration=600,
                selected_index=0,
                tabs=[
                    
                    
                ]
            )
        ])

        aba_cupcake = ft.Column([
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                border_radius = 16,
                border=ft.border.all(3,color=ft.Colors.PINK_200),
                content=ft.Column([
                    header,
                ])
            ),
            item_pedido,
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                content=ft.Column([
                    form_cup,
                ])
            ),
        ])

        aba_doces = ft.Column([
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                border_radius = 16,
                border=ft.border.all(3,color=ft.Colors.PINK_200),
                content=ft.Column([
                    header,
                ])
            ),
            item_pedido,
            ft.RadioGroup(
                content=ft.Row([
                    ft.Radio(value='docest',label="Tradicionais"),
                    ft.Radio(value='docesp',label="Especiais"),
                ]),
                on_change=lambda e:form_itens(e)
            ),
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            conteudo_doces := ft.Container(
                bgcolor=ft.Colors.PINK_100,
                content=ft.Column(
                    alignment=ft.CrossAxisAlignment.START,
                    controls=[
                                                
                    ],
                )
            ),
            
        ])

        aba_salgados = ft.Column([
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                border_radius = 16,
                border=ft.border.all(3,color=ft.Colors.PINK_200),
                content=ft.Column([
                    header,
                ])
            ),
            item_pedido,
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                content=ft.Column([
                    form_salgados,
                ])
            ),
        ])

        aba_outros = ft.Column([
            ft.Container(
                bgcolor=ft.Colors.PINK_100,
                border_radius = 16,
                border=ft.border.all(3,color=ft.Colors.PINK_200),
                content=ft.Column([
                    header,
                ])
            ),
            item_pedido,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    outros_itens,
                ]
            ),
            conteudo_outros := ft.Container(
                bgcolor=ft.Colors.PINK_100,
                content=ft.Column(
                    controls=[
                        
                    ],
                )
            ),
            
        ])

        pag_principal = ft.Column([
            ft.Container(
                height=100,
            ),
            ft.Container(
                alignment=ft.Alignment(0.0,0.0),
                content=ft.Column([
                    ft.Image(
                        src=f"app/src/assets/logo_fabidoces.png",width=250,height=250,
                    ),
                    
                ])
            )
        ])
        pag_pedidos = ft.Column([
            ft.Container(
                content=ft.Column([
                    cabecalho,
                ])
            ),
            ft.Container(
                bgcolor=ft.Colors.PINK_50,
                content=ft.Column([
                    nome := ft.TextField(label='Nome do cliente:',capitalization=(ft.TextCapitalization.WORDS),autofocus=True),
                    endereco := ft.TextField(label='Endereço:',capitalization=(ft.TextCapitalization.WORDS)),
                    contato := ft.TextField(label='Contato:'),
                    ft.Row(
                        controls=[
                            data_p := ft.TextField(label='Data do Pedido:',expand=True),
                            ft.ElevatedButton('Data',icon=ft.Icons.CALENDAR_MONTH,
                                                on_click=lambda e:self.page.open(
                                                    ft.DatePicker(
                                                            first_date=datetime(year=2000, month=1, day=1),
                                                            last_date=datetime(year=2040, month=1, day=1),
                                                            on_change=lambda e:set_datas(e,'p'),
                                                        )
                                                    )),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            data_c := ft.TextField(label='Data p/ Conclusão:',expand=True),
                            ft.ElevatedButton('Data',icon=ft.Icons.CALENDAR_MONTH,
                                                on_click=lambda e:self.page.open(
                                                    ft.DatePicker(
                                                            first_date=datetime(year=2000, month=1, day=1),
                                                            last_date=datetime(year=2040, month=1, day=1),
                                                            on_change=lambda e:set_datas(e,'c'),
                                                        )
                                                    )),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            hora_c := ft.TextField(label='Hora da Conclusão:',expand=True),
                            ft.ElevatedButton('Hora',icon=ft.Icons.PUNCH_CLOCK_ROUNDED,
                                                on_click=lambda e:self.page.open(
                                                    ft.TimePicker(
                                                        confirm_text="Confirmar",
                                                        error_invalid_text="Hora Invalida!",
                                                        help_text="Selecione a Hora",
                                                        on_change=lambda e:set_hora(e),
                                                    )
                                                )),
                        ]
                    ),
                    ft.Row([
                        ft.Text('Serviço:',size=20),
                        servico := ft.RadioGroup(
                            content=ft.Column([
                                ft.Radio(value='Retirada',label='Retirada'),
                                ft.Radio(value='Delivery',label='Delivery'),
                            ])
                        ),
                    ft.VerticalDivider(width=9,thickness=3),
                    ft.ElevatedButton('Confirma',icon=ft.Icons.CHECK_CIRCLE,bgcolor=ft.Colors.GREEN_900,
                                        icon_color=ft.Colors.WHITE,color=ft.Colors.WHITE,on_click=lambda e:add_cliente(e))
                    ]),
                    #item_pedido,
                    ft.Row([
                        #btn_return_item
                    ])
                ])
            ),
        ])
        pag_agenda = ft.Column([
            ft.Container(
                content=ft.Column([
                    cabecalho,
                ])
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE70,
                content=ft.Column([
                    ft.ListTile(
                        title=ft.Text(f"Agenda do Dia: {data_agenda}",text_align='center',
                            size=16,weight=ft.FontWeight.BOLD),
                    ),
                    pedido_painel,
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Row([
                        btn_return_item
                    ]),
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ])
            ),            
        ])
        pag_relatorios = ft.Column([
            ft.Container(
                content=ft.Column([
                    cabecalho,
                ])
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE70,
                content=ft.Column([
                ft.Text('Página Relatórios')
                ])
            ),
        ])
        pag_pesquisa = ft.Column([
            ft.Container(
                content=ft.Column([
                    cabecalho,
                ])
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE70,
                content=ft.Column([
                    ft.ListTile(
                        title=ft.Text("Pesquisar Pedidos por:",
                                        text_align='center',size=16,weight=ft.FontWeight.BOLD)),
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Row(
                        controls=[
                            pesquisa_data_c,
                            ft.ElevatedButton('Data',icon=ft.Icons.CALENDAR_MONTH,
                                on_click=lambda e:self.page.open(
                                    ft.DatePicker(
                                        first_date=datetime(year=2000, month=1, day=1),
                                        last_date=datetime(year=2040, month=1, day=1),
                                        on_change= lambda e:set_datas(e,'pesq_data_c'),
                                    )
                                )
                            ),
                            btn_pesquisa_un(on_click=lambda e:pesquisa_unitaria('pesq_data_c')),
                        ]
                    ),
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Row([
                        pesquisa_nome,
                        btn_pesquisa_un(on_click=lambda e:pesquisa_unitaria('pesq_nome'))
                    ]),
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Row([
                        ft.Text('Serviço: '),
                        pesquisa_servico,
                        btn_pesquisa_un(on_click=lambda e:pesquisa_unitaria('pesq_serviço'))
                    ]),
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Row([
                        pesquisa_tema,
                        btn_pesquisa_un(on_click=lambda e:pesquisa_unitaria('pesq_tema'))
                    ]),
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.Row([
                        pesquisa_num_pedido,
                        btn_pesquisa_un(on_click=lambda e:pesquisa_unitaria('pesq_numped'))
                    ]),
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                    ft.ListTile(
                        title=ft.Text("Resultado(s):",
                                    text_align='center',size=16,weight=ft.FontWeight.BOLD)),
                    pesquisa_painel,
                    ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
                ])
                
            ),
        ])
        pag_item_pedido = ft.Column([
            ft.Container(
                content=ft.Column([
                    cabecalho,
                ])
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE70,
                content=ft.Column([
                    item_pedido,
                ])
            ),
        ])
        pag_carrinho = ft.Column([
            ft.Container(
                content=ft.Column([
                    cabecalho,
                ])
            ),
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            tabela_cliente,
            tabela_pedido,
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                ft.Text('Total: ',size=17,weight=ft.FontWeight.BOLD),
                total_pedido,
            ]),
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                btn_cancel('Cancelar Pedido',on_click=lambda e:cancelar_pedido(e)),
                btn_confirm('Confirmar Pedido',on_click=lambda e:salvar_pedido(e)),
            ]),
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            ft.Row([
                btn_return_item
            ]),
            ft.Divider(height=9, thickness=3,color=ft.Colors.PINK_200),
            
        ])
        
        
        self.page.add(
            pag_principal,
            navigation,
        )

ft.app(target=Fabidoces)
