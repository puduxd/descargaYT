from tkinter import * 
import tkinter as tk
from pytube import YouTube
from tkinter import messagebox, filedialog

#Función limpiar
def clearTextInput():
    raiz.linkText.delete(0, 'end')

#Función para crear Widgets
def Widgets():
 
    head_label = Label(raiz, text="Descarga video de Youtube",
                       padx=15,
                       pady=15,
                       font='Helvetica 15 bold',
                       fg="black")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=1)

    link_label = Label(raiz,
                       text="Linkazo : ",
                       font='Helvetica 18 bold',                    
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)    

    raiz.linkText = Entry(raiz,
                          width=40,
                          font="Arial 14",
                          textvariable=video_Link)
    raiz.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    link_label = Label(raiz,
                       text="Directorio: ",
                       font='Helvetica 18 bold',                      
                       pady=5,
                       padx=5)  
    link_label.grid(row=3,
                    column=0,
                    pady=5,
                    padx=5)  

    raiz.destinationText = Entry(raiz,                          
                                width=30,
                                font="Arial 14",
                                textvariable=download_Path,
                                state=DISABLED)
    raiz.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(raiz,
                      text="Explorar",
                      width=10,
                      font='Helvetica 11 bold',
                      background="Gray",
                      relief=GROOVE,
                      command=Browse)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(raiz,
                        text="Descargar Video",
                        width=11,
                        background="Gray",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font='Helvetica 11 bold',
                        command=Download)
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)

    Clear_B = Button(raiz,
                        text="Limpiar",
                        width=5,
                        background="Gray",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font='Helvetica 11 bold',
                        command=clearTextInput)
    Clear_B.grid(row=4,
                column=2,
                pady=20,
                padx=20)

    Label_L= Label(raiz,
                    text="Todos los derechos reservados para Pudú @PuduFC",
                    font='Helvetica 10 bold')
    Label_L.grid(row=5,
                column=1,
                pady=20,
                padx=20)

#Función explorar
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Video Guardado")
 
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)
 
#Función descarga              
def Download():

    try:
        #Variable para pasar el link
        Youtube_link = video_Link.get()

        if Youtube_link=="" or download_Path.get()=="":
            messagebox.showinfo("Información","Debe ingresar un linkazo y directorio válido")
        else:
            if Youtube_link.__contains__("https://www.youtube.com/"):
                messagebox.showinfo("Atención!!","Su descarga comenzará en Breve, espere un momento :) ")
            else:
                messagebox.showerror("Error!!","Ingrese link válido")
        


        #Carpeta de destino
        download_Folder = download_Path.get()
        getVideo = YouTube(Youtube_link)

        #Descarga máxima calidad
        videoStream = getVideo.streams.get_highest_resolution()
        #Descarga
        videoStream.download(download_Folder)

        messagebox.showinfo("Felicidades!","Su descarga se Guardó en: \n"+ download_Folder)
        
    except:
        messagebox.showerror("Error!","Error inesperado compa. Verifique el link o inténtelo nuevamente")

  
#Menu raiz
raiz= tk.Tk()
#raiz.eval('tk::PlaceWindow . center')

#Centrar pantalla
windowWidth = raiz.winfo_reqwidth()
windowHeight = raiz.winfo_reqheight()
positionRight = int(raiz.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(raiz.winfo_screenheight()/2 - windowHeight/2)
raiz.geometry("+{}+{}".format(positionRight, positionDown))

#Configuración de pantalla
raiz.title("Programilla")
raiz.iconbitmap("Asset/yt.ico")
raiz.resizable(0,0)

#Tamaño pantalla

raiz.geometry("700x400")

# Creando variables de tkinter
video_Link = StringVar()
download_Path = StringVar()



#Llamando a los Widgets
Widgets()


#Loop
raiz.mainloop()
