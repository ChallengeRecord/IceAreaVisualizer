import matplotlib.pyplot as plt
import pandas as pd
import boto3
from IPython.display import clear_output
import json

# バケット名
AWS_S3_BUCKET_NAME = '<YOUR-S3-Bucket>'
GET_OBJECT_KEY_NAME = 'GW1AM2_201810160147_199D_L2SGSSTLB3300300.h5'
PUT_OBJECT_KEY_NAME = 'GW1AM2_201810160147_199D_L2SGSSTLB3300300.json'
H5_FILENAME = "test.h5"

s3 = boto3.resource('s3')
bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
bucket.download_file(GET_OBJECT_KEY_NAME, H5_FILENAME)

h5file = h5py.File(H5_FILENAME,"r")

geo_data_list = h5file["Geophysical Data"].value.tolist()
lat_data_list = h5file["Latitude of Observation Point"].value.tolist()
lng_data_list = h5file["Longitude of Observation Point"].value.tolist()

output = []

clear_output()
count = 0;
for i in range(len(geo_data_list)) :
    for j in range(len(geo_data_list[i])) :
#for i in range(10) :
#    for j in range(10) :
        #    print("geo : " + str(geo_data_list[i][j][0]) + ", lat :" + str(lat_data_list[i][j]) + ", lng : " + str(lng_data_list[i][j]) )
        if geo_data_list[i][j][0] >= 0:
            count += 1;
#            if count <= 1000:
            output.append({"geo": geo_data_list[i][j][0], "lat": lat_data_list[i][j], "lng": lng_data_list[i][j]});

obj = s3.Object(AWS_S3_BUCKET_NAME,PUT_OBJECT_KEY_NAME)

json_str = json.dumps(output)
# print(json_str)

#fw = open(PUT_OBJECT_KEY_NAME,'w')
#json.dump(json_str,fw)
#bucket.download_file(PUT_OBJECT_KEY_NAME, PUT_OBJECT_KEY_NAME)

obj = s3.Object(AWS_S3_BUCKET_NAME,PUT_OBJECT_KEY_NAME)
obj.put(Body = json_str);

print("finish")
