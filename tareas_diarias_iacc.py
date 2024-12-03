class TaskNode:
    def __init__(self, description, date, priority, status='Pendiente'):
        self.description = description
        self.date = date
        self.priority = priority
        self.status = status
        self.prev = None
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, description, date, priority, status='Pendiente'):
        new_task = TaskNode(description, date, priority, status)
        if not self.head:
            self.head = self.tail = new_task
        else:
            current = self.head
            while current and current.date <= date:
                current = current.next
            if not current:  # Insert at the end
                self.tail.next = new_task
                new_task.prev = self.tail
                self.tail = new_task
            elif current == self.head:  # Insert at the beginning
                new_task.next = self.head
                self.head.prev = new_task
                self.head = new_task
            else:  # Insert in the middle
                prev_node = current.prev
                prev_node.next = new_task
                new_task.prev = prev_node
                new_task.next = current
                current.prev = new_task

    def remove_task(self, description):
        current = self.head
        while current:
            if current.description == description:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def update_status(self, description, new_status):
        current = self.head
        while current:
            if current.description == description:
                current.status = new_status
                return True
            current = current.next
        return False

    def display_tasks(self):
        if not self.head:
            print("No hay tareas en la agenda.")
            return
        current = self.head
        while current:
            print(f"Tarea: {current.description}, Fecha: {current.date}, Prioridad: {current.priority}, Estado: {current.status}")
            current = current.next

    def search_by_priority(self, priority):
        current = self.head
        found = False
        while current:
            if current.priority == priority:
                print(f"Tarea: {current.description}, Fecha: {current.date}, Estado: {current.status}")
                found = True
            current = current.next
        if not found:
            print(f"No se encontraron tareas con prioridad {priority}.")

def main():
    agenda = TaskList()
    while True:
        print("\n--- Menú de Gestión de Agenda ---")
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Actualizar estado de tarea")
        print("4. Mostrar todas las tareas")
        print("5. Buscar tareas por prioridad")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            description = input("Descripción de la tarea: ")
            date = input("Fecha y hora (YYYY-MM-DD HH:MM): ")
            priority = input("Prioridad (Alta, Media, Baja): ")
            agenda.add_task(description, date, priority)
            print("Tarea añadida correctamente.")
        elif opcion == "2":
            description = input("Descripción de la tarea a eliminar: ")
            if agenda.remove_task(description):
                print("Tarea eliminada correctamente.")
            else:
                print("Tarea no encontrada.")
        elif opcion == "3":
            description = input("Descripción de la tarea a actualizar: ")
            new_status = input("Nuevo estado (Pendiente, En progreso, Completada): ")
            if agenda.update_status(description, new_status):
                print("Estado actualizado correctamente.")
            else:
                print("Tarea no encontrada.")
        elif opcion == "4":
            print("Tareas en la agenda:")
            agenda.display_tasks()
        elif opcion == "5":
            priority = input("Prioridad a buscar (Alta, Media, Baja): ")
            print(f"Tareas con prioridad {priority}:")
            agenda.search_by_priority(priority)
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()