import urllib3 as urllib
import re 
class Manager:
    def __init__(self,orginUrl):
        self.orginUrl=orginUrl
        self.pages=set()
        self.photos=[]
    def addPageUrl(self,newPageUrl):
        self.pages.add(newPageUrl)
    def addPhotoUrl(self,newPhotoUrl):
        self.photos.append(newPhotoUrl)
        pass
    def hasPageUrl(self):
        return (len(self.pages)!=0 or self.pages[-1]==None)
    def analyser(self,_orginUrl):
        str0=re.findall(r"[a-zA-z]+://[^\s]*?/",_orginUrl)
        self.domain=str0[0]
       #[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?
        str1=re.findall(r"manhua/(.*?).html",_orginUrl)
        str1=str1[0].split(r"/")
        self.viewId=str1[1]
        return self.domain,self.viewId
        pass
    def getPage(self):
        return self.pages.pop()