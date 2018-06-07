import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
	_exec_notebook('./basic-ml-algo/classification-algo/LogisticRegression.ipynb')
	_exec_notebook('./basic-ml-algo/clustering-algo/K-Means.ipynb')
	_exec_notebook('./basic-ml-algo/regression-algo/LinearRegression.ipynb')