from utils.utils import format_number


def soma(x: str, y: str) -> float:
    """
    Realiza a soma de dois números representados como strings.

    Converte as strings de entrada para números formatados usando a função
    'format_number()' antes de realizar a soma.

    Parâmetros:
    - x (str): A primeira string que representa o número a ser somado.
    - y (str): A segunda string que representa o número a ser somado.

    Retorna:
    - float: O resultado da soma dos números convertidos.

    Exemplo:
    >> soma('12.34', '56.78')
    69.12
    """

    x = format_number(x)
    y = format_number(y)

    return x + y


if __name__ == '__main__':
    print(soma('R$2.500', 'R$2.500'))
    print(soma('R$ 2.500', 'R$ 2.500'))
    print(soma('USD2.500', 'USD 2.500'))
    print(soma('2.500', 'R$2.500'))
    print(soma('2500', '2500'))
