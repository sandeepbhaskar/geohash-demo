import sys
import geohash

def encdec():
	print 'geohash.encode '+geohash.encode(12.963787,77.637789)
	print 'geohash.encode with precision-5: '+geohash.encode(12.963787,77.637789, precision=5)
	print 'geohash.decode '+str(geohash.decode('tdr1wxype953'))
	print 'geohash.decode exactly'+str(geohash.decode_exactly('tdr1wxype953'))

def nearby():
	print 'geohash.bounding box'
	print geohash.bbox('tdr1w')
	print 'geohash neighbours'
	print geohash.neighbors('tdr1wxype953')
	print 'geohash expand'
	print geohash.expand('tdr1wxype953')
	
def main():
	args = sys.argv
	if args[1] == 'encode':
		print 'Encoding/decoding Functions'
		encdec()
	else:
		print 'Bounding Box and Neighbors'
		nearby()
	
if __name__ == "__main__":
	main()
    
		
