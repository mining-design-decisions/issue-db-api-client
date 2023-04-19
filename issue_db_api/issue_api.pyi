import typing


class IssueRepository:
    def __init__(self,
                 url: str, *,
                 credentials: tuple[str, str] | None = None,
                 label_caching_policy: str = 'no_caching',
                 config_handling_policy='read_fetch_write_fetch'):
        ...

    def __repr__(self) -> str:
        ...

    def search(self, q: Query) -> list[Issue]:
        ...

    @property
    def repos(self) -> list[Repo]:
        ...

    @property
    def tags(self) -> list[Tag]:
        ...

    def add_new_tag(self, name: str, description: str):
        ...

    @property
    def embeddings(self) -> list[Embedding]:
        ...

    def create_embedding(self, name: str, config: dict[str, typing.Any]) -> Embedding:
        ...

    def find_issues_by_key(self, *args: tuple[str, str]) -> list[Issue]:
        ...

    @property
    def models(self) -> list[Model]:
        ...

    def add_model(self, name: str, config: dict[str, typing.Any]) -> Model:
        ...


class Repo:
    def __repr__(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def projects(self) -> str:
        ...


class Query:
    def __init__(self):
        ...

    def __repr__(self) -> str:
        ...

    def lor(self, *args: Query) -> Query:
        ...

    def land(self, *args: Query) -> Query:
        ...

    def tag(self, name: str) -> Query:
        ...

    def not_tag(self, name: str) -> Query:
        ...


class Label:

    def __init__(self,
                 existence: bool,
                 executive: bool,
                 property: bool):
        ...

    def __repr__(self) -> str:
        ...

    def __eq__(self, other) -> bool | NotImplemented:
        ...

    def __hash__(self) -> int:
        ...

    @property
    def existence(self) -> bool:
        ...

    @property
    def executive(self) -> bool:
        ...

    @property
    def non_architectural(self) -> bool:
        ...


    @property
    def property(self) -> bool:
        ...


class Issue:
    def __new__(cls):
        ...

    def __repr__(self) -> str:
        ...

    def __eq__(self, other) -> bool | NotImplemented:
        ...

    def __hash__(self) -> int:
        ...

    @property
    def manual_label(self) -> str:
        ...

    @manual_label.setter
    def manual_label(self, value: str) -> str:
        ...

    def invalidate_label_cache(self):
        ...

    @property
    def tags(self) -> list[str]:
        ...

    def add_tag(self, name: str):
        ...

    def remove_tag(self, name: str):
        ...

    @property
    def is_in_review(self) -> bool:
        ...

    @is_in_review.setter
    def is_in_review(self, value: bool):
        ...

    @property
    def labelling_comments(self) -> list[str]:
        ...

    def add_labelling_comment(self, text: str):
        ...

    def remove_labelling_comment(self, comment: Comment):
        ...

    @property
    def key(self) -> str:
        ...

    @property
    def summary(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    @property
    def comments(self) -> list[str]:
        ...

    @property
    def status(self) -> str:
        ...

    @property
    def priority(self) -> str:
        ...

    @property
    def resolution(self) -> str | None:
        ...

    @property
    def issue_type(self) -> str:
        ...

    @property
    def issue_links(self) -> list[Issue]:
        ...

    @property
    def parent(self) -> Issue | None:
        ...

    @property
    def subtasks(self) -> list[Issue]:
        ...

    @property
    def watches(self) -> int:
        ...

    @property
    def votes(self) -> int:
        ...

    @property
    def date_created(self) -> str:
        ...

    @property
    def date_updated(self) -> str:
        ...

    @property
    def date_resolved(self) -> str:
        ...

    @property
    def labels(self) -> list[str]:
        ...

    @property
    def components(self) -> list[str]:
        ...

    @property
    def fix_versions(self) -> list[str]:
        ...

    @property
    def affected_versions(self) -> list[str]:
        ...


class Comment:
    def __repr__(self) -> str:
        ...

    @property
    def author(self) -> str:
        ...

    @property
    def body(self) -> str:
        ...

    @body.setter
    def body(self, text: str):
        ...


class Tag:
    def __repr__(self) -> str:
        ...

    def __eq__(self, other) -> bool | NotImplemented:
        ...

    def __hash__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    @description.setter
    def description(self, description: str):
        ...

    @property
    def tag_type(self) -> str:
        ...


class Embedding:
    def __repr__(self) -> str:
        ...

    def __eq__(self, other) -> bool | NotImplemented:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, name: str):
        ...

    @property
    def config(self) -> dict[str, typing.Any]:
        ...

    @config.setter
    def config(self, value: dict[str, typing.Any]):
        ...

    def download_binary(self, path: str):
        ...

    def upload_binary(self, path: str):
        ...

    def delete_binary(self):
        ...


class Model:

    def __repr__(self) -> str:
        ...

    def __eq__(self, other) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, name: str):
        ...

    @property
    def config(self) -> dict[str, typing.Any]:
        ...

    @config.setter
    def config(self, config: dict[str, typing.Any]):
        ...

    @property
    def versions(self) -> list[Version]:
        ...

    def add_version(self, time: str, path: str) -> Version:
        ...

    def remove_version(self, version: Version):
        ...

    @property
    def test_runs(self, data: list[typing.Any]) -> TestRun:
        ...

    def delete_test_run(self, run: TestRun):
        ...


class Version:

    def __repr__(self) -> str:
        ...

    def __eq__(self, other) -> bool:
        ...

    def download(self, path: str):
        ...

    @property
    def predictions(self) -> dict[str, typing.Any]:
        ...

    @predictions.setter
    def predictions(self, predictions: dict[str, typing.Any]):
        ...

    def delete_predictions(self):
        ...


class TestRun:

    def __repr__(self) -> str:
        ...

    @property
    def data(self) -> list[typing.Any]:
        ...