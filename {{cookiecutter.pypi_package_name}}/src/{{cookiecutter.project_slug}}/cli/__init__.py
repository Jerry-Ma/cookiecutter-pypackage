"""Console script for {{cookiecutter.project_slug}}."""

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for {{cookiecutter.project_slug}}."""
    console.print("This is {{cookiecutter.project_slug}} CLI.")


if __name__ == "__main__":
    app()
