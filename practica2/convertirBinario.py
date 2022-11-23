import io
import PIL.Image as Image


class convertirBinario:

    imagen = "img.jpg"


    def __init__(self) -> None:

        # Ejemplos

        # self.image_to_bits("img.jpg", "binario.txt")
        # self.bits_to_image("binario.txt", "prueba.jpg")

        self.text_to_bits("texto.txt", "binario.txt")
        self.bits_to_text("binario.txt", "texto2.txt")


    def bytes_to_bits(self, bytes):
        bits = ""
        for i in range(len(bytes)):
            bits += '{0:08b}'.format(bytes[i])

        return bits


    def bits_to_bytes(self, s):
        return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
    

    def image_to_bits(self, imagen = "img.jpg", binario = "binario.txt"):
        with open("./imagenes/" + imagen, "rb") as image:
            f = image.read()
            bytes = bytearray(f)
        
        bits = self.bytes_to_bits(bytes)
  
        with open("./ficheros/" + binario, 'w') as fp:
            for item in bits:
                fp.write("%s" % item)
    

    def bits_to_image(self, binario = "binario.txt", imagen = "prueba.jpg"):
        fichero = open("./ficheros/" + binario)
        binario = fichero.read()

        bytes = bytearray(self.bits_to_bytes(binario))
        
        image = Image.open(io.BytesIO(bytes))
        image.save("./imagenes/" + imagen)


    def bits_to_string(self, b=None):
        return ''.join([chr(int(x, 2)) for x in b])

    
    def text_to_bits(self, texto = "texto2.txt", binario = "binario.txt"):
        bits = []

        fichero = open("./ficheros/" + texto)
        while 1:
            char = fichero.read(1).lower()         
            if not char:
                break
            if char != " " and char.isalpha():
                bits.append(format(ord(char),'08b'))

        with open("./ficheros/" + binario, 'w') as fp:
            for item in bits:
                fp.write("%s" % item)


    def bits_to_text(self, binario = "binario.txt", texto = "texto2.txt"):
        fichero = open("./ficheros/" + binario)
        binario = fichero.read()

        bytes = []
        for i in range(int(len(binario) / 8)):
            bytes.append(int(binario[i*8:i*8+8],2))

        texto_plano = ""
        for byte in bytes:
            texto_plano += chr(byte)
        
        with open("./ficheros/" + texto, 'w') as fp:
            for item in texto_plano:
                fp.write("%s" % item)
        

prueba = convertirBinario()
