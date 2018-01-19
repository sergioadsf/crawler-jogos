from app import scheduler

from app import classificacao, calendario

def schedule_job():
	print("Vamos executar o job!")
	classificacao.executar()
	calendario.executar()

def main():
	scheduler.add_job(schedule_job, 'interval', minutes=20)
	scheduler.start()