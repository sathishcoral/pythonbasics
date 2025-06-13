import urllib.request
import json

def printResults(data):
    jsondata = json.loads(data)
    #print("Inside printResults func",jsondata)
    count = jsondata["metadata"]["count"]
    title = jsondata["metadata"]["title"]
    status = jsondata["metadata"]["status"]
    print(title, "occurred", count, "times. Status now is", status)

    for line in jsondata["features"]:
        print(line["properties"]["place"])
        
    print("---------------------")

    for x in jsondata["features"]:
        #print(x["properties"]["mag"])
        if (x["properties"]["mag"]) >= 1.5:
            print(x["properties"]["place"])
    
    print("---------------------")

    for y in jsondata["features"]:
        print(y["properties"]["alert"])
        #if (y["properties"]["felt"]) >= 1:
         #   print("people felt more that 5 times ", y["properties"]["place"])



def main():
    weburl = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
    print("URL response code", weburl.getcode())

    if weburl.getcode() == 200:
        data = weburl.read().decode('utf-8')  # decode bytes to string here
        #print(data)  # raw JSON string
        printResults(data)
    else:
        print("Received error code", weburl.getcode())

if __name__ == "__main__":
    main()
