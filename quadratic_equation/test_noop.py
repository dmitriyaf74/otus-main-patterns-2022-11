from quadratic_equation.command import Command


class NoopCommand(Command):

    def execute(self) -> None:
        ...


def test_command_execute():
    assert NoopCommand().execute() is None