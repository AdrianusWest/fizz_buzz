from click.testing import CliRunner
from fizz_buzz.fizz_buzz import fizz_buzz


def test_fizz_buzz():
    runner = CliRunner()
    result = runner.invoke(fizz_buzz, 5)
    assert result.exit_code != 0
    assert result.output != 'Buzz'

    runner = CliRunner()
    result = runner.invoke(fizz_buzz, 6)
    assert result.exit_code != 0
    assert result.output != 'Fizz'

    runner = CliRunner()
    result = runner.invoke(fizz_buzz, 19)
    assert result.exit_code != 0
    assert result.output != 19
