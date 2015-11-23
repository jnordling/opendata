__author__ = 'jnordling'
import requests
url = 'http://www.arcgis.com/sharing/rest/content/items/'

class AgolItem(object):
    def __init__(self,**kwargs):
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.itemID = kwargs.get('id', None)
        if self.itemID == None:
            raise Exception ("Must Provide Agol Item ID")

        self.itemJSON = self.getDataObject()

        self.id = self.get_id()
        self.owner = self.get_owner()
        self.created = self.get_created()
        self.modified = self.get_modified()
        self.name = self.get_name()
        self.title = self.get_title()
        self.url = self.get_url()
        self.type = self.get_type()
        self.typeKeywords = self.get_typeKeywords()
        self.description = self.get_description()
        self.tags = self.get_tags()
        self.snippet = self.get_snippet()
        self.thumbnail = self.get_thumbnail()
        self.extent = self.get_extent()
        self.spatialReference = self.get_spatialReference()
        self.accessInformation = self.get_accessInformation()
        self.licenseInfo = self.get_licenseInfo()
        self.culture = self.get_culture()
        self.access = self.get_access()
        self.industries = self.get_industries()
        self.languages = self.get_languages()
        self.largeThumbnail = self.get_largeThumbnail()
        self.banner = self.get_banner()
        self.screenshots = self.get_screenshots()
        self.listed = self.get_listed()
        self.size = self.get_size()
        self.numComments = self.get_numComments()
        self.numRatings = self.get_numRatings()
        self.avgRating = self.get_avgRating()
        self.numViews = self.get_numViews()


    def getDataObject(self):
        itemURL = url + str(self.itemID) + '?f=json'
        return requests.get(itemURL).json()
    def get_id(self):
        return self.itemJSON['id']

    def get_owner(self):
        return self.itemJSON['owner']

    def get_created(self):
        return self.itemJSON['created']

    def get_modified(self):
        return self.itemJSON['modified']

    def get_name(self):
        return self.itemJSON['name']

    def get_title(self):
        return self.itemJSON['title']

    def get_url(self):
        return self.itemJSON['url']

    def get_type(self):
        return self.itemJSON['type']

    def get_typeKeywords(self):
        return self.itemJSON['typeKeywords']

    def get_description(self):
        return self.itemJSON['description']

    def get_tags(self):
        return self.itemJSON['tags']

    def get_snippet(self):
        return self.itemJSON['snippet']

    def get_thumbnail(self):
        return url + self.itemID + '/info/' + self.itemJSON['thumbnail']

    def get_extent(self):
        return self.itemJSON['extent']

    def get_spatialReference(self):
        return self.itemJSON['spatialReference']

    def get_accessInformation(self):
        return self.itemJSON['accessInformation']

    def get_licenseInfo(self):
        return self.itemJSON['licenseInfo']

    def get_culture(self):
        return self.itemJSON['culture']

    def get_access(self):
        return self.itemJSON['access']

    def get_industries(self):
        return self.itemJSON['industries']

    def get_languages(self):
        return self.itemJSON['languages']

    def get_largeThumbnail(self):
        return self.itemJSON['largeThumbnail']

    def get_banner(self):
        return self.itemJSON['banner']

    def get_screenshots(self):
        return self.itemJSON['screenshots']

    def get_listed(self):
        return self.itemJSON['listed']

    def get_size(self):
        return self.itemJSON['size']

    def get_numComments(self):
        return self.itemJSON['numComments']

    def get_numRatings(self):
        return self.itemJSON['numRatings']

    def get_avgRating(self):
        return self.itemJSON['avgRating']

    def get_numViews(self):
        return self.itemJSON['numViews']

