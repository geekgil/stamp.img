# stamp.img

Carimbe as suas imagens com uma marca d'água invisível!

Este algoritmo usa as bibliotecas cv2, wget, pyunpack e invisible-watermark para criar uma marca d'água invisível nas suas imagens.

## TO-DO
 - puxar foto (download/arquivo interno/pasta zipada)
	 - em caso de pasta zipada
		 - descompactar pasta
	 - em caso de download
		 - baixar foto
 - criar pasta para a(s) foto(s) carimbada(s)
	 - em caso de pasta zipada
		 - iterar por todas as fotos da pasta
			 - carimbar foto (https://github.com/ShieldMnt/invisible-watermark)
         - decode de fotos recém-carimbadas.
         - compactar pasta.
 - carimbar foto (https://github.com/ShieldMnt/invisible-watermark)
 - decode de fotos recém-carimbadas.