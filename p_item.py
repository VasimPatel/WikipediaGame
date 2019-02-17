from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    """ Link + similarity to dest (priority) """
    priority: float
    item: Any = field(compare=False)
