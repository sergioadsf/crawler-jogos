from app import scheduler

from app import classificacao, calendario

def schedule_job():
	classificacao.executar()
	calendario.executar()

def main():
	schedule_job()
	scheduler.add_job(schedule_job, 'interval', minutes=2)
	scheduler.start()