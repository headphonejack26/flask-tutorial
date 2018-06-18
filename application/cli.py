import os
import click

def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system(
            'pybabel init -i messages.pot -d application/translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')


    @translate.command()
    def update():
        """Update all languages."""
        if os.system('pybabel estract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabe update -i messages.pot -d application/translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d application/translations'):
            raise RuntimeError('compile command failed')
