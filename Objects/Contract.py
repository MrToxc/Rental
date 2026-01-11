from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Contract:
    total_price: float
    id_customer: int = None
    created_at: datetime = field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )
    id_contract: int = None
