from __future__ import print_function
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_service():
    print("🔄 Iniciando get_calendar_service...")
    creds = None

    if os.path.exists('token.json'):
        print("🔑 Arquivo token.json encontrado.")
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        print("✅ Credenciais carregadas:", creds)

    if not creds or not creds.valid:
        print("⚠️ Credenciais inválidas ou ausentes.")
        if creds and creds.expired and creds.refresh_token:
            print("♻️ Atualizando credenciais expiradas...")
            creds.refresh(Request())
        # Primeiro fluxo
        else:
            print("🌐 Iniciando fluxo de autenticação...")
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            print("✅ Credenciais obtidas:", creds)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            print("💾 Token salvo em token.json.")

    print("✅ Autenticado com sucesso.")
    service = build('calendar', 'v3', credentials=creds)
    print("📅 Serviço do Google Calendar inicializado.")
    return service