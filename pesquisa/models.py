from django.db import models

class Pesquisa(models.Model):
    GENERO_CHOICES = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outro', 'Outro'),
        ('Prefiro não declarar', 'Prefiro não declarar'),
    ]

    IDADE_CHOICES = [
        ('18 a 35', '18 a 35'),
        ('36 a 50', '36 a 50'),
        ('51 a 65', '51 a 65'),
        ('+ de 66', '+ de 66'),
    ]

    COLABORADORA_CHOICES = [
        ('Tábata', 'Tábata'),
        ('Raquel', 'Raquel'),
        ('Melissa', 'Melissa'),
        ('Carina', 'Carina'),
        ('Camila', 'Camila'),
    ]

    FREQUENCIA_CHOICES = [
        ('2x semana', '2x semana'),
        ('1x semana', '1x semana'),
        ('Todo dia', 'Todo dia'),
        ('2x mês', '2x mês'),
        ('1x mês', '1x mês'),
    ]

    GASTO_MEDIO_CHOICES = [
        ('400 ou +', '400 ou +'),
        ('350 a 400', '350 a 400'),
        ('300 a 350', '300 a 350'),
        ('250 a 300', '250 a 300'),
        ('200 a 250', '200 a 250'),
        ('150 a 200', '150 a 200'),
        ('100 a 150', '100 a 150'),
        ('até 100', 'até 100'),
    ]

    LOJAS_CHOICES = [
        ('Outros', 'Outros'),
        ('Inter', 'Inter'),
        ('Zona Sul', 'Zona Sul'),
        ('Assaí', 'Assaí'),
        ('Princesa', 'Princesa'),
        ('Carrefour', 'Carrefour'),
        ('Unidos', 'Unidos'),
        ('Extra', 'Extra'),
        ('Multi Market', 'Multi Market'),
        ('Prezunic', 'Prezunic'),
        ('Mundial', 'Mundial'),
        ('Supermarket', 'Supermarket'),
        ('Guanabara', 'Guanabara'),
        ('Vianense', 'Vianense'),
        ('Campeao', 'Campeão'),
    ]

    MOTIVOS_CHOICES = [
        ('Promoção', 'Promoção'),
        ('Preço', 'Preço'),
        ('Proximidade', 'Proximidade'),
        ('Variedade', 'Variedade'),
        ('Qualidade', 'Qualidade'),
        ('Cartão', 'Cartão'),
        ('Vantagens do aplicativo', 'Vantagens do aplicativo'),
    ]

    MIDIAS_CHOICES = [
        ('Site', 'Site'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Youtube', 'Youtube'),
        ('Tiktok', 'Tiktok'),
        ('Canal do Whatsapp', 'Canal do Whatsapp'),
        ('Televisão', 'Televisão'),
        ('Rádio', 'Rádio'),
        ('Lojas físicas', 'Lojas físicas'),
        ('Não acompanho ofertas e novidades da Redeconomia', 'Não acompanho ofertas e novidades da Redeconomia'),
    ]

    TV_CHOICES = [
        ('Globo', 'Globo'),
        ('Record', 'Record'),
        ('SBT', 'SBT'),
        ('Band', 'Band'),
        ('RedeTV', 'RedeTV'),
        ('Outro', 'Outro'),
        ('Nenhum', 'Nenhum'),
    ]

    RADIO_CHOICES = [
        ('Melodia', 'Melodia'),
        ('Tupi', 'Tupi'),
        ('FM O Dia', 'FM O Dia'),
        ('Rádio Mix', 'Rádio Mix'),
        ('Band News', 'Band News'),
        ('MPB FM', 'MPB FM'),
        ('CBN', 'CBN'),
        ('Transamérica', 'Transamérica'),
        ('Outro', 'Outro'),
        ('Nenhum', 'Nenhum'),
    ]

    APP_CHOICES = [
        ('Não conheço o APP', 'Não conheço o APP'),
        ('Já ouvi falar mas nunca baixei', 'Já ouvi falar mas nunca baixei'),
        ('Já baixei o APP mas nunca usei', 'Já baixei o APP mas nunca usei'),
        ('Uso as vezes', 'Uso as vezes'),
        ('Uso em todas as minhas compras', 'Uso em todas as minhas compras'),
    ]

    FATORES_ESCOLHA_CHOICES = [
        ('Preço', 'Preço'),
        ('Promoções', 'Promoções'),
        ('Qualidade', 'Qualidade'),
        ('Marca', 'Marca'),
        ('Sustentabilidade', 'Sustentabilidade'),
        ('Proximidade', 'Proximidade'),
        ('Atendimento', 'Atendimento'),
        ('Possibilidade de realizar as compras de forma online', 'Possibilidade de realizar as compras de forma online'),
    ]

    MOTIVOS_REDECONOMIA_CHOICES = [
        ('Promoção', 'Promoção'),
        ('Preço', 'Preço'),
        ('Proximidade', 'Proximidade'),
        ('Variedade', 'Variedade'),
        ('Qualidade', 'Qualidade'),
        ('Atendimento', 'Atendimento'),
        ('Outros', 'Outros'),
    ]

    PONTOS_POSITIVOS_CHOICES = [
        ('Preço', 'Preço'),
        ('Qualidade', 'Qualidade'),
        ('Limpeza', 'Limpeza'),
        ('Atendimento', 'Atendimento'),
        ('Variedade', 'Variedade'),
        ('Localização', 'Localização'),
        ('Conforto', 'Conforto'),
        ('Padaria', 'Padaria'),
        ('Hortifruti', 'Hortifruti'),
        ('Outro', 'Outro'),
    ]

    PONTOS_NEGATIVOS_CHOICES = [
        ('Preço', 'Preço'),
        ('Qualidade', 'Qualidade'),
        ('Limpeza', 'Limpeza'),
        ('Atendimento', 'Atendimento'),
        ('Variedade', 'Variedade'),
        ('Localização', 'Localização'),
        ('Conforto', 'Conforto'),
        ('Padaria', 'Padaria'),
        ('Hortifruti', 'Hortifruti'),
        ('Outro', 'Outro'),
    ]

    AVALIACAO_CHOICES = [
        ('Bom', 'Bom'),
        ('Muito bom', 'Muito bom'),
        ('Ruim', 'Ruim'),
        ('Regular', 'Regular'),
    ]

    MELHORIAS_CHOICES = [
        ('Melhorar os preços', 'Melhorar os preços'),
        ('Oferecer mais promoções', 'Oferecer mais promoções'),
        ('Ampliar a variedade de produtos', 'Ampliar a variedade de produtos'),
        ('Melhorar o atendimento', 'Melhorar o atendimento'),
        ('Vendas online', 'Vendas online'),
        ('Outro', 'Outro'),
    ]

    LOJAS_REDECONOMIA_CHOICES = [
        ('Redeconomia Alfa e Omega', 'Redeconomia Alfa e Omega'),
        ('Redeconomia Reunidos', 'Redeconomia Reunidos'),
        ('Redeconomia Mix Certo', 'Redeconomia Mix Certo'),
        ('Redeconomia Feira Nova Nilópolis ', 'Redeconomia Feira Nova Nilópolis '),
        ('Redeconomia Feira Nova Parque, Queimados ', 'Redeconomia Feira Nova Parque, Queimados '),
        ('Redeconomia Flor da Posse Teresópolis ', 'Redeconomia Flor da Posse Teresópolis '),
        ('Redeconomia Flor da Posse Guapimirim', 'Redeconomia Flor da Posse Guapimirim'),
        ('Redeconomia Emanuel Pedra de Guaratiba', 'Redeconomia Emanuel Pedra de Guaratiba'),
        ('Redeconomia Emanuel Campo Grande', 'Redeconomia Emanuel Campo Grande'),
        ('Redeconomia Polisuper', 'Redeconomia Polisuper'),
        ('Redeconomia Celeiro', 'Redeconomia Celeiro'),
        ('Redeconomia Super Pax Realengo', 'Redeconomia Super Pax Realengo'),
        ('Redeconomia Super Pax Vila da Penha', 'Redeconomia Super Pax Vila da Penha'),
        ('Redeconomia Super Pax Rio de Janeiro', 'Redeconomia Super Pax Rio de Janeiro'),
        ('Redeconomia Super Pax Del Castilho', 'Redeconomia Super Pax Del Castilho'),
        ('Redeconomia CAB', 'Redeconomia CAB'),
        ('Redeconomia Campeão Barra da Tijuca', 'Redeconomia Campeão Barra da Tijuca'),
        ('Redeconomia Campeão Madureira', 'Redeconomia Campeão Madureira'),
        ('Redeconomia Campeão Centro, Nova Iguaçu', 'Redeconomia Campeão Centro, Nova Iguaçu'),
        ('Redeconomia Cariocão', 'Redeconomia Cariocão'),
        ('Redeconomia Principal', 'Redeconomia Principal'),
        ('Redeconomia Superprix', 'Redeconomia Superprix'),
        ('Redeconomia Princesa Arraial do Cabo', 'Redeconomia Princesa Arraial do Cabo'),
        ('Redeconomia Princesa Copacabana', 'Redeconomia Princesa Copacabana'),
        ('Redeconomia Princesa Laranjeiras', 'Redeconomia Princesa Laranjeiras'),
        ('Redeconomia Magé', 'Redeconomia Magé'),
        ('Redeconomia Mix Certo', 'Redeconomia Mix Certo'),
    ]

    genero = models.CharField(max_length=20, choices=GENERO_CHOICES)
    idade = models.CharField(max_length=10, choices=IDADE_CHOICES)
    frequencia_compra = models.CharField(max_length=10, choices=FREQUENCIA_CHOICES)
    gasto_medio = models.CharField(max_length=15, choices=GASTO_MEDIO_CHOICES)
    outras_lojas = models.CharField(max_length=20, choices=LOJAS_CHOICES)
    principais_motivos = models.CharField(max_length=30, choices=MOTIVOS_CHOICES)
    meios_deacompanhamento = models.CharField(max_length=60, choices=MIDIAS_CHOICES)
    canal_tv = models.CharField(max_length=10, choices=TV_CHOICES)
    canal_radio = models.CharField(max_length=15, choices=RADIO_CHOICES)
    uso_app = models.CharField(max_length=30, choices=APP_CHOICES)
    fatores_escolha = models.CharField(max_length=60, choices=FATORES_ESCOLHA_CHOICES)
    motivos_redeconomia = models.CharField(max_length=20, choices=MOTIVOS_REDECONOMIA_CHOICES)
    pontos_positivos = models.CharField(max_length=20, choices=PONTOS_POSITIVOS_CHOICES)
    pontos_negativos = models.CharField(max_length=20, choices=PONTOS_NEGATIVOS_CHOICES)
    avaliacao_variedade = models.CharField(max_length=10, choices=AVALIACAO_CHOICES)
    avaliacao_limpeza = models.CharField(max_length=10, choices=AVALIACAO_CHOICES)
    avaliacao_preços = models.CharField(max_length=10, choices=AVALIACAO_CHOICES)
    produtos_anunciados = models.CharField(max_length=10, choices=[('Sim', 'Sim'), ('Não', 'Não')])
    avaliacao_atendimento = models.CharField(max_length=10, choices=AVALIACAO_CHOICES)
    sugestoes_melhorias = models.CharField(max_length=40, choices=MELHORIAS_CHOICES)
    colaboradora = models.CharField(max_length=50, choices=COLABORADORA_CHOICES)
    loja_redeconomia = models.CharField(max_length=50, choices=LOJAS_REDECONOMIA_CHOICES)

    def __str__(self):
        return f"Pesquisa {self.id}"