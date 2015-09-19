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
		self.response.headers['Content-Disposition'] = 'attachment; filename=medcsdump19.csv'

		modelKeys = ['caseType','caseNum','caseID','caseSuffix','caseState','numberOfEmployees','initNumOfIssues','docketDate','taDate','ratifyDate','amendableDate','newAmendableDate','closedDate','closurereason','scheduledDate','initAssignment','isAssigned','isProfferRequested','hasInitReport','railVsAir','carriersorgs','crafts','nmbmembers']

		textstr = """caseType,caseNum,caseID,caseSuffix,caseState,numberOfEmployees,initNumOfIssues,docketDate,taDate,ratifyDate,amendableDate,newAmendableDate,closedDate,closurereason,scheduledDate,initAssignment,isAssigned,isProfferRequested,hasInitReport,railVsAir,carriersorgs,crafts,nmbmembers\n\r"""
				
		logging.info("attempt 1")
		for cs in cases:
			csDict = cs.to_dict()
			csKeys = csDict.keys()
			logging.info("csDict = " + str(csKeys))

			if 'caseType' in csKeys:
				textstr = textstr + str(cs.caseType).replace(",", "") + ","
			else:
				textstr = textstr + ","

			if 'caseNum' in csKeys:
				textstr = textstr + str(cs.caseNum).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'caseID' in csKeys:
				textstr = textstr + str(cs.caseID).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'caseSuffix' in csKeys:
				textstr = textstr + str(cs.caseSuffix).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'caseState' in csKeys:
				textstr = textstr + str(cs.caseState).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'numberOfEmployees' in csKeys:
				textstr = textstr + str(cs.numberOfEmployees).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'initNumOfIssues' in csKeys:
				textstr = textstr + str(cs.initNumOfIssues).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'docketDate' in csKeys:
				textstr = textstr + str(cs.docketDate).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'taDate' in csKeys:
				textstr = textstr + str(cs.taDate).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'ratifyDate' in csKeys:
				textstr = textstr + str(cs.ratifyDate).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'amendableDate' in csKeys:
				textstr = textstr + str(cs.amendableDate).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'newAmendableDate' in csKeys:
				textstr = textstr + str(cs.newAmendableDate).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'closedDate' in csKeys:
				textstr = textstr + str(cs.closedDate).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'closurereason' in csKeys:
				textstr = textstr + str(cs.closurereason).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'scheduledDate' in csKeys:
				textstr = textstr + str(cs.scheduledDate).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'initAssignment' in csKeys:
				textstr = textstr + str(cs.initAssignment).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'isAssigned' in csKeys:
				textstr = textstr + str(cs.isAssigned).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'isProfferRequested' in csKeys:
				textstr = textstr + str(cs.isProfferRequested).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'hasInitReport' in csKeys:
				textstr = textstr + str(cs.hasInitReport).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'railVsAir' in csKeys:
				textstr = textstr + str(cs.railVsAir).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'carriersorgs' in csKeys:
				textstr = textstr + str(cs.carriersorgs).replace(",", "") + ","
			else:
				textstr = textstr + ","
			if 'crafts' in csKeys:
				textstr = textstr + str(cs.crafts).replace(",", "").replace("&amp;", "and") + ","
			else:
				textstr = textstr + ","
			if 'nmbmembers' in csKeys:
				textstr = textstr + str(cs.nmbmembers).replace(",", "") + ","
			else:
				textstr = textstr 
			
			textstr = textstr + "\n\r"
			
		self.response.write(textstr)



app = webapp2.WSGIApplication(
	[
	('/', HomeHandler)
	],
	debug=True)