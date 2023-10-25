from distutils.core import setup
setup(
  name = 'cli_tls',         # How you named your package folder (MyLib)
  packages = ['cli_tls'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TLS Client for CLI',   # Give a short description about your library
  author = 'Oein',                   # Type in your name
  author_email = 'oein0219@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Oein/cli_tls',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Oein/cli_tls/archive/v1.0.0.tar.gz',    # I explain this later on
  keywords = ["tls", "cli", "tls_client"],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
    'tls_client',
    'argparse',
    'typing'
],
  classifiers=[
  ],
)