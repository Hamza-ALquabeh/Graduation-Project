
import requests

output_file = "int_results.txt"
f = open(output_file, 'w')

url = "https://pulsedive.com/api/info.php"



params = {
  "threat": "zeus",
  "summary": "1",
  "pretty": "1",
  "key": "3ca73c27035595858527af975e1e58415bc7630b5a5eb29fe7020cc638c41e0e"
}
# threat = input("What threat would you like to search for\n")
params["threat"] = "locky"
url = url + "?threat="+params["threat"] + "&summary="+ params["summary"] + "&pretty=" + params["pretty"] + "&key="+ params["key"]
def get_api(url):
  response = requests.get(url)
  if response.status_code != 200:
      f.write(f"Error connecting to api\n")
      return
  
  response_json = response.json()
  f.write(f"Threat name: {response_json['threat']}\n")
  f.write(f"Category: {response_json['category']}\n")
  f.write(f"Risk: {response_json['risk']}\n")   
  f.write(f"summary: {response_json['wikisummary']}\n")
    
get_api(url)