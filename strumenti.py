class Strumenti:
    # Definisco la classe strumento e ne inizializzo le variabili
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)

    # Definisco la funzione che mi fa returnare lo strumento: incarico lo strumento di returnare se stesso
    def __str__(self):
        return f"{self.id_strumento}: {self.tipo} di {self.marca} acquistato nel {self.anno_acquisto} a {self.valore}€"