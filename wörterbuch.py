import customtkinter as ctk 
import json
import requests

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("700x600")
app.title("Wörterbuch App")
app.attributes('-fullscreen', True)

header_frame = ctk.CTkFrame(app)
header_frame.pack(fill="x")
header_label = ctk.CTkLabel(header_frame, text="Englisch Wörterbuch App", font=("Arial", 24))
header_label.pack(pady=10)

word_entry = ctk.CTkEntry(app, placeholder_text="Worteingabe...", width=200)
word_entry.pack(pady=20)

def search():
    word = word_entry.get()
    if word:
        definition, example, synonyms = get_definition_from_api(word)
        definition_label.configure(text=definition)
        example_label.configure(text=example)
        syn_label.configure(text=synonyms)

search_button = ctk.CTkButton(app, text="Suchen", command=search)
search_button.pack(pady=20)

container_frame = ctk.CTkFrame(app, height=200)
container_frame.pack(fill="x", padx=20, pady=20)
container_frame.pack_propagate(False)

definition_left_frame = ctk.CTkFrame(container_frame, width=200, fg_color="darkgreen")
definition_left_frame.pack(side="left", fill="y")
definition_left_frame.pack_propagate(False)
definition_title_lable = ctk.CTkLabel(definition_left_frame, text="Definition", font=("Arial", 20), text_color="white")
definition_title_lable.pack(expand=True)

definition_frame = ctk.CTkFrame(container_frame)
definition_frame.pack(side="left", fill="both", expand=True)
definition_label = ctk.CTkLabel(definition_frame, text="", wraplength=1500)
definition_label.pack(pady=20, padx=20)

container_frame2 = ctk.CTkFrame(app, height=200)
container_frame2.pack(fill="x", padx=20, pady=20)
container_frame2.pack_propagate(False)

example_left_frame = ctk.CTkFrame(container_frame2, width=200, fg_color="darkgreen")
example_left_frame.pack(side="left", fill="y")
example_left_frame.pack_propagate(False)
example_left_frame = ctk.CTkLabel(example_left_frame, text="Beispiel", font=("Arial", 20), text_color="white")
example_left_frame.pack(expand=True)

example_frame = ctk.CTkFrame(container_frame2)
example_frame.pack(side="left", fill="both", expand=True)
example_label = ctk.CTkLabel(example_frame, text="", wraplength=1500)
example_label.pack(pady=20, padx=20)

container_frame3 = ctk.CTkFrame(app, height=200)
container_frame3.pack(fill="x", padx=20, pady=20)
container_frame3.pack_propagate(False)

syn_left_frame = ctk.CTkFrame(container_frame3, width=200, fg_color="darkgreen")
syn_left_frame.pack(side="left", fill="y")
syn_left_frame.pack_propagate(False)
syn_left_frame = ctk.CTkLabel(syn_left_frame, text="Synonyme", font=("Arial", 20), text_color="white")
syn_left_frame.pack(expand=True)

syn_frame = ctk.CTkFrame(container_frame3)
syn_frame.pack(side="left", fill="both", expand=True)
syn_label = ctk.CTkLabel(syn_frame, text="", wraplength=400)
syn_label.pack(pady=20, padx=20)

def get_definition_from_api(word):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            data = response.json()

            definitions_list = [d['definition'] for meaning in data[0]['meanings'] for d in meaning['definitions']]
            definitions = " / ".join(definitions_list) if definitions_list else "Keine Definition gefunden"

            examples_list = []
            for meaning in data[0]['meanings']:
                for definition in meaning['definitions']:
                    if 'example' in definition and definition['example']:
                        examples_list.append(f"- {definition['example']}")
                        examples = " / ".join(examples_list) if examples_list else "Kein Beispiel verfügbar."

            synonyms_set = set()
            for meaning in data[0]['meanings']:
                for d in meaning['definitions']:
                    synonyms = ", ".join(synonyms_set) if synonyms_set else "Keine Synonyme verfügbar."

            return definitions, examples, synonyms
        else:
            return "Keine Definition gefunden.", "Kein Beispiel verfügbar.", "Keine Synonyme verfügbar."
    except Exception as e:
        return f"Fehler: {e}"


app.mainloop()