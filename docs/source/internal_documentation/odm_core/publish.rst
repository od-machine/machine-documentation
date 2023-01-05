.. _publish_odmcore:

Publish a new package version 
-----------------------------

`Internal Guide Doc <https://docs.google.com/document/d/1cVFGhPi-kM0akkToB5YEN50seQ8f_Ghjr9zPJhDp0MI/edit#>`_

Introduction
~~~~~~~~~~~~

A new package version will be automatically published (by git action) to AWS Codeartifact when a new release is created.

Steps
~~~~~

1. Merge version branch to main 
2. Pull –rebase origin main in branch of new  version  
3. Create a new tag for the last commit. ODB - git strategy 
4. The tag consensus should contain only digits separated by dots. (for example:0.0.7)
5. Go to release on Github, chose - draft a new release
6. Chose the last tag (Must contains only digits otherwise the package publish will fail)
7. The release name should be v+tag number (for example:v0.0.7)
8. Creating automatically generated release notes for a new release  (edit it as the all last releases )
9. Create a new release  
