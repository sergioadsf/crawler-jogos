import schedule
import time

import classificacao
import calendario

def schedule_job():
	classificacao.executar()
	calendario.executar()

def main():
	schedule.every(2).minutes.do(schedule_job)
	while True:
		schedule.run_pending()
		time.sleep(1)

main()
