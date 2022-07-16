
models = ['Persona', 'Ninja', 'Genin', 'Chunin', 'Jounin', 'Tecnica', 'TecnicaAtaque', 'TecnicaCurativa', 'NinjaTecnica', 'NinjaMedico', 'Equipo', 'Mision', 'EquipoEnMision', 'Pergamino', 'EquipoEnMisionPergamino', 'BestiaMitica', 'BestiaMisionPergamino']

def exist_model(data):
    for model in models:
        if data == model:
            return True
    return False
