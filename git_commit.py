from git import Repo 
from datetime import date


Git_Path = 'D:\Development\Github Repositories\WebScraper'
Com_Msg = date.today().strftime("%d/%m/%Y")+' - News Update'

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