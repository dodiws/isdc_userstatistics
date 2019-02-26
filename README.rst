==============
userstatistics
==============

Display user statistics data.
Optional Module for ASDC

Quick start
-----------

1. Add "userstatistics" to your ISDC_ADDITIONAL_APPS setting like this::

   ISDC_ADDITIONAL_APPS = [
       ...
       'userstatistics',
   ]

   For development in virtualenv add USERSTATISTICS_PROJECT_DIR path to VENV_NAME/bin/activate:
       export PYTHONPATH=${PYTHONPATH}:\
       ${HOME}/USERSTATISTICS_PROJECT_DIR
