Openshift template for python flask and mysql sqlachemy
=======================================================

Run the following commands:
rhc app create yournameapp python-2.7 --from-code=https://github.com/rchampa/openshift-template-python-flask-mysql.git -s
rhc cartridge add mysql-5.5 -a yournameapp

If you face any other problem check rhc tail yournameapp
In my case I was an error "undefined OPENSHIFT_MYSQL_DB_URL var" so it's wierd, and try to restart or reload openshift but without success, so just try a dummy commit and the everithing goes well.

Enjoy.