import sqlite3
from random import randint
class datainserter():

   def __init__(self, dbpath : dict) -> None:
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
