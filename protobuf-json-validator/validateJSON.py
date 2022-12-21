# python script for validating JSON data with Google Protocol Buffers

import sys #for getting input file from command line
import os
import VIPData_pb2
import google.protobuf.json_format as jsonFormat

argc = len(sys.argv)
if argc >= 2 :
    if sys.argv[1].endswith(".json") or sys.argv[1].endswith(".JSON") :
        print("Received Input File: ",sys.argv[1]);
        path = os.path.join(os.getcwd(),sys.argv[1]);
        print("Path : ",os.path.exists(path))
        if os.path.exists(path) :
            jsonfile = open(path,"rb");
            if jsonfile : 
                print("File open Successfully");
                jsonstring = jsonfile.read();
                #print(jsonstring)
                VIPData = VIPData_pb2.VIPData()
                jsonFormat.Parse(jsonstring,VIPData)
                if VIPData :
                    print("\n       ", jsonfile, " Validated successfully");
                else :
                    print("JSON Parse Error")
                jsonfile.close();
            else :
                print("File Open Failed");
        else :
            print("No File ", path," Exists");
    else :
        print("Input File Extention is not JSON");
else :
    print("Invalid arguments");
    print("Help : \n Syntax : python validateJSON.py <jsonFileName> "); 
    
