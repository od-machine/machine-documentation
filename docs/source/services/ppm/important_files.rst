1. Answers format/types
""""""""""""""""""""""
   Files containing the required types of the fields in the questionnaire.
   (string / int / binary int (0/1/2) / string array)

   .. important:: Dates format

      - the questionnaire json name: '{patient_id}_%Y-%m-%d-%H-%M-%S'
      - 'Date_Of_Birth': '%Y-%m-%d'
      - 'Fill_Date': '%Y-%m-%d-%H-%M-%S'

   `format_patients_answers_male.json <https://drive.google.com/file/d/1GOq6vJw7oBONFrHmSdsKslzcxbqj0LzR/view?usp=sharing>`_

   `format_patients_answers_female.json <https://drive.google.com/file/d/1Z7gXkbcWNI3tnbebq9Rbw21GzcBldZ2c/view?usp=sharing>`_


2. Answers options
""""""""""""""""""
   Files containing the required options of the fields in the questionnaire.
   (yes_no / yes_no_maybe / free_text / single_choice / multiple_choice / int_in_range / tuples)

   `typeAnswers.json <https://docs.google.com/document/d/1hJJ2PGcMDbVNqRRzewGRKiLCpGotBdrv67zVS-t3E6k/edit?usp=sharing>`_


3. Full answers examples
"""""""""""""""""""""""
   A full questionnaire file containing all possible fields.
   .. important:: 

      Such files cannot be created because, for example, there is information from a current smoker and a former smoker. In practice, a person can only answer yes to one of the options.

   `answers_dict_male <https://drive.google.com/file/d/1iOzCjHubzkJCFlZ-e8lRhu-LUAbpMRiy/view?usp=sharing>`_

   `answers_dict_female <https://drive.google.com/file/d/1gouKmwsy8DojPV9v4EkguQYOwKDoGpJQ/view?usp=sharing>`_


4. Choice questions - answers options
""""""""""""""""""""""""""""""""""""
   Table contains question fields that require the user to select an answer from a list (checkbox/list) 

   `ApiAnswers.json <https://drive.google.com/file/d/1a2fyDvKl77PXD4MbxC_a8xoX31s1_2af/view?usp=sharing>`_


5. Countries
""""""""""""
   It is a table containing the English and Hebrew names of the countries for the purpose of answering the Country_Of_Birth question.
   expect to receive the exact string of the country's name in English

   `Country.csv <https://docs.google.com/spreadsheets/d/1C2BE3FIDWs5PCY_kLfhs528vz1kxCIEyNp3afT_EWR4/edit?usp=sharing>`_


6. Hebrew questionnaire
""""""""""""""""""""""

   Final: `male questionnaire with <https://docs.google.com/document/d/1HBA0OeHqcQhL_oHGa6gBUXVc2mPyUTWt/edit?usp=sharing&ouid=114881368951833308399&rtpof=true&sd=true>`_ 

   `male questionnaire with changes <https://docs.google.com/document/d/1PxI07ZBhQuV8WVvGG6ecEWilynl-S0C6/edit?usp=sharing&ouid=114881368951833308399&rtpof=true&sd=true>`_

   Final: `female_questionnaire <https://docs.google.com/document/d/13wWxC8kjxrZoBI-WzG-ea3JpDSfcCnqU/edit?usp=sharing&ouid=114881368951833308399&rtpof=true&sd=true>`_
   
   `female questionnaire with changes <https://docs.google.com/document/d/1fXIHwgmqpaqWLtASeba0twBrA8jcAoas/edit?usp=sharing&ouid=114881368951833308399&rtpof=true&sd=true>`_

7. Decision tree
"""""""""""""""

   `updated_male_decision_tree <https://whimsical.com/malequestionnaire-femi-BJ5LW6ty2Sv4BqcQRZk18r>`_

   Password: ``maleQuest``

   `female_decision_tree <https://whimsical.com/femalequestionnaire-femi-SFPLi11s6bRrXh2NUL61dw>`_

   Password: ``femaleQuest``
