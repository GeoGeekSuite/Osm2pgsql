from cobra.helper.logging import Logger
from cobra.tools.osm2pgsql import Osm2pgsqlEngine

engine = Osm2pgsqlEngine(queue='osm2pgsql')
engine.listen()
