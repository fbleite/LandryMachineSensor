# jsonStruct = {
#    "Records":[
#       {
#          "eventID":"095c970f72fcf6559aac3e3b9a68dedf",
#          "eventName":"INSERT",
#          "eventVersion":"1.1",
#          "eventSource":"aws:dynamodb",
#          "awsRegion":"us-east-1",
#          "dynamodb":{
#             "ApproximateCreationDateTime":1542759060.0,
#             "Keys":{
#                "deviceId":{
#                   "N":"1"
#                },
#                "timestamp":{
#                   "S":"2018-11-20T19:11:36.796337"
#                }
#             },
#             "NewImage":{
#                "payload":{
#                   "M":{
#                      "machineStatusOn":{
#                         "BOOL":False
#                      },
#                      "hasStatusChanged":{
#                         "BOOL":False
#                      },
#                      "deviceId":{
#                         "N":"1"
#                      },
#                      "currentIntensity":{
#                         "N":"9.682870718149038"
#                      },
#                      "timestamp":{
#                         "S":"2018-11-20T19:11:36.796337"
#                      }
#                   }
#                },
#                "deviceId":{
#                   "N":"1"
#                },
#                "timestamp":{
#                   "S":"2018-11-20T19:11:36.796337"
#                }
#             },
#             "SequenceNumber":"4373000000000008985840904",
#             "SizeBytes":209,
#             "StreamViewType":"NEW_AND_OLD_IMAGES"
#          },
#          "eventSourceARN":"arn:aws:dynamodb:us-east-1:335553235753:table/LaundryMachineState/stream/2018-11-20T02:05:55.471"
#       }
#    ]
# }
#
# print (jsonStruct['Records'][0]['dynamodb'])
# image = [key for key in jsonStruct['Records'][0]['dynamodb']  if key.endswith('Image')][0]
# print(image)
# print(jsonStruct['Records'][0]['dynamodb'][image]['payload']['M']['hasStatusChanged']['BOOL'])
# machineStatusOn = True
#
# message = 'Machine turned ' +  ('ON' if machineStatusOn else 'OFF')
# print (message)
arr = [0] * 100
print (arr)