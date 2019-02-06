import datetime
from ecolyzer.system import System
from ecolyzer.repository import Repository, Commit, CommitInfo, Author
from ecolyzer.dataaccess import SQLAlchemyEngine

db_url = 'postgresql://postgres:postgres@localhost:5432/commit_test'
db = SQLAlchemyEngine(db_url)
db.create_all(True)

def test_commit_crud():
	#create
	repo = Repository('repo/terrame')
	sys = System('terrame', repo)
	commit_info = CommitInfo('hashhashhash')
	commit_info.date = datetime.datetime(2019, 2, 6, 14, 14, 55)  
	commit_info.msg = 'commit message'
	commit_info.author_name = 'author'
	commit_info.author_email = 'author@email.com'	
	author = Author(commit_info.author_name, commit_info.author_email)
	commit = Commit(commit_info, author, repo)
	
	session = db.create_session()
	session.add(repo)
	session.add(sys)
	session.commit()

	#read	
	commitdb = session.query(Commit).get(1)
	assert commitdb.msg == commit_info.msg
	assert commitdb.date.strftime('%Y-%m-%d %H:%M:%S') == '2019-02-06 14:14:55'
	assert commitdb.hash == commit_info.hash
	assert commitdb.repository.path == repo.path
	assert commitdb.author.name == commit_info.author_name
	assert commitdb.author.email == commit_info.author_email

	#update
	commit.msg = 'updating message'
	session.commit()	
	commitdb = session.query(Commit).get(1)
	assert commitdb.msg == commit.msg

	#delete
	session.delete(commit)
	session.commit()
	commitdb = session.query(Commit).get(1)
	repodb = session.query(Repository).get(1)
	authordb = session.query(Author).get(1)
	assert commitdb == None
	assert repodb.path == repo.path 
	assert authordb.name == author.name

	session.close()
	db.drop_all()
	