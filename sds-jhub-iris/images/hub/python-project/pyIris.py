# Uncomment this if you haven't set up your environment variables
# These paths may also be wrong for your machine, please check them

import jaydebeapi
import os
import time
import logging

# Create logger
log = logging.getLogger('python-data-busybox')
log.setLevel(logging.INFO)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create and add formatter to ch
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Add console handler to logger
log.addHandler(ch)

log.info("Starting, waiting for 10 seconds")
time.sleep(10)

os.environ['CLASSPATH'] = './intersystems-jdbc-3.3.1.jar'

jdbcConnectionString = os.environ.get('BUSYBOX_IRIS_JDBC_URL')
driver = 'com.intersystems.jdbc.IRISDriver'
irisUsername = os.environ.get('IRIS_USERNAME')
irisPassword = os.environ.get('IRIS_PASSWORD')
fullTableName = os.environ.get('BUSYBOX_TABLE_NAME')
insertRate = os.environ.get('BUSYBOX_INSERT_RATE')


log.info("Connecting to InterSystems IRIS using " + jdbcConnectionString)
conn = jaydebeapi.connect(driver, jdbcConnectionString, [irisUsername, irisPassword])

log.info("Connected!")
curs = conn.cursor()

# Create table if it doesn't already exist
try:
    curs.execute("CREATE TABLE " + fullTableName + " (Value VARCHAR(10))")
except Exception:
    pass
log.info("Created table "+ fullTableName +" in given database...")

# Insert record in the table
sql = "INSERT INTO " + fullTableName + " VALUES (?)"

# Insert values every 30 seconds
for x in range(15):
    curs.execute(sql, [x])
    time.sleep(int(insertRate))
log.info("Values inserted!")

curs.close()
conn.close()

