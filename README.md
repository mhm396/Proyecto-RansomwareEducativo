# Creación de un ransomware utilizando criptosistemas RSA y McEliece (post-cuántica)

Este proyecto implementa un ransomware funcional en Python para sistemas Linux x64, diseñado en tres fases, que utiliza diferentes técnicas de criptografía para encriptar archivos y exigir un rescate para su recuperación. El objetivo es ilustrar cómo los sistemas criptográficos avanzados pueden ser utilizados en la creación de un malware.

## Fases del Proyecto

### Fase 1: Ransomware con criptosistema de clave simétrica (AES + CBC)
El ransomware encripta los archivos en el directorio **Documentos** usando el algoritmo AES en modo CBC con una clave de 128 bits. Se utiliza el módulo **Fernet** para la encriptación, que emplea una clave simétrica para proteger los archivos de texto, imágenes, etc. Los archivos encriptados son acompañados de un archivo de texto que exige el pago de un rescate.

### Fase 2: Ransomware con criptosistema de clave asimétrica (RSA)
Se mejora la seguridad del ransomware al encriptar la clave simétrica (AES) con **RSA**. Este método utiliza la factorización de números enteros para asegurar la clave privada, y solo el propietario de la clave privada podrá descifrar los archivos.

### Fase 3: Ransomware con criptosistema McEliece (Criptografía post-cuántica)
La última fase implementa el **criptosistema McEliece**, un algoritmo asimétrico robusto contra ataques cuánticos. McEliece usa códigos lineales y matrices aleatorias para encriptar la clave privada. Este paso prepara el ransomware para un escenario post-cuántico, donde los algoritmos como RSA podrían ser vulnerables a la computación cuántica.

## Tecnologías y Librerías Utilizadas

- **Python 3.0**: Lenguaje de programación utilizado para implementar el ransomware.
- **Fernet**: Para encriptación simétrica de archivos.
- **RSA**: Para encriptar la clave simétrica utilizando criptografía de clave pública.
- **McEliece**: Algoritmo post-cuántico basado en códigos lineales.
- **PyInstaller**: Para convertir el código en un ejecutable.
- **PyCryptodome**: Para generar claves y firmas digitales.
- **Tkinter**: Para interfaces gráficas y cuadros de diálogo.

## Descripción del Proceso

1. **Infección**: El usuario descarga un videojuego (ejemplo: "Tres en raya") que contiene el ransomware. Una vez ejecutado, el malware encripta los archivos en el directorio **Documentos**.
2. **Cifrado**: Los archivos se cifran utilizando primero AES con una clave simétrica, luego RSA encripta la clave, y finalmente se usa McEliece para encriptar la clave privada de manera segura.
3. **Exigencia de Rescate**: Un archivo de texto es creado en el directorio afectado, solicitando un rescate para la recuperación de los archivos.

## Seguridad y Consideraciones

- El uso de AES, RSA y McEliece asegura que el ransomware sea difícil de descifrar sin la clave adecuada.
- McEliece proporciona una solución robusta contra posibles futuros avances en computación cuántica.

## Importante

Este proyecto es para fines educativos y de investigación. El uso de este código con fines maliciosos es ilegal y está en contra de las políticas éticas. No se debe utilizar para afectar a sistemas de otros usuarios sin su consentimiento.


