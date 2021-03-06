from classes.PyCellDB import PyCellDB
from classes.CellIDStore import CellIDStore
import config as c
from time import time

start_time = time()

# Load previous data if it exists
cs = CellIDStore(c.ALLOWED_RATS, c.ALLOWED_MCCS, c.ALLOWED_MNCS)

# Download latest data


# Update data
cs.read_csv(c.EXPORTS_DIR, '234-14th-feb-2019.csv')
cs.read_csv(c.EXPORTS_DIR, 'cell_towers_2021-01-22-T000000.csv')
cs.read_csv(c.EXPORTS_DIR, 'cell_towers_2021-01-22-T000000.csv')
cs.read_csv(c.EXPORTS_DIR, 'MLS-full-cell-export-2020-02-22T000000.csv')
cs.read_csv(c.EXPORTS_DIR, 'MLS-full-cell-export-2021-02-23T000000.csv')
cs.read_csv(c.EXPORTS_DIR, 'MLS-full-cell-export-2021-03-31T000000.csv')
cs.update_node_meta()

# Save data
cs.save_store()

# Update database
db = PyCellDB(driver='mysql+pymysql', user=c.db_user, password=c.db_password, host=c.db_addr, port=c.db_port, db='pycellsort')
db.insert_cells(cs.cell_ids)
db.commit()

print('Done update after %ss' % (round(time() - start_time, 3)))
