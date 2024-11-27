import customtkinter as ctk 
import json

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ToDoList(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To-Do-liste")
        self.geometry("700x800")

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.header_frame = ctk.CTkFrame(self.main_frame)
        self.header_frame.pack(fill="x")
        self.header_label = ctk.CTkLabel(self.header_frame, text="To-Do-Liste", font=("Arial", 24))
        self.header_label.pack(pady=10)

        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(fill="x", pady=10)
        self.task_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Neue Aufgabe hinzufügen")
        self.task_entry.pack(side="left", fill="x", expand=True, padx=5)

        self.add_task_button = ctk.CTkButton(self.input_frame, text="Hinzufügen", command=self.add_task)
        self.add_task_button.pack(side="left", padx=5)

        self.search_frame = ctk.CTkFrame(self.main_frame)
        self.search_frame.pack(fill="x", pady=10)
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Suche...")
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.search_button = ctk.CTkButton(self.search_frame, text="Suchen", command=self.search_tasks)
        self.search_button.pack(side="right", padx=5)

        self.task_list = ctk.CTkLabel(self.main_frame, text="Aufgaben:")
        self.task_list.pack(pady=10, padx=10)

        self.tasks_frame = ctk.CTkFrame(self.main_frame)
        self.tasks_frame.pack(fill="both", expand=True, pady=10, padx=10)

        
        self.tasks = []
        self.filtered_tasks = []

        self.task_entry.bind("<Return>", self.on_enter)

        self.load_tasks()
        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        if task:
            self.tasks.append({"task": task, "priority": priority})
            self.update_task_list()
            self.task_entry.delete(0, "end")
            self.save_tasks()

    def update_task_list(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        tasks_to_display = self.filtered_tasks if self.filtered_tasks else self.tasks
        sorted_tasks = sorted(tasks_to_display, key=lambda x: ["Niedrig", "Normal", "Hoch"].index(x["priority"]), reverse=True)

        for i, task in enumerate(sorted_tasks):
            task_frame = ctk.CTkFrame(self.tasks_frame, height=40)
            task_frame.pack(fill="x", pady=5)
            task_frame.pack_propagate(False)

            priority_color = {"Hoch": "red", "Normal": "yellow", "Niedrig": "green"}
            color_frame=ctk.CTkFrame(task_frame, width=10, fg_color=priority_color[task["priority"]])
            color_frame.pack(side="left", fill="y")

            task_label = ctk.CTkLabel(task_frame, text=f"{i+1}. {task['task']}({task['priority']})")
            task_label.pack(side="left", fill="x", expand=True, padx=5)

            delete_button = ctk.CTkButton(task_frame, text="Löschen", command=lambda task=task: self.delete_task(task), fg_color="red", text_color="black")
            delete_button.pack(padx=10, pady=5, side="right")

            edit_button = ctk.CTkButton(task_frame, text="Bearbeiten", command=lambda t=task: self.edit_task(t))
            edit_button.pack(side="right", padx=5)

    def edit_task(self, task):
        edit_window=ctk.CTkToplevel(self)
        edit_window.grab_set()
        edit_window.focus_set()
        edit_window.title("Aufgabe bearbeiten")
        edit_window.geometry("300x200")

        edit_entry=ctk.CTkEntry(edit_window, width=200)
        edit_entry.pack(pady=10)
        edit_entry.insert(0, task["task"])

        priority_var = ctk.StringVar(value=task["priority"])
        priority_menu = ctk.CTkOptionMenu(edit_window, variable=priority_var, values=["Hoch", "Normal", "Niedrig"])
        priority_menu.pack(pady=5)

        def save_edit():
            new_task=edit_entry.get()
            new_priority=priority_var.get()
            if new_task:
                index=self.tasks.index(task)
                self.tasks[index] = {"task": new_task, "priority": new_priority}
                self.update_task_list()
                self.save_tasks()
                edit_window.destroy()

        save_button=ctk.CTkButton(edit_window, text="Speichern", command=save_edit)
        save_button.pack(pady=5)

    def delete_task(self, task):
        self.tasks.remove(task)
        self.filtered_tasks = []
        self.update_task_list()
        self.save_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks=json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with  open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def search_tasks(self):
        search_term = self.search_entry.get().lower()
        if search_term:
            self.filtered_tasks = [task for task in self.tasks if search_term in task["task"].lower()]
        else:
            self.filtered_tasks = []
        self.update_task_list()

    def on_enter(self, event):
        self.add_task()

if __name__ == "__main__":
    try:
        app=ToDoList()
        app.mainloop()
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")