========================
django-elb-project
========================

1.Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

========================

2.Migrate Photologue
=============================

python manage.py migrate photologue


========================

3.install Custom apps in site_packages
=============================

gallery_orders
editorials

*note: These apps are located in the git repository elb/custom_apps they need to be moved to site_packages for installation .*


