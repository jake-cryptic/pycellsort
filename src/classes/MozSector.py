class MozSector:
	def __init__(self, sector_id, pci, tac, lat, lng, cellrange, samples, created, updated):
		self.sector_id = sector_id
		self.pci = pci
		self.tac = tac

		self.lat = float(lat)
		self.lng = float(lng)

		self.range = int(cellrange)
		self.samples = int(samples)
		self.created = int(created)
		self.updated = int(updated)
