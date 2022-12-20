import subprocess
from . import test_dir


def test_idr(tmpdir):

    filename = tmpdir.join("test.txt")
    cmd = f"idr --sample {test_dir}/data/peak1_sub_pass {test_dir}/data/peak2_sub_pass --output-file {filename}"
    subprocess.call(cmd.split())

