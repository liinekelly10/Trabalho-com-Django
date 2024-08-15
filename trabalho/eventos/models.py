from django.db import models

class EventoCultural(models.Model):
    TIPO_CHOICES = [
        ('', 'Escolha um evento'),
        ('SERESTA', 'Seresta dos Namorados'),
        ('PAGODE', 'Pagode só Para Amigos'),
        ('RODEIO', 'Rodeio'),
        ('CIRCO', 'Circo Fantástico'),
        ('SHOW', 'Show Taty Girl'),
        ('APRESENTAÇÃO', 'Show Henrique e Juliano'),
    ]

    LOCAL_CHOICES = [
        ('', 'Escolha o Local do Evento a seguir'),
        ('PRAÇA_DA_IGREJA_MATRIZ', 'Praça da Igreja Matriz'),
        ('AVENIDA_OSMAR_BASTOS', 'Avenida Osmar Bastos'),
        ('ESCOLA_EUDES_MAGALHÃES', 'Escola Eudes Magalhães'),
        ('LOTEAMENTO_ALTA_VISTA', 'Loteamento Alta Vista'),
        ('PRAÇA_DO_JAURO', 'Praça do Jauro'),
    ]

    ENTRADA_CHOICES = [
        ('', 'Escolha a entrada do seu evento a seguir'),
        ('GRATUITO', 'Gratuito'),
        ('PAGO', 'Pago'),
        ('INTEIRA', 'Inteira'),
        ('MEIA', 'Meia')
    ]

    evento = models.CharField(
        max_length=100,
        choices=TIPO_CHOICES,
        default='',
    )
    data_evento = models.DateField(null=False)
    entrada = models.CharField(
        max_length=50,
        choices=ENTRADA_CHOICES,
        default='',
    )
    horário = models.TimeField(null=False)
    local = models.CharField(
        max_length=50,
        choices=LOCAL_CHOICES,
        default='',
    )

    ENTRADA_CHOICES = [
        ('INTEIRA', 'Inteira'),
        ('MEIA', 'Meia'),
        ('GRATUITA', 'Gratuita'),
    ]

    entrada = models.CharField(
        max_length=50,
        choices=ENTRADA_CHOICES,
        default='INTEIRA'
    )

    quantidade_de_ingressos = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.evento} - {self.local}'

    def get_local_display(self):
        return dict(self.LOCAL_CHOICES).get(self.local, self.local)

    class Meta:
        db_table = 'dados_eventos'
