from tools.calendar_auth import get_calendar_service

def listar_eventos(input: str = None) -> str:
    try:
        service = get_calendar_service()
        events_result = service.events().list(
            calendarId='primary', timeMin='2025-04-21T00:00:00Z',
            maxResults=5, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            return "Nenhum evento encontrado."
        
        texto = "🗓️ Próximos eventos:\n"
        for event in events:
            inicio = event['start'].get('dateTime', event['start'].get('date'))
            texto += f"- {event['summary']} em {inicio}\n"
        return texto
    except Exception as e:
        return f"Erro ao acessar o Google Calendar: {str(e)}"