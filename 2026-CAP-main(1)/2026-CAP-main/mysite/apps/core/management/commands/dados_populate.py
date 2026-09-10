from datetime import datetime, time, timedelta
from django.utils import timezone


def datetime_aware(ano, mes, dia, hora, minuto):
    return timezone.make_aware(datetime(ano, mes, dia, hora, minuto))

hoje = timezone.localdate()
dias_ate_domingo = (hoje.weekday() + 1) % 7
domingo = hoje - timedelta(days=dias_ate_domingo)

domingo = timezone.make_aware(datetime.combine(domingo, datetime.min.time()))
segunda = domingo + timedelta(days=1)
terca = domingo + timedelta(days=2)
quarta = domingo + timedelta(days=3)
quinta = domingo + timedelta(days=4)
sexta = domingo + timedelta(days=5)
sabado = domingo + timedelta(days=6)


dados_usuarios = [
    {
        'email': 'g.giordanni@escolar.ifrn.edu.br',
        'password': 'senha',
        'nome_completo': 'Giordanni Gomes Maciel',
    },
    {
        'email': 'isaque.andre@academico.ifrn.edu.br',
        'password': 'senha',
        'nome_completo': 'André Isaque da Silva Lima',
    },
    {
        'email': 'carlos.danilo@academico.ifrn.edu.br',
        'password': 'senha',
        'nome_completo': 'Carlos Danilo Ramos dos Santos'
    },
    {
        'email': 'j.feitosa@academico.ifrn.edu.br',
        'password': 'senha',
        'nome_completo': 'João Gabriel Figueiredo Feitosa'
    },
    {
        'email': 'alexandre.lima@ifrn.edu.br',
        'password': 'senha',
        'nome_completo': 'Alexandre Gomes de Lima'
    }
]

calendarios_infoweb_3M = [
    {
        'nome': 'Física',
        'eventos': [
            {
                'nome': 'Física - aula',
                'inicio': segunda + timedelta(hours=7),
                'fim': segunda + timedelta(hours=8, minutes=30)
            },
            {
                'nome': 'Física - aula',
                'inicio': quarta + timedelta(hours=7),
                'fim': quarta + timedelta(hours=8, minutes=30)
            }
        ]
    },
    {
        'nome': 'ICS',
        'eventos': [
            {
                'nome': 'ICS - atividade em sala 20/100',
                'inicio': segunda + timedelta(hours=9),
                'fim': segunda + timedelta(hours=10, minutes=30)
            }
        ]
    },
    {
        'nome': 'PAW',
        'eventos': [
            {
                'nome': 'PAW - aula',
                'inicio': segunda + timedelta(hours=10, minutes=30),
                'fim': segunda + timedelta(hours=12)
            },
            {
                'nome': 'PAW - prova',
                'inicio': sexta + timedelta(hours=10, minutes=30),
                'fim': sexta + timedelta(hours=12)
            }
        ]
    },
    {
        'nome': 'Português',
        'eventos': [
            {
                'nome': 'Português - produção de redação',
                'inicio': terca + timedelta(hours=7),
                'fim': terca + timedelta(hours=8, minutes=30)
            },
            {
                'nome': 'Português - prova',
                'inicio': quinta + timedelta(hours=7),
                'fim': quinta + timedelta(hours=8, minutes=30)
            }
        ]
    },
    {
        'nome': 'História',
        'eventos': [
            {
                'nome': 'História - prova',
                'inicio': terca + timedelta(hours=9),
                'fim': terca + timedelta(hours=10, minutes=30)
            }
        ]
    },
    {
        'nome': 'Biologia',
        'eventos': [
            {
                'nome': 'Biologia - aula',
                'inicio': terca + timedelta(hours=10, minutes=30),
                'fim': terca + timedelta(hours=12)
            },
            {
                'nome': 'Biologia - prova',
                'inicio': quinta + timedelta(hours=10, minutes=30),
                'fim': quinta + timedelta(hours=12)
            }
        ]
    },
    {
        'nome': 'Filosofia',
        'eventos': [
            {
                'nome': 'Filosofia - prova',
                'inicio': quarta + timedelta(hours=9),
                'fim': quarta + timedelta(hours=10, minutes=30)
            }
        ]
    },
    {
        'nome': 'Inglês nível 4',
        'eventos': [
            {
                'nome': 'Inglês nível 4 - prova',
                'inicio': quarta + timedelta(hours=10, minutes=30),
                'fim': quarta + timedelta(hours=12)
            }
        ]
    },
    {
        'nome': 'Gestão e empreendedorismo',
        'eventos': [
            {
                'nome': 'Gestão e empreendedorismo - prova',
                'inicio': quinta + timedelta(hours=9),
                'fim': quinta + timedelta(hours=10, minutes=30)
            }
        ]
    },
    {
        'nome': 'Matemática',
        'eventos': [
            {
                'nome': 'Matemática - prova',
                'inicio': sexta + timedelta(hours=7),
                'fim': sexta + timedelta(hours=8, minutes=30)
            }
        ]
    },
    {
        'nome': 'Projeto Integrador',
        'eventos': [
            {
                'nome': 'Projeto Integrador - apresentação 2º marco',
                'inicio': sexta + timedelta(hours=9),
                'fim': sexta + timedelta(hours=10, minutes=30)
            }
        ]
    }
]

calendarios_infoweb_2V = [
    {
        'nome': 'Autoria web',
        'eventos': [
            {
                'nome': 'Autoria web - aula',
                'inicio': segunda + timedelta(hours=14, minutes=30),
                'fim': segunda + timedelta(hours=16)
            }
        ]
    },
    {
        'nome': 'POO',
        'eventos': [
            {
                'nome': 'POO - prova',
                'inicio': quarta + timedelta(hours=16, minutes=30),
                'fim': quarta + timedelta(hours=18)
            }
        ]
    }
]

dados_calendarios = [
    {
        'nome': 'Atividade física',
        'numero_paleta': 1,
        'eventos': [
            {
                'nome': 'Academia - peito, tríceps e ombro',
                'inicio': segunda + timedelta(hours=13),
                'fim': segunda + timedelta(hours=14)
            },
            {
                'nome': 'Academia - coxa, panturrilha e glúteos',
                'inicio': quarta + timedelta(hours=17),
                'fim': quarta + timedelta(hours=18)
            },
            {
                'nome': 'Academia - dorsal, bíceps e abdômen',
                'inicio': sexta + timedelta(hours=17),
                'fim': sexta + timedelta(hours=18)
            },
            {
                'nome': 'Corrida',
                'inicio': terca + timedelta(hours=17),
                'fim': terca + timedelta(hours=17, minutes=30)
            },
            {
                'nome': 'Corrida',
                'inicio': domingo + timedelta(hours=17),
                'fim': domingo + timedelta(hours=17, minutes=30)
            }
        ],
    },
    {
        'nome': 'Hobbies',
        'numero_paleta': 2,
        'eventos': [
            {
                'nome': 'Simulado OBMEP',
                'inicio': terca + timedelta(hours=15),
                'fim': terca + timedelta(hours=18)
            },
            {
                'nome': 'Praticar violão',
                'inicio': quarta + timedelta(hours=18, minutes=30),
                'fim': quarta + timedelta(hours=19)
            },
            {
                'nome': 'Praticar violão',
                'inicio': sexta + timedelta(hours=18, minutes=30),
                'fim': sexta + timedelta(hours=19)
            }
        ]
    },
    {
        'nome': 'Compromissos semanais',
        'numero_paleta': 6,
        'eventos': [
            {
                'nome': 'Terapia com psicólogo',
                'inicio': terca + timedelta(hours=13, minutes=30),
                'fim': terca + timedelta(hours=14, minutes=30)
            },
            {
                'nome': 'Missa',
                'inicio': domingo + timedelta(hours=15),
                'fim': domingo + timedelta(hours=17)
            }
        ]
    },
    {
        'nome': 'Estudos',
        'numero_paleta': 5,
        'eventos': [
            {
                'nome': 'Atividades de ICS',
                'inicio': segunda + timedelta(hours=16, minutes=30),
                'fim': segunda + timedelta(hours=17, minutes=30)
            },
            {
                'nome': 'Estudar determinantes',
                'inicio': quinta + timedelta(hours=13),
                'fim': quinta + timedelta(hours=14, minutes=30)
            },
            {
                'nome': 'Revisar genética',
                'inicio': sexta + timedelta(hours=13),
                'fim': sexta + timedelta(hours=14, minutes=30)
            }
        ]
    },
]

dados_turmas = [
    {
        'nome': 'Infoweb 3M',
        'calendarios': calendarios_infoweb_3M,
        'numero_paleta': 3,
    },
    {
        'nome': 'Infoweb 2V',
        'calendarios': calendarios_infoweb_2V,
        'numero_paleta': 7,
    }
]
