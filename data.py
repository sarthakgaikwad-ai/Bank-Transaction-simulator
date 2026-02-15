import json
from pathlib import Path

DATA_FILE: Path = Path("account_data.json")


def load_account_data() -> tuple[str, float]:
    if not DATA_FILE.exists():
        return "123456789", 2000.0

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)
        return data["account_number"], data["balance"]


def save_account_data(account_number: str, balance: float) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            {
                "account_number": account_number,
                "balance": balance,
            },
            file,
            indent=4,
        )