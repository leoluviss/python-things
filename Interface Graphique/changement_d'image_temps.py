import tkinter as tk
from PIL import Image, ImageTk

images = []

root = tk.Tk()
root.title("Choix : ")
root.geometry("300x200")

Text1 = tk.Label(root, text="Temps entre les images (en secondes) : ")
Entry1 = tk.Entry(root)
Text1.pack()
Entry1.pack()

Text2 = tk.Label(root, text="Nombre d'images : ")
Entry2 = tk.Entry(root)
Text2.pack()
Entry2.pack()

def popup1():
    res_ent2 = int(Entry2.get())
    temps = int(Entry1.get())

    # Nettoyer l'écran
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Adresse des images : ")
    root.geometry("400x200")

    def principal(x):
        for widget in root.winfo_children():
            widget.destroy()

        root.title("Diaporama des images")
        root.geometry("1920x1080")

        label = tk.Label(root)
        label.pack(expand=True)

        def chang_ph(index=0):
            adresse = x[index].replace("\\", "/")
            try:
                img = Image.open(adresse)
                img.thumbnail((1920, 1080))
                photo = ImageTk.PhotoImage(img)
                label.config(image=photo)
                label.image = photo
            except Exception as e:
                print(f"Erreur avec l'image {adresse}: {e}")

            next_index = (index + 1) % len(x)
            root.after(temps * 1000, lambda: chang_ph(next_index))

        chang_ph()

    def adr_img(i=0):
        for widget in root.winfo_children():
            widget.destroy()

        if i < res_ent2:
            Text_img = tk.Label(root, text=f"Adresse de l'image {i + 1} : ")
            Entry_img = tk.Entry(root, width=50)
            Button_img = tk.Button(root, text="Valider", command=lambda: valider(i))
            Text_img.pack()
            Entry_img.pack()
            Button_img.pack()

            def valider(index):
                images.append(Entry_img.get())
                adr_img(index + 1)
        else:
            principal(images)

    adr_img()

Button = tk.Button(root, text="Valider", command=popup1)
Button.pack(pady=10)

root.mainloop()

