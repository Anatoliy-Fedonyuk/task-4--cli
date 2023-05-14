"""--Pytest for CLI collect_framework--"""
import pytest
from click.testing import CliRunner
from collect_framework.collect_framework import main


def test_cli_string():
    """Кейс 1: передали только --string"""
    runner = CliRunner()
    result = runner.invoke(main, ['--string', 'hello world'])
    assert result.exit_code == 0
    assert result.output.strip() == 'THERE ARE 6 UNIQUE CHARACTERS IN THIS TEXT!'


def test_cli_file(tmp_path):
    """Кейс 2: передали только --file"""
    file_content = 'hello world\n'
    file_path = tmp_path / 'test.txt'
    file_path.write_text(file_content)
    runner = CliRunner()
    result = runner.invoke(main, ['--file', str(file_path)])
    assert result.exit_code == 0
    assert result.output.strip() == 'THERE ARE 7 UNIQUE CHARACTERS IN THIS TEXT!'


def test_cli_both(tmp_path):
    """Кейс 3: передали и --string и --file, string must have ignored"""
    file_content = 'hello world\n'
    file_path = tmp_path / 'test.txt'
    file_path.write_text(file_content)
    runner = CliRunner()
    result = runner.invoke(main, ['--string', 'hello', '--file', str(file_path)])
    assert result.exit_code == 0
    assert result.output.strip() == 'THERE ARE 7 UNIQUE CHARACTERS IN THIS TEXT!'


def test_cli_no_args():
    """Кейс 4: didn't pass any argument"""
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert 'Either --string or --file must be provided!' in result.output


if __name__ == '__main__':
    pytest.main()
