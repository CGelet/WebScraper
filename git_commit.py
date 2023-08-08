from git import Repo 
from datetime import datetime


Git_Path = 'D:\Development\Github Repositories\WebScraper'
Com_Msg = datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - News Update'

def git_push():
    try:
        repo = Repo(Git_Path)
        repo.git.add(update=True)
        repo.index.commit(Com_Msg)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()