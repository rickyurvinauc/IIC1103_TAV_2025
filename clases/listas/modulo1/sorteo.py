import random

emails = [
    "gael.sanchez@estudiante.uc.cl",
    "antosapag@uc.cl",
    "avs@estudiante.uc.cl",
    "vicente.viera@estudiante.uc.cl",
    "nalvarado@estudiante.uc.cl",
    "mbt@estudiante.uc.cl",
    "amanda.cardone@estudiante.uc.cl",
    "matiascaro@estudiante.uc.cl",
    "martinchodowiecki@estudiante.uc.cl",
    "gcontrerasarav@estudiante.uc.cl",
    "milagroscuezzo@estudiante.uc.cl",
    "carlos.degiorgis@uc.cl",
    "tdelamazal@estudiante.uc.cl",
    "jderodt@estudiante.uc.cl",
    "rdevidts@estudiante.uc.cl",
    "paz.leaplaza@estudiante.uc.cl",
    "felipe.mamani@estudiante.uc.cl",
    "sebastian.maraboli@estudiante.uc.cl",
    "pedro.marquinez@estudiante.uc.cl",
    "smaturana04@estudiante.uc.cl",
    "diegolivares@estudiante.uc.cl",
    "bperezp5@estudiante.uc.cl"
]

random_emails = random.sample(emails, 2)
print(random_emails)
