import subprocess
from . import test_dir


def test_cli_entrypoint_import():
    """Test that the main function is importable from idr package."""
    from idr import main
    assert callable(main)


def test_cli_help():
    """Test that the idr CLI help command works."""
    result = subprocess.run(["idr", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage: idr" in result.stdout


def test_cli_version():
    """Test that the idr CLI version command works."""
    result = subprocess.run(["idr", "--version"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "2.1.0" in result.stdout


def test_idr(tmpdir):

    filename = tmpdir.join("test.txt")
    cmd = f"idr --sample {test_dir}/data/peak1_sub_pass {test_dir}/data/peak2_sub_pass --output-file {filename} --plot"
    subprocess.call(cmd.split())

