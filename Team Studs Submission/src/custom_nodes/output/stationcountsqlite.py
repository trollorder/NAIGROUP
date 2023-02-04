"""
Node template for creating custom nodes.
"""

from typing import Any, Dict
from datetime import datetime
from peekingduck.pipeline.nodes.abstract_node import AbstractNode
import sqlite3

DB_FILE = "stationcount.db"           # name of database file

class Node(AbstractNode):
   """ Stationsql node to save unique persons which is a list of unqiue id on screen and count on screen. Exclusive of train count

   Args:
      config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
   """

   def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
      super().__init__(config, node_path=__name__, **kwargs)
      self.uniqueperson,self.count='',0
      self.conn = None
      try:
         # try to establish connection to database,
         # will create DB_FILE if it does not exist
         self.conn = sqlite3.connect(DB_FILE)
         self.logger.info(f"Connected to {DB_FILE}")
         sql = """ CREATE TABLE IF NOT EXISTS stationcounttable (
                        datetime text,
                        uniqueperson text,
                        stationcount text
                   ); """
         cur = self.conn.cursor()
         cur.execute(sql)
      except sqlite3.Error as e:
         self.logger.info(f"SQL Error: {e}")

   def update_db(self, obj_attrs: str, stationcount: int) -> None:
      """Helper function to save current time stamp, hand direction and
      wave count into DB wavetable.
      """
      uniqueperson = str(obj_attrs) #manual coversion due to inability to rename
      now = datetime.now()
      dt_str = f"{now:%Y-%m-%d %H:%M:%S}"
      sql = """ INSERT INTO stationcounttable(datetime,uniqueperson,stationcount)
                values (?,?,?) """
      cur = self.conn.cursor()
      cur.execute(sql, (dt_str, uniqueperson, stationcount))
      self.conn.commit()

   def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
      """Node to output hand wave data into sqlite database.

      Args:
            inputs (dict): Dictionary with keys "hand_direction", "num_waves"

      Returns:
            outputs (dict): Empty dictionary
      """

      uniqueperson = inputs["obj_attrs"]
      stationcount = inputs["count"]
      self.update_db(uniqueperson, stationcount)

      return {}
