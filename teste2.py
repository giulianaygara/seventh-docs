from locust import HttpUser, TaskSet, task, between

class TesteDePerformance(TaskSet):

    @task
    def testar_soma(self):
        # Simula uma requisição ao serviço de soma
        self.client.get("/soma?a=10&b=20")

class UsuarioSimulado(HttpUser):
    tasks = [TesteDePerformance]
    wait_time = between(1, 2)


if __name__ == '__main__':
    import os
    os.system("locust -f teste2.py")