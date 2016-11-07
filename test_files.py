import pytest
import json, files
from files_commands import get_content_by_file

@pytest.fixture
def client(request):
    client = e.app.test_client()
    return client


@pytest.mark.order1
def test_jenkins_service_create_fail(client):

        #Se inicia con la comprobación de que el servicio no agregue archivos corruptos
        #Se crean archivos con parametros vacios en formato Json
        testFile1  = {'filename': 'fileJenkinsTest1', 'content':''}
        testFile2  = {'filename': '', 'content':'This is a test 2 from Jenkins'}
        testFile3  = {'filename': '', ''}

        #Se ejecuta el servicio POST por cada JSON
        execute1 = client.post('/v1.0/files', data = json.dumps(testFile1), content_type='application/json')
        execute2 = client.post('/v1.0/files', data = json.dumps(testFile2), content_type='application/json')
        execute3 = client.post('/v1.0/files', data = json.dumps(testFile3), content_type='application/json')

        #Se comprueba que efectivamente no se pueden crear
        assert execute1.status == '404 NOT FOUND'
        assert execute2.status == '404 NOT FOUND'
        assert execute3.status == '404 NOT FOUND'


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
        assert execute1.status == '200 OK'
        assert execute2.status == '200 OK'
        assert execute3.status == '200 OK'
        assert execute4.status == '200 OK'
        assert execute5.status == '200 OK'

        #Se procede a verificar que efectivamente los archivos creados poseen el contenido mandado
        assert get_content_by_file("fileJenkinsTest1") == "This is a test 1 from Jenkins"
        assert get_content_by_file("fileJenkinsTest2") == "This is a test 2 from Jenkins"
        assert get_content_by_file("fileJenkinsTest3") == "This is a test 3 from Jenkins"
        assert get_content_by_file("fileJenkinsTest4") == "This is a test 4 from Jenkins"
        assert get_content_by_file("fileJenkinsTest5") == "This is a test 6 from Jenkins"


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
