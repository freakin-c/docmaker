# docmaker

Prepare your odt file with *Jinja2* placeholders and pass related data as JSON to *docmaker*.
If *libreoffice* is installed, its `--convert-to pdf` command line option is called.

## Basic usage

`python docmaker.py -s source.odt -t name --data '{"name": "Your Name", "address": "Your Address Street no 100", "birthdate": "21nd Oct"}'`

## Credits

* [Jinja2 templating library](http://jinja.pocoo.org/docs/2.10/intro/#basic-api-usage)
