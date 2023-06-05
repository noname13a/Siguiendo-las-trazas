Para recrear este reto son necesarias dos máquinas: una con un servidor, puede ser la tuya, y una virtual, con un cliente, para no capturar nada que no deba serlo.

Los dos script en python se pueden correr tal cual están, salvo que habrá que modificar, como mínimo, la dirección del servidor en los dos scripts.

Para cambiar la conversación basta con modificar los mensajes mandados a través del método sendall(), y se puede copiar el código múltiples veces para añadir mas trafico.

Tal y como están los scripts, la dificultad del reto es demasiado sencilla. Se puede añadir trafico "basura" que dificultaría encontrar la comunicación TCP con diferentes herramientas, en mi caso: https://github.com/1tayH/noisy
Bastaría con correr ese script mientras se captura con Wireshark, y luego lanzar los dos scripts de python, empezando por server.py. Para finalizar, dejar de capturar, guardar el .pcap y eso es todo lo necesario. También, parar la ejecución de noisy.py. Cabe añadir, que la herramienta para generar trafico basura tiene un archivo config para determinar que páginas visita, el cual es editable para añadir o eliminar mas opciones. Entre una de las opciones se haya una página de pornografía, o un foro troll online.
