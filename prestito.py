# Procedimento analogo a cosa accade nel file strumenti.py

class Prestito:
    def __init__(self, id_prestito, data, codice, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.codice = codice
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.id_prestito}: Strumento {self.codice} prestato a {self.cognome_allievo} in data {self.data}"