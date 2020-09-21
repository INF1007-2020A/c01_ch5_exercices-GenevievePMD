#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math

def convert_to_absolute() -> float:
    nombre = float(input('Veuillez entrer un nombre quelconque : '))
    return abs(nombre)
    # ou return abs(float(input('Veuillez entrer un nombre quelconque : ')))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'

    result = []
    #for i in range(len(prefixes)): # METHODE 1
    #    noms = prefixes[i] + suffixes
    #    result.append(noms)

    # return result (manque 1 bout)
    #return [letter + suffixes in

    for letter in prefixes:
        result.append(letter + suffixes)

    return result


def prime_integer_summation() -> int:
    # initialiser liste
    primes = []
    i = 2
    x = 0

    while len(primes) < 100 :
        is_prime = True

        for divider in range(2, int(math.sqrt(i)) + 1) : # plus efficace que int(i/2) + 1 OU i-1
            if i % divider == 0 :
                is_prime = False
        if is_prime :
            primes.append(i)

        i += 1

    return sum(primes)


def factorial(number: int) -> int:
    return math.factorial(number)


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombres premiers est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
