<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>

</table>
</div>

<div align="center">
<span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Django</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>

<tr><td colspan="6">INTEGRANTES:
    <ul>
        <li><P>Luis Edgar Arocutipa Gutierrez</P></li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Carlo Corrales Delgado</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

#

## EJERCICIOS PROPUESTOS
-   Reproducir las actividades de los videos donde trabajamos:

    1. Relación de uno a muchos

    2. Relación muchos a muchos

    3. Impresión de pdfs 

    4. Envio de emails

- Crear su video Flipgrid:  https://flip.com/8a44775d
#

## SOLUCIÓN DE LOS EJERCICIOS PROPUESTOS
- Para la resolución del segundo laboratorio se creó el siguiente repositoiro en GitHub:
https://github.com/LuisArocutipa/Pweb2-Lab07
- En Django, puedes definir diferentes tipos de relaciones entre modelos utilizando campos relacionales. Dos de las relaciones más comunes son la relación de uno a muchos y la relación de muchos a muchos.

- Relación de uno a muchos:
    - La relación de uno a muchos se establece cuando un objeto de un modelo está relacionado con varios objetos de otro modelo, pero cada objeto relacionado solo puede estar asociado con un objeto del modelo de origen.
    - Por ejemplo, considera los modelos "Autor" y "Libro". Un autor puede tener varios libros, pero cada libro solo puede tener un autor.
    - Aquí, el campo autor en el modelo de Libro establece la relación de uno a muchos con el modelo de Autor. El parámetro on_delete=models.CASCADE indica que si se elimina un autor, todos los libros asociados a ese autor también se eliminarán
    <br><img src="https://github.com/LuisArocutipa/Pweb2-Lab07/blob/main/imagenes/unomuchos.PNG?raw=true" style="width:80%; height:auto"/><br>

- Relación de muchos a muchos:
    - La relación de muchos a muchos se establece cuando varios objetos de un modelo están relacionados con varios objetos de otro modelo, y viceversa. Ambos modelos pueden tener varios objetos relacionados entre sí.
    - Por ejemplo, considera los modelos "Alumno" y "Asignatura". Varios estudiantes pueden estar inscritos en varias asignaturas, y varias asignaturas pueden tener varios alumnos matriculados.
    - Aquí, el campo asignaturas en el modelo de Alumno y el modelo de Asignatura establecen una relación de muchos a muchos entre ellos. Django creará automáticamente una tabla de relación intermedia para almacenar los pares de estudiantes y asignaturas asociados.
    <br><img src="https://github.com/LuisArocutipa/Pweb2-Lab07/blob/main/imagenes/muchosmuchos.PNG?raw=true" style="width:80%; height:auto"/><br>
- Para la impresión de PDF primero se instala el framework xhtml2pdf con comando pip. A continuación, se crea el archivo utils.py el cual importara las funciones necesarias para poder implementar la funcion render_to_pdf(), la cual nos servira para convertir el contenido a PDF.
- Luego se crea el archivo invoice.html dentro del directorio templates. En este archivo ira todo el contenido que nosotros queramos que se convierta en PDF. Además, le añade un diseño al contenido de la página. Luego, en el archivo view.py se importa la función antes creada render_to_pdf y se utiliza para crear la Clase GeneratePDF() en la cual se crea un contexto de ejemplo para poder convertirlo a PDF. Además, se le añade la función para poder descargar el archivo o imprimirlo.
<br><img src="https://github.com/LuisArocutipa/Pweb2-Lab07/blob/main/imagenes/pdf.PNG?raw=true" style="width:80%; height:auto"/><br>
- Para poder enviar emails a traves de Django, primero se modifican las urls del proyecto para que incluyan las de la app('Send'). Luego, se crea el archivo urls.py dentro de la app y se le añade un nuevo enlace con el cual se podrá llamar a una función para que se muestre un mensaje. A continuación, dentro del directorio templates/send/ se crea el archivo index.html que contiene el mensaje de confirmación de envio de email.
- Luego en el archivo settings.py se añade toda la configuración, esta incluye el host, puerto, correo, contraseña y tipo de conexión. Despues, en el archivo views.py se crea la función index con la cual se podrá enviar el mensaje poniendo los siguientes requisitos: asunto, el mensaje, el correo al que se va a enviar, el correo que va enviar el mensaje y finalmente un aviso si hubo un error. Finalmente, se muestra en pantalla un mensaje que muestra si se envió el email.
<br><img src="https://github.com/LuisArocutipa/Pweb2-Lab07/blob/main/imagenes/email.PNG?raw=true" style="width:80%; height:auto"/><br>