import argparse
import zipfile
from jinja2 import Template
import json
import subprocess

if __name__ == '__main__':
    argp = argparse.ArgumentParser()
    argp.add_argument('-s', '--source')
    argp.add_argument('-t', '--target', help='Data key to derive target name from.')
    argp.add_argument('--data')

    args = argp.parse_args()

    source = zipfile.ZipFile(args.source)

    source_name = args.source.split('.')

    data = json.loads(args.data)
    target = ''.join(data[args.target].split()).lower()
    output_name = '.'.join(source_name[:-1]) + f'-{target}.odt'
    output = zipfile.ZipFile(output_name, 'x')

    for file_ in source.infolist():
        if file_.filename == 'content.xml': continue
        output.writestr(file_, source.read(file_), file_.compress_type)

    content = source.read('content.xml').decode()
    template = Template(content)
    output.writestr('content.xml',
                    template.render(**data).encode(),
                    source.getinfo('content.xml').compress_type)
    output.close()
    source.close()

    try:
        subprocess.run(['libreoffice', '--convert-to', 'pdf', output_name])
    except OSError as e:
        exit('libreoffice not found. cannot convert odt to pdf.')
    except Exception as e:
        exit(e)

