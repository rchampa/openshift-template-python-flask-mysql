import os
#MYSQL_URI = 'mysql://'+os.environ['OPENSHIFT_MYSQL_DB_USERNAME']+':'+os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']+"@"+os.environ['OPENSHIFT_MYSQL_DB_HOST']+':'+os.environ['OPENSHIFT_MYSQL_DB_PORT']
MYSQL_URI = os.environ['OPENSHIFT_MYSQL_DB_URL']+os.environ['OPENSHIFT_APP_NAME']
#MYSQL_URI = 'mysql://root:@localhost/scheduler'