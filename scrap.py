import requests
from bs4 import BeautifulSoup
import json

class WikiScrape:
	def __init__(self,link):
		register_headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
		try:
			content=requests.get(link,headers=register_headers).text
			content=content.replace('<br />',' <br />')
			self.soup = BeautifulSoup(content, 'lxml')
		except Exception:
			print("Unable to connect to Internet")
			exit()
		
	def descripiton(self):
		res = self.soup.find(class_="mw-parser-output")
		desfind=False
		matter=''
		for i in res.children:
			if (i.name!='p')&desfind:
				break
			if (i.name=='p'):
				if (i.text=='\n'):
					continue
				matter+=i.text
				desfind=True
		return matter

	def infoBox(self):
		infobox=None
		res = self.soup.findAll('table')
		for i in res:
			try:
				if ('infobox' in i['class']):
					infobox=i	
			except Exception:
				pass	
		data={}
		if (infobox==None):
			return None
		finder1=infobox.findAll('tr')
		for i in finder1:
			name=i.find('th')
			if (name!=None):
				try:
					data[name.text.replace('\n','')]=i.find('td').text.replace('\n','')
				except Exception:
					pass
		return data

	def tableData(self,linkMode=False):
		res = self.soup.findAll('table')
		data={}
		no=1
		if (linkMode):
			for i in res:
			    temp_data=[]
			    try:
			        if ('infobox' in i['class']):
			        	continue
			    except Exception:
			    	pass	
			    data1=i.findAll('tr')
			    for j in data1:
			        child_data={}
			        data2=j.findAll("td")
			        for k in data2:
			            try:
			                child_data[k.text.replace('\n','')]=k.find('a')['href']
			            except Exception:
			                child_data[k.text.replace('\n','')]=None
			        temp_data.append(child_data)
			    data['table'+str(no)]=temp_data
			    no+=1
		else:
			for i in res:
			    temp_data=[]
			    try:
			        if ('infobox' in i['class']):
			        	continue
			    except Exception:
			    	pass	
			    data1=i.findAll('tr')
			    for j in data1:
			        child_data=[]
			        data2=j.findAll("td")
			        for k in data2:
			            child_data.append(k.text.replace('\n',''))
			        temp_data.append(child_data)
			    data['table'+str(no)]=temp_data
			    no+=1

		return data

	def allInfo(self):
		return {"short-description":self.descripiton(),"Info-data":self.infoBox(),"Tabuler data":self.tableData()}

link='https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam'
wiki=WikiScrape(link)
print(json.dumps(wiki.allInfo()))
