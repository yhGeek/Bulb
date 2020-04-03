import bs4,json,re,js2py
import urllib.request as ur
import urllib.parse as up
class Parpser:
    def parse(self,context,domain,viewId,url,isGetName=False):
        self.domain=domain
        self.viewId=viewId
        if context is None:
            return None
        soup=bs4.BeautifulSoup(context,"html.parser",from_encoding="utf-8")
        newData=self.getNewData(soup)
        newPage=self.getNewPage(soup,url)
        if isGetName:
            name=self.getName(soup)
            return name , newPage , newData
        return newPage , newData
    def getName(self,soup):
        newData=soup.find_all("script",language="javascript",type="text/javascript")
        js=(newData[0].get_text())
        name=js2py.eval_js(js+";comicname;")
        return name

    def getNewData(self,soup):
        newData=soup.find_all("script",language="javascript",type="text/javascript")
        js=(newData[0].get_text())
        server="http://res.img.jituoli.com/"
        photors=js2py.eval_js(js+";photosr;")
        title=js2py.eval_js(js+";viewname;")
        for i in range(1,len(photors)):
            photors[i]=server+photors[i]
        photors.pop(-1)
        return {title:photors}
    def getNewPage(self,soup,url):
        flag=0
        while flag<=10:
            try:
                data=up.urlencode({"id":self.viewId}).encode("UTF8")
                req = ur.Request(url=self.domain+r"/e/extend/ret_page/index.php", data=data,method='POST')
                response = ur.urlopen(req)
                data=json.loads(response.read())
                if response.getcode() != 200:
                    return None
                if data["status"]==1:
                    return "http://www.pufei8.com"+str(data['url'])
                else:
                    
                    return None
            except:
                print("get page Fail")
    