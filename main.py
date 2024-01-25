import typer
from typing import Optional
from typing_extensions import Annotated
from recon.dns_ops import ScanAndSearch, ReverseAndSearch

app = typer.Typer()
recon_app = typer.Typer()
app.add_typer(recon_app, name="recon")

# TODO: Configure an output format for scans, searches and threat intelligence.

@recon_app.command("searchscan")
def searchscan(
    domain: str = typer.Argument(..., help="The domain to scan."),
    dpath: Optional[str] = typer.Option('defaults', help="The path to the dictionary to use."),
    nums: Optional[bool] = typer.Option(
        False, help="Include numbers in the scan."
    ),
    output: Optional[str] = typer.Option(None, help="The output file to write to."),
):
    """
    This function takes a domain name as input and returns a list of subdomains associated with that domain.
    """
    typer.echo(f"Searching for subdomains of {domain} using {dpath} as dictionary...")
    typer.echo(f"Include numbers: {nums}")
    dictionary = []
    if dpath == 'defaults':
        with open(dpath, "r") as f:
            dictionary = f.read().splitlines()

    results = ScanAndSearch(domain, dictionary, nums)
    if output:
        with open(output, "w") as f:
            for result in results:
                f.write(f"{result}\n")
    else:
        for result in results:
            typer.echo(result)



    if __name__ == "__main__":
        app()




