import requests
import json
class RunMain:

	def send_get(self,url,data):
		res = requests.get(url=url,data=data).json()
		return res
		
	def send_post(self,url,data):
		res = requests.post(url=url,data=data).json()
		return res

	def run_main(self,url,method,data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url,data)
		else:
			res = self.send_post(url,data)
		return res

if __name__ == '__main__':
	url = 'https://datamarketapi.apyfc.com/api/RegionData/TransactionPriceDistribution'
	data = {
		"region":"东城区","startTime":"2017-11-27","endTime":"2018-11-27","property":"洋房","topNum":0,"model":1,"startSection":60,"endSection":200,"sectionSize":10,"priceMinSection":6000,"priceMaxSection":25000,"priceSectionSize":1000
	}
	res = requests.post(url, data)
	# run = RunMain(url,'post',data)
	# print (run.res)
	# # unittest
	#print run.run_main(url,'GET',data)
