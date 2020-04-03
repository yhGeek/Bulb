import bs4,re,json
from tools import urlManager
from tools import downloader
from tools import parser
from tools import output
class _Main :
    def __init__(self,url):
        self.orginUrl=url
        self.urlManager=urlManager.Manager(url)
        self.domain,self.viewId = self.urlManager.analyser(url)
        self.urlManager.addPageUrl(url)
        self.downloader=downloader.Downloader()
        self.parser=parser.Parpser()
    def start(self):
        domain=self.domain
        viewId=self.viewId
        i=0
        while self.urlManager.hasPageUrl():
            newPageUrl=self.urlManager.getPage()
            if newPageUrl==None:
                break
            print(str(i)+":"+newPageUrl)
            context=self.downloader.downloadHtml(newPageUrl)
            domain,viewId = self.urlManager.analyser(newPageUrl)
            if i==0:
                self.name,newPageUrl,newPhotoUrl=self.parser.parse(
                    context=context,
                    domain=domain,
                    viewId=viewId,
                    url = newPageUrl,
                    isGetName=True
                    )
            newPageUrl,newPhotoUrl=self.parser.parse(context,domain,viewId,newPageUrl)
            self.urlManager.addPageUrl(newPageUrl)
            self.urlManager.addPhotoUrl(newPhotoUrl)
            i+=1
        print("分析完成，开始下载")
        self.downloader.downloadImage(self.urlManager.photos,self.name)

if __name__=="__main__":

    main=_Main(input("请输入扑飞漫画（第一话）的地址 要带http:// \n"))
    main.start()
