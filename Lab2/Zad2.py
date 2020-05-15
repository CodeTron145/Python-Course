import sys

ascii_array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def base64_encode(argv3, argv4):
    with open(argv3, 'r') as bin_file:
        reader = bin_file.read()
        bin_file.close()

    binary = reader
    i = 0
    length = len(binary)
    final_ascii_encode = ''
    while length > 0:
        if length % 3 != 0 and length < 6:
            binary += '00'
            length += 2
            continue
        else:
            tmp = binary[i: i + 6]
            tmp_int = int(tmp, 2)
            final_ascii_encode += ascii_array[tmp_int]
            length -= 6
            i += 6

    final_ascii_encode_list = [final_ascii_encode]
    while len(final_ascii_encode) % 4 != 0:
        final_ascii_encode_list.append('=')
        final_ascii_encode = ''.join(final_ascii_encode_list)

    with open(argv4, 'w') as decoded_file:
        decoded_file.seek(0)
        decoded_file.truncate()
        decoded_file.write(final_ascii_encode)
        decoded_file.close()


base64_encode("plik.bin", "plik_enc.txt")


def base64_decode(argv3, argv4):
    with open(argv3, 'r') as encoded_file:
        data = encoded_file.read()
        encoded_file.close()

    decoded_file_list = ""
    for i in data:
        if i == '=':
            decoded_file_list = decoded_file_list[:-2]
            continue
        decoded_file_list += format(ascii_array.index(i), '06b')

    with open(argv4, 'w') as bin_file:
        bin_file.write(decoded_file_list)
        bin_file.close()


if sys.argv[1] == '--encode':
    base64_encode(sys.argv[2], sys.argv[3])
elif sys.argv[1] == '--decode':
    base64_decode(sys.argv[2], sys.argv[3])
