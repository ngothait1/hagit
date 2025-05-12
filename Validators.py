from typing import Any
def check_digit(value: str) -> None:
    if not value:
        raise ValueError("The value cannot be empty")
    if not value.isdigit():
        raise ValueError("The value must be a number")

def is_available(key: str, data: dict[str, Any]) -> None:
    if key in data:
        raise ValueError(f"The {key} already exists: {data[key]}")

def is_not_available(key: str, data: dict[str, Any]) -> None:
    if key not in data:
         raise ValueError(f"The {key} does not exist.")

def check_range(index: int, items: list) -> None:
    if index < 0 or index >= len(items):
        raise ValueError("The index is out of range")
    
def check_range_option(index: int, items: list) -> None:
    if not index in items:
        raise ValueError("Your choice is not in the list of options.")
    
def empty_system(data: dict[str, Any]) -> None:
    if not data:
        raise ValueError("The system is empty")