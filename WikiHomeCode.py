import tkinter as tk
from tkinter import messagebox
import wikipedia

def search_wikipedia():
    query = entry.get()
    try:
        page = wikipedia.page(query)
        content_text.delete(1.0, tk.END)
        content_text.insert(tk.END, page.content)
    except wikipedia.exceptions.DisambiguationError as e:
        messagebox.showinfo("Résultats ambigus", "La recherche est ambiguë. Veuillez sélectionner l'une des options suivantes :\n" + "\n".join(e.options))
    except wikipedia.exceptions.PageError:
        messagebox.showinfo("Aucun résultat", "Aucun résultat trouvé pour cette recherche.")

root = tk.Tk()
root.title("Recherche Wikipedia")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Entrez le sujet que vous souhaitez rechercher sur Wikipedia :")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(frame, text="Rechercher", command=search_wikipedia)
search_button.grid(row=0, column=2, padx=5, pady=5)

content_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
content_text.pack(padx=10, pady=10)

root.mainloop()
