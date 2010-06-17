# A simple url shortener written in Python
# by Kenny Shen (www.northpole.sg)

# import settings
from settings import *

# constants
ALP = "23456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# squash
class Squash:
	def __init__(self):
		self.alp = ALP
		self.base_length = len(self.alp)

	def _squash(self, num):
		if (num == 0):
			return self.alp[0]
		squash_collect = []
		while num:
			rem = num % self.base_length
			num = num // self.base_length
			squash_collect.append(self.alp[rem])
		squash_collect.reverse()
		return ''.join(squash_collect)

	def _unsquash(self,shorturl):
		short_length = len(shorturl) - 1
		decoded_id = 0
		
		bpower = len(self.alp)
		for char in shorturl:
		    result =  self.alp.index(char) * (bpower ** (short_length))
		    decoded_id += result
		    short_length -= 1
		return decoded_id
	
	# example for communicating with a key/val db, in this case lightcloud
	def sendto_lightcloud(self, fullurl):
                import lightcloud
                LIGHT_CLOUD = {'lookup1_A': LIGHTCLOUD_LOOKUPS,'storage1_A': LIGHTCLOUD_STORAGES}	

            	lookup_nodes, storage_nodes = lightcloud.generate_nodes(LIGHT_CLOUD)
            	lightcloud.init(lookup_nodes, storage_nodes)
	
            	# get last id and increment
                try:
            	        last_id = lightcloud.get("last_id")
            	        if last_id:
            	                pass
            	        else:
            	           lightcloud.set("last_id","0")     
            	except:
            	        pass
            	next_id = int(last_id) + 1
            	# get shortened url id from current id
            	shortened_url_id = self._squash(next_id)
                try:
            	        # store id, url into db
            	        lightcloud.set(str(next_id),fullurl)
	        
            	        # update last_id
            	        lightcloud.set("last_id", str(next_id))
                except:
                        print "lightcloud update fail"
                        pass

            	# return id
            	return shortened_url_id

        # example for communicating with a key/val db, in this case lightcloud
	def getfrom_lightcloud(self, shorturlid):
		import lightcloud
		
		LIGHT_CLOUD = {
			'lookup1_A': LIGHTCLOUD_LOOKUPS,
			'storage1_A': LIGHTCLOUD_STORAGES
		}

		lookup_nodes, storage_nodes = lightcloud.generate_nodes(LIGHT_CLOUD)
		lightcloud.init(lookup_nodes, storage_nodes)
		
		# get db key
		db_key = self._unsquash(shorturlid)
		# return url or None
		fullurl = None
		fullurl = lightcloud.get(str(db_key))

		# return url
		return fullurl	
