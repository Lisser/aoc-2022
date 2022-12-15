from typing import TypeVar, Sequence, Iterable

T = TypeVar('T')


def chunks(list_: Sequence[T], chunk_size: int) -> Iterable[T]:
    """Yield successive chunk_size-sized chunks from list_."""
    for i in range(0, len(list_), chunk_size):
        yield list_[i:i + chunk_size]