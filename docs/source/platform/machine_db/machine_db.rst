Machine DB
==========

The machine DB is the Where & How the data is saved in the platform.

.. attention:: 
   Machine DB is the platform indexer, machine DB services provided by APIs and next year we will open the option for using UI,
   The job of Machine DB is to normalize any healthcare & life-science data and upload it to the platform by ODM modelization.

.. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
.. table::
   :name:
   :widths: 20, 30, 50
   :class: longtable
   :align: center
   :width: 66%

   +-----------------------------------+-----------------------------+
   | Data Types                        | Data Source                 |
   +===================================+=============================+
   | - Data types                      | - Data source               |
   | - Text & numerics                 | - Payer (insurance)         |
   | - Images                          | - Providers                 |
   | - EHR (electronic health records) | - Labs                      |
   | - Sequence data                   | - Medical devices outputs   |
   | - Videos                          | - Local files               |
   | - Audios                          | - Public Data               |
   +-----------------------------------+-----------------------------+


Libraries:
---------

.. toctree::
   :maxdepth: 3
   :
   
   odm_core/odm_core