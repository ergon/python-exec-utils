import exec_utils


def test_simple_call():
    ret = exec_utils.exec_strict("true")
    assert ret == ""

def test_simple_call_with_stdin():
    ret = exec_utils.exec_strict("cat", stdin_str="hello world")
    assert ret == "hello world"


def test_simple_call_with_log_handles():
    logs = []
    ret = exec_utils.exec_strict("cat",
                                 stdin_str="hello world",
                                 log_handle=lambda line: logs.append(line))

    assert len(logs) == 1
    assert logs[0] == "hello world"

def test_capture_stderr():

    cmd = ["bash", "-c", "echo stdout; echo 'onstderr' 1>&2"]

    stdout, stderr = exec_utils.exec_strict(cmd, return_stderr=True)

    assert stdout == "stdout\n"
    assert stderr == "onstderr\n"

