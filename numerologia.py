# coding: utf-8
from re import compile, match

tabela = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
    's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8, ' ': 0
}


def soma_numeros_nome(nome):
    c = 0
    for letra in nome:
        c += tabela[letra]
    return c


def numero_numerologico(numero_base):
    while True:
        if numero_base in [11, 22, 33]:
            return numero_base
        numero_base = sum([int(x) for x in str(numero_base)])
        if numero_base <= 9:
            return numero_base


def numero_do_nome(nome):
    return numero_numerologico(soma_numeros_nome(nome))


def soma_numeros_data(data):
    nums_exp = compile(r'(\d+)[/\- ](\d+)[/\- ](\d+)')
    return sum([int(x) for x in nums_exp.findall(data)[0]])


def numero_da_data(data):
    return numero_numerologico(soma_numeros_data(data))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', help=u'Dá a soma numerológica de uma data')
    parser.add_argument('--nome',
                        help=u'Dá a soma numerológica de um nome (sem acentos entre aspas)')
    args = parser.parse_args()
    if args.nome:
        print(numero_do_nome(args.nome))
    elif args.data:
        print(numero_da_data(args.data))
