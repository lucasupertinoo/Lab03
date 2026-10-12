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
            s = Strumenti(campi[0], campi[1], campi[2], int(campi[3]), campi[4])  # Creo uno strumento che finisce nella classe Strumenti
            self.strumenti[s.id_strumento] = s  # Salvo nel dizionario della classe DepositoStrumenti lo strumento con il suo codice come chiave

            num_id = int(s.id_strumento[1:])   # Leggo che cosa viene dopo la S che è il carattere 0
            if num_id > self.ultimo_codice:
                self.ultimo_codice = num_id

            riga = file.readline()
        file.close()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        id_strumento = f"S{(self.ultimo_codice + 1)}" # Metto l'ID del nuovo strumento guardando l'ultimo e aggiungendo 1
        self.ultimo_codice = self.ultimo_codice + 1 # Aggiorno anche la variabile ultimo_codice aggiungendo 1
        nuovo_s = Strumenti(id_strumento, tipo, marca, anno_acquisto, valore) # Creo un nuovo strumento da inserire nella classe Strumenti
        self.strumenti[id_strumento] = nuovo_s # Metto il nuovo strumento nel dizionario della classe DepositoStrumenti
        return nuovo_s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti.values(), key=attrgetter("marca"))  # Essendo strumenti un dizionario, uso .values()

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        for p in self.prestiti.values():
            if p.id_strumento == id_strumento:
                raise Exception("Strumento già prestato!")
        if id_strumento not in self.strumenti:
            raise Exception("Strumento non esistente!")

        id_prestito = f"P{(self.ultimo_id_prestito + 1)}" # Metto l'ID del nuovo prestito guardando l'ultimo e facendo +1
        self.ultimo_id_prestito = self.ultimo_id_prestito + 1 # Aggiorno anche la variabile corrispondente
        nuovo_p = Prestito(id_prestito, data, id_strumento, cognome_allievo) # Creo un nuovo prestito nella classe Prestiti
        self.prestiti[id_prestito] = nuovo_p # Aggiorno il dizionario nella classe DepositoStrumenti
        return nuovo_p

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception("Prestito non esistente!")
        self.prestiti.pop(id_prestito)  # Con pop rimuovo il prestito