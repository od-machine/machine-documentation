Internal files
--------------

* Technical document
   
   `Technical doc <https://docs.google.com/document/d/1qRsXLzHGGjI3Q1E04guzxmzXIRX6OJW6hWiRSTxhlkM/edit?usp=sharing>`_


* Doctors' recommendations

   file to index the conditions & risk groups & recommendations to neo4j

   `conditions-recommendations <https://drive.google.com/drive/folders/1XZHDR8kY1CECVRVPZAEp6n3b01uBVbcQ?usp=sharing>`_


* Don't know answers

   The guide file provides information about how to refer to questions answered "don't know" - yes or no.

   `dont know questions <https://docs.google.com/spreadsheets/d/1_4UFBOHQ7O3b4Z8i26RKV0uPVKuqAupHwo6EoOwTyyg/edit?usp=sharing>`_


* Test cases

   A set of profiles to test the product

   `test profiles <https://drive.google.com/drive/folders/1qrHG9whHDsGynPJi1xeYroUQz4E1HPPz?usp=sharing>`_


Shared files
------------

* Updated Hebrew questionnaire

   `Hebrew questionnaire folder <https://drive.google.com/drive/folders/1o0DW6qlwEI8sA0p09IA2su7jol4FCNIM?usp=sharing>`_

   `male_questionnaire <https://docs.google.com/document/d/1nC6BDZjqFciA9bm1ZDLMmQj8MRm0CaJ2/edit?usp=sharing&ouid=114881368951833308399&rtpof=true&sd=true>`_

   `female_questionnaire <https://docs.google.com/document/d/1duTAIC5O2aRF3BQZjtxEWriBjd-w4qlr/edit?usp=sharing&ouid=114881368951833308399&rtpof=true&sd=true>`_


* Summary translation and categories

   `summary translation <https://docs.google.com/document/d/1TuXR4hkp1u_uX7Iuv5mHbWMk3klyybnjfekIORLeBiQ/edit?usp=sharing>`_


* Decision tree

   `male_decision_tree <https://secure-web.cisco.com/1W8GFV7ry5FKdHSnnqV5qR9s5ao4Nvz9pBJ5pLIpnw7uT_zzNwQli6WlSpyT5RPU111tJ39agVPGC6vWbadjLXI85CMDjVOX6-amBtNgJRqQ-viKodcIfSlHsFszrvW7m59VKi25aNZbfRW_IYphuaOSWQSba95LWnIK7Hup5uWn6wsntDRZmyQdvqEyPv8WSDvJuASP1z94JypgIeIyVjUdvoGgNRQt7VzFez6y--pgZSbiITW0qbVA-GfgKKAjADRLlXnP54OyGFvh0BUCPYaOxJUxPqAu0wqWL9z3XriKlzOWh0SdxXy9Gkuwc7bGy/https%3A%2F%2Fwhimsical.com%2Fmalequestionnaire-version-4-13HjgRrDRkJdzryWZdrQEY>`_

   Password: ``maleQuest4``

   `female_decision_tree <https://secure-web.cisco.com/1QY__MfNWddyR6eI0J5nrtLVxZ_kjCRQc7v4XGAzEeRAH5OQkfisza1_ZqutzB5XgjH80lLE691czQ5YyanpO9BKGWLPUc7W3Zm-myDet0-WUadBsA6O6oaP0mCRvZCkuHCVVAzPk5ZeKoARo_p8RYU3--OKBlW7-VHToGop0swYVIZWnLALI3Trydidb_99joQppz9W98ZQ49je1IYTaLYXArYGgg5mCkcl4Jt_o1iDuaWD3xj77_wDNzuhEviwPFEYeUtx5Zb-e0ABSxJjpdcMQ4TaIRJso-AocrO-VF3iOjLutjBp1JiwiAayUnsBD/https%3A%2F%2Fwhimsical.com%2Ffemalequestionnaire-version-4-JmheGNeRfGMpEBwGpryttq>`_

   Password: ``femaleQuest4``


* Answers format/types

   Files containing the required types of the fields in the questionnaire.
   (string / int / binary int (0/1/2) / string array)

   .. important:: Dates format

      - the questionnaire json name: '{patient_id}_%Y-%m-%d-%H-%M-%S'
      - 'Date_Of_Birth': '%Y-%m-%d'
      - 'Fill_Date': '%Y-%m-%d-%H-%M-%S'

   `format_patients_answers_male.json <https://drive.google.com/file/d/1GOq6vJw7oBONFrHmSdsKslzcxbqj0LzR/view?usp=sharing>`_

   `format_patients_answers_female.json <https://drive.google.com/file/d/1Z7gXkbcWNI3tnbebq9Rbw21GzcBldZ2c/view?usp=sharing>`_


* Answers required

   Files containing the required options of the fields in the questionnaire.
   (yes_no / yes_no_maybe / free_text / single_choice / multiple_choice / int_in_range / tuples)

   `typeAnswers.json <https://docs.google.com/document/d/1hJJ2PGcMDbVNqRRzewGRKiLCpGotBdrv67zVS-t3E6k/edit?usp=sharing>`_


* Choice questions - answers options

   A file containing optional answers to a question that requires choosing an answer from a list

   `ApiAnswers.json <https://drive.google.com/file/d/1a2fyDvKl77PXD4MbxC_a8xoX31s1_2af/view?usp=sharing>`_


* Countries

   It is a table containing the English and Hebrew names of the countries for the purpose of answering the Country_Of_Birth question.
   expect to receive the exact string of the country's name in English

   `Country.csv <https://docs.google.com/spreadsheets/d/1C2BE3FIDWs5PCY_kLfhs528vz1kxCIEyNp3afT_EWR4/edit?usp=sharing>`_


* Full answers examples**

   A full questionnaire file containing all possible fields.
   
   .. important:: 

      Such files cannot be created because, for example, there is information from a current smoker and a former smoker. In practice, a person can only answer yes to one of the options.

   `answers_dict_male <https://drive.google.com/file/d/1iOzCjHubzkJCFlZ-e8lRhu-LUAbpMRiy/view?usp=sharing>`_

   `answers_dict_female <https://drive.google.com/file/d/1gouKmwsy8DojPV9v4EkguQYOwKDoGpJQ/view?usp=sharing>`_


* Sample recommendations file

   `recommendations PDF <https://drive.google.com/file/d/1iQLYrdt3Jcp-e0ZK0xG0LxcRccDYa29T/view?usp=sharing>`_
