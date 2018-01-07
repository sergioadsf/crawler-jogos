from app import app, main, manager, scheduler

@manager.command
def execute():
	main.main()
	print('subindo')
	app.run()
	print('subiu')

if(__name__ == '__main__'):
	manager.run()
