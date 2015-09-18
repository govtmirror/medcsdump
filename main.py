import webapp2
from google.appengine.ext import ndb
import csv
import logging

class MedCase(ndb.Model):
	"""Models an individual MedCase entry with content and date."""
	caseType = ndb.StringProperty()
	caseNum = ndb.IntegerProperty()
	caseID = ndb.StringProperty()
	caseSuffix = ndb.StringProperty()
	caseState = ndb.StringProperty()
	carriers = ndb.StringProperty(repeated=True)
	orgs = ndb.StringProperty(repeated=True)
	crafts = ndb.StringProperty(repeated=True)
	numberOfEmployees = ndb.IntegerProperty()
	nmbmembers = ndb.StringProperty(repeated=True)
	initNumOfIssues = ndb.IntegerProperty()
	docketDate = ndb.StringProperty()
	taDate = ndb.StringProperty()
	ratifyDate = ndb.StringProperty()
	amendableDate = ndb.StringProperty()
	newAmendableDate = ndb.StringProperty()
	closedDate = ndb.StringProperty()
	closurereason = ndb.StringProperty()
	agedCaseComment = ndb.TextProperty()
	scheduledDate = ndb.StringProperty()
	initAssignment = ndb.StringProperty()
	isAssigned = ndb.StringProperty()
	isProfferRequested = ndb.StringProperty()
	hasInitReport = ndb.StringProperty()
	railVsAir = ndb.StringProperty()


class HomeHandler(webapp2.RequestHandler):
	def get(self):
		qry = MedCase.query()
		cases = qry.fetch()
		logging.info("in homehandler")
		self.response.headers['Content-Type'] = 'text/csv'
		self.response.headers['Content-Disposition'] = 'attachment; filename=studenttransreqs.csv'
		writer = csv.writer(self.response.out)
		for cs in cases:
			logging.info("got a case")


		

			writer.writerow([
				'caseType', 
				'caseNum',
				'caseID'#,
				# 'caseSuffix',
				# 'caseState',
				# 'carriers',
				# orgs,
				# crafts,
				# 'numberOfEmployees',
				# nmbmembers,
				# 'initNumOfIssues',
				# 'docketDate',
				# 'taDate',
				# 'ratifyDate',
				# 'amendableDate',
				# 'newAmendableDate',
				# 'closedDate',
				# 'closurereason',
				# 'agedCaseComment',
				# 'scheduledDate',
				# 'initAssignment',
				# 'isAssigned',
				# 'isProfferRequested',
				# 'hasInitReport',
				# 'yo'
				# 'railVsAir'
				])
			for cs in cases:
				writer.writerow([
					cs.caseType,
					cs.caseNum,
					cs.caseID#,
					# cs.caseSuffix,
					# cs.caseState,
					# 'carriers',
					# orgs,
					# crafts,
					# cs.numberOfEmployees,
					# nmbmembers,
					# cs.initNumOfIssues,
					# cs.docketDate,
					# cs.taDate,
					# cs.ratifyDate,
					# cs.amendableDate,
					# cs.newAmendableDate,
					# cs.closedDate,
					# cs.closurereason,
					# cs.agedCaseComment,
					# cs.scheduledDate,
					# cs.initAssignment,
					# cs.isAssigned,
					# cs.isProfferRequested,
					# cs.hasInitReport,
					# 'yes'
					# str(cs.railVsAir)
					])



app = webapp2.WSGIApplication(
	[
	('/', HomeHandler)
	],
	debug=True)