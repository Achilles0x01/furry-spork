cores = {
    'italic':'\033[3m',
    'verde':'\033[92m',
    'amarelo':'\033[1;93m',
    'finale':'\033[0m',
}

exibir = """

{verde} __
|__)  _  _  |_ . |  _
| \  (- |_) |_ | | (-
        |{finale}{amarelo} version-beta 0.0 {finale}

Gerenciador de usuários desenvolvido como trabalho academico para a FIAP

Author: Henrique Galdino {italic}a.k.a{finale} Achilles
{verde}{italic}Blog{finale}: achilles0x01.github.io

Para sair: CTRL + C
""".format(**cores)

def banner():
    return(exibir)