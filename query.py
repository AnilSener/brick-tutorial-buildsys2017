# high-level interface for interacting with Brick graphs using rdflib
# setup our query environment
from rdflib import RDFS, RDF, Namespace, Graph, URIRef

class BrickGraph(object):
    def __init__(self, filename='metadata/sample_building.ttl'):
        self.bldg = Graph()
        self.bldg = Graph()
        self.bldg.parse("Brick/dist/Brick.ttl", format='turtle')
        self.bldg.parse(filename, format='turtle')
        BRICK = Namespace('https://brickschema.org/schema/1.0.1/Brick#')
        BF = Namespace('https://brickschema.org/schema/1.0.1/BrickFrame#')
        EX = Namespace('http://example.com#')
        self.bldg.bind('ex', EX)
        self.bldg.bind('brick', BRICK)
        self.bldg.bind('bf', BF)
        self.m = {
        'https://brickschema.org/schema/1.0.1/Brick': 'brick',
        'http://www.w3.org/1999/02/22-rdf-syntax-ns': 'rdf',
        'http://www.w3.org/2000/01/rdf-schema': 'rdfs',
        'https://brickschema.org/schema/1.0.1/BrickFrame': 'bf',
        'http://www.w3.org/2002/07/owl': 'owl',
        'http://www.w3.org/2004/02/skos/core': 'skos',
        'http://example.com': 'ex',
        }
    def query(self, query, fullURI=False):
        query = """PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
PREFIX ex: <http://example.com#>
"""+query
        rows = self.bldg.query(query)
        if not fullURI:
            rows = [[self.m[r.split('#')[0]] + ':' + r.split('#')[1] if isinstance(r, URIRef) and '#' in r else r for r in row] for row in rows]
            return rows
        return list(rows)