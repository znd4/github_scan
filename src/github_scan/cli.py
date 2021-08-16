import typer

app = typer.Typer()


@app.command()
def scan_repo():
    """Scan a github repository for secrets"""
