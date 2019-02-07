from enum import Enum
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from ecolyzer.repository.commit import CommitInfo
from ecolyzer.repository.file_modification import FileModificationInfo

class RepositoryMiner:
	"""RepositoryMiner"""
	def __init__(self, repo_path):
		self.repo_path = repo_path
		self.source_file_extensions = [
			#'c', 'cc', 'cpp', 'h', 'hpp', 'hxx',
			#'ui', 'qrc',
			'lua',
			#'cmake', 'in',
			#'photo',
			#'sh',
			#'bat',
			#'rc',
			# 'log', # verificar
			#'lp', 'css',
		]		

	def extract(self):
		for commit in RepositoryMining(self.repo_path, only_in_branches=['master']).traverse_commits():
			self._add_commit(commit)
			#for mod in commit.modifications:
				
				# if mod.change_type != None:
					# if ((mod.change_type.name == "ADD") and (mod.added > 0)):
						# git_file = GitFile(mod.new_path)
						# git_file.added = mod.added
						# git_files.append(git_file)

		#return git_files
		
	def get_commit_info(self, hash):
		repo_driller = GitRepository(self.repo_path)
		commit_driller = repo_driller.get_commit(hash)
		return self._get_commit_info(commit_driller)	
		
	def _get_commit_info(self, commit_driller):
		commit_info = CommitInfo(commit_driller.hash)
		commit_info.date = commit_driller.author_date
		commit_info.msg = commit_driller.msg
		author_driller = commit_driller.author
		commit_info.author_name = author_driller.name
		commit_info.author_email = author_driller.email
		commit_info.files_modification = self._get_modifications_info(commit_driller.modifications)
		#commit_info.project_name = commit_driller.project_name
		#commit_info.project_path = commit_driller.project_path
		#commit_info.merge = commit_driller.merge
		#commit_info.in_main_branch = commit_driller.in_main_branch		
		return commit_info
	
	def _get_modifications_info(self, modifications):
		files_modification = []
		for mod in modifications:
			file_mod = FileModificationInfo(mod.filename)
			file_mod.old_path = mod.old_path
			file_mod.new_path = mod.new_path
			file_mod.added = mod.added
			file_mod.removed = mod.removed
			file_mod.type = mod.change_type.name
			files_modification.append(file_mod)
		return files_modification
