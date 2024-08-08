import flet as ft

def main(pagina: ft.Page):
    # Definindo um fundo com gradiente usando container
    gradiente_container = ft.Container(
        width=pagina.window_width,
        height=pagina.window_height,  # Corrigido: 'heigth' para 'height'
        gradient=ft.LinearGradient(
            colors=["#33FF6", "#9809A2"],
            begin=ft.Alignment(-1, -1),  # top-left
            end=ft.Alignment(1, 1)  # bottom-right
        )
    )

    # Criando componentes com cores personalizadas
    title = ft.Text(
        value="Login",
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        color="#FFFFFF"
    )
    subtitle = ft.Text(
        value="Bem vindo(a)!",
        style=ft.TextThemeStyle.TITLE_MEDIUM,
        color="#FFFFFF"
    )
    username = ft.TextField(
        label="Usuário",
        hint_text="Digite seu usuário",
        width=300,
        text_style=ft.TextStyle(color="#FFFFFF")
    )
    password = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        width=300,
        text_style=ft.TextStyle(color="#333333")
    )
    login_button = ft.ElevatedButton(
        text="Login",
        on_click=lambda e: print("Botão de login clicado!"),
        bgcolor="#000000",
        color="#FFFFFF"
    )

    # Adicionando os componentes à página dentro do container com o fundo degradê
    gradiente_container.content = ft.Container(
        content=ft.Column(
            [title, subtitle, username, password, login_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=20
    )

    pagina.add(gradiente_container)

ft.app(target=main)
