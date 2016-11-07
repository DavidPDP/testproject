import pytest
import json, files
from files_commands import get_content_by_file

@pytest.fixture
def client(request):

    client = e.app.test_client()

    client = files.app.test_client()

    return client


@pytest.mark.order1
def test_jenkins_service_create_fail(client):


        
        testFile1  = {'filename': 'fileJenkinsTest1', 'content':''}
        testFile2  = {'filename': '', 'content':'This is a test 2 from Jenkins'}
        testFile3  = {'filename': '', ''}

    
        execute1 = client.post('/v1.0/files', data = json.dumps(testFile1), content_type='application/json')
        execute2 = client.post('/v1.0/files', data = json.dumps(testFile2), content_type='application/json')
        execute3 = client.post('/v1.0/files', data = json.dumps(testFile3), content_type='application/json')

       
        assert execute1.status == '404 NOT FOUND'
        assert execute2.status == '404 NOT FOUND'
        assert execute3.status == '404 NOT FOUND'

        
        testFile1  = {'filename': 'fileJenkinsTest1', 'content':''}
        testFile2  = {'filename': '', 'content':'This is a test 2 from Jenkins'}

        
        execute1 = client.post('/v1.0/files', data = json.dumps(testFile1), content_type='application/json')
        execute2 = client.post('/v1.0/files', data = json.dumps(testFile2), content_type='application/json')

        
        assert execute1.status == '400 BAD REQUEST'
        assert execute2.status == '400 BAD REQUEST'



@pytest.mark.order2
def test_jenkins_service_create(client):
        

      

        
        testFile1 = {'filename': 'fileJenkinsTest1', 'content': 'This is a test 1 from Jenkins'}
        testFile2 = {'filename': 'fileJenkinsTest2', 'content': 'This is a test 2 from Jenkins'}
        testFile3 = {'filename': 'fileJenkinsTest3', 'content': 'This is a test 3 from Jenkins'}
        testFile4 = {'filename': 'fileJenkinsTest4', 'content': 'This is a test 4 from Jenkins'}
        testFile5 = {'filename': 'fileJenkinsTest5', 'content': 'This is a test 5 from Jenkins'}


       



        execute1 = client.post('/v1.0/files', data = json.dumps(testFile1), content_type='application/json')
        execute2 = client.post('/v1.0/files', data = json.dumps(testFile2), content_type='application/json')
        execute3 = client.post('/v1.0/files', data = json.dumps(testFile3), content_type='application/json')
        execute4 = client.post('/v1.0/files', data = json.dumps(testFile4), content_type='application/json')
        execute5 = client.post('/v1.0/files', data = json.dumps(testFile5), content_type='application/json')


        assert execute1.status == '200 OK'
        assert execute2.status == '200 OK'
        assert execute3.status == '200 OK'
        assert execute4.status == '200 OK'
        assert execute5.status == '200 OK'

      


        assert execute1.status == '201 CREATED'
        assert execute2.status == '201 CREATED'
        assert execute3.status == '201 CREATED'
        assert execute4.status == '201 CREATED'
        assert execute5.status == '201 CREATED'

        

        assert get_content_by_file("fileJenkinsTest1") == "This is a test 1 from Jenkins"
        assert get_content_by_file("fileJenkinsTest2") == "This is a test 2 from Jenkins"
        assert get_content_by_file("fileJenkinsTest3") == "This is a test 3 from Jenkins"
        assert get_content_by_file("fileJenkinsTest4") == "This is a test 4 from Jenkins"

        assert get_content_by_file("fileJenkinsTest5") == "This is a test 6 from Jenkins"

        assert get_content_by_file("fileJenkinsTest5") == "This is a test 5 from Jenkins"



@pytest.mark.order3
def test_jenkins_service_read_recent_file(client):


        
        execute1 = client.get('/v1.0/files/recently_created',follow_redirects=True)



        
        execute1 = client.get('/v1.0/files/recently_created',follow_redirects=True)

        

        assert "fileJenkinsTest3" in execute1.data
        assert "fileJenkinsTest4" in execute1.data
        assert "fileJenkinsTest5" in execute1.data


@pytest.mark.order4
def test_jenkins_service_get_all_files(client):

        execute1 = client.get('/v1.0/files',follow_redirects=True)

   
        
        execute1 = client.get('/v1.0/files',follow_redirects=True)

        

        assert "fileJenkinsTest1" in execute1.data
        assert "fileJenkinsTest2" in execute1.data
        assert "fileJenkinsTest3" in execute1.data
        assert "fileJenkinsTest4" in execute1.data
        assert "fileJenkinsTest5" in execute1.data


@pytest.mark.order5
def test_jenkins_service_remove_file(client):


       
        client.delete('/v1.0/files', follow_redirects=True)

        execute1 = client.get('/v1.0/files',follow_redirects=True)

       
        
        client.delete('/v1.0/files', follow_redirects=True)

        
        execute1 = client.get('/v1.0/files',follow_redirects=True)

        

        assert "fileJenkinsTest1" not in execute1.data
        assert "fileJenkinsTest2" not in execute1.data
        assert "fileJenkinsTest3" not in execute1.data
        assert "fileJenkinsTest4" not in execute1.data
        assert "fileJenkinsTest5" not in execute1.data


        #Finaliza el test de los servicios, se debe tener en cuenta que los otros request no se encuentran implementados
        #Lo cual significa que no ejercen ninguna acción, por lo tanto no se necesitan probar por el momento

        


