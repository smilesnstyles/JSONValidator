# python script for validating JSON data with Google Protocol Buffers

import sys #for getting input file from command line
import os
import MyProto_pb2
import google.protobuf.json_format as jsonFormat

print("Starting JSON Validation in Python Script");
path = os.path.join(os.getcwd(),"data-elements/MyJson.json");
print("Path : ", path);
if os.path.exists(path) :
	jsonfile = open(path,"rb");
	if jsonfile : 
		print("File open Successfully");
		jsonstring = jsonfile.read();
		jsonfile.close();
		if jsonstring :
			print("JSON File Read Successfully'");
			someMessage = MyProto_pb2.SomeMessage();
			try:
				jsonFormat.Parse(jsonstring,someMessage)
				print(someMessage.color);
				jsonfile.close();
			except jsonFormat.ParseError:
				print("JSON Parse Error")
				jsonfile.close();
		else :
			print("Unable to Read JSON file to String")
	else :
		print("File Open Failed");
else :
    print("No File ", path," Exists");    
