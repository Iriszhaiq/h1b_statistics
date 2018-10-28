from collections import defaultdict
import sys

soc_list = []
status_list = []
state_list = []
inputs = None

def read_input(input_file):
	with open(input_file,'r') as f:
		label = f.readline().strip('\n').split(';')
		inputs = f.readlines()

	for i in range(len(label)):
		l = label[i]
		if 'SOC_NAME' in l:
			soc_ind = i 
		if 'STATUS' in l:
			status_ind = i 
	
	for i in range(len(label)):
		l = label[i]
		if "WORKLOC1_STATE" in l or "STATE" in l and "WORK" in l:
			state_ind = i 
			break
	soc_list = [i.strip('\n').replace('"','').strip('\'').split(';')[soc_ind] for i in inputs]
	status_list = [i.strip('\n').split(';')[status_ind] for i in inputs]
	state_list = [i.strip('\n').split(';')[state_ind] for i in inputs]

	return soc_list,status_list,state_list,inputs


def main():

	#initialize path
	if len(sys.argv) < 4:
  		sys.exit(1) 
	input_file = sys.argv[1]
	output_occu_file = sys.argv[2]
	output_state_file = sys.argv[3]

	#Create dictionary to store occupation and state and their relative count.
	occupations = defaultdict(int)
	states = defaultdict(int)

	soc_list,status_list,state_list,inputs = read_input(input_file)
	# with open(input_file,'r') as f:
	# 	label = f.readline().strip('\n').split(';')
	# 	inputs = f.readlines()

	# for i in range(len(label)):
	# 	l = label[i]
	# 	if 'SOC_NAME' in l:
	# 		soc_ind = i 
	# 	if 'STATUS' in l:
	# 		status_ind = i 
	
	# for i in range(len(label)):
	# 	l = label[i]
	# 	if "WORKLOC1_STATE" in l or "STATE" in l and "WORK" in l:
	# 		state_ind = i 
	# 		break

	# soc_list = [i.strip('\n').replace('"','').strip('\'').split(';')[soc_ind] for i in inputs]
	# status_list = [i.strip('\n').split(';')[status_ind] for i in inputs]
	# state_list = [i.strip('\n').split(';')[state_ind] for i in inputs]
	# total_certified,occupations,states = store_records(inputs,soc_list,state_list)
	for i in range(len(inputs)):
		if status_list[i]=='CERTIFIED':
			occupations[soc_list[i]]+=1 
			states[state_list[i]]+=1

	total_certified = sum(occupations.values())

	file = open(output_occu_file,'w')
	file.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")

	for key,value in sorted(occupations.items(),key = lambda x:(x[1]*(-1),x[0]))[:10]:
		tmp = ';'.join([key,str(value), "{:.1%}".format(value*100/(total_certified*100.0))])
		file.write(tmp+'\n')

	file = open(output_state_file,'w')
	file.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
	for key,value in sorted(states.items(),key = lambda x:(x[1]*(-1),x[0]))[:10]:
		tmp = ';'.join([key,str(value), "{:.1%}".format(value*100/(total_certified*100.0))])
		file.write(tmp+'\n')
		
if __name__=='__main__':
	main()
