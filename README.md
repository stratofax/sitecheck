# sitecheck

Tools to check a website and its pages by analyzing HMTL code.

For more information about sitecheck, see the [FAQ](docs/FAQ.md).

## Install and run this code

Ths project uses `poetry` to manage its dependencies.  To get started, install `poetry` for your system, as described in [the Introduction of the Poetry Documentation](https://python-poetry.org/docs/). Then clone this repo.

After you've cloned this repo onto your local machine, run the Python scripts like this:

```bash
cd /path/to/sitecheck-repo/
poetry install
cd /src/sitecheck
poetry run python read_file.py index.html
```
