import flet as ft
from database import Database


class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        
        
class CadastroScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.db = Database()
        
    def on_register_click(self, e):
        username = self.username_field.value
        email = self.email_field.value
        password = self.password_field.value
        
        if username and email and password:
            self.db.add_user(username, email, password)
            self.page.snack_bar = ft.SnackBar(ft.Text("Cadastrado com sucesso."))
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos."), open=True)
        
    def show(self):
        self.page.title = 'Aula BD'
        self.username_field = ft.TextField(
            label="Usuario",
        )
        self.email_field = ft.TextField(
            label="Email"
        )
        self.password_field = ft.TextField(
            label="Senha"
        )
        
        Cadastro_container = ft.Container(
            width=self.page.window_width,
            height=self.page.window_height,
            gradient=ft.LinearGradient(
                colors=['#FFFFFF', '#000000'],
                begin=ft.Alignment(-1, 5),
                end=ft.Alignment(5, 1)
            ),
            
            content= ft.Column(
                [
                    self.username_field,
                    self.email_field,
                    self.password_field,
                    ft.ElevatedButton(
                        "Registrar",
                        on_click=self.on_register_click
                    ),
                ],
            )
        )
        
        self.page.add(Cadastro_container)
        