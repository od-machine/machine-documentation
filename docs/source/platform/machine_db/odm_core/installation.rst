Installation
============

`Internal Installation Doc <https://docs.google.com/document/d/1zZLX74gGT0mU2Dcq4aOPTVzHG7SVPALFE1M1LqbC4NU/edit#>`_

Introduction:
~~~~~~~~~~~~~

1. Since we update the odmcore package from time to time it is recommended to often update the package version. (you can check the last version in the AWS Codeartifact console).

2. The current versions are for dev used, for production additional changes have to be added 
    (for example  -  using psycopg2 instead of psycopg2-binary).

3. Pay attention that the connection to the AWS Codeartifact is done by a token. 
    That means that the connection will be expired after a while, so you usually have to create a new token every time you connect to the Codeartifact.
    Read more about AWS STS (Security Token Service) `here <https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html>`_.

Connection to AWS CodeArtifact:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Install AWS CLI - version 2 (for macOS chose the all user option) <https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html>`_
    +++++
    Pay attention to the AWS version - must be 2.0.30 at least.

2. `Configure your AWS CLI with your details <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html>`_
    ++++
    * Open your terminal and run:

    .. code-block:: 
        
        aws configure

    * Fill the follow details:
    
    .. code-block::

        AWS Access Key ID [None]: *****
        AWS Secret Access Key [None]: ****
        Default region name [None]: *region*
        Default output format [None]: json

    Note:
    If you don't know what is your Access Key and Secret Access Key follow the next steps:

    * Open AWS and search for IAM.
    * On the IAM console click on users.
    * Click on your name
    * In the security credentials tab, you can see your private Access key ID
    * If you don't remember your Secret Access Key you can regenerate it. (Make sure to save it for the next time)


3. Install odmcore package:
   ++++

    **Option I (recommended) - define index-url path:** (if you're using windows read Appendix B)

        * Open new terminal
        * Type :
        
        .. code-block:: 
            
            export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
        
        * Type: 
        
        .. code-block:: 
            
            export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token --domain odm-core --domain-owner "${AWS_ACCOUNT_ID}" --query authorizationToken --output text)
        
        * Type: 
        
        .. code-block:: 
            
            export PIP_INDEX_URL="https://aws:${CODEARTIFACT_AUTH_TOKEN}@odm-core-${AWS_ACCOUNT_ID}.d.codeartifact.eu-central-1.amazonaws.com/pypi/odm-core/simple/"
        
        OR
        
        You can run the above commands by one line:
        
        .. code-block:: 
            
            export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text) && \
            export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token --domain odm-core --domain-owner "${AWS_ACCOUNT_ID}" --query authorizationToken --output text) && \
            export PIP_INDEX_URL="https://aws:${CODEARTIFACT_AUTH_TOKEN}@odm-core-${AWS_ACCOUNT_ID}.d.codeartifact.eu-central-1.amazonaws.com/pypi/odm-core/simple/"
        
        * Install odmcore package by:
        
        .. code-block:: 
            
            pip install odmcore -i $PIP_INDEX_URL 
        
        This command will install the package from the AWS CodeArtifact and not from the regular pip
        
        (If you have issues with psycopg2-binary installation read appendix a)
        
        * Close terminal
        
        To update your package version run:

        .. code-block::  
            
            pip install --upgrade odmcore -i $PIP_INDEX_URL
        
        Read more about this option `here <https://www.jfrog.com/confluence/display/JFROG/PyPI+Repositories>`_

    **Option II - login to AWS CodeArtifact: **

        * Open new terminal
        * Run:
        
        .. code-block:: 
            
            aws codeartifact login --tool pip --domain odm-core --domain-owner ${AWS_ACCOUNT_ID} --repository odm-core --duration-seconds 900
        
        This command will configure pip to install packages from AWS CodeArtifact.
        That means that each pip command will be done with the AWS CodeArtifact and not with the regular pip.
        This login will expire after 15 minutes and then you will be able to use pip as always.
        `more_information <https://docs.aws.amazon.com/codeartifact/latest/ug/python-configure-pip.html>`_
        
        * Run 
        
        .. code-block:: 
            
            pip install odmcore
        
        (you must run this command within the logged-in 15 minutes because this package exists only on AWS CodeArtifact and not on the regular pip)
        
        * Close terminal.


4. Test installation:
    
    .. code-block:: 
        
        pip show odmcore

    .. code-block:: 
        
        import odmcore 
