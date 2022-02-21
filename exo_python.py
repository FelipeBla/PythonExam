
import datetime
import time
import threading
import random



################################################################################
#   Watchdog to stop tasks
################################################################################
class Watchdog(threading.Thread):

	period = -1
	current_cpt = -1

    	############################################################################
	def __init__(self, period):

		self.period = period
		
		threading.Thread.__init__(self)


    	############################################################################
	def run(self):

		print(" : Starting watchdog")

		self.current_cpt = self.period

		while (1):

			if(self.current_cpt >= 0):

				self.current_cpt -= 1
				time.sleep(1)
				
			else :
				print("!!! Watchdog stops tasks.")
				global watchdog
				watchdog = True
				self.current_cpt = self.period



################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():


	name = None
	priority = -1
	period = -1
	execution_time = -1
	last_deadline = -1
	last_execution_time = None


    	############################################################################
	def __init__(self, name, priority, period, execution_time, last_execution):

		self.name = name
		self.priority = priority
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution


	############################################################################
	def run(self):

		# Update last_execution_time
		self.last_execution_time = datetime.datetime.now()

		global watchdog
		
		execution_time = random.randint(2, 30)

		print(self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ") : execution time = " + str(execution_time))

		while (watchdog == False):

			execution_time -= 1

			time.sleep(1)

			if (execution_time <= 0):
				print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
				return
		

		print(self.name + " : Pre-empting task (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")

	

####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':


	# Init and instanciation of watchdog
	global watchdog
	watchdog = False

	my_watchdog = Watchdog(period = 10)		# Watchdog 10 seconds
	my_watchdog.start()


	last_execution = datetime.datetime.now()
	
	# Instanciation of task objects
	task_list = []
	task_list.append(my_task(name="thread_1", priority = 1, period = 15, execution_time = 10, last_execution = last_execution))
	task_list.append(my_task(name="thread_2", priority = 1, period = 30, execution_time = 5, last_execution = last_execution))
	task_list.append(my_task(name="thread_3", priority = 1, period = 60, execution_time = 30, last_execution = last_execution))



	# Global scheduling loop
	while(1):

		print("\nScheduler tick : " + datetime.datetime.now().strftime("%H:%M:%S"))
		
		# Reinit watchdog
		watchdog = False
		my_watchdog.current_cpt = 10
	
		for task_to_run in task_list :
		
			# Reinit watchdog
			watchdog = False
			my_watchdog.current_cpt = 10
		
			task_to_run.run()
			
			
			
		if task_to_run.name  == "pump_1":
                if oil == 0 :
                    task_to_run.priority = 1
                if oil > 0 and oil < 26:
                    task_to_run.priority = 2
                if oil > 25 and oil < 50:
                    task_to_run.priority = 3
                if oil == 50:
                    task_to_run.priority = 4
                    
                if operator.ge(datetime.datetime.now(), last_execution + datetime.timedelta(0, task_to_run.period)) and task_to_run.priority != 4:
                    if task_to_run.priority == 1:
                        oil += 10
                        time.sleep(task_to_run.execution_time)
                        task_to_run.last_execution_time = datetime.datetime.now()
                    if task_to_run.priority == 2:
                        oil += 10
                        time.sleep(task_to_run.execution_time)  
                        task_to_run.last_execution_time = datetime.datetime.now()    
                        
                    if oil > 50:
                        oil = oil - (oil - 50)
                    print( task_to_run.last_execution_time.strftime("%H:%M:%S") +" :" + task_to_run.name + ": add 10 oil in tank. Tank have now " + str(oil) + " oil")
                
		
		



