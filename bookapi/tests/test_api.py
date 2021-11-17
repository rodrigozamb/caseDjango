import requests

def test_get_all_books():
    
    #Testing getting all the books, should be able

    headers = {
        'Accept':"*/*",
        'User-Agent':"request"
    }

    url = "http://localhost:8000/books/"

    resp = requests.get(url,headers=headers)
    resp_dict = resp.json()
    
    assert(resp.status_code == 200)


def test_create_a_valid_book():
    
    #Testing the creation of a new book, should not be able

    headers = {
        'Accept':"*/*",
        'User-Agent':"request"
    }

    url = "http://localhost:8000/books/"
    newbook = {'nome':"Game of Thrones","descricao":"luta","nota":10}
    insertReq = requests.post(url,data=newbook,headers=headers)
    insertReqJson = insertReq.json()

    resp = requests.delete(url+str(insertReqJson['id'])+'/',headers=headers)
    
    assert(insertReq.status_code == 201)   

def test_create_a_invalid_book():

    #Testing the creation of a repeated book, should not be able

    headers = {
        'Accept':"*/*",
        'User-Agent':"request"
    }

    url = "http://localhost:8000/books/"
    newbook = {'nome':"Game of Thrones","descricao":"luta","nota":10}
    insertReq = requests.post(url,data=newbook,headers=headers)
    insertReqJson = insertReq.json()

    repeatedInsertReq = requests.post(url,data=newbook,headers=headers)
    
    resp = requests.delete(url+str(insertReqJson['id'])+'/',headers=headers)
    
    assert(insertReq.status_code == 201 and repeatedInsertReq.status_code == 400)    

def test_get_one_book():

    # Testing getting one specific book by its id, should be able 
    
    headers = {
        'Accept':"*/*",
        'User-Agent':"request"
    }

    url = "http://localhost:8000/books/"

    newbook = {'nome':"Game of Thrones","descricao":"luta","nota":10}
    insertReq = requests.post(url,data=newbook,headers=headers)

    insertReqJSon = insertReq.json()


    resp = requests.get(url+str(insertReqJSon['id'])+'/',headers=headers)
    resp_dict = resp.json()
    

    resp = requests.delete(url+str(insertReqJSon['id'])+'/',headers=headers)

    assert(insertReq.status_code == 201 and resp_dict['id'] == insertReqJSon['id'])


def test_updating_a_book():

    #Testing the book update, should be able

    headers = {
        'Accept':"*/*",
        'User-Agent':"request"
    }

    url = "http://localhost:8000/books/"
    newbook = {'nome':"Game of Thrones","descricao":"luta","nota":10}
    insertReq = requests.post(url,data=newbook,headers=headers)
    insertReqJson = insertReq.json()


    updatedbook = {'nome':"Game of Thrones","descricao":"dragoes","nota":10}
    putReq = requests.put(url+str(insertReqJson['id'])+'/',data=updatedbook,headers=headers)


    getReq = requests.get(url+str(insertReqJson['id'])+'/',headers=headers)
    getReqJson = getReq.json()
    
    resp = requests.delete(url+str(insertReqJson['id'])+'/',headers=headers)
    
    assert(insertReq.status_code == 201 and putReq.status_code==200 and getReqJson['descricao'] == 'dragoes')   


def test_deleting_a_book():

    #Testing the book delete, should be able

    headers = {
        'Accept':"*/*",
        'User-Agent':"request"
    }

    url = "http://localhost:8000/books/"
    newbook = {'nome':"Game of Thrones","descricao":"luta","nota":10}
    insertReq = requests.post(url,data=newbook,headers=headers)
    insertReqJson = insertReq.json()
    
    deleteReq = requests.delete(url+str(insertReqJson['id'])+'/',headers=headers)
    
    assert(insertReq.status_code == 201 and deleteReq.status_code == 204 )   


