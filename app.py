#web: gunicorn -b 0.0.0.0:$PORT app:app
from app import app, main, manager, scheduler
import os

@manager.command
def execute():
	main.main()
	print('subindo')
	app.run()
	print('subiu')

if(__name__ == '__main__'):
	#manager.run()
	main.main()
	print('subindo')
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port)
	print('subiu')
