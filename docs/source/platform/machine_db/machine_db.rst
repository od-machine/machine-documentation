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
   | - Text & numerics                 | - Payer (insurance)         |
   | - Images                          | - Providers                 |
   | - EHR (electronic health records) | - Labs                      |
   | - Sequence data                   | - Medical devices outputs   |
   | - Videos                          | - Local files               |
   | - Audios                          | - Public Data               |
   +-----------------------------------+-----------------------------+


Functionality
-------------

* Normalize
   The platform provides collection services that recognize  the source data types and normalize all of it for upload.

* Modelling 
   
   * The Platform provides modelling process constructed  by our:

   * Medical experts

   * Data experts

* Indexing

   The platform provides auto indexing services, once the platform is Normalized & Modelized, the indexing services index data onto the ODM graph

* Compliance
   
   * Option for anonymizing services

      * The platform provides build-in anonymizing services and each new anonymizing use case became to an automatic service.

   * Security (credentials, data ownership, etc)

      * The platform is build in a secure manner by design.


Libraries
---------

.. toctree::
   :maxdepth: 2
   
   odm_core/odm_core