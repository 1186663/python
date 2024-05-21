import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def dodawanie_wielomianow(w1, w2):
    n = max(len(w1), len(w2))
    w1 = w1[::-1] + [0] * (n - len(w1))
    w2 = w2[::-1] + [0] * (n - len(w2))
    result = [w1[i] + w2[i] for i in range(n)]
    result.reverse()
    return wielomian_to_string(result) + "\n" + str(result)

def odejmowanie_wielomianow(w1, w2):
    n = max(len(w1), len(w2))
    w1 = w1[::-1] + [0] * (n - len(w1))
    w2 = w2[::-1] + [0] * (n - len(w2))
    result = [w1[i] - w2[i] for i in range(n)]
    result.reverse()
    return wielomian_to_string(result) + "\n" + str(result)

def mnozenie_wielomianow(w1, w2):
    wynik = [0] * (len(w1) + len(w2) - 1)
    for i in range(len(w1)):
        for j in range(len(w2)):
            wynik[i + j] += w1[i] * w2[j]
    return wielomian_to_string(wynik) +"\n"+ str(wynik)

def dzielenie_wielomianow(w1, w2):
    iloraz = [0] * (len(w1) - len(w2) + 1)
    dzielna = w1[:]
    for i in range(len(iloraz)):
        coef = dzielna[i] / w2[0]
        iloraz[i] = coef
        for j in range(len(w2)):
            if i + j < len(dzielna):
                dzielna[i + j] -= coef * w2[j]
    reszta = [round(num, 5) for num in dzielna[len(iloraz) - 1:]]
    while reszta and reszta[0] == 0:
        reszta.pop(0)
    iloraz_str = wielomian_to_string(iloraz)
    reszta_str = wielomian_to_string(reszta) if reszta else '0'
    return f'Iloraz: {iloraz_str}\nReszta: {reszta_str}'


def horner_wielomian(p, x):
    wynik = p[0]
    for i in range(1, len(p)):
        wynik = wynik * x + p[i]
    return wynik

def oblicz_miejsca_zerowe(wielomian):
    miejsca_zerowe = np.roots(wielomian)
    return miejsca_zerowe


def wielomian_to_string(wielomian):
    n = len(wielomian) - 1
    wynik = ''
    pierwszy_element = True
    for i, wspolczynnik in enumerate(wielomian):
        stopien = n - i
        if wspolczynnik == 0:
            continue
        elif stopien == 0:
            wynik += ' ' + znak(wspolczynnik, pierwszy_element) + ' ' + str(abs(wspolczynnik))
        elif stopien == 1:
            wynik += ' ' + znak(wspolczynnik, pierwszy_element) + ' ' + str(abs(wspolczynnik)) + 'x'
        else:
            wynik += ' ' + znak(wspolczynnik, pierwszy_element) + ' ' + str(abs(wspolczynnik)) + 'x^' + str(stopien)
        pierwszy_element = False
    return wynik.strip()

def znak(wspolczynnik, pierwszy_element):
    if wspolczynnik < 0:
        return '-'
    if pierwszy_element:
        return ''
    return '+'

class KalkulatorWielomianow:
    def __init__(self, master):
        self.master = master
        master.config(bg="#f0f0f0")
        master.title("Kalkulator wielomianów")

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)
        for i in range(7):
            master.grid_rowconfigure(i, weight=1)

        label_font = ("Arial", 10)
        entry_font = ("Arial", 10)
        button_font = ("Arial", 12, "bold")
        button_color = "#d9d9d9"

        self.wielomian1_label = tk.Label(master, bg="#f0f0f0", fg="black", font=label_font, text="Wielomian 1:")
        self.wielomian1_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
        self.wielomian1_entry = tk.Entry(master, font=entry_font, justify='center')
        self.wielomian1_entry.grid(row=0, column=1, sticky='nsew', padx=10, pady=5)

        self.wielomian2_label = tk.Label(master, bg="#f0f0f0", fg="black", font=label_font, text="Wielomian 2:")
        self.wielomian2_label.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
        self.wielomian2_entry = tk.Entry(master, font=entry_font, justify='center')
        self.wielomian2_entry.grid(row=1, column=1, sticky='nsew', padx=10, pady=5)

        self.x_label = tk.Label(master, bg="#f0f0f0", fg="black", font=label_font, text="Wartość x:")
        self.x_label.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        self.x_entry = tk.Entry(master, font=entry_font, justify='center')
        self.x_entry.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)

        self.dodawanie_button = tk.Button(master, text="Dodaj", font=button_font, bg=button_color, command=self.dodawanie)
        self.dodawanie_button.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

        self.odejmowanie_button = tk.Button(master, text="Odejmij", font=button_font, bg=button_color, command=self.odejmowanie)
        self.odejmowanie_button.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

        self.mnozenie_button = tk.Button(master, text="Pomnóż", font=button_font, bg=button_color, command=self.mnozenie)
        self.mnozenie_button.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)

        self.horner_button = tk.Button(master, text="Oblicz", font=button_font, bg=button_color, command=self.horner)
        self.horner_button.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)

        self.dzielenie_button = tk.Button(master, text="Dziel", font=button_font, bg=button_color, command=self.dzielenie)
        self.dzielenie_button.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)  

        self.rysuj_wykres_button = tk.Button(master, text="Rysuj wykres", font=button_font, bg=button_color, command=self.rysuj_wykres)
        self.rysuj_wykres_button.grid(row=5, column=1, sticky='nsew', padx=10, pady=10)

        self.miejsca_zerowe_button = tk.Button(master, text="Miejsca zerowe", font=button_font, bg=button_color, command=self.miejsca_zerowe)
        self.miejsca_zerowe_button.grid(row=6, column=0, sticky='nsew', padx=10, pady=10)
        
        self.wynik_text = tk.StringVar()
        self.wynik = tk.Label(master, bg="#f0f0f0", fg="black", font=entry_font, textvariable=self.wynik_text)
        self.wynik.grid(row=6, column=1, sticky='nsew', padx=10, pady=5)


    def oblicz_wynik(self, operacja):
        if not self.wielomian1_entry.get() or not self.wielomian2_entry.get():
            messagebox.showinfo("Błąd", "Wprowadź oba wielomiany")
            return
        try:
            w1 = [float(x) for x in self.wielomian1_entry.get().split(',')]
            w2 = [float(x) for x in self.wielomian2_entry.get().split(',')]
        except ValueError:
            messagebox.showinfo("Błąd", "Wprowadzono nieprawidłowe dane")
            return

        if operacja == 'dodawanie':
            wynik = dodawanie_wielomianow(w1, w2)
        elif operacja == 'odejmowanie':
            wynik = odejmowanie_wielomianow(w1, w2)
        elif operacja == 'mnozenie':
            wynik = mnozenie_wielomianow(w1, w2)
        elif operacja == 'dzielenie':
            if not w2 or all(coef == 0 for coef in w2):
                messagebox.showinfo("Błąd","Dzielnik nie może być pustym wielomianem lub wielomianem zerowym.")
                return
            wynik = dzielenie_wielomianow(w1, w2)
        elif operacja == 'horner':
            if not self.x_entry.get():
                messagebox.showinfo("Błąd", "Wprowadź wartość x")
                return
            x = float(self.x_entry.get())
            wynik1 = horner_wielomian(w1, x)
            wynik2 = horner_wielomian(w2, x)
            wynik = "Wynik pierwszego wielomianu: " + str(wynik1) + "\nWynik drugiego wielomianu: " + str(wynik2)

        self.wynik_text.set(str(wynik))

    def dodawanie(self):
        self.oblicz_wynik('dodawanie')

    def odejmowanie(self):
        self.oblicz_wynik('odejmowanie')

    def mnozenie(self):
        self.oblicz_wynik('mnozenie')

    def dzielenie(self):
        self.oblicz_wynik('dzielenie')

    def horner(self):
        self.oblicz_wynik('horner')

    def rysuj_wykres(self):
        try:
            w1 = [float(x) for x in self.wielomian1_entry.get().split(',')]
            w2 = [float(x) for x in self.wielomian2_entry.get().split(',')] if self.wielomian2_entry.get() else None
            x_value = float(self.x_entry.get()) if self.x_entry.get() else None
        except ValueError:
            messagebox.showinfo("Błąd", "Wprowadzono nieprawidłowe dane")
            return

        x = np.linspace(-10, 10, 1000)
        y1 = np.polyval(w1, x)
        plt.figure(figsize=(8, 5))
        plt.plot(x, y1, label='Wielomian 1')

        if w2 is not None:
            y2 = np.polyval(w2, x)
            plt.plot(x, y2, label='Wielomian 2')

        if x_value is not None:
            y_value1 = np.polyval(w1, x_value)
            plt.plot(x_value, y_value1, 'ro', label=f'Punkt x={x_value}')
            if w2 is not None:
                y_value2 = np.polyval(w2, x_value)
                plt.plot(x_value, y_value2, 'bo')

        plt.title('Wykres wielomianu')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()


    def miejsca_zerowe(self):
        try:
            w1 = [float(x) for x in self.wielomian1_entry.get().split(',')]
            mz1 = oblicz_miejsca_zerowe(w1)
            wynik = f"Miejsca zerowe: {mz1}\n"
            if self.wielomian2_entry.get():
                w2 = [float(x) for x in self.wielomian2_entry.get().split(',')]
                mz2 = oblicz_miejsca_zerowe(w2)
                wynik += f"Miejsca zerowe: {mz2}"
            self.wynik_text.set(wynik)
        except ValueError as e:
            messagebox.showinfo("Błąd", "Nieprawidłowe współczynniki wielomianu.")
        except np.lib.polynomial.PolyError as e:
            messagebox.showinfo("Błąd", "Nie można obliczyć miejsc zerowych dla podanych danych.")



root = tk.Tk()
app = KalkulatorWielomianow(root)
root.minsize(800, 400)
root.mainloop()