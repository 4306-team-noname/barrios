from typing import Any, Protocol


class Repo(Protocol):
    store: Any

    def get_one(self, identifier: Any) -> Any:
        pass


class Service(Protocol):
    repo: Repo

    def get(self, identifier: Any) -> Any:
        pass


class Store:
    def add_two(self, num: int) -> int:
        return num + 2


class MyRepo:
    store: Store

    def __init__(self, store: Store) -> None:
        self.store = store

    def get_one(self, id: int) -> int:
        return self.store.add_two(id)


class FakeRepo:
    store: Store

    def __init__(self, store: Store):
        self.store = store

    def get_one_times_two(self, id: int) -> int:
        return self.store.add_two(id) * 2


class MyService:
    repo: Repo

    def __init__(self, repo: Repo) -> None:
        self.repo = repo

    def get(self, id: int) -> int:
        return self.repo.get_one(id)


the_repo = MyRepo(Store())
the_fake_repo = FakeRepo(Store())
the_service = MyService(the_repo)
the_faked_out_service = MyService(FakeRepo)

the_faked_out_service.get(55)
