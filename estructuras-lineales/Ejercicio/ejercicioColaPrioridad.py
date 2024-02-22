import heapq

class SistemaPlanificacionTareas:
    def __init__(self):
        #Inicializamos la cola
        self.tareas = []
    
    def agregar_tarea(self, tarea, prioridad):
        #Encolar tareas
        heapq.heappush(self.tareas, (prioridad, tarea))

    def procesar_tareas(self):
        #Mostrar Tareas Encoladas
        while self.tareas:
            prioridad, tarea = heapq.heappop(self.tareas)
            print("Procesando tarea: ", tarea, "(prioridad:", prioridad, ")")

sistema = SistemaPlanificacionTareas()
sistema.agregar_tarea("Comer",4)
sistema.agregar_tarea("Despertar",2)
sistema.agregar_tarea("Desayunar",1)
sistema.agregar_tarea("Salir de casa",3)

sistema.procesar_tareas()
