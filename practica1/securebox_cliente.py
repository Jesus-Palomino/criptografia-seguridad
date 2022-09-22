import argparse

from file import upload, list_files, download, delete_file
from functions import search, create, sign, encrypt, delete, decipher, enc_sign

TOK = "6fEFde1c8aD4bA03"


def SecureBoxClient():
    print("iniciando\n")
    parser = argparse.ArgumentParser(description='Parse the func action')
    parser.add_argument('--create_id', dest='create', nargs='+', default=False,
                        help='Registra un usuario. Indicar nombre, apellido/s y email.')
    parser.add_argument('--search_id', dest='search', nargs='+', default=False,
                        help='Busca un usuario. Indicar nombre, apellido/s o email.')
    parser.add_argument('--delete_id', dest='delete', nargs='+', default=False,
                        help='Borra un usuario. Indicar Id.')
    parser.add_argument('--sign', dest='sign', nargs='+', default=False,
                        help='Firma un Fichero')
    parser.add_argument('--encrypt', dest='encrypt', nargs='+', default=False,
                        help='Encriptar un Fichero')
    parser.add_argument('--dest_id', dest='dest_id', nargs='+', default=False,
                        help='Id receptor')
    parser.add_argument('--source_id', dest='source_id', nargs='+', default=False,
                        help='Id emisor')
    parser.add_argument('--enc_sign', dest='enc_sign', nargs='+', default=False,
                        help='firma y cifra fichero')
    parser.add_argument('--dencrypt', dest='dencrypt', nargs='+', default=False,
                        help='descifra un mensaje y valida su Firma')
    parser.add_argument('--upload', dest='upload', nargs='+', default=False,
                        help='Sube un fichero al servidor')
    parser.add_argument("--list_files", dest='list', nargs="?",
                        help='lista los ficheros del servidor')
    parser.add_argument("--download", dest='download', nargs="+", default=False,
                        help='descarga fichero del servidor')
    parser.add_argument("--delete_file", dest='deletef', nargs="+", default=False,
                        help='borra fichero del servidor')
    args = parser.parse_args()

    return args


def case(args):
    if args.create:
        token = TOK
        alias = ""
        if len(args.create) == 2:
            name = args.create[0]
            email = args.create[1]
            create(name, email, alias, token)
        elif len(args.create) == 3:
            name = args.create[0] + " " + args.create[1]
            email = args.create[2]
            create(name, email, alias, token)
        else: 
            print("Error parametros de registro.\n")

    elif args.search:
        token = TOK
        search(args.search[0], token)

    elif args.delete:
        token = TOK
        delete(args.delete[0], token)

    elif args.sign:
        if args.sign is not None:
            sign(args.sign[0])

    elif args.encrypt:
        token = TOK
        if args.encrypt is not None:
            encrypt(args.encrypt[0], args.dest_id[0], token)

    elif args.enc_sign:
        token = TOK
        if args.enc_sign is not None:
            enc_sign(args.enc_sign[0], args.dest_id[0], token)

    elif args.dencrypt:
        token = TOK
        if args.dencrypt is not None:
            decipher(args.dencrypt[0], args.dest_id[0], token)

    elif args.upload:
        token = TOK
        if args.upload is not None:
            upload(args.upload[0], args.dest_id[0], token)

    elif args.list:
        token = TOK
        list_files(token)

    elif args.download:
        token = TOK
        if args.download is not None:
            download(args.download[0], args.source_id[0], token)

    elif args.deletef:
        token = TOK
        if args.deletef is not None:
            delete_file(args.deletef[0], token)


def start():
    args = SecureBoxClient()
    case(args)


if __name__ == "__main__":
    start()
