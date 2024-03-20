import flet as ft

def main(pagina):
    Texto = ft.text("Hashzap")
    
    def iniciar_chat(evento):
        print("Iniciar o chat")

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    pagina.add(Texto)
    pagina.add(botao_iniciar)

ft.app(main)





