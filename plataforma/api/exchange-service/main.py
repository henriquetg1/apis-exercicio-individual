import os
from datetime import datetime, timezone
from typing import Any, Dict
import base64

import jwt
import requests
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Exchange Service")

# segurança JWT
security = HTTPBearer()
raw_secret = os.getenv("JWT_SECRET_KEY")
JWT_SECRET = base64.b64decode(raw_secret)
JWT_ALGO   = os.getenv("JWT_ALGORITHM", "HS256")

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> Dict[str, Any]:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# modelo de resposta
class ExchangeResponse(BaseModel):
    sell: float
    buy: float
    date: datetime
    account_id: str

# endpoint
@app.get(
    "/exchange/{from_currency}/{to_currency}",
    response_model=ExchangeResponse,
    summary="Converte de uma moeda para outra"
)
def get_exchange(
    from_currency: str,
    to_currency: str,
    token_payload: Dict[str, Any] = Depends(verify_token),
):
    """
    1. Chama API externa
    2. Extrai bid/ask
    3. Preenche o modelo com a sub do JWT como account_id
    """
    # Example Request: https://v6.exchangerate-api.com/v6/5b598b9eb728fb2dcfc9d467/latest/USD
    base = os.getenv("EXCHANGE_API_BASE_URL")
    key  = os.getenv("EXCHANGE_API_KEY")
    print("Base URL:", base)
    print("API Key:", key)
    url = f"{base}/{key}/latest/{from_currency}"

    resp = requests.get(url, timeout=5)
    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail="Erro na API externa")

    rates = resp.json().get("conversion_rates")
    if not rates or to_currency not in rates:
        raise HTTPException(status_code=404, detail="Taxa não encontrada")

    rate = rates[to_currency]

    return ExchangeResponse(
        sell=rate,
        buy=rate,
        date=datetime.now(timezone.utc),
        account_id = token_payload.get("sub") or token_payload.get("jti"),
    )
