#######################################
# BB84HO.py
# 20210601 : ajout de Eve
#######################################

#alice_message_clair = "110110010010110100110101101001010001011011010011011011001010110010110100010101011001101101100110010110100100010110011001100100110100110010100110110110011010011011010101101100011010101001011010010110010101011001101101100011011011010101000110101101001001100010110011001001011010100101001001011010001100100110101101001010101001011001101011010010110011010100100110110011010110110010101010110001001010100110001011011010110001011011010010110100101011010100101010010011010011000110010010110100110110010100110100101011010100011010110101101100011010110110100101010100110011001011011010010101001101101101010100110101011010011010101101001101101011001010010101001101011001010011001011010110101100110110110010110100110110100110101101101011"

from qiskit import QuantumCircuit, execute, Aer
from random import randint
# le message qu'Alice veut envoyer

alice_message_clair = "110110010010110100110101101001010001011011010011011011001010110010110100010101011001101101100110010110100100010110011001100100110100110010100110110110011010011011010101101100011010110100100110001011001100100101101010010100100101101000100101010011000110110010110010100110100110010011010010110011010011000110010010110100110110010100110100101011010100110110101011011000110101010010110100101100101010110011011011000110101101011011000"

eve = randint(0,1)

def prepare_alice_qubit(j,base,clef):
    '''
    alice_prepare_qubit(j,base,clef) : cette fonction prépare un qubit d'Alice:

        - à la position j
        - en fonction du choix de la base à l'indice j
        - et en fonction de la valeur de la clef à l'indice j

            + si z et 0 : état |0> le circuit est vide
            + si z et 1 : état |1> le circuit contient une porte X
            + si x et 0 : état |+> le circuit contient une porte H
            + si x et 1 : état |-> le circuit contient une porte X et une porte H

       la fonction renvoie un QuantumCircuit qui à son exécution produit l'état voulu sur un qubit
             '''
    aqc = QuantumCircuit(1,1)
    if clef[j] == "1":
        aqc.x([0])
    if base[j] == "x":
        aqc.h([0])
    # dans le cas ou Eve écoute, alors dans un cas sur deux, on
    # change la base de mesure
    if eve:
        if randint(0,1):
            aqc.h([0])
    return aqc

def code(msg,key):
    ''' calcule le XOR bit à bit de deux bit-strings : msg et key
        il faut que la longueur de key > longueur de msg
    '''
    if len(msg) > len(key):
        print("La clef n'est pas assez longue, recommencez")
        return "La clef n'est pas assez longue, recommencez"
    else:
        res = ""
        for i in range(len(msg)):
            res += str( ( int(key[i]) + int(msg[i]) ) % 2 )
        return res
