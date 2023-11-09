import pytest
import requests

endpoint = "http://127.0.0.1:5000"

resp = requests.get(endpoint)

data = resp.json()
print(data)

status_code = resp.status_code
print(status_code)




def test_create_question(self):
    #create
    payload = new_task_payload()
    resp = requests.post(endpoint, json=payload)
    assert resp.status_code == 200
    #get   
    data = resp.json()
    print(data) 
    pass

def get_questions(self):
    #create
    resp = requests.get(endpoint)
    assert resp.status_code == 200

    data = resp.json()
    question_id = data["questions"]["question_id"]
    resp = requests.get(endpoint + f"/questions/{question_id}")
    assert resp.status_code == 200

    data = resp.json()
    print(data)

    assert data["id"] == payload["id"]
    #list
    pass


# Helper functions
def test_update_question():
    #create
    payload = new_task_payload()
    create_task_resp = create_task(payload)
    task_id = create_task_resp.json()["task"]["task_id"]
    #update
    new_payload = {
        "author": "Sonye Woyinka",
		"id": payload["id"],
		"rating": 5,
		"title": "Things fall apart"
    }
    #get
    update_task_resp = update_task(new_payload)
    assert update_task_resp.status_code == 200
    pass

def delete_question():
    #create
    
    #delete
    #get
    pass
def new_task_payload():
    return {
        "author": "Chinua Achebe",
		"id": 54,
		"rating": 5,
		"title": "Things fall apart"
    }
def create_task(payload):
    return requests.get(endpoint, json=payload)


def update_task(payload):
    return requests.patch(endpoint, json=payload)


def get_task(task_id):
    return requests.get(endpoint + f"/task/{task_id}")