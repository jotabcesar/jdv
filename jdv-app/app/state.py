from dataclasses import dataclass
from typing import Optional

@dataclass
class Session:
    token: Optional[str] = None
    role: Optional[str] = None
    user_id: Optional[int] = None

class AppState:
    def __init__(self):
        self.session = Session()
        # Emulador Android → 10.0.2.2 ; Celular físico → troque para http://SEU_IP_DO_PC:8000
        self.backend_url = "http://10.0.2.2:8000"
        self.sei_atual: Optional[str] = None
        self.checkin_atual_id: Optional[int] = None
