from app import app, main, manager, scheduler

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
	app.run(host='0.0.0.0', port=port, debug=True)
	#app.run(debug=True)
	print('subiu')
