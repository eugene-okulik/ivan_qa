from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)
    headers = {'Content-Type': 'application/json'}

    def on_start(self):
        body = {
            "name": "Ivan",
            "data": {
                "age": 20,
                "city": "Budva"
            }
        }

        response = self.client.post(
            '/object', json=body, headers=self.headers
        )
        self.obj_id = response.json()['id']

    @task(1)
    def get_all_obj(self, headers=None):
        self.client.get(
            '/object', headers=self.headers
        )

    @task(10)
    def create_obj(self, name='Ivan', age=20, city='Budva', headers=None):
        body = {
            "name": name,
            "data": {
                "age": age,
                "city": city
            }
        }

        headers = headers if headers else self.headers
        self.client.post(
            '/object', json=body, headers=headers
        )

    @task(30)
    def get_object(self):
        self.client.get(
            f'/object/{self.obj_id}', headers=self.headers
        )

    @task(4)
    def put_object(self, name='Mark', age=30, city='Bar', headers=None):
        body = {
            "name": name,
            "data": {
                "age": age,
                "city": city
            }
        }

        headers = headers if headers else self.headers
        self.client.put(
            f'/object/{self.obj_id}', json=body, headers=headers
        )

    @task(5)
    def patch_object(self, name='Mark', age=31, headers=None):
        body = {
            "name": name,
            "data": {
                "age": age
            }
        }

        headers = headers if headers else self.headers
        self.client.patch(
            f'/object/{self.obj_id}', json=body, headers=headers
        )

    @task(1)
    def delete_object(self):
        self.client.delete(
            f'/object/{self.obj_id}', headers=self.headers
        )

        # создаем новый объект
        body = {
            "name": "Ivan",
            "data": {
                "age": 20,
                "city": "Budva"
            }
        }
        response = self.client.post(
            '/object', json=body, headers=self.headers
        )
        self.obj_id = response.json()['id']
