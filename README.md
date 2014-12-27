Openshift template for python flask and mysql sqlachemy
=======================================================

Run the following commands:  
+   ``rhc app create yournameapp python-2.7 --from-code=https://github.com/rchampa/openshift-template-python-flask-mysql.git -s``   
+   ``rhc cartridge add mysql-5.5 -a yournameapp``   

If you face any other problem check ``rhc tail yournameapp``     
In my case I had an error "undefined OPENSHIFT_MYSQL_DB_URL var" so it's wierd, and I tried to restart or reload openshift but without success, so I finally made a dummy commit and everything goes well.   


Enjoy.
