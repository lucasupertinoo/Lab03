from operator import attrgetter
from strumenti import Strumenti
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}   # Creo un dizionario per tenere traccia degli strumenti nel deposito
        self.prestiti = {}    # Creo un dizionario per tenere traccia dei prestiti
        self.ultimo_codice = 0
        self.ultimo_id_prestito = 0
        # Creo riga 13 e 14 per proseguire con la numerazione corretta quando aggiungerò strumenti

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        file = open(file_path, "r", encoding="utf-8")   # Se il file non esiste si scatena un'eccezione FileNotFoundError

        riga = file.readline()
        while riga != "":
            campi = riga.strip().split(",")
            s = Strumenti(campi[1], campi[2], int(campi[3]), campi[4])
            self.strumenti[s.codice] = s  # Salvo nel dizionario lo strumento che ha come chiave il codice

            num_id = int(s.codice[1:])   # Leggo che cosa viene dopo la S che è il carattere 0
            if num_id > self.ultimo_codice:
                self.ultimo_codice = num_id

            riga = file.readline()
        file.close()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        codice = f"S{(self.ultimo_codice + 1)}"
        self.ultimo_codice = self.ultimo_codice + 1
        nuovo_s = Strumenti(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti[codice] = nuovo_s
        return nuovo_s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
