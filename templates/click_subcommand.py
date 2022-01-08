# https://blog.imind.jp/entry/2019/11/16/041413
import click


def log_title(s: str) -> None:
    click.secho(f"==> {s}", fg="green")


def log_error(s: str) -> None:
    click.secho("error:", bg="red", fg="white", nl=False, err=True)
    click.echo(f" {s}", err=True)


@click.group()
def cli():
    pass


@cli.command()
@click.option("-o", "--out", default="", help="output filepath")
@click.option("-c", "--config", default="portfolio.yml", help="config filepath")
def build(out, config):
    log_title("build command")
    log_error("build command")


if __name__ == "__main__":
    cli()
