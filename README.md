# Segundo Parcial Jenkins

<b>Autor:</b> Johan David Ballesteros<br>
<b>Código:</b> 13103036<br>
<b>Repositorio:</b> https://github.com/DavidPDP/testproject


# Jenkins

Para entender qué es Jenkins, primero necesitamos comprender que es integración continua.

##Integración Continua
Según Martin Fowler, "*La integración continua es una práctica de desarrollo de software en la cuál los miembros de un equipo integran su trabajo frecuentemente, como mínimo de forma diaria. Cada integración se verifica mediante una herramienta de construcción automática para detectar los errores de integración tan pronto como sea posible. Muchos equipos creen que este enfoque lleva a una reducción significativa de los problemas de integración y permite a un equipo desarrollar software cohesivo de forma más rápida*".

## ¿Qué es Jenkins?
Jenkins es un servidor de integración continua, actualmente es uno de los más utilizados en el mercado para esta función, teniendo en cuenta que Jenkins es open-source. Esta basado en el proyecto Hudson desarrollado por Kohsuke Kawaguchi.<br>
Puede soportar herramientas de control de versiones como:<br>
* CVS.
* Subversion.
* Git.
* Mercurial.

Puede ejecutar proyectos basados en:
* Apache Ant.
* Apache Maven.

Y ejecutar:
* Scripts de shell.
* Programas batch de Windows.

-----------

#Desarrollo Parcial
A continuación se muestra el desarrollo del segundo parcial, como supuestos para este desarrollo se tiene instalado CentOS 6.8 y la fecha del Servidor se encuentra actualizada.

##Configuraciones Iniciales
Primero se realiza la configuración del entorno de Jenkins, para esto se realizó los siguientes pasos. <br>

Se instala el Jenkins con sus dependencias.
```sh
# yum install java-1.7.0-openjdk
# yum install wget -y
# yum install git -y
# sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
# sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
# sudo yum install jenkins
```
Iniciar el servicio de Jenkins y habilitar su puerto
```sh
# chkconfig jenkins on
# service jenkins start
# iptables -I INPUT 5 -p tcp -m state --state NEW -m tcp --dport 8080 -j ACCEPT
# service iptables save
```
Se crea el usuario y ambiente virtual para Jenkins
```sh
# useradd jenkins
# passwd jenkins
# su jenkins
$ mkdir /var/lib/jenkins/.virtualenvs
$ cd /var/lib/jenkins/.virtualenvs
$ virtualenv testproject
$ . testproject/bin/activate
```
Se procede a instalar las herramientas para el parcial y exportar el archivo de requerimientos.
```sh
$ pip install xmlrunner
$ pip install unittest2
$ pip install pytest
$ pip install pytest-cov
$ pip install flask

$ pip freeze > requirements.txt
```
Con lo anterior se finaliza la pre-configuración del entorno de trabajo.
------

## Enlazar Jenkins con GitHub
Para esto procedemos a ingresar al sitio web de Jenkins, como se definió anteriormente, Jenkins quedó atendiendo por el puerto 8080.

Esta es la vista general del sitio web de Jenkins.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins1.PNG)

Se procede a crear un proyecto.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins2.PNG)

Se procede a enlazar el Jenkins con el repositorio por medio de la URL del repositorio.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins3.PNG)

Se procede a configurar el tiempo de ejecución periodica.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins4.PNG)

Se procede a ingresar el comando de ejecución con el archivo que contiene el test.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins10.PNG)

Se procede a ingresar la ruta del fichero XML donde se guardará la traza del test.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins11.PNG)

El proyecto se ha instalado correctamente.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins12.PNG)


## Pruebas 
A continuación se presentan los servicios que se probarán.

[Servicios a probar](https://github.com/DavidPDP/testproject/blob/master/files.py)

Para probar los anteriores servicios se realizó el siguiente test.
```py
import pytest
import json, files
from files_commands import get_content_by_file

@pytest.fixture
def client(request):
    client = files.app.test_client()
    return client


@pytest.mark.order1
def test_jenkins_service_create_fail(client):

        #Se inicia con la comprobación de que el servicio no agregue archivos corruptos
        #Se crean archivos con parametros vacios en formato Json
        testFile1  = {'filename': 'fileJenkinsTest1', 'content':''}
        testFile2  = {'filename': '', 'content':'This is a test 2 from Jenkins'}

        #Se ejecuta el servicio POST por cada JSON
        execute1 = client.post('/v1.0/files', data = json.dumps(testFile1), content_type='application/json')
        execute2 = client.post('/v1.0/files', data = json.dumps(testFile2), content_type='application/json')

        #Se comprueba que efectivamente no se pueden crear
        assert execute1.status == '400 BAD REQUEST'
        assert execute2.status == '400 BAD REQUEST'


@pytest.mark.order2
def test_jenkins_service_create(client):
        
        #Se sigue con la comprobacìón de que el servicio agrega correctamente los archivos
        #Se crean los archivos de prueba en formato Json
        testFile1 = {'filename': 'fileJenkinsTest1', 'content': 'This is a test 1 from Jenkins'}
        testFile2 = {'filename': 'fileJenkinsTest2', 'content': 'This is a test 2 from Jenkins'}
        testFile3 = {'filename': 'fileJenkinsTest3', 'content': 'This is a test 3 from Jenkins'}
        testFile4 = {'filename': 'fileJenkinsTest4', 'content': 'This is a test 4 from Jenkins'}
        testFile5 = {'filename': 'fileJenkinsTest5', 'content': 'This is a test 5 from Jenkins'}

        #Se ejecuta el servicio POST por cada Json creado
        execute1 = client.post('/v1.0/files', data = json.dumps(testFile1), content_type='application/json')
        execute2 = client.post('/v1.0/files', data = json.dumps(testFile2), content_type='application/json')
        execute3 = client.post('/v1.0/files', data = json.dumps(testFile3), content_type='application/json')
        execute4 = client.post('/v1.0/files', data = json.dumps(testFile4), content_type='application/json')
        execute5 = client.post('/v1.0/files', data = json.dumps(testFile5), content_type='application/json')

        #Se procede a verificar si efectivamente realizó el servicio POST
        assert execute1.status == '201 CREATED'
        assert execute2.status == '201 CREATED'
        assert execute3.status == '201 CREATED'
        assert execute4.status == '201 CREATED'
        assert execute5.status == '201 CREATED'

        #Se procede a verificar que efectivamente los archivos creados poseen el contenido mandado
        assert get_content_by_file("fileJenkinsTest1") == "This is a test 1 from Jenkins"
        assert get_content_by_file("fileJenkinsTest2") == "This is a test 2 from Jenkins"
        assert get_content_by_file("fileJenkinsTest3") == "This is a test 3 from Jenkins"
        assert get_content_by_file("fileJenkinsTest4") == "This is a test 4 from Jenkins"
        assert get_content_by_file("fileJenkinsTest5") == "This is a test 5 from Jenkins"


@pytest.mark.order3
def test_jenkins_service_read_recent_file(client):

        #Se sigue con la comprobación del servicio que devuelve los tres archivos que han sido creados recientemente
        #Se aprovecha correr la anterior prueba para que la prueba de este servicio contenga los archivos creados anteriormente
        #Se procede a ejecutar el servicio GET
        execute1 = client.get('/v1.0/files/recently_created',follow_redirects=True)

        #Se procede a verificar que efectivamente retornó los tres archivos creados recientemente
        assert "fileJenkinsTest3" in execute1.data
        assert "fileJenkinsTest4" in execute1.data
        assert "fileJenkinsTest5" in execute1.data


@pytest.mark.order4
def test_jenkins_service_get_all_files(client):

        #Se sigue con la comprobación del servicio que devuelve todos los archivos
        #Se aprovecha correr la anterior prueba para que la prueba de este servicio contenga los archivos creados anteriormente
        #Se procede a ejecutar el request GET
        execute1 = client.get('/v1.0/files',follow_redirects=True)

        #Se procede a verificar que efectivamente retornó los archivos creados anteriormente
        assert "fileJenkinsTest1" in execute1.data
        assert "fileJenkinsTest2" in execute1.data
        assert "fileJenkinsTest3" in execute1.data
        assert "fileJenkinsTest4" in execute1.data
        assert "fileJenkinsTest5" in execute1.data


@pytest.mark.order5
def test_jenkins_service_remove_file(client):

        #Para finalizar el test se procede a eliminar a comprobar el servicio que elimina todos los archivos
        #Se procede a ejecutar el request DELETE
        client.delete('/v1.0/files', follow_redirects=True)

        #Para comprobar que se eliminaron los archivos se solicita el servicio que retorna todos los archivos
        #Se procede a ejecutar el request GET
        execute1 = client.get('/v1.0/files',follow_redirects=True)

        #Se procede a verificar que efectivamente se eliminaron todos los archivos
        assert "fileJenkinsTest1" not in execute1.data
        assert "fileJenkinsTest2" not in execute1.data
        assert "fileJenkinsTest3" not in execute1.data
        assert "fileJenkinsTest4" not in execute1.data
        assert "fileJenkinsTest5" not in execute1.data
        
        #Finaliza el test de los servicios, se debe tener en cuenta que los otros request no se encuentran implementados
        #Lo cual significa que no ejercen ninguna acción, por lo tanto no se necesitan probar por el momento
```

## Resultados
A continuación se muestran y explican los resultados obtenidos tras realizadas las pruebas.

![alt text](https://github.com/DavidPDP/testproject/blob/master/imagenes/parcialJenkins9.PNG)
