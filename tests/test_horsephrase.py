import six
from io import StringIO

if six.PY2:
    import __builtin__ as builtins_module
    import mock
else:
    import builtins as builtins_module
    from unittest import mock


import horsephrase

def test_generate():
    pw = horsephrase._implementation.generate()
    assert all(word in horsephrase.__main__.words for word in pw.split(' '))

def test_estimate():
    with mock.patch.object(builtins_module, 'print') as mock_print:
        namespace = mock.MagicMock(
            count=5, choices=len(horsephrase.__main__.words),
            guesses_per_second=1000 * 1000 * 1000 * 1000,
            numeric=True
        )
        horsephrase.__main__.do_estimate(namespace)
        assert mock_print.call_count

def test_main():
    with mock.patch.object(builtins_module, 'print') as mock_print:
        horsephrase.__main__.main()
        assert mock_print.call_count
