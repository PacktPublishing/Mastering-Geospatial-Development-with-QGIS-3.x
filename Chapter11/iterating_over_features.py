rect = QgsRectangle(1223070.695, 2293653.357, 9046974.211,  
   4184988.662) 
myVector.setSubsetString('"AREA_MI" > 1000') 
request =  QgsFeatureRequest() 
request.setSubsetOfAttributes([0, 2]) 
request.setFilterRect(rect) 

for index, feature in enumerate(myVector.getFeatures(request)):
    print("The record %d has ID %d" %(index, feature.id()))
