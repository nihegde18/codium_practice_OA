from dataclasses import dataclass

@dataclass
class FileOperation:
    operation: str  # 'create', 'modify', 'delete'
    filename: str
    content: str = ""  # Only used for create/modify operations

# You can add more dataclasses if needed
