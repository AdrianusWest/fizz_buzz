import click


@click.command()
@click.option('--input_number', type=click.INT, prompt='Number',
              help='Input number for analyze')
def fizz_buzz(input_number):
    if input_number % 15 == 0:
        click.echo('FizzBuzz')
    elif input_number % 3 == 0:
        click.echo('Fizz')
    elif input_number % 5 == 0:
        click.echo('Buzz')
    else:
        click.echo(input_number)
    fizz_buzz()


click.echo('Welcome to Fizz Buzz!')
click.echo('Submit a number and get an answer!!')

if __name__ == "__main__":
    fizz_buzz()
