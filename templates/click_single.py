# https://click.palletsprojects.com/en/8.0.x/
import click
import time


@click.command()
@click.option("-c", "--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")
    with click.progressbar(range(1, count, 0.2)) as bar:
        for x in bar:
            time.sleep(x)


if __name__ == "__main__":
    hello()